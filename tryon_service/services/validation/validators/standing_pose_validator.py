from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.validation.base import BaseValidator
from tryon_service.shared.constants.mediapipe import PoseLandmark

MAX_HORIZONTAL_DIFF = 0.08
MIN_VISIBILITY = 0.60


class StandingPoseValidator(BaseValidator):
    """
    Validates that the person is standing in a suitable pose.
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
                "No pose detected."
            )

        left_shoulder = pose.landmark(
            PoseLandmark.LEFT_SHOULDER
        )

        right_shoulder = pose.landmark(
            PoseLandmark.RIGHT_SHOULDER
        )

        left_hip = pose.landmark(
            PoseLandmark.LEFT_HIP
        )

        right_hip = pose.landmark(
            PoseLandmark.RIGHT_HIP
        )

        left_ankle = pose.landmark(
            PoseLandmark.LEFT_ANKLE
        )

        right_ankle = pose.landmark(
            PoseLandmark.RIGHT_ANKLE
        )

        if (
            left_ankle.visibility < MIN_VISIBILITY
            or right_ankle.visibility < MIN_VISIBILITY
        ):
            return Result.failure(
                "Feet are not clearly visible."
            )

        shoulder_diff = abs(
            left_shoulder.y - right_shoulder.y
        )

        if shoulder_diff > MAX_HORIZONTAL_DIFF:
            return Result.failure(
                "Shoulders are not level."
            )

        hip_diff = abs(
            left_hip.y - right_hip.y
        )

        if hip_diff > MAX_HORIZONTAL_DIFF:
            return Result.failure(
                "Hips are not level."
            )

        return Result.success(None)