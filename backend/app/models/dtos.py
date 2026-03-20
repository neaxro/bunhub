from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class DTO_CreateBurger(BaseModel):
    name: str
    description: Optional[str] = None
