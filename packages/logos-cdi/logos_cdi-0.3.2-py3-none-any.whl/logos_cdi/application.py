from importlib import import_module
from zipimport import zipimporter
from typing import Callable, Type

from logos_cdi.abstract import AbstractContainer, R
from logos_cdi.builder import ContainerBuilder
from logos_cdi.container import CacheContainer, ContainerGroup, Container
from logos_cdi.resource import Parameter, Group


class Module(AbstractContainer):

    def __init__(self):
        self._container = None
        self._container_builder = ContainerBuilder()

    def container_builder(self):
        return self._container_builder

    def get(self, name: str, context: AbstractContainer = None, _type: Type[R] = object) -> R:
        if not self._container:
            self._container = self._container_builder.build(context)
        return self._container.get(name, context, _type)

    def has(self, name: str, context: AbstractContainer = None) -> bool:
        if not self._container:
            self._container = self._container_builder.build(context)
        return self._container.has(name, context)

    def resource_names(self) -> list:
        container = self._container
        if not container:
            from logos_cdi import __container__
            container = self._container_builder.build(__container__)
        return container.resource_names()


class Application(AbstractContainer):

    def __init__(self, modules, **kwargs):
        self.modules = modules
        for field, value in kwargs.items():
            setattr(self, field, value)
        self._container = None

    @property
    def container(self):
        if not self._container:
            resources = {
                'application': Parameter(self),
                'modules': Group(r'module:(?P<name>[\w+.]*)', resolve_resources=True)
            }
            containers = [
                Container(resources)
            ]
            for module_path in self.modules: #type: str
                if module_path.startswith('zip://'):
                    zip_name, path = module_path.replace('zip://', '').split(':')
                    zip_module = zipimporter(f'{zip_name}.zip')
                    module = zip_module.load_module(path)
                    if hasattr(module, '__container__'):
                        containers.append(getattr(module, '__container__'))
                    resources[f'module:{path}'] = Parameter(module)
                else:
                    module = import_module(module_path)
                    if hasattr(module, '__container__'):
                        containers.append(getattr(module, '__container__'))
                    resources[f'module:{module_path}'] = Parameter(module)
            self._container = CacheContainer('application', ContainerGroup(containers))
        return CacheContainer('runtime', self._container)

    def get(self, name: str, context: AbstractContainer = None, _type: Type[R] = object) -> R:
        return self.container.get(name, context or self, _type)

    def has(self, name: str, context: AbstractContainer = None) -> bool:
        return self.container.has(name, context or self)

    def resource_names(self) -> list:
        return self.container.resource_names()


