from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from pydantic import BaseModel
from database import Base

# --- СХЕМА ДЛЯ БАЗИ ДАНИХ (SQLAlchemy) ---
class MemeDB(Base):
    __tablename__ = "memes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    image_url = Column(String)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# --- СХЕМИ ДЛЯ ПЕРЕДАЧІ ДАНИХ (Pydantic) ---
class MemeCreate(BaseModel):
    title: str
    image_url: str
    category: str

class MemeResponse(BaseModel):
    id: int
    title: str
    image_url: str
    category: str
    created_at: datetime

    class Config:
        from_attributes = True  # Дозволяє Pydantic читати дані з бази
