from __future__ import annotations

import cv2
import mediapipe as mp

from tryon_service.core.container import container
from tryon_service.models.human.landmark import Landmark
from tryon_service.models.human.pose import HumanPose


class MediaPipeService:
    """
    Wrapper around MediaPipe Pose.
    """

    def __init__(self) -> None:
        self._model = container.models.get(
            "mediapipe_pose"
        )

    def detect(
        self,
        image_path: str,
    ) -> HumanPose:

        image = cv2.imread(image_path)

        rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB,
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb,
        )

        result = self._model.detect(mp_image)

        if not result.pose_landmarks:
            return HumanPose(
                detected=False,
            )

        landmarks = [
            Landmark(
                x=lm.x,
                y=lm.y,
                z=lm.z,
                visibility=lm.visibility,
            )
            for lm in result.pose_landmarks[0]
        ]

        xs = [lm.x for lm in landmarks]
        ys = [lm.y for lm in landmarks]

        from tryon_service.models.human.bounding_box import BoundingBox

        bounding_box = BoundingBox(
            left=min(xs),
            top=min(ys),
            right=max(xs),
            bottom=max(ys),
        )

        return HumanPose(
            detected=True,
            landmarks=landmarks,
            bounding_box=bounding_box,
        )