from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import terms

app = FastAPI(
    title="Glossary API",
    description="API для глоссария терминов электронного документооборота",
    version="1.0.0"
)

# CORS настройки для работы с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(terms.router)


@app.get("/")
async def root():
    """Корневой endpoint"""
    return {
        "message": "Glossary API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    """Проверка работоспособности"""
    return {"status": "ok"}
