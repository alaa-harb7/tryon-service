from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from tryon_service.config.base import CONFIG_DIR, ENV_FILE
from tryon_service.config.loader import ConfigLoader


class Settings:
    """
    Central application settings.

    Loads:
    - Environment Variables
    - YAML Configuration Files
    """

    def __init__(self) -> None:
        load_dotenv(ENV_FILE)

        # -----------------------------
        # Environment Variables
        # -----------------------------
        self.mongodb_uri: str = self._get_env("MONGODB_URI")
        self.db_name: str = self._get_env("DB_NAME")

        # -----------------------------
        # YAML Configuration
        # -----------------------------
        self.app: dict[str, Any] = ConfigLoader.load(CONFIG_DIR / "app.yaml")
        self.logging: dict[str, Any] = ConfigLoader.load(CONFIG_DIR / "logging.yaml")
        self.validation: dict[str, Any] = ConfigLoader.load(CONFIG_DIR / "validation.yaml")
        self.models: dict[str, Any] = ConfigLoader.load(CONFIG_DIR / "models.yaml")
        self.storage: dict[str, Any] = ConfigLoader.load(CONFIG_DIR / "storage.yaml")
        self.cloudinary: dict[str, Any] = ConfigLoader.load(
            CONFIG_DIR / "storage.yaml"
        )["cloudinary"]
        self.queue: dict[str, Any] = ConfigLoader.load(CONFIG_DIR / "queue.yaml")
        self.person_detection: dict[str, Any] = ConfigLoader.load(
            CONFIG_DIR / "person_detection.yaml"
        )

    @staticmethod
    def _get_env(key: str) -> str:
        """
        Read a required environment variable.

        Raises:
            RuntimeError: if the variable is missing.
        """
        value = os.getenv(key)

        if not value:
            raise RuntimeError(
                f"Required environment variable '{key}' is missing."
            )

        return value


settings = Settings()