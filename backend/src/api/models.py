from pydantic import BaseModel


class DataRequestScan(BaseModel):
    name: str
    description: str
    range: str


class DataRequestNmap(BaseModel):
    pass
