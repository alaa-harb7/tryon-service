from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator


class FileValidator(BaseValidator):

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        image = context.assets.user_image

        if image is None:
            return Result.failure(
                "User image is missing."
            )

        if not image.path.exists():
            return Result.failure(
                "Image file does not exist."
            )

        return Result.success(None)