from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

# Модель для отримання даних від користувача (POST)
class MemeCreate(BaseModel):
    title: str
    image_url: str # Використовуємо звичайний рядок для простоти, але можна HttpUrl
    category: str

# Модель для відправки даних на фронтенд (GET)
class MemeResponse(BaseModel):
    id: int
    title: str
    image_url: str
    category: str
    created_at: datetime
