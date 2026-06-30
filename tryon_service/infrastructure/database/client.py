from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorClient

from tryon_service.config.settings import settings


class MongoClientManager:
    """
    MongoDB client lifecycle manager.
    """

    def __init__(self) -> None:
        self._client: AsyncIOMotorClient | None = None

    async def connect(self) -> None:
        if self._client is None:
            self._client = AsyncIOMotorClient(
                settings.mongodb_uri,
            )

    async def disconnect(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None

    @property
    def client(self) -> AsyncIOMotorClient:
        if self._client is None:
            raise RuntimeError(
                "MongoDB client has not been initialized."
            )

        return self._client