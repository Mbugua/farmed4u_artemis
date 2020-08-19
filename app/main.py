from fastapi import FastAPI, Request, Response, HTTPException

from starlette.middleware.cors import CORSMiddleware

from app.core.conf import settings
from app.api.api_v1.api import api_router
from app.utils.logging import InterceptHandler, format_record
from app.db.session import SessionLocal, engine
from loguru import logger

from pathlib import Path
import logging
import sys


# config_path = Path(__file__).with_name("logger.json")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=True,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )
    logging.getLogger().handlers = [InterceptHandler()]
    logger.configure(
        handlers=[{"sink": sys.stdout, "level": logging.DEBUG, "format": format_record}]
    )

    # Also set loguru handler for uvicorn loger.
    # Default format:
    # INFO:     127.0.0.1:35238 - "GET / HTTP/1.1" 200 OK
    #
    # New format:
    # 2020-04-18 16:33:49.728 | INFO     | uvicorn.protocols.http.httptools_impl:send:447 - 127.0.0.1:35942 - "GET / HTTP/1.1" 200

    # uvicorn loggers: .error .access .asgi
    # https://github.com/encode/uvicorn/blob/master/uvicorn/config.py#L243
    # logging.getLogger(settings.APP_NAME).handlers = [InterceptHandler()]
    logger.add("log/app.log")
    app.logger = logger

    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    return app


app = create_app()

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal Server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#         request.app.logger.info("response {}",response)
#     finally:
#         request.state.db.close()
#     return response


app.include_router(api_router, prefix=settings.API_V1_STR)
