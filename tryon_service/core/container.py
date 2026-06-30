from __future__ import annotations

from tryon_service.core.models.manager import ModelManager
from tryon_service.infrastructure.database.client import MongoClientManager
from tryon_service.infrastructure.database.collections import Collections
from tryon_service.infrastructure.database.database import DatabaseManager


class Container:

    def __init__(self) -> None:
        self.mongo = MongoClientManager()

        self.database = DatabaseManager(self.mongo)

        self.collections = Collections(self.database)

        self.models = ModelManager()


container = Container()