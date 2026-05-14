📄 3. Документація (README.md)

# 😹 Meme Gallery - Mini Project

Проєкт створено для вивчення FastAPI, роботи з REST API та управління версіями за допомогою Git. 
Це платформа для перегляду, додавання та видалення мемів з можливістю сортування.

## 🚀 Функціонал
- **Backend:** Створено на FastAPI (GET, POST, DELETE запити). Валідація через Pydantic.
- **Frontend:** Vanilla HTML/CSS/JS. Асинхронні запити через `fetch API`.
- **Фічі:**
  - Галерея мемів.
  - Додавання нових мемів через форму.
  - Фільтрація за категоріями.
  - Сортування (найновіші/найстаріші).
  - Видалення мемів.

## 👥 Команда та Розподіл завдань
- **Учасник 1 (Backend):** Розробка API, моделей Pydantic, обробка помилок (FastAPI).
- **Учасник 2 (Frontend):** Верстка, CSS, написання JS для взаємодії з бекендом (`app.js`).
- **Учасник 3 (DevOps/PM):** Налаштування GitHub репозиторію, код-рев'ю, деплой на хостинги, документація.

## 💻 Як запустити локально

### 1. Запуск Backend
Відкрийте термінал у папці `backend`:
```bash
# Створення віртуального середовища (опціонально)
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

# Встановлення залежностей
pip install -r requirements.txt

# Запуск сервера
uvicorn main:app --reload

API буде доступне за адресою: http://localhost:8000 Документація Swagger:
http://localhost:8000/docs

2. Запуск Frontend

Просто відкрийте файл frontend/index.html у вашому браузері або використайте
розширення Live Server у VS Code.

🌍 Посилання на проєкт (Деплой)

  - Frontend: Посилання на Vercel / GitHub Pages
  - Backend API: Посилання на Render / Railway
  - Swagger Docs: Посилання на Render/docs


---

### 🐙 4. GitHub WorkFlow (Інструкція для команди)

Ця частина — покроковий план для управління репозиторієм (завдання для 3-ї людини або для всієї команди):

1. **Створення репозиторію:** 
   Один учасник створює репозиторій на GitHub і запрошує інших у *Settings -> Collaborators*.
2. **Клонування:**
   Усі учасники роблять `git clone <посилання>`.
3. **Робота в гілках:**
   - Backend-розробник: `git checkout -b feature/backend-api`
   - Frontend-розробник: `git checkout -b feature/frontend-ui`
4. **Правильні коміти:**
   - `git commit -m "feat: додано POST запит для створення мема"`
   - `git commit -m "style: покращено вигляд кнопок"`
   - `git commit -m "fix: виправлено помилку CORS"`
5. **Pull Request (PR):**
   - Після завершення фічі розробник пушить гілку (`git push origin feature/назва`).
   - На GitHub створює Pull Request у гілку `main`.
   - Інший учасник дивиться код (Review), пише коментарі та тисне **Approve**, а потім **Merge**.

### ☁️ 5. Інструкція з деплою

**Бекенд (через Render.com):**
1. Створити акаунт на Render.
2. Обрати **New Web Service** -> підключити ваш GitHub репозиторій.
3. Вказати **Root Directory**: `backend`
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Після успішного деплою взяти отриманий URL і замінити ним `http://localhost:8000` у файлі `frontend/app.js` (`const API_URL = '...'`).

**Фронтенд (через GitHub Pages або Vercel):**
- **Vercel:** Зайти на Vercel, імпортувати репозиторій, вказати Root Directory `frontend` і натиснути Deploy.
- **GitHub Pages:** В налаштуваннях репозиторію зайти в *Pages*, обрати гілку `main` і вказати папку `/root` або налаштувати через Actions.
