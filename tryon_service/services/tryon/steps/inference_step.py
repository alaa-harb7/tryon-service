from __future__ import annotations

import torch

from tryon_service.config.tryon import TryOnConfig
from tryon_service.providers.pipeline.provider import (
    CatVTONPipelineProvider,
)


class InferenceStep:

    def __init__(
        self,
        pipeline: CatVTONPipelineProvider,
    ) -> None:

        self._pipeline = pipeline

        self._generator = torch.Generator(
            device="cuda" if torch.cuda.is_available() else "cpu"
        ).manual_seed(
            TryOnConfig.RANDOM_SEED
        )

    def execute(
        self,
        person,
        garment,
        mask,
    ):

        return self._pipeline.pipeline(
            person,
            garment,
            mask,
            num_inference_steps=TryOnConfig.NUM_INFERENCE_STEPS,
            guidance_scale=TryOnConfig.GUIDANCE_SCALE,
            height=TryOnConfig.OUTPUT_HEIGHT,
            width=TryOnConfig.OUTPUT_WIDTH,
            generator=self._generator,
        )