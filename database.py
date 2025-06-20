# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from logger import logger


# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

# Create database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
logger.info("📦 Database engine created")


# SessionLocal will be used to interact with the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()
logger.info("🗂️  Base class for models declared")
