from __future__ import annotations

from typing import Any

from tryon_service.core.models.exceptions import ModelNotLoadedError


class ModelManager:
    """
    Keeps loaded AI models in memory.

    All AI services must obtain models through this manager.
    """

    def __init__(self) -> None:
        self._models: dict[str, Any] = {}

    def register(
        self,
        name: str,
        model: Any,
    ) -> None:
        self._models[name] = model

    def get(
        self,
        name: str,
    ) -> Any:

        model = self._models.get(name)

        if model is None:
            raise ModelNotLoadedError(
                f"Model '{name}' has not been loaded."
            )

        return model

    def is_loaded(
        self,
        name: str,
    ) -> bool:
        return name in self._models