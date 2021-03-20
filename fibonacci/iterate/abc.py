from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Iterator


class AbcIterator(ABC):
    def __iter__(self) -> Iterator[Any]:
        while True:
            try:
                yield self.__next__()
            except StopIteration:
                return

    @abstractmethod
    def __next__(self) -> Any:
        pass


class AbcIteratorFactory(ABC):
    @abstractmethod
    def __call__(self) -> AbcIterator:
        pass
