from fastapi import APIRouter

from api.endpoints.data import router as data_router

router = APIRouter()

router.include_router(data_router)
