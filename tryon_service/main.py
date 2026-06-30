from fastapi import FastAPI

from tryon_service.api.router import router
from fastapi.staticfiles import StaticFiles

from tryon_service.api.exceptions.handlers import (
    validation_exception_handler,
    unhandled_exception_handler,
)

from tryon_service.core.exceptions import ValidationException
from tryon_service.api.middleware.logging import (
    LoggingMiddleware,
)
from tryon_service.api.middleware.request_id import (
    RequestIdMiddleware,
)

from tryon_service.api.main import lifespan

app = FastAPI(
    title="Try-On Service",
    lifespan=lifespan,
)
app.add_middleware(
    RequestIdMiddleware,
)

app.add_middleware(
    LoggingMiddleware,
)
app.add_exception_handler(
    ValidationException,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    unhandled_exception_handler,
)


app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs",
)

app.include_router(router)