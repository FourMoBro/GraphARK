from ..models.stock import Stock
from ..schemas.stock import StockCreate, Stock as STOCK
from sqlalchemy.orm import Session

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