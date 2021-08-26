from fastapi import Header, HTTPException
from .dbconfig.pg_sqla import SessionLocal

def get_pg_sqla():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()