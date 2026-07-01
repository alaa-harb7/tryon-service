from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.models.image import ImageData
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator


MIN_WIDTH = 384
MIN_HEIGHT = 512


class ResolutionValidator(BaseValidator):

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        image = context.assets.user_image

        if image is None:
            return Result.failure(
                "User image is missing."
            )

        if image.width < MIN_WIDTH:
            return Result.failure(
                "Image width is too small."
            )

        if image.height < MIN_HEIGHT:
            return Result.failure(
                "Image height is too small."
            )

        return Result.success(None)