from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class RequestContext(BaseModel):

    request_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    user_id: str | None = None

    trace_id: str | None = None

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    garment_type: str = "upper"