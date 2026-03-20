import logging
from fastapi import APIRouter, HTTPException
from app.service.burgers import burgerService
from app.models.dtos import DTO_CreateBurger

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/", status_code=200)
async def get_all_burgers(offest: int = 0, limit: int = 10):
    burgers = await burgerService.get_burgers(offest, limit)
    return burgers

@router.get("/{id}", status_code=200)
async def get_burger(id: int):
    try:
        burger = await burgerService.get_burger(id)
        return burger
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.post("/", status_code=201)
async def insert_burger(burger: DTO_CreateBurger):
    return {"burger_data": burger}

@router.delete("/{id}", status_code=204)
async def delete_burger(id: int):
    return f"Delete burger with ID: {id}"
