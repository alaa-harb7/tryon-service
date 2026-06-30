from __future__ import annotations

from functools import lru_cache

from tryon_service.providers.masking.provider import (
    AutoMaskerProvider,
)
from tryon_service.providers.pipeline.provider import (
    CatVTONPipelineProvider,
)


@lru_cache
def get_pipeline_provider() -> CatVTONPipelineProvider:
    provider = CatVTONPipelineProvider()
    provider.load()
    return provider


@lru_cache
def get_automask_provider() -> AutoMaskerProvider:
    provider = AutoMaskerProvider()
    provider.load()
    return provider