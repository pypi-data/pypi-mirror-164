""" """

from __future__ import annotations

import inspect
from typing import Any

from labctrl.logger import logger


class ResourceMetaclass(type):
    """ """

    def __init__(cls, name, bases, kwds) -> None:
        """ """
        super().__init__(name, bases, kwds)

        # find the parameters (gettable and settable) of the Resource class
        mro = inspect.getmro(cls)  # mro means method resolution order
        properties = {
            k: v for c in mro for k, v in c.__dict__.items() if isinstance(v, property)
        }
        cls.properties = properties.keys()
        cls.gettables = {k for k, v in properties.items() if v.fget is not None}
        cls.settables = {k for k, v in properties.items() if v.fset is not None}

    def __repr__(cls) -> str:
        """ """
        return f"<class '{cls.__name__}'>"


class Resource(metaclass=ResourceMetaclass):
    """ """

    def __init__(self, name: str, **parameters) -> None:
        """ """
        self._name = str(name)
        logger.debug(f"Initialized {self}.")
        # set parameters with default values supplied by the user
        self.configure(**parameters)

    def __repr__(self) -> str:
        """ """
        return f"{self.__class__.__name__} '{self._name}'"

    @property
    def name(self) -> str:
        """ """
        return self._name

    def _attributes(self) -> set[str]:
        """ """
        return {k for k in self.__dict__.keys() if not k.startswith("_")}

    def parametrize(self) -> set[str]:
        """ """
        return self.__class__.properties | self._attributes()

    def configure(self, **parameters) -> None:
        """ """
        settables = self._attributes() | self.__class__.settables
        for name, value in parameters.items():
            if name in settables:
                setattr(self, name, value)
                logger.debug(f"Set {self} '{name}' = {value}.")

    def snapshot(self) -> dict[str, Any]:
        """ """
        gettables = self._attributes() | self.__class__.gettables
        return {name: getattr(self, name) for name in sorted(gettables)}
