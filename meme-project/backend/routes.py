from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from models import MemeCreate, MemeResponse

router = APIRouter()

# Імітація бази даних (in-memory)
db_memes = [
    {
        "id": 1,
        "title": "Коли код запрацював з першого разу",
        "image_url": "https://i.imgflip.com/1g8my4.jpg",
        "category": "IT",
        "created_at": datetime(2023, 10, 1, 12, 0, 0)
    },
    {
        "id": 2,
        "title": "Очікування vs Реальність",
        "image_url": "https://i.imgflip.com/2wifvo.jpg",
        "category": "Життя",
        "created_at": datetime(2023, 10, 2, 15, 30, 0)
    }
]
current_id = 2

# 1. GET: Отримати всі меми (з фільтрацією та сортуванням)
@router.get("/memes", response_model=List[MemeResponse])
def get_memes(
    category: Optional[str] = None, 
    sort_by: str = Query("desc", description="asc або desc")
):
    result = db_memes.copy()
    
    # Фільтрація за категорією
    if category:
        result = [m for m in result if m["category"].lower() == category.lower()]
        
    # Сортування за давністю
    if sort_by == "desc":
        result.sort(key=lambda x: x["created_at"], reverse=True) # Найновіші перші
    else:
        result.sort(key=lambda x: x["created_at"]) # Найстаріші перші
        
    return result

# 2. GET: Отримати список унікальних категорій
@router.get("/categories", response_model=List[str])
def get_categories():
    categories = set(m["category"] for m in db_memes)
    return list(categories)

# 3. GET: Отримати мем за ID (обробка помилки)
@router.get("/memes/{meme_id}", response_model=MemeResponse)
def get_meme(meme_id: int):
    for meme in db_memes:
        if meme["id"] == meme_id:
            return meme
    raise HTTPException(status_code=404, detail="Мем не знайдено")

# 4. POST: Додати новий мем
@router.post("/memes", response_model=MemeResponse, status_code=201)
def create_meme(meme: MemeCreate):
    global current_id
    current_id += 1
    
    new_meme = {
        "id": current_id,
        "title": meme.title,
        "image_url": meme.image_url,
        "category": meme.category,
        "created_at": datetime.now()
    }
    db_memes.append(new_meme)
    return new_meme

# 5. DELETE: Видалити мем
@router.delete("/memes/{meme_id}", status_code=204)
def delete_meme(meme_id: int):
    global db_memes
    initial_length = len(db_memes)
    db_memes = [m for m in db_memes if m["id"] != meme_id]
    
    if len(db_memes) == initial_length:
        raise HTTPException(status_code=404, detail="Мем не знайдено, неможливо видалити")
    return {"message": "Успішно видалено"}