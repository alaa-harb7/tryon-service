from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.services.validation.base import (
    BaseValidator,
)
from tryon_service.pipelines.base.context import (
    PipelineContext,
)


class SinglePersonValidator(BaseValidator):
    """
    Ensures exactly one person exists in the image.
    """

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        if context.human.person_count == 0:
            return Result.failure(
                "No person detected in the image."
            )

        if context.human.person_count > 1:
            return Result.failure(
                "Multiple people detected. Please upload an image containing exactly one person."
            )

        return Result.success(None)