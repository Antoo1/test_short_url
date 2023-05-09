from contextlib import asynccontextmanager
from fastapi import FastAPI

from short_url.app.config import config
from short_url.api.views.views import routes
from short_url.app.database import engine
from short_url.app.logging_configuration import init_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine()
    yield
    engine.dispose()


def create_app() -> FastAPI:
    if config.INIT_LOGGING:
        init_logging()

    fastapi_params = {
        'title': config.APP_NAME,
        'lifespan': lifespan,
    }

    app = FastAPI(**fastapi_params)

    app.include_router(
        routes,
        prefix='/v1',
        tags=['v1'],
    )

    return app
