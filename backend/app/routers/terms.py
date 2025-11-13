from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models import Term, TermCreate, TermsResponse, CategoryResponse
from app.database import db

router = APIRouter(prefix="/api/terms", tags=["terms"])


@router.get("", response_model=TermsResponse)
async def get_terms(
    skip: int = Query(0, ge=0, description="Количество пропускаемых записей"),
    limit: int = Query(100, ge=1, le=1000, description="Максимальное количество записей")
):
    """Получить все термины с пагинацией"""
    terms = db.get_all_terms(skip=skip, limit=limit)
    total = db.count_terms()
    return TermsResponse(total=total, items=terms)


@router.get("/search", response_model=List[Term])
async def search_terms(
    q: str = Query(..., min_length=1, description="Поисковый запрос")
):
    """Поиск терминов по названию или определению"""
    results = db.search_terms(q)
    return results


@router.get("/categories", response_model=CategoryResponse)
async def get_categories():
    """Получить список всех категорий"""
    categories = db.get_categories()
    return CategoryResponse(categories=categories)


@router.get("/category/{category}", response_model=List[Term])
async def get_terms_by_category(category: str):
    """Получить термины по категории"""
    terms = db.get_terms_by_category(category)
    return terms


@router.get("/{term_id}", response_model=Term)
async def get_term(term_id: str):
    """Получить термин по ID"""
    term = db.get_term_by_id(term_id)
    if not term:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return term


@router.post("", response_model=Term, status_code=201)
async def create_term(term: TermCreate):
    """Создать новый термин"""
    return db.create_term(term)


@router.put("/{term_id}", response_model=Term)
async def update_term(term_id: str, term: TermCreate):
    """Обновить термин"""
    updated_term = db.update_term(term_id, term)
    if not updated_term:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return updated_term


@router.delete("/{term_id}", status_code=204)
async def delete_term(term_id: str):
    """Удалить термин"""
    success = db.delete_term(term_id)
    if not success:
        raise HTTPException(status_code=404, detail="Термин не найден")
