from fastapi import APIRouter
from api.models import DataRequestNmap
from api.services import insert_data

router = APIRouter()

@router.post("/store/nmap")
async def store_cpu_data(data: DataRequestNmap):
    result = insert_data(data, "nmap")
    if result:
        return {"status": "success"}
    return {"status": "failed"}

