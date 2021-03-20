from __future__ import annotations
from abc import ABC, abstractmethod
from typing import AnyStr

from fibonacci.iterate.abc import AbcIterator


class AbcDump(ABC):
    @abstractmethod
    def __call__(self, iterator: AbcIterator) -> None:
        pass


class AbcFormatter(ABC):
    @abstractmethod
    def __call__(self, iterator: AbcIterator) -> AnyStr:
        pass


class AbcStream(ABC):
    @abstractmethod
    def write(self, text: AnyStr) -> None:
        pass
