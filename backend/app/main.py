import logging

from fastapi import FastAPI
from app.routes import shef, burgers
from app.utils.config import config
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)

logger.info("Starting up backend...")
app = FastAPI(
    title="BunHub API",
    root_path=config.ROOTPATH
)

if config.APP_ENVIRONMENT == "test":
    origins = [
        "http://localhost:3000",  # React dev server
        "http://127.0.0.1:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

logger.info("Attaching routers...")
app.include_router(shef.router, prefix="/shef")
app.include_router(burgers.router, prefix="/burgers")
