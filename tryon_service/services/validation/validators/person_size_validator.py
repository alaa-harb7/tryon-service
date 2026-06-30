from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator


class PersonSizeValidator(BaseValidator):
    """
    Ensures the detected person is large enough.
    """

    MIN_AREA = 120_000

    async def validate(
        self,
        context: PipelineContext,
    ) -> Result[None]:

        detection = context.human.person_detection

        if detection is None:
            return Result.success(None)

        person = detection.main_person

        if person is None:
            return Result.success(None)

        if person.area < self.MIN_AREA:

            return Result.failure(
                "The person is too small. Please move closer to the camera."
            )

        return Result.success(None)