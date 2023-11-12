from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from web.schema.response import Response


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=Response(resultCode=422, resultMsg="error", resultData={"errorMsg": "Validation error"}).dict(),
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 500:
        return JSONResponse(
            status_code=500,
            content=Response(resultCode=500, resultMsg="error", resultData={"errorMsg": "Internal Server Error"}).dict(),
        )
    return JSONResponse(
        status_code=exc.status_code,
        content=Response(resultCode=exc.status_code, resultMsg="error", resultData={"errorMsg": str(exc.detail)}).dict(),
    )
