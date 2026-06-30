from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.pipelines.base.pipeline import BasePipeline


class UploadPipeline(BasePipeline):
    """
    First pipeline stage.

    Responsible only for accepting the uploaded image
    into the pipeline context.
    """

    async def execute(
        self,
        context: PipelineContext,
    ) -> Result[PipelineContext]:

        if context.assets.user_image is None:
            return Result.failure(
                "User image was not provided."
            )

        return Result.success(context)