from pydantic import BaseModel


class Response(BaseModel):
    resultCode: int
    resultMsg: str
    resultData: dict
