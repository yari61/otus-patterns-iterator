from __future__ import annotations

from fibonacci.collection import AbcLinearCollection


class FibonacciLinear(AbcLinearCollection):
    __slots__ = ["_cache"]

    def __init__(self) -> None:
        self._cache = [0, 1]

    def __getitem__(self, index: int) -> int:
        """Returns the Fibonacci number at the given index
        """
        if len(self._cache) <= index:
            self._generate(index=index)
        return self._cache[index]

    def _generate(self, index: int) -> None:
        """Generates the Fibonacci number at the given index
        """
        while len(self._cache) <= index:
            self._cache.append(self._cache[-1] + self._cache[-2])
