from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import pg_crud, pg_models, pg_schemas
from .pg_database import SessionLocal, engine

#This is if we are not using alembic
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_pgdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def get_root():
    return ("hello")

@app.get("/stocks/", response_model=List[pg_schemas.Stock])
def read_stocks(skip: int = 0, limit: int = 100, db: Session = Depends(get_pgdb)):
    stocks = pg_crud.get_stocks(db, skip=skip, limit=limit)
    return stocks

@app.get("/stocks/{stock_id}", response_model=pg_schemas.Stock)
def read_stock(stock_id: int, db: Session = Depends(get_pgdb)):
    db_stock = pg_crud.get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock

@app.post("/stocks/", response_model=pg_schemas.Stock)
def create_stock(stock: pg_schemas.StockCreate, db: Session = Depends(get_pgdb)):
    db_stock = pg_crud.get_stock_by_symbol(db, symbol=stock.symbol)
    if db_stock:
        raise HTTPException(status_code=400, detail="Symbol already registered")
    return pg_crud.create_stock(db=db, stock=stock)