from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.models.image import ImageData
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator
from tryon_service.services.vision.image_analysis_service import (
    ImageAnalysisService,
)

MIN_BRIGHTNESS = 40
MAX_BRIGHTNESS = 220


class BrightnessValidator(BaseValidator):

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        image = context.assets.user_image

        if image is None:
            return Result.failure(
                "User image is missing."
            )

        cv_image = ImageAnalysisService.load(image.path)

        value = ImageAnalysisService.brightness(cv_image)

        if value < MIN_BRIGHTNESS:
            return Result.failure(
                "Image is too dark."
            )

        if value > MAX_BRIGHTNESS:
            return Result.failure(
                "Image is too bright."
            )

        return Result.success(None)