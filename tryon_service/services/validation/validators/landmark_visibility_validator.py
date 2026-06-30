from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator

from tryon_service.shared.constants.mediapipe import PoseLandmark

VISIBILITY_THRESHOLD = 0.60

REQUIRED_LANDMARKS = [
    PoseLandmark.NOSE,
    PoseLandmark.LEFT_SHOULDER,
    PoseLandmark.RIGHT_SHOULDER,
    PoseLandmark.LEFT_HIP,
    PoseLandmark.RIGHT_HIP,
    PoseLandmark.LEFT_KNEE,
    PoseLandmark.RIGHT_KNEE,
    PoseLandmark.LEFT_ANKLE,
    PoseLandmark.RIGHT_ANKLE,
]



class LandmarkVisibilityValidator(BaseValidator):
    """
    Ensures all required body landmarks are sufficiently visible.
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
                "No human pose detected."
            )

        for index in REQUIRED_LANDMARKS:

            landmark = pose.landmarks[index]

            if landmark.visibility < VISIBILITY_THRESHOLD:
                return Result.failure(
                    f"Required body landmark {index} is not sufficiently visible."
                )

        return Result.success(None)