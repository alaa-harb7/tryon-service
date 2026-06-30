from fastapi import APIRouter

from tryon_service.api.v1.tryon.router import (
    router as tryon_router,
)
from tryon_service.api.v1.health.router import (
    router as health_router,
)

router = APIRouter()

router.include_router(tryon_router)
router.include_router(health_router)