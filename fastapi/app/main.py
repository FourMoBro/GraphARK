from fastapi import FastAPI
from .routes import stock


#SQLModel test
# from .sql_model_example.sql_m_config import SessionLocal2
# from .sql_model_example.unified import Stock2
# from sqlmodel import select

#This is if we are not using alembic
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(stock.router)

@app.get("/")
def get_root():
    return ("hello")


