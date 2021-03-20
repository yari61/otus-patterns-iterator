from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import MagicMock, Mock
from collections.abc import Iterator

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Configuration

from fibonacci.iterate.linear import LinearIterator
from fibonacci.collection import AbcLinearCollection


class Container(DeclarativeContainer):
    collection = Factory(MagicMock, AbcLinearCollection)
    indices = Factory(MagicMock, Iterator)
    iterator = Factory(LinearIterator, indices=indices, collection=collection)


class Next(TestCase):
    def test_next_index_extracted(self):
        container = Container()
        indices = container.indices()
        iterator = container.iterator(indices=indices)

        iterator.__next__()

        indices.__next__.assert_called_once()

    def test_correct_item_extracted(self):
        container = Container()
        indices = container.indices()
        collection = container.collection()
        iterator = container.iterator(collection=collection, indices=indices)

        iterator.__next__()

        collection.__getitem__.assert_called_once_with(indices.__next__())
    
    def test_stop_iteration_raised_on_last_index(self):
        container = Container()
        indices = container.indices()
        indices.__next__ = Mock(side_effect=StopIteration)
        iterator = container.iterator(indices=indices)

        with self.assertRaises(StopIteration):
            iterator.__next__()

if __name__ == "__main__":
    main()
