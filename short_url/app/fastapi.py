from fastapi import FastAPI, Depends
# from markdown2 import markdown_path
from starlette.middleware.base import BaseHTTPMiddleware

from .config import config
from ..api.views.views import routes
# from .dependencies import require_request_id
# from .exception_handlers import setup_exception_handlers
# from .health_check import healthcheck_route
from .logging_configuration import init_logging
# from .headers_filter import set_headers_context_middleware


def create_app() -> FastAPI:
    if config.INIT_LOGGING:
        init_logging()

    fastapi_params = {
        'title': config.APP_NAME,
        # 'description': markdown_path(config.README_PATH),
        'redoc_url': None,
    }

    if not config.ENABLE_SWAGGER:
        fastapi_params['openapi_url'] = None
        fastapi_params['docs_url'] = None

    app = FastAPI(**fastapi_params)
    # Порядок регистрации middleware ниже важен.
    # setup_exception_handlers(app)
    # app.add_middleware(BaseHTTPMiddleware, dispatch=set_headers_context_middleware)
    # app.add_middleware(BaseHTTPMiddleware, dispatch=handle_request_id_middleware)

    # app.include_router(healthcheck_route)
    app.include_router(
        routes,  # noqa F405
        prefix='/v1',
        tags=['v1'],
        # dependencies=[Depends(require_request_id)]
    )

    return app
