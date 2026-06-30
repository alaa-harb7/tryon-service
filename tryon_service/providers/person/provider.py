from __future__ import annotations

from pathlib import Path

import onnxruntime as ort

from tryon_service.config.settings import settings


class PersonDetectionProvider:
    """
    Loads and manages the YOLO ONNX model.
    """

    def __init__(self) -> None:

        config = settings.person_detection

        self._model_path = Path(
            config["model"]["path"]
        )

        self._execution_provider = (
            config["provider"]["execution_provider"]
        )

        self._session: ort.InferenceSession | None = None

    def load(self) -> None:

        if self._session is not None:
            return

        if not self._model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {self._model_path}"
            )

        self._session = ort.InferenceSession(
            str(self._model_path),
            providers=[
                self._execution_provider,
            ],
        )

    @property
    def session(
        self,
    ) -> ort.InferenceSession:

        if self._session is None:
            raise RuntimeError(
                "Person Detection model is not loaded."
            )

        return self._session

    @property
    def input_name(
        self,
    ) -> str:
        return self.session.get_inputs()[0].name

    @property
    def output_names(
        self,
    ) -> list[str]:
        return [
            output.name
            for output in self.session.get_outputs()
        ]