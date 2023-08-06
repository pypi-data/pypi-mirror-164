import os
from enum import Enum
from importlib.abc import FileLoader
from importlib.util import spec_from_loader
from typing import List, Type

import loguru
from loguru import logger
from web_foundation.app.infrastructure.plugins.plugin import Plugin
from web_foundation.app.resources.cache.repo import AppStore
from web_foundation.app.resources.file_repo.repo import FileRepository, AppFileSections


class SourceCodeLoader(FileLoader):
    def __init__(self, fullname: str, source):
        super().__init__(fullname, source)
        self.path = source

    def get_source(self, fullname: str) -> str | bytes:
        return self.path


class PluginsManager:
    debug: bool
    available_plugins: List[Plugin]
    repo: FileRepository
    store: AppStore
    sections: Type[Enum]

    def __init__(self, repo: FileRepository, store: AppStore, debug: bool = False, sections: Type[Enum] = AppFileSections):
        self.debug = debug
        self.repo = repo
        self.store = store
        self.available_plugins = []
        self.sections = sections

    async def store_plugins(self):
        await self.store.set_item("plugins", self.available_plugins)

    async def _import_plugin(self, pl: Plugin):
        try:
            spec = spec_from_loader(pl.name, loader=SourceCodeLoader(pl.name, pl.source))
            pl.import_it(spec)
            if pl not in self.available_plugins:
                self.available_plugins.append(pl)
        except Exception as e:
            if self.debug:
                logger.debug(f"Can't load plugin {pl.name}, cause {str(e)}")

    async def import_plugins(self):
        for pl in self.available_plugins:
            await self._import_plugin(pl)
        await self.store_plugins()

    async def configure_plugin(self, plugin: Plugin, *args, **kwargs) -> Plugin:
        raise NotImplementedError

    async def _discover_plugin(self, filename) -> Plugin | None:
        async with (await self.repo.take(filename, self.sections.PLUGINS)) as file_:
            pl = Plugin(filename, await file_.read())
            pl = await self.configure_plugin(pl)
            if pl.name is None:
                raise AttributeError("Plugin name must be specified")
            if pl not in self.available_plugins:
                self.available_plugins.append(pl)
                return pl
            return None

    async def discover_plugins(self):
        for filename in await self.repo.open_section(self.sections.PLUGINS):
            await self._discover_plugin(filename)

    async def reload_from_event(self, filename: str):
        await self.add_new_plugin(filename)

    async def add_new_plugin(self, filename: str):
        pl = await self._discover_plugin(filename)
        if pl:
            await self._import_plugin(pl)
            await self.store_plugins()
            if self.debug:
                logger.debug(f"New plugin added {pl}")

    async def _drop_stored_plugins(self):
        await self.store.set_item("plugins", None)

    async def find_plugin_by_target(self, target: str) -> List[Plugin]:
        plugins = await self.store.get_item("plugins")
        if not plugins:
            return []
        else:
            cell_plugins: List[Plugin] = []
            for pl in plugins:
                if pl.target == target and pl.enable:
                    cell_plugins.append(pl)
            return cell_plugins

    #
    # async def reload_all_plugins(self):
    #     self.available_plugins = []
    #     await self._drop_stored_plugins()
    #     await self.discover_plugins()
    #     await self.import_plugins()
    #     await self.store_plugins()
