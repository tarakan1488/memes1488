from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db, engine, Base
import models

# Створюємо таблиці в базі при запуску, якщо їх ще немає
Base.metadata.create_all(bind=engine)

router = APIRouter()

# 1. GET: Отримати всі меми (з фільтрацією та сортуванням)
@router.get("/memes", response_model=List[models.MemeResponse])
def get_memes(
    category: Optional[str] = None, 
    sort_by: str = Query("desc", description="asc або desc"),
    db: Session = Depends(get_db)
):
    query = db.query(models.MemeDB)
    
    # Фільтрація за категорією
    if category:
        query = query.filter(models.MemeDB.category == category)
        
    # Сортування за давністю
    if sort_by == "desc":
        query = query.order_by(models.MemeDB.created_at.desc())
    else:
        query = query.order_by(models.MemeDB.created_at.asc())
        
    return query.all()

# 2. GET: Отримати список унікальних категорій
@router.get("/categories", response_model=List[str])
def get_categories(db: Session = Depends(get_db)):
    # Витягуємо всі унікальні категорії з бази
    categories = db.query(models.MemeDB.category).distinct().all()
    # Перетворюємо результат у звичайний список рядків
    return [cat[0] for cat in categories if cat[0]]

# 3. GET: Отримати мем за ID (обробка помилки)
@router.get("/memes/{meme_id}", response_model=models.MemeResponse)
def get_meme(meme_id: int, db: Session = Depends(get_db)):
    meme = db.query(models.MemeDB).filter(models.MemeDB.id == meme_id).first()
    if not meme:
        raise HTTPException(status_code=404, detail="Мем не знайдено")
    return meme

# 4. POST: Додати новий мем (БЕЗ ПАРОЛЯ)
@router.post("/memes", response_model=models.MemeResponse, status_code=201)
def create_meme(meme: models.MemeCreate, db: Session = Depends(get_db)):
    # Створюємо запис у базі
    db_meme = models.MemeDB(
        title=meme.title,
        image_url=meme.image_url,
        category=meme.category
    )
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme

# 5. DELETE: Видалити мем (БЕЗ ПАРОЛЯ)
@router.delete("/memes/{meme_id}", status_code=204)
def delete_meme(meme_id: int, db: Session = Depends(get_db)):
    meme = db.query(models.MemeDB).filter(models.MemeDB.id == meme_id).first()
    if not meme:
        raise HTTPException(status_code=404, detail="Мем не знайдено, неможливо видалити")
    
    db.delete(meme)
    db.commit()
    return {"message": "Успішно видалено"}