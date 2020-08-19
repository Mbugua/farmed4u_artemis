from typing import Generator
from app.db.session import SessionLocal
from app.core.conf import settings

from fastapi import Response, Request

# python ^3.7 use yield
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# def get_db(request: Request):
#     return request.state.db
