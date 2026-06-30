from __future__ import annotations

from fastapi import APIRouter

from fastapi import Depends

from tryon_service.api.v1.health.dependencies import (
    get_automask_provider,
    get_pipeline_provider,
)

from tryon_service.providers.masking.provider import (
    AutoMaskerProvider,
)
from tryon_service.providers.pipeline.provider import (
    CatVTONPipelineProvider,
)

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health(
    pipeline: CatVTONPipelineProvider = Depends(
        get_pipeline_provider,
    ),
    automask: AutoMaskerProvider = Depends(
        get_automask_provider,
    ),
):
    return {
        "status": "ready",
        "pipeline_loaded": pipeline.is_loaded,
        "automask_loaded": automask.is_loaded,
    }