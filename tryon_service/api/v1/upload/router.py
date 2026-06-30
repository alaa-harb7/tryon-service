from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile
from PIL import Image

from tryon_service.api.v1.upload.mapper import UploadMapper
from tryon_service.application.upload.dependencies import get_upload_use_case
from tryon_service.application.upload.dto import UploadImageCommand
from tryon_service.application.upload.use_case import UploadUseCase
from tryon_service.services.storage_service import StorageService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("")
async def upload_image(
    user_id: str,
    file: UploadFile = File(...),
    use_case: UploadUseCase = Depends(get_upload_use_case),
):
    storage = StorageService()

    storage_path = await storage.save(file)

    image = Image.open(storage_path)

    width, height = image.size

    size = Path(storage_path).stat().st_size

    image_data = UploadMapper.to_image_data(
        file=file,
        storage_path=storage_path,
        width=width,
        height=height,
        size_bytes=size,
    )

    result = await use_case.execute(
        UploadImageCommand(
            user_id=user_id,
            image=image_data,
        )
    )

    if not result.is_success:
        raise HTTPException(
            status_code=400,
            detail=result.error,
        )

    return result.value