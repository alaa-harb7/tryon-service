from fastapi import Request
from fastapi.responses import JSONResponse

from tryon_service.api.exceptions.schemas import ErrorResponse
from tryon_service.services.tryon.validation import (
    VirtualTryOnValidationError,
)

from tryon_service.core.exceptions import ValidationException


async def validation_exception_handler(
    request: Request,
    exc: ValidationException,
):
    code = getattr(exc, "code", "VALIDATION_ERROR")
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            success=False,
            error={
                "code": code,
                "message": exc.message,
            },
        ).model_dump(),
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            success=False,
            error={
                "code": "INTERNAL_ERROR",
                "message": "Internal Server Error",
            },
        ).model_dump(),
    )