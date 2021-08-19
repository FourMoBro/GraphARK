from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
pg_url2 = os.environ.get("PG_URL")

engine=create_engine(pg_url2,
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)