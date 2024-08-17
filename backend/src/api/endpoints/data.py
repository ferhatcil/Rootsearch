from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from api.models import DataRequestNmap, DataRequestScan
from api.services import insert_data, update_data
from redis import Redis
import time

router = APIRouter()
redis = Redis(host="localhost", port=6379, db=0)


@router.post("/scan")
async def scan_scan_data(data: DataRequestScan):
    try:
        data["finished_at"] = time.time()
        data["created_at"] = time.time()
        redis.set(data, data.json())
        results = insert_data(data, "scans")
        return JSONResponse(
            status_code=status.HTTP_201_CREATED, content={"results": results}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"status": "failed", "error": str(e)},
        )


@router.patch("/scan")
async def update_scan_data(data: DataRequestScan):
    finished_at = time.time()
    result = update_data({"scan_id": data.scan_id}, {"finished_at": finished_at})
    if result:
        return {"status": "success"}
    return {"status": "failed"}


@router.post("/store")
async def store_scan_data(data: DataRequestNmap):
    result = insert_data(data, "nmap")
    if result:
        return {"status": "success"}
    return {"status": "failed"}
