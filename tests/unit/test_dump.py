from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock, MagicMock

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory

from fibonacci.output.dump import Dump
from fibonacci.output.abc import AbcFormatter, AbcStream
from fibonacci.iterate.abc import AbcIterator


class Container(DeclarativeContainer):
    stream = Factory(Mock, AbcStream)
    formatter = Factory(Mock, AbcFormatter)
    dump = Factory(Dump, stream=stream, formatter=formatter)


class Call(TestCase):
    def test_formatter_called_with_iterator(self):
        container = Container()
        formatter = container.formatter()
        dump = container.dump(formatter=formatter)
        iterator = MagicMock(AbcIterator)

        dump(iterator=iterator)

        formatter.assert_called_once_with(iterator=iterator)

    def test_formatted_text_written(self):
        container = Container()
        formatted_text = Mock()
        formatter = container.formatter(return_value=formatted_text)
        stream = container.stream()
        dump = container.dump(stream=stream, formatter=formatter)
        iterator = MagicMock(AbcIterator)

        dump(iterator=iterator)

        stream.write.assert_called_once_with(text=formatted_text)

if __name__ == "__main__":
    main()
