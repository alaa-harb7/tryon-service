from __future__ import annotations

from tryon_service.providers.base.provider import BaseProvider


class CatVTONProvider(BaseProvider):
    """
    Provider responsible for loading the official CatVTON model.
    """

    def __init__(self) -> None:
        self._loaded = False

    async def load(self) -> None:
        """
        CatVTON loading logic will be implemented
        in the next step.
        """
        self._loaded = True

    @property
    def is_loaded(self) -> bool:
        return self._loaded