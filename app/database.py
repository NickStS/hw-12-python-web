from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings


DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
