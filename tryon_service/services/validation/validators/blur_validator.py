from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.models.image import ImageData
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator
from tryon_service.services.vision.image_analysis_service import (
    ImageAnalysisService,
)

MIN_BLUR_SCORE = 100.0


class BlurValidator(BaseValidator):

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

        score = ImageAnalysisService.blur_score(cv_image)

        if score < MIN_BLUR_SCORE:
            return Result.failure(
                f"Image is too blurry. Score={score:.2f}"
            )

        return Result.success(None)