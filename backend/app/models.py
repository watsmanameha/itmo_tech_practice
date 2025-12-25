from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class RelationType(str, Enum):
    """Типы связей между терминами"""
    HAS = "имеет"
    IS_PART_OF = "является частью"
    CHARACTERIZES = "характеризует"
    PARTICIPATES_IN = "участвует в"
    INCLUDES = "включает в себя"
    CONTAINS = "вмещает в себя"
    IS_SUBTASK = "является подзадачей"
    IS_SUBPROPERTY = "является подсвойством"
    IS_PROPERTY = "имеет свойство"
    RELATED_TO = "связан с"
    USED_IN = "используется в"
    TRANSFORMS_TO = "преобразуется в"
    CREATES = "создает"
    IS_RESULT_OF = "является результатом"
    PRODUCES = "производит"
    RECOGNIZED_BY = "распознается через"


class Relation(BaseModel):
    """Связь между терминами"""
    target_term_id: str = Field(..., description="ID целевого термина")
    relation_type: RelationType = Field(..., description="Тип связи")
    description: Optional[str] = Field(None, description="Дополнительное описание связи")


class TermBase(BaseModel):
    """Базовая модель термина"""
    term: str = Field(..., description="Название термина", min_length=1)
    definition: str = Field(..., description="Определение термина", min_length=1)
    category: Optional[str] = Field(None, description="Категория термина")
    relations: List[Relation] = Field(default_factory=list, description="Связи с другими терминами")
    sources: List[str] = Field(default_factory=list, description="Список источников (URL)")


class TermCreate(TermBase):
    """Модель для создания термина"""
    pass


class Term(TermBase):
    """Полная модель термина"""
    id: str = Field(..., description="Уникальный идентификатор термина")

    class Config:
        from_attributes = True


class TermsResponse(BaseModel):
    """Ответ со списком терминов"""
    total: int = Field(..., description="Общее количество терминов")
    items: List[Term] = Field(..., description="Список терминов")


class CategoryResponse(BaseModel):
    """Ответ со списком категорий"""
    categories: List[str] = Field(..., description="Список категорий")
