import secrets

from typing import Any, List, Dict, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, HttpUrl, validator
from starlette.config import Config


class Settings(BaseSettings):
    config = Config(".env")
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    SERVER_NAME: str = "localhost"
    SERVER_HOST: str = "localhost"

    APP_NAME: str = "Farmed4U_API"  # Project name

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:8080",
        "http://localhost",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    DB_SERVER: str = config("DB_SERVER", cast=str, default="localhost")
    DB_USER: str = config("DB_USER", cast=str)
    DB_PASS: str = config("DB_PASS", cast=str)
    DB_PORT: int = config("DB_PORT", cast=int, default=5432)
    DB: str = config("DB", cast=str)
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASS"),
            host=values.get("DB_SERVER"),
            path=f"/{values.get('DB')or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
