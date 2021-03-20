from __future__ import annotations
from sys import stdout
from io import TextIOBase

from .abc import AbcStream


class StdoutStream(AbcStream):
    __slots__ = []

    def write(self, text: str) -> None:
        stdout.write(text)


class DefaultStream(AbcStream):
    __slots__ = ["_stream"]

    def __init__(self, stream: TextIOBase) -> None:
        self._stream = stream

    def write(self, text: str) -> None:
        self._stream.write(text)
