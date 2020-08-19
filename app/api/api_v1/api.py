from fastapi import APIRouter

from app.api.api_v1.endpoints import test

api_router = APIRouter()

# api endpoints
api_router.include_router(test.router)
