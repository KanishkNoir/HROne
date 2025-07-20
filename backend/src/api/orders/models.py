from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    productId: str
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[Item]
    