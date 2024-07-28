from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.src.routes.api import router
from app.src.config.logger import logger
from .app_exception import CustomException

app = FastAPI()

logger.info("Starting API ...")

@app.exception_handler(404)
def not_found_exception_handler(request: Request, exc: HTTPException):
    return not_found_error(request, exc)

@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.statusCode,
        content={"message": f"Oops! {exc.message}."},
    )


# Define a custom error handler for 404
def not_found_error(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": exc.detail or "The requested resource was not found."
        },
    )

app.include_router(router)