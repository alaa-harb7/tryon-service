from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseProvider(ABC):
    """
    Base interface for AI model providers.
    """

    @abstractmethod
    async def load(self) -> None:
        ...

    @property
    @abstractmethod
    def is_loaded(self) -> bool:
        ...