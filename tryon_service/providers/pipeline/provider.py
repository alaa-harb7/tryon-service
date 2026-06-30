from __future__ import annotations

from importlib import import_module

import torch

from tryon_service.bootstrap.catvton_environment import (
    CatVTONEnvironment,
)
from tryon_service.services.models.model_registry import (
    ModelRegistry,
)


class CatVTONPipelineProvider:
    """
    Loads the official CatVTON Pipeline.
    """

    def __init__(self) -> None:
        self._pipeline = None

    @property
    def pipeline(self):
        return self._pipeline

    @property
    def is_loaded(self) -> bool:
        return self._pipeline is not None

    def load(self) -> None:

        if self.is_loaded:
            return

        CatVTONEnvironment.initialize()

        module = import_module("model.pipeline")

        CatVTONPipeline = module.CatVTONPipeline

        device = "cuda" if torch.cuda.is_available() else "cpu"

        dtype = (
            torch.float16
            if device == "cuda"
            else torch.float32
        )

        self._pipeline = CatVTONPipeline(
            base_ckpt=ModelRegistry.CATVTON_BASE,
            attn_ckpt=ModelRegistry.CATVTON_ATTENTION,
            attn_ckpt_version="mix",
            weight_dtype=dtype,
            device=device,
            compile=False,
            skip_safety_check=False,
        )

    def unload(self) -> None:
        self._pipeline = None