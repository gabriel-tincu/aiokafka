import abc
from typing import Any

class AbstractType(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    @abc.abstractmethod
    def encode(cls, value: Any) -> Any: ...
    @abc.abstractmethod
    def decode(cls, data: Any) -> Any: ...
    @classmethod
    def repr(cls, value: Any): ...
