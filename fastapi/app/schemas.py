from pydantic import BaseModel
from typing import List, Optional

class StockBase(BaseModel):
    symbol: str
    description: Optional[str] = None

#When creating a stock, these columns must be specified
class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int

    class Config:
        orm_mode = True