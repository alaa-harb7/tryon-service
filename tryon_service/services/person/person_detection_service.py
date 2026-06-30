from __future__ import annotations

import cv2
import numpy as np

from tryon_service.providers.person.provider import (
    PersonDetectionProvider,
)
from tryon_service.models.person.result import (
    PersonDetectionResult,
)

from tryon_service.services.person.yolo_decoder import (
    YOLODecoder,
)


class PersonDetectionService:
    """
    Runs YOLO person detection.
    """

    IMAGE_SIZE = 640

    def __init__(
        self,
        provider: PersonDetectionProvider,
    ) -> None:

        self._provider = provider
        self._decoder = YOLODecoder()

    def preprocess(
        self,
        image: np.ndarray,
    ) -> np.ndarray:
        """
        Converts image into YOLO input tensor.
        """

        image = cv2.resize(
            image,
            (
                self.IMAGE_SIZE,
                self.IMAGE_SIZE,
            ),
        )

        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB,
        )

        image = image.astype(
            np.float32,
        )

        image /= 255.0

        image = np.transpose(
            image,
            (
                2,
                0,
                1,
            ),
        )

        image = np.expand_dims(
            image,
            axis=0,
        )

        return image
    

    def detect(
        self,
        image: np.ndarray,
    ) -> PersonDetectionResult:

        tensor = self.preprocess(image)

        outputs = self._provider.session.run(
            self._provider.output_names,
            {
                self._provider.input_name: tensor,
            },
        )

        return self._decoder.decode(
            outputs[0],
        )