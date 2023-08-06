from __future__ import annotations

import asyncio
import copy
import os
import socket
from functools import partial
from typing import List, Callable, Any, Type

import loguru
from dependency_injector import providers
from pydantic import BaseModel as PDModel
from sanic import Sanic
from sanic.server.socket import bind_socket

from web_foundation.app.app import AppContainer
from web_foundation.app.events.store import StoredPluginsUpdate
from web_foundation.app.infrastructure.plugins.manager import PluginsManager
from web_foundation.kernel import GenericIMessage, IMessage
from web_foundation.workers.io.http.ext_error_handler import ExtendedErrorHandler
from web_foundation.workers.io.http.routers.ext_router import ExtRouter
from web_foundation.workers.io.rt_connection import RtConnection, RtEventCallback
from web_foundation.workers.worker import Worker


class ServerConfig(PDModel):
    host: str
    port: int


class HttpServer(Worker):
    config: providers.Configuration
    sock: socket.socket
    sanic_app: Sanic
    router: ExtRouter | None
    rt_connections: List[RtConnection]
    plugin_manager: PluginsManager | None

    def __init__(self, config: providers.Configuration, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config

    def _configure(self, sock: socket.socket = None, ext_router: ExtRouter = None,
                   plugin_manager: PluginsManager = None):  # type: ignore
        self.sock = sock if sock else self.create_socket(self.config.get("host"), self.config.get("port"))
        self.router = copy.deepcopy(ext_router)
        self.sanic_app = Sanic(self.name, router=self.router)
        # self.sanic_app.extend(built_in_extensions=False)
        self.sanic_app.error_handler = ExtendedErrorHandler()
        self.sanic_app.after_server_stop(self.close)
        self.sanic_app.ctx.channel = self.channel
        self.rt_connections = []
        self._set_sanic_confs()
        self.plugin_manager = plugin_manager
        self.plugin_manager.debug = self.debug
        self.channel.add_event_listener(StoredPluginsUpdate, self.on_plugin_update_event)
        if self.router and issubclass(self.router.__class__, ExtRouter):
            self.router.apply_routes(self.sanic_app)

    def _set_sanic_confs(self):
        self.sanic_app.config.SWAGGER_UI_CONFIGURATION = {
            "docExpansion": 'none'
        }

    async def _init_wrk(self, app):
        await self._init_resources()
        if self.plugin_manager:
            await self.plugin_manager.import_plugins()

    async def _run(self):
        self.sanic_app.register_listener(self._init_wrk, "before_server_start")
        # noinspection PyAsyncCall
        self.sanic_app.add_task(self.channel.listen_consume())

    def _startup(self):
        super(HttpServer, self)._startup()
        try:
            self.sanic_app.run(sock=self.sock)
        except KeyboardInterrupt:
            self._close()

    def _close(self, *args, **kwargs):
        self.sock.close()

    def wire_worker(self, container: AppContainer) -> None:  # type: ignore
        if not self.router:
            raise AttributeError(f"{self.__class__} has no router")
        for chain in self.router.chains:
            for method in chain.methods:
                if method.protector:
                    container.wire(modules=[method.protector.__module__])
                container.wire(modules=[method.handler.__module__])

    @staticmethod
    def create_socket(host: str, port: int) -> socket.socket:
        sock = bind_socket(host, port)
        sock.set_inheritable(True)
        return sock

    async def on_plugin_update_event(self, event: StoredPluginsUpdate):
        if self.name != event.sender:
            await self.plugin_manager.reload_from_event(event.filename)

    async def add_new_plugin(self, filename: str):
        if not self.plugin_manager:
            raise AttributeError("Worker has not attribute plugin_manager")
        await self.plugin_manager.add_new_plugin(filename)
        await self.channel.produce(StoredPluginsUpdate(filename))

    async def on_rt_event(self, message: GenericIMessage, resolve_callback: RtEventCallback = None):
        await self.broadcast_rt_events(message, resolve_callback)

    async def broadcast_rt_events(self, event: GenericIMessage,
                                  resolve_callback: RtEventCallback):
        await asyncio.gather(*[conn.send_after_call(event, resolve_callback) for conn in self.rt_connections])

    async def accept_rt_connection(self, conn: RtConnection,
                                   on_disconnect_callback: Callable[[HttpServer, RtConnection], Any] | None = None):
        conn.debug = self.debug if self.debug else conn.debug
        self.rt_connections.append(conn)

        async def _on_rt_close():
            nonlocal self
            nonlocal conn
            nonlocal on_disconnect_callback
            self.rt_connections.remove(conn)
            if on_disconnect_callback:
                await on_disconnect_callback(self, conn)

        await conn.freeze_request(_on_rt_close)


def create_io_workers(server_cls: Type[HttpServer],
                      config: providers.Configuration,
                      router: ExtRouter,
                      plugin_manager: PluginsManager = None,
                      workers_num: int = 1,
                      fast: bool = False,
                      **kwargs
                      ) -> List[HttpServer]:
    """
    RESERVE 0 WORKER TO CREATE FRONT SERVICE SERVING
    """
    sock = HttpServer.create_socket(config.get("host"),
                                    config.get("port"))
    workers: List[HttpServer] = []
    w_num = workers_num
    if fast and workers_num != 1:
        raise RuntimeError("You cannot use both fast=True and workers=X")
    if fast:
        try:
            w_num = len(os.sched_getaffinity(0))
        except AttributeError:  # no cov
            w_num = os.cpu_count() or 1
    for i in range(w_num):
        worker = server_cls(config)
        worker.configure(f"web_worker_{i + 1}", ext_router=router, sock=sock,
                         plugin_manager=plugin_manager, **kwargs)
        workers.append(worker)
    return workers


def subscribe_worker_rt_callback(*workers: HttpServer,
                                 event_type: List[Type[IMessage] | str] | Type[IMessage] | str,
                                 callback: RtEventCallback,
                                 use_nested_classes: bool = False):
    for worker in workers:
        worker.channel.add_event_listener(event_type, partial(worker.on_rt_event, resolve_callback=callback),
                                          use_nested_classes=use_nested_classes)
