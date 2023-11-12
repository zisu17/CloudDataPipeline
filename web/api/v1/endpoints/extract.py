from fastapi import HTTPException, status
from fastapi import APIRouter

from etl.extract.extract_naver_fashion_keyword import extract_naver_fashion_keyword

router = APIRouter()

@router.post("/naver-trend-keyword")
async def naver_trend_keyword():
    return extract_naver_fashion_keyword()