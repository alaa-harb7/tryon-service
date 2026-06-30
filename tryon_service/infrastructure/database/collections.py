from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorCollection

from tryon_service.infrastructure.database.database import DatabaseManager


class Collections:
    """
    MongoDB collection registry.
    """

    def __init__(
        self,
        database: DatabaseManager,
    ) -> None:
        self._database = database

    @property
    def tryon_jobs(self) -> AsyncIOMotorCollection:
        return self._database.database["tryon_jobs"]

    @property
    def tryon_results(self) -> AsyncIOMotorCollection:
        return self._database.database["tryon_results"]

    @property
    def tryon_user_images(self) -> AsyncIOMotorCollection:
        return self._database.database["tryon_user_images"]

    @property
    def tryon_history(self) -> AsyncIOMotorCollection:
        return self._database.database["tryon_history"]