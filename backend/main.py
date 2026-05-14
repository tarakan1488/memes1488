from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(
    title="Meme API",
    description="API для сайту з мемами (створення, перегляд, фільтрація)",
    version="1.0.0"
)

# Налаштування CORS (щоб фронтенд міг робити запити до бекенду)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # У продакшені замініть на домен фронтенду
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення маршрутів
app.include_router(router)

# Запуск локально: uvicorn main:app --reload