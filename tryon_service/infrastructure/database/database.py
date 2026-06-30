from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorDatabase

from tryon_service.config.settings import settings
from tryon_service.infrastructure.database.client import MongoClientManager


class DatabaseManager:
    """
    MongoDB database accessor.
    """

    def __init__(
        self,
        client_manager: MongoClientManager,
    ) -> None:
        self._client_manager = client_manager

    @property
    def database(self) -> AsyncIOMotorDatabase:
        return self._client_manager.client[
            settings.db_name
        ]