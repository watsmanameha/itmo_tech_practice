# Backend - Glossary API

FastAPI приложение для управления глоссарием терминов электронного документооборота.

## Технологии

- **FastAPI** - веб-фреймворк
- **Pydantic** - валидация данных
- **Uvicorn** - ASGI сервер
- **JSON** - хранение данных

## Установка и запуск

### 1. Создание виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate  # Windows
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Инициализация базы данных

```bash
python init_db.py
```

### 4. Запуск сервера

```bash
uvicorn app.main:app --reload --port 8000
```

Сервер будет доступен по адресу: http://localhost:8000

## API Документация

После запуска сервера документация доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Получить все термины
```
GET /api/terms?skip=0&limit=100
```

### Поиск терминов
```
GET /api/terms/search?q=документ
```

### Получить термин по ID
```
GET /api/terms/{term_id}
```

### Получить категории
```
GET /api/terms/categories
```

### Получить термины по категории
```
GET /api/terms/category/{category}
```

### Создать термин
```
POST /api/terms
```

### Обновить термин
```
PUT /api/terms/{term_id}
```

### Удалить термин
```
DELETE /api/terms/{term_id}
```

## Структура проекта

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI приложение
│   ├── models.py            # Pydantic модели
│   ├── database.py          # Работа с данными
│   ├── routers/
│   │   ├── __init__.py
│   │   └── terms.py         # API endpoints
│   └── data/
│       └── glossary.json    # Данные глоссария
├── requirements.txt
├── Dockerfile
└── init_db.py              # Скрипт инициализации БД
```

## Docker

### Сборка образа
```bash
docker build -t glossary-api .
```

### Запуск контейнера
```bash
docker run -p 8000:8000 glossary-api
```
