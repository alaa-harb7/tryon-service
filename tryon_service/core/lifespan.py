from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from tryon_service.core.container import container
from tryon_service.core.logger import logger
from tryon_service.services.models.mediapipe_loader import MediaPipePoseLoader


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting TryOn Service...")

    await container.mongo.connect()

    await container.mongo.client.admin.command("ping")

    loader = MediaPipePoseLoader()
    pose_model = await loader.load()
    container.models.register(
        "mediapipe_pose",
        pose_model,
    )

    logger.info("MediaPipe Pose model loaded.")

    logger.info("MongoDB connected successfully.")

    yield

    logger.info("Stopping TryOn Service...")

    await container.mongo.disconnect()

    logger.info("MongoDB disconnected.")