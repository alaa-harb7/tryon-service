from __future__ import annotations

from pathlib import Path


class ModelRegistry:
    """
    Central registry for AI model assets.
    """

    ROOT = Path("assets/models")

    # ----------------------------
    # MediaPipe
    # ----------------------------

    MEDIAPIPE_POSE = (
        ROOT
        / "mediapipe"
        / "pose_landmarker.task"
    )

    # ----------------------------
    # CatVTON
    # ----------------------------

    CATVTON = ROOT / "catvton"

    CATVTON_DENSEPOSE = CATVTON / "DensePose"

    CATVTON_SCHP = CATVTON / "SCHP"

    # HuggingFace Stable Diffusion base model
    CATVTON_BASE = (
        "booksforcharlie/stable-diffusion-inpainting"
    )

    # Official CatVTON attention weights
    CATVTON_ATTENTION = (
        "zhengchong/CatVTON"
    )