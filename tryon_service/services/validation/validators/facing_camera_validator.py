from __future__ import annotations

from tryon_service.core.result import Result
from tryon_service.pipelines.base.context import PipelineContext
from tryon_service.services.geometry.geometry_service import GeometryService
from tryon_service.services.validation.base import BaseValidator
from tryon_service.shared.constants.mediapipe import PoseLandmark

MAX_CENTER_OFFSET = 0.15


class FacingCameraValidator(BaseValidator):
    """
    Validates that the person is approximately facing the camera.
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

        shoulder_center, _ = GeometryService.midpoint(
            left_shoulder,
            right_shoulder,
        )

        hip_center, _ = GeometryService.midpoint(
            left_hip,
            right_hip,
        )

        offset = abs(
            shoulder_center - hip_center
        )

        if offset > MAX_CENTER_OFFSET:
            return Result.failure(
                "Person is not facing the camera."
            )

        return Result.success(None)