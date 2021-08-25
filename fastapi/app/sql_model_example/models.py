from typing import Optional
from sqlmodel import Field, SQLModel


class Stock2(SQLModel, table=True):
    id = Optional[int] = Field(default=None, primary_key=True)
    symbol = str
    description = str
    figi = str
    type = str