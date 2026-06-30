from __future__ import annotations

import cv2
import numpy as np

from tryon_service.models.person.detection import (
    PersonDetection,
)
from tryon_service.models.person.result import (
    PersonDetectionResult,
)


class YOLODecoder:

    PERSON_CLASS = 0

    def decode(
        self,
        predictions: np.ndarray,
        confidence_threshold: float = 0.40,
        iou_threshold: float = 0.50,
    ) -> PersonDetectionResult:

        predictions = predictions.squeeze().T

        boxes = []

        scores = []

        detections = []

        for row in predictions:

            x, y, w, h = row[:4]

            class_scores = row[4:]

            class_id = np.argmax(class_scores)

            confidence = class_scores[class_id]

            if class_id != self.PERSON_CLASS:
                continue

            if confidence < confidence_threshold:
                continue

            x1 = x - w / 2
            y1 = y - h / 2
            x2 = x + w / 2
            y2 = y + h / 2

            boxes.append(
                [
                    x1,
                    y1,
                    x2 - x1,
                    y2 - y1,
                ]
            )

            scores.append(float(confidence))

            detections.append(
                PersonDetection(
                    x1=float(x1),
                    y1=float(y1),
                    x2=float(x2),
                    y2=float(y2),
                    confidence=float(confidence),
                )
            )

        indices = cv2.dnn.NMSBoxes(
            boxes,
            scores,
            confidence_threshold,
            iou_threshold,
        )

        if len(indices) == 0:
            return PersonDetectionResult(
                detections=[],
            )

        filtered = [
            detections[int(i)]
            for i in indices.flatten()
        ]

        return PersonDetectionResult(
            detections=filtered,
        )