import uvicorn
import uuid
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from databases import Database

DB_URL = "postgresql://postgres:postgres@0.0.0.0:5432/postgres"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(engine, expire_on_commit=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(engine)

app = FastAPI()

if __name__ == "__main__":
   uvicorn.run("main:app")