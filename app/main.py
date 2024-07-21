from fastapi import FastAPI
from src.routes.api import router
from src.config.logger import logger

app = FastAPI()

logger.info("Starting API ...")

app.include_router(router)