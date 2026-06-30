from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")


@dataclass(slots=True)
class Result(Generic[T]):
    """
    Represents the result of an operation.
    """

    is_success: bool
    value: T | None = None
    error: str | None = None

    @classmethod
    def success(cls, value: T) -> "Result[T]":
        return cls(
            is_success=True,
            value=value,
            error=None,
        )

    @classmethod
    def failure(cls, error: str) -> "Result[T]":
        return cls(
            is_success=False,
            value=None,
            error=error,
        )