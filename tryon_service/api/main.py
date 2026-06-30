from __future__ import annotations

from fastapi import FastAPI

from tryon_service.core.lifespan import lifespan
from tryon_service.api.router import router as api_router

app = FastAPI(
    title="TryOn Service",
    description="Production-grade AI Virtual Try-On Microservice",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(api_router)


@app.get("/", tags=["System"])
async def root() -> dict[str, str]:
    return {
        "service": "TryOn Service",
        "status": "running",
    }


@app.get("/health", tags=["System"])
async def health() -> dict[str, str]:
    return {
        "status": "healthy",
    }