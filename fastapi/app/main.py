from typing import List

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .pg_database import SessionLocal, engine

#SQLModel test
from .sql_model_example.sql_m_config import SessionLocal2
from .sql_model_example.unified import Stock2
from sqlmodel import select

#This is if we are not using alembic
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_session():
    with SessionLocal2 as session:
        yield session

@app.get("/")
def get_root():
    return ("hello")

#SQLAlchemy Path Operations
@app.get("/stocks/", response_model=List[schemas.Stock])
def read_stocks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stocks = crud.get_stocks(db, skip=skip, limit=limit)
    return stocks

@app.get("/stocks/{stock_id}", response_model=schemas.Stock)
def read_stock(stock_id: int, db: Session = Depends(get_db)):
    db_stock = crud.get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock

@app.post("/stocks/", response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    db_stock = crud.get_stock_by_symbol(db, symbol=stock.symbol)
    if db_stock:
        raise HTTPException(status_code=400, detail="Symbol already registered")
    return crud.create_stock(db=db, stock=stock)

#SQLModel Path Operations
@app.get("/stocks2/", response_model=List[Stock2])
def read_stocks2(*, 
    session: Session = Depends(get_session), 
    offset: int = 0, 
    limit: int = Query(default=100, lte=100),
):

    stocks2 = session.exec(select(Stocks2).offset(offset).limit(limit)).all
    return stocks2