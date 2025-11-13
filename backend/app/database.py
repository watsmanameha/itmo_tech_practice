import json
import os
from typing import List, Optional
from app.models import Term, TermCreate, Relation


class Database:
    """Простая JSON-based база данных для терминов"""

    def __init__(self, db_path: str = "app/data/glossary.json"):
        self.db_path = db_path
        self.data: dict = {"terms": {}}
        self._load()

    def _load(self):
        """Загрузка данных из файла"""
        if os.path.exists(self.db_path):
            with open(self.db_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self._save()

    def _save(self):
        """Сохранение данных в файл"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def get_all_terms(self, skip: int = 0, limit: int = 100) -> List[Term]:
        """Получить все термины с пагинацией"""
        terms_list = list(self.data["terms"].values())
        return [Term(**term) for term in terms_list[skip:skip + limit]]

    def get_term_by_id(self, term_id: str) -> Optional[Term]:
        """Получить термин по ID"""
        term_data = self.data["terms"].get(term_id)
        if term_data:
            return Term(**term_data)
        return None

    def search_terms(self, query: str) -> List[Term]:
        """Поиск терминов по названию или определению"""
        query_lower = query.lower()
        results = []
        for term_data in self.data["terms"].values():
            if (query_lower in term_data["term"].lower() or
                query_lower in term_data["definition"].lower()):
                results.append(Term(**term_data))
        return results

    def get_terms_by_category(self, category: str) -> List[Term]:
        """Получить термины по категории"""
        results = []
        for term_data in self.data["terms"].values():
            if term_data.get("category") == category:
                results.append(Term(**term_data))
        return results

    def get_categories(self) -> List[str]:
        """Получить список всех категорий"""
        categories = set()
        for term_data in self.data["terms"].values():
            if term_data.get("category"):
                categories.add(term_data["category"])
        return sorted(list(categories))

    def create_term(self, term: TermCreate) -> Term:
        """Создать новый термин"""
        # Генерируем ID из названия термина
        term_id = term.term.lower().replace(" ", "_")

        term_dict = term.model_dump()
        term_dict["id"] = term_id

        self.data["terms"][term_id] = term_dict
        self._save()

        return Term(**term_dict)

    def update_term(self, term_id: str, term: TermCreate) -> Optional[Term]:
        """Обновить термин"""
        if term_id not in self.data["terms"]:
            return None

        term_dict = term.model_dump()
        term_dict["id"] = term_id

        self.data["terms"][term_id] = term_dict
        self._save()

        return Term(**term_dict)

    def delete_term(self, term_id: str) -> bool:
        """Удалить термин"""
        if term_id in self.data["terms"]:
            del self.data["terms"][term_id]
            self._save()
            return True
        return False

    def count_terms(self) -> int:
        """Получить количество терминов"""
        return len(self.data["terms"])


# Singleton instance
db = Database()
