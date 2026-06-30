from __future__ import annotations

from tryon_service.models.human.body_analysis import BodyAnalysis
from tryon_service.models.human.pose import HumanPose
from tryon_service.services.geometry.geometry_service import GeometryService
from tryon_service.shared.constants.mediapipe import PoseLandmark


class BodyAnalysisService:
    """
    Computes high-level geometric information
    from a HumanPose.
    """

    @staticmethod
    def analyze(
        pose: HumanPose,
    ) -> BodyAnalysis:

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

        shoulder_angle = GeometryService.angle(
            left_shoulder,
            right_shoulder,
        )

        hip_angle = GeometryService.angle(
            left_hip,
            right_hip,
        )

        center_x, center_y = GeometryService.midpoint(
            left_hip,
            right_hip,
        )

        body_area = (
            pose.bounding_box.area
            if pose.bounding_box
            else 0.0
        )

        return BodyAnalysis(
            shoulder_angle=shoulder_angle,
            hip_angle=hip_angle,
            body_center_x=center_x,
            body_center_y=center_y,
            body_area=body_area,
        )