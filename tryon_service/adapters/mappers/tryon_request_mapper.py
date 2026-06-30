from __future__ import annotations

from tryon_service.pipelines.base.context import (
    PipelineContext,
)

from tryon_service.services.tryon.request import (
    VirtualTryOnRequest,
)


class TryOnRequestMapper:

    @staticmethod
    def to_pipeline_context(
        request: VirtualTryOnRequest,
    ) -> PipelineContext:

        context = PipelineContext()

        context.request.garment_type = (
            request.garment_type
        )

        context.assets.user_image = (
            request.person
        )

        context.assets.garment_image = (
            request.garment
        )

        return context