from __future__ import annotations

import time

from starlette.middleware.base import BaseHTTPMiddleware

from tryon_service.logging.logger import (
    get_logger,
)


logger = get_logger("HTTP")


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next,
    ):
        start = time.perf_counter()

        response = await call_next(request)

        elapsed = time.perf_counter() - start

        request_id = getattr(
            request.state,
            "request_id",
            "unknown",
        )

        logger.info(
            "[%s] %s %s -> %s (%.2fs)",
            request_id,
            request.method,
            request.url.path,
            response.status_code,
            elapsed,
        )

        return response