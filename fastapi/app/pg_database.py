from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
pg_url2 = os.environ.get("PG_URL")

engine = create_engine(pg_url2)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()