from __future__ import annotations
from json import dumps

from .abc import AbcFormatter
from fibonacci.iterate.abc import AbcIterator


class JsonFormatter(AbcFormatter):
    def __call__(self, iterator: AbcIterator) -> str:
        return dumps([i for i in iterator])
