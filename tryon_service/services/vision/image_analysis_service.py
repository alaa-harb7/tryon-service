from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


class ImageAnalysisService:
    """
    Computer vision utilities used by validators.
    """

    @staticmethod
    def load(path: Path) -> np.ndarray:
        image = cv2.imread(str(path))

        if image is None:
            raise ValueError(
                f"Unable to load image: {path}"
            )

        return image

    @staticmethod
    def blur_score(image: np.ndarray) -> float:
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        return float(
            cv2.Laplacian(
                gray,
                cv2.CV_64F,
            ).var()
        )

    @staticmethod
    def brightness(image: np.ndarray) -> float:
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )
        return float(gray.mean())
    
    @staticmethod
    def resolution(
        image: np.ndarray,
    ) -> tuple[int, int]:
        """
        Returns (width, height).
        """

        height, width = image.shape[:2]

        return width, height

    @staticmethod
    def aspect_ratio(
        image: np.ndarray,
    ) -> float:
        """
        Returns width / height.
        """

        width, height = (
            ImageAnalysisService.resolution(image)
        )

        return width / height

    @staticmethod
    def is_portrait(
        image: np.ndarray,
    ) -> bool:
        """
        Checks whether the image is portrait.
        """

        width, height = (
            ImageAnalysisService.resolution(image)
        )

        return height >= width