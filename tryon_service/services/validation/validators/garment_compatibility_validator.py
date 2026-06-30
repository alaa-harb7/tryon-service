from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator


class GarmentCompatibilityValidator(BaseValidator):
    """
    Validates that the uploaded image is suitable
    for the requested garment type.
    """

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        garment_type = context.request.garment_type

        if garment_type == "upper":

            if not context.human.upper_body_visible:
                return Result.failure(
                    "Upper body is not visible."
                )

        elif garment_type == "lower":

            if not context.human.lower_body_visible:
                return Result.failure(
                    "Lower body is not visible."
                )

        elif garment_type == "overall":

            if not context.human.full_body:
                return Result.failure(
                    "Full body image is required."
                )

        elif garment_type == "shoes":

            if not context.human.feet_visible:
                return Result.failure(
                    "Feet are not visible."
                )

        else:
            return Result.failure(
                f"Garment type '{garment_type}' is not supported for compatibility check."
            )

        return Result.success(None)

    