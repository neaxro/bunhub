import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/")
async def login():
    return "Chef admin console"
