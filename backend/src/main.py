from fastapi import FastAPI
from api.endpoints import data_router

app = FastAPI()

app.include_router(data_router, prefix="/data", tags=["Data"])

@app.get("/")
async def root():
    return {"message": "Welcome to Rootsearch API"}
