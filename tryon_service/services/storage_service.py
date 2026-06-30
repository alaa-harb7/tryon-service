from __future__ import annotations

import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


class StorageService:
    """
    Local storage implementation.

    Can later be replaced by MinIO or S3
    without changing business logic.
    """

    ROOT = Path("storage/uploads/original")

    async def save(
        self,
        file: UploadFile,
    ) -> Path:

        self.ROOT.mkdir(
            parents=True,
            exist_ok=True,
        )

        extension = Path(file.filename).suffix

        filename = f"{uuid4()}{extension}"

        destination = self.ROOT / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        return destination