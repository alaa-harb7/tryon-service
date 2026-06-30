from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseModelLoader(ABC):
    """
    Base class for AI model loaders.
    """

    @abstractmethod
    async def load(self) -> object:
        ...