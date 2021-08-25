from sqlmodel import Session, SQLModel, create_engine

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
pg_url2 = os.environ.get("PG_URL")

engine = create_engine(pg_url2, echo=True)

SessionLocal2 = Session(engine)