from typing import Optional
from sqlmodel import Field, SQLModel


class Stock2Base(SQLModel):
    symbol : str
    description : str
    figi : str
    type : str

class Stock2(Stock2Base, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)

class Stock2Create(Stock2Base):
    pass

class Stock2Read(Stock2Base):
    id: int
    