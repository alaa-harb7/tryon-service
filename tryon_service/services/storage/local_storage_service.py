from __future__ import annotations

from pathlib import Path
import uuid

from PIL import Image

from tryon_service.services.storage_service import StorageService


class LocalStorageService(StorageService):
    """
    Stores generated images on the local filesystem.
    """

    def __init__(
        self,
        output_directory: str = "outputs",
    ) -> None:

        self._output_dir = Path(output_directory)

        self._output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        image: Image.Image,
    ) -> str:

        filename = f"{uuid.uuid4()}.png"

        path = self._output_dir / filename

        image.save(path)

        return f"/outputs/{filename}"