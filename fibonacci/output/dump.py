from __future__ import annotations
from typing import final

from .abc import AbcDump, AbcFormatter, AbcStream
from fibonacci.iterate.abc import AbcIterator


@final
class Dump(AbcDump):
    def __init__(self, stream: AbcStream, formatter: AbcFormatter) -> None:
        self._stream = stream
        self._formatter = formatter
    
    def __call__(self, iterator: AbcIterator) -> None:
        text = self._formatter(iterator=iterator)
        self._stream.write(text=text)
