from app.repository.postgres import PostgresRepository
from app.models.models import (
    BurgerRead,
    BurgerDetailed
)
from typing import List, Union

class BurgerService():
    def __init__(self):
        self.repository = PostgresRepository()

    async def get_burgers(self, offset: int, limit: int) -> List[BurgerRead]:
        burgers = self.repository.get_burgers(offset, limit)

        return burgers
    
    async def get_burger(self, burger_id: int) -> Union[BurgerDetailed, None]:
        ingredients = self.repository.get_burger_ingredients(burger_id)
        burger = self.repository.get_burger_by_id(burger_id)

        if not burger:
            raise Exception(f"Burger not found with ID: {burger_id}")
        
        return BurgerDetailed(
            **burger.model_dump(),
            ingredients=ingredients
        )

burgerService = BurgerService()
