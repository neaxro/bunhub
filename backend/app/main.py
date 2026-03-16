import logging

from fastapi import FastAPI
from app.routes import shef
from app.utils.config import config

logger = logging.getLogger(__name__)

logger.info("Starting up backend...")
app = FastAPI(
    title="BunHub API",
    root_path=config.ROOTPATH
)

logger.info("Attaching routers...")
app.include_router(shef.router, prefix="/shef")
