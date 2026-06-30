from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class TryOnUserImage(BaseModel):
    """
    Persistent user image entity.
    """

    id: str = Field(default_factory=lambda: str(uuid4()))

    user_id: str

    storage_path: str

    filename: str

    content_type: str

    width: int

    height: int

    size_bytes: int

    status: str = "uploaded"

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)