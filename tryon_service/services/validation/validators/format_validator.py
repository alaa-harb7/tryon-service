from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.models.image import ImageData
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator


SUPPORTED_FORMATS = {
    "image/jpeg",
    "image/png",
    "image/webp",
}


class ImageFormatValidator(BaseValidator):

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        image = context.assets.user_image

        if image is None:
            return Result.failure(
                "User image is missing."
            )

        if image.content_type not in SUPPORTED_FORMATS:
            return Result.failure(
                f"Unsupported format: {image.content_type}"
            )

        return Result.success(None)