from __future__ import annotations
from collections.abc import Iterator

from .abc import AbcIterator, AbcIteratorFactory
from fibonacci.collection import AbcLinearCollection


class LinearIterator(AbcIterator):
    """Iterates over given indices of the collection
    """
    __slots__ = ["_collection", "_indices"]

    def __init__(self, collection: AbcLinearCollection, indices: Iterator[int]) -> None:
        """Initialization method

        Args:
            collection (AbcLinearCollection)
            indices (Iterator): sequence of indices to extract from the collection
        """

        self._collection = collection
        self._indices = indices

    def __next__(self) -> Any:
        try:
            index = next(self._indices)
        except StopIteration:
            raise StopIteration
        else:
            return self._collection[index]


class LinearIteratorFactory(AbcIteratorFactory):
    __slots__ = ["_collection", "_indices"]

    def __init__(self, collection: AbcLinearCollection, indices: Iterator[int]) -> None:
        self._collection = collection
        self._indices = indices

    def __call__(self) -> LinearIterator:
        return LinearIterator(collection=self._collection, indices=self._indices)
