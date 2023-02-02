from fastapi import FastAPI, Depends

from .config import config
from ..api.views.views import routes
from .logging_configuration import init_logging


def create_app() -> FastAPI:
    if config.INIT_LOGGING:
        init_logging()

    fastapi_params = {
        'title': config.APP_NAME,
        'redoc_url': None,
    }

    if not config.ENABLE_SWAGGER:
        fastapi_params['openapi_url'] = None
        fastapi_params['docs_url'] = None

    app = FastAPI(**fastapi_params)

    app.include_router(
        routes,
        prefix='/v1',
        tags=['v1'],
    )

    return app
