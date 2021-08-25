from sqlalchemy.orm import Session

from . import pg_models, pg_schemas


#READ section
def get_stock(db: Session, stock_id: int):
    return db.query(pg_models.Stock).filter(pg_models.Stock.id == stock_id).first()


def get_stock_by_symbol(db: Session, symbol: str):
    return db.query(pg_models.Stock).filter(pg_models.Stock.symbol == symbol).first()


def get_stocks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(pg_models.Stock).offset(skip).limit(limit).all()


#CREATE section
def create_stock(db: Session, stock: pg_schemas.StockCreate):
    db_stock = pg_models.Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock


