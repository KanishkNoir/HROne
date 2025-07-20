from pydantic import BaseModel
from typing import List

class Size(BaseModel):
    size: str 
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[Size]