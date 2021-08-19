
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .pg_database import Base

#description, symbol, figi, type
class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    description = Column(String)
    figi = Column(String)
    type = Column(String)


