from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_pg_sqla

from ..models.stock import Stock
from ..schemas.stock import StockCreate, Stock as STOCK
from sqlalchemy.orm import Session

from typing import List

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"]
)

#Helper Functions
#READ section
def get_stock(db: Session, stock_id: int):
    return db.query(Stock).filter(Stock.id == stock_id).first()


def get_stock_by_symbol(db: Session, symbol: str):
    return db.query(Stock).filter(Stock.symbol == symbol).first()


def get_stocks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Stock).offset(skip).limit(limit).all()

#CREATE section
def create_stock(db: Session, stock: StockCreate):
    db_stock = Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

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
