from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class ConfigLoader:
    """Loads YAML configuration files."""

    @staticmethod
    def load(file_path: Path) -> dict[str, Any]:
        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {file_path}"
            )

        with file_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if data is None:
            return {}

        if not isinstance(data, dict):
            raise ValueError(
                f"{file_path.name} must contain a YAML object."
            )

        return data