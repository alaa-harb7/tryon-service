from __future__ import annotations

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from tryon_service.core.models.loader import BaseModelLoader
from tryon_service.services.models.model_registry import ModelRegistry


class MediaPipePoseLoader(BaseModelLoader):
    """
    Loads the MediaPipe Pose Landmarker model.
    """

    async def load(self) -> vision.PoseLandmarker:

        base_options = python.BaseOptions(
            model_asset_path=str(
                ModelRegistry.MEDIAPIPE_POSE
            )
        )

        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
        )

        return vision.PoseLandmarker.create_from_options(
            options
        )