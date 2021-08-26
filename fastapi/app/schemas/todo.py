from pydantic import BaseModel, Field
from typing import Optional

import uuid

class Todo(BaseModel):
    title: str
    description: str
    completed: bool

# class StockBase(BaseModel):
#     symbol: str
#     description: Optional[str] = None
#     figi: Optional[str] = None
#     type: Optional[str] = None

# class StockCreate(StockBase):
#     pass

# class Stock(StockBase):
#     id: int
        
