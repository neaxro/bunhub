from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class Statuse(BaseModel):
    status_id: int
    name: str

class Burger(BaseModel):
    burger_id: int
    name: str
    description: Optional[str]

class Ingredient(BaseModel):
    ingredient_id: int
    name: str
    is_available: Optional[bool] = True

class BurgerIngredients(BaseModel):
    burger_id: int
    ingredient_id: int
    quantity: Optional[int] = 1

class Order(BaseModel):
    order_id: int
    burger_id: int
    status_id: int
    guest_name: str
    email: Optional[str] = None
    comment: Optional[str] = None
    created_at: datetime

class BurgerRead(Burger):
    class Config:
        from_attributes = True

class IngredientRead(Ingredient):
    class Config:
        from_attributes = True

class BurgerDetailed(Burger):
    ingredients: List[IngredientRead]

