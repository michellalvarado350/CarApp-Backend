from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DATABASE_URL
from dotenv import load_dotenv
import os

load_dotenv()

SQL_DATABASE_URL = os.getenv("DATABASE_URL")

if SQL_DATABASE_URL.startswith("postgres://"):
    SQL_DATABASE_URL = SQL_DATABASE_URL.replace(
        "postgres://",
        "postgresql://"
    )

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()
