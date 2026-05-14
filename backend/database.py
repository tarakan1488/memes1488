from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Render автоматично надасть посилання на базу через змінну оточення
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:zalupadeda228@db.sttlsmpdrcwvkqypvouc.supabase.co:5432/postgres")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Функція для отримання сесії бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()