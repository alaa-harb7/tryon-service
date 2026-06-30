from __future__ import annotations


class TryOnException(Exception):
    """
    Base exception for the TryOn Service.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ConfigurationException(TryOnException):
    """
    Raised when configuration loading fails.
    """


class ValidationException(TryOnException):
    """
    Raised when validation fails.
    """

    def __init__(self, message: str, code: str = "VALIDATION_ERROR"):
        self.code = code
        super().__init__(message)


class ProviderException(TryOnException):
    """
    Raised when an AI provider fails.
    """


class StorageException(TryOnException):
    """
    Raised when storage operations fail.
    """


class PipelineException(TryOnException):
    """
    Raised when a pipeline execution fails.
    """