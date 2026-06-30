from __future__ import annotations


class ModelNotLoadedError(RuntimeError):
    """
    Raised when a requested AI model has not been loaded.
    """