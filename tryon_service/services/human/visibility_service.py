from __future__ import annotations

from tryon_service.models.human.pose import HumanPose
from tryon_service.shared.constants.mediapipe import PoseLandmark


class VisibilityService:
    """
    Computes body-part visibility from MediaPipe landmarks.
    """

    VISIBILITY_THRESHOLD = 0.5

    @classmethod
    def _visible(
        cls,
        pose: HumanPose,
        landmark: PoseLandmark,
    ) -> bool:

        point = pose.landmark(landmark)

        if point is None:
            return False

        return point.visibility >= cls.VISIBILITY_THRESHOLD

    @classmethod
    def is_face_visible(
        cls,
        pose: HumanPose,
    ) -> bool:

        return (
            cls._visible(pose, PoseLandmark.NOSE)
            and cls._visible(
                pose,
                PoseLandmark.LEFT_EYE,
            )
            and cls._visible(
                pose,
                PoseLandmark.RIGHT_EYE,
            )
        )

    @classmethod
    def is_upper_body_visible(
        cls,
        pose: HumanPose,
    ) -> bool:

        required = [
            PoseLandmark.LEFT_SHOULDER,
            PoseLandmark.RIGHT_SHOULDER,
            PoseLandmark.LEFT_ELBOW,
            PoseLandmark.RIGHT_ELBOW,
            PoseLandmark.LEFT_HIP,
            PoseLandmark.RIGHT_HIP,
        ]

        return all(
            cls._visible(pose, landmark)
            for landmark in required
        )

    @classmethod
    def is_lower_body_visible(
        cls,
        pose: HumanPose,
    ) -> bool:

        required = [
            PoseLandmark.LEFT_HIP,
            PoseLandmark.RIGHT_HIP,
            PoseLandmark.LEFT_KNEE,
            PoseLandmark.RIGHT_KNEE,
            PoseLandmark.LEFT_ANKLE,
            PoseLandmark.RIGHT_ANKLE,
        ]

        return all(
            cls._visible(pose, landmark)
            for landmark in required
        )

    @classmethod
    def are_feet_visible(
        cls,
        pose: HumanPose,
    ) -> bool:

        return (
            cls._visible(
                pose,
                PoseLandmark.LEFT_FOOT_INDEX,
            )
            and cls._visible(
                pose,
                PoseLandmark.RIGHT_FOOT_INDEX,
            )
        )

    @classmethod
    def is_full_body(
        cls,
        pose: HumanPose,
    ) -> bool:

        return (
            cls.is_face_visible(pose)
            and cls.is_upper_body_visible(pose)
            and cls.is_lower_body_visible(pose)
            and cls.are_feet_visible(pose)
        )