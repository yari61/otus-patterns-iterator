from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class AbcLinearCollection(ABC):
    @abstractmethod
    def __getitem__(self, index: int) -> Any:
        pass
