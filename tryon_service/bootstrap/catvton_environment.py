from __future__ import annotations

import sys
from pathlib import Path


class CatVTONEnvironment:
    """
    Prepares the Python environment for importing
    the official CatVTON repository.
    """

    _initialized = False

    @classmethod
    def initialize(cls) -> None:

        if cls._initialized:
            return

        repository = (
            Path("external")
            / "catvton"
        ).resolve()

        repository_str = str(repository)

        if repository_str not in sys.path:
            sys.path.insert(0, repository_str)

        cls._initialized = True