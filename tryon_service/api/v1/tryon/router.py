from __future__ import annotations

from pathlib import Path
import uuid

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    UploadFile,
)

from tryon_service.api.v1.tryon.builders.request_builder import (
    TryOnRequestBuilder,
)
from tryon_service.api.v1.tryon.dependencies import (
    get_local_storage_service,
    get_request_builder,
    get_virtual_tryon_service,
)
from tryon_service.api.v1.tryon.schemas import (
    TryOnResponse,
)
from tryon_service.services.storage.local_storage_service import (
    LocalStorageService,
)
from tryon_service.services.tryon.virtual_tryon_service import (
    VirtualTryOnService,
)

router = APIRouter(
    prefix="/tryon",
    tags=["Virtual Try-On"],
)


@router.post(
    "/",
    response_model=TryOnResponse,
)
async def virtual_tryon(
    person: UploadFile = File(...),
    garment: UploadFile | None = File(None),
    garment_url: str | None = Form(None),
    garment_type: str = Form(...),
    builder: TryOnRequestBuilder = Depends(
        get_request_builder,
    ),
    service: VirtualTryOnService = Depends(
        get_virtual_tryon_service,
    ),
    storage: LocalStorageService = Depends(
        get_local_storage_service,
    ),
):

    request = await builder.build(
        person=person,
        garment=garment,
        garment_url=garment_url,
        garment_type=garment_type,
    )


    result = await service.generate(request)

    image_url = storage.save(
        result.image,
    )

    return TryOnResponse(
        success=True,
        image_url=image_url,
    )