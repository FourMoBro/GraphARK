from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_pg_sqla

from sqlalchemy.orm import Session

from typing import List

from ..cruds.stock import get_stock, get_stock_by_symbol, get_stocks, create_stock
from ..schemas.stock import StockCreate, Stock as STOCK

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"]
)



#Path Operations
@router.get("/", response_model=List[STOCK])
async def read_stocks(skip: int = 0, limit: int = 100, db: Session = Depends(get_pg_sqla)):
    stocks = get_stocks(db, skip=skip, limit=limit)
    return stocks

@router.get("/{stock_id}", response_model=STOCK)
async def read_stock(stock_id: int, db: Session = Depends(get_pg_sqla)):
    db_stock = get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock

@router.post("/", response_model=STOCK)
async def create_stock(stock: StockCreate, db: Session = Depends(get_pg_sqla)):
    db_stock = get_stock_by_symbol(db, symbol=stock.symbol)
    if db_stock:
        raise HTTPException(status_code=400, detail="Symbol already registered")
    return create_stock(db=db, stock=stock)
