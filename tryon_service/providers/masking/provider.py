from __future__ import annotations

from importlib import import_module

import torch

from tryon_service.bootstrap.catvton_environment import (
    CatVTONEnvironment,
)
from tryon_service.services.models.model_registry import (
    ModelRegistry,
)


class AutoMaskerProvider:
    """
    Loads the official CatVTON AutoMasker.
    """

    def __init__(self) -> None:
        self._masker = None

    @property
    def masker(self):
        return self._masker

    @property
    def is_loaded(self) -> bool:
        return self._masker is not None

    def load(self) -> None:

        if self.is_loaded:
            return

        # Make the official CatVTON repository importable
        CatVTONEnvironment.initialize()

        # Import after sys.path has been prepared
        module = import_module("model.cloth_masker")
        AutoMasker = module.AutoMasker

        device = "cuda" if torch.cuda.is_available() else "cpu"

        self._masker = AutoMasker(
            densepose_ckpt=str(ModelRegistry.CATVTON_DENSEPOSE),
            schp_ckpt=str(ModelRegistry.CATVTON_SCHP),
            device=device,
        )

    def unload(self) -> None:
        self._masker = None