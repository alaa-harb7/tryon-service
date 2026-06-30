from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator

MIN_BODY_AREA = 0.20
MAX_BODY_AREA = 0.90


class BodyCoverageValidator(BaseValidator):
    """
    Validates that the detected body occupies
    a reasonable portion of the image.
    """

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        pose = context.human.pose

        if pose is None:
            return Result.failure(
                "Human pose is missing."
            )

        if not pose.detected:
            return Result.failure(
                "No body detected."
            )

        if pose.bounding_box is None:
            return Result.failure(
                "Bounding box is missing."
            )

        area = pose.bounding_box.area

        if area < MIN_BODY_AREA:
            return Result.failure(
                "Person is too far from the camera."
            )

        if area > MAX_BODY_AREA:
            return Result.failure(
                "Person is too close to the camera."
            )

        return Result.success(None)