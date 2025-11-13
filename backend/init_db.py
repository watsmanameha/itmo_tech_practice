"""
Скрипт инициализации базы данных терминами из глоссария
"""
import json
import os


def create_initial_data():
    """Создание начальных данных глоссария"""

    terms = {
        "singleton": {
            "id": "singleton",
            "term": "Singleton",
            "definition": "Порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа",
            "category": "Порождающие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                }
            ]
        },
        "abstract_factory": {
            "id": "abstract_factory",
            "term": "Abstract Factory",
            "definition": "Порождающий паттерн проектирования, который позволяет создавать семейства связанных объектов, не привязываясь к конкретным классам создаваемых объектов",
            "category": "Порождающие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                },
                {
                    "target_term_id": "factory_method",
                    "relation_type": "связан с",
                    "description": None
                }
            ]
        },
        "factory_method": {
            "id": "factory_method",
            "term": "Factory Method",
            "definition": "Порождающий паттерн проектирования, который определяет общий интерфейс для создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов",
            "category": "Порождающие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                }
            ]
        },
        "strategy": {
            "id": "strategy",
            "term": "Strategy",
            "definition": "Поведенческий паттерн проектирования, который определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми",
            "category": "Поведенческие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                }
            ]
        },
        "observer": {
            "id": "observer",
            "term": "Observer",
            "definition": "Поведенческий паттерн проектирования, который создает механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах",
            "category": "Поведенческие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                }
            ]
        },
        "decorator": {
            "id": "decorator",
            "term": "Decorator",
            "definition": "Структурный паттерн проектирования, который позволяет динамически добавлять объектам новую функциональность, оборачивая их в полезные обёртки",
            "category": "Структурные паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                }
            ]
        },
        "adapter": {
            "id": "adapter",
            "term": "Adapter",
            "definition": "Структурный паттерн проектирования, который позволяет объектам с несовместимыми интерфейсами работать вместе",
            "category": "Структурные паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                }
            ]
        },
        "composite": {
            "id": "composite",
            "term": "Composite",
            "definition": "Структурный паттерн проектирования, который позволяет сгруппировать объекты в древовидную структуру, а затем работать с ними так, как будто это единичный объект",
            "category": "Структурные паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью",
                    "description": None
                }
            ]
        },
        "ast": {
            "id": "ast",
            "term": "Abstract Syntax Tree (AST)",
            "definition": "Древовидное представление абстрактной синтаксической структуры исходного кода, используемое в статическом анализе для распознавания паттернов проектирования",
            "category": "Анализ кода",
            "relations": [
                {
                    "target_term_id": "static_analysis",
                    "relation_type": "используется в",
                    "description": None
                },
                {
                    "target_term_id": "gnn",
                    "relation_type": "преобразуется в",
                    "description": None
                }
            ]
        },
        "gnn": {
            "id": "gnn",
            "term": "Graph Neural Network (GNN)",
            "definition": "Класс нейронных сетей для обработки данных, представленных в виде графов, применяется для анализа AST и распознавания паттернов в коде",
            "category": "Machine Learning",
            "relations": [
                {
                    "target_term_id": "embeddings",
                    "relation_type": "создает",
                    "description": None
                },
                {
                    "target_term_id": "static_analysis",
                    "relation_type": "используется в",
                    "description": None
                }
            ]
        },
        "embeddings": {
            "id": "embeddings",
            "term": "Code Embeddings",
            "definition": "Векторные представления фрагментов кода, полученные с помощью моделей машинного обучения (CodeLlama, DeepSeek Coder), используются для семантического анализа и распознавания паттернов",
            "category": "Machine Learning",
            "relations": [
                {
                    "target_term_id": "feature_extraction",
                    "relation_type": "является результатом",
                    "description": None
                }
            ]
        },
        "static_analysis": {
            "id": "static_analysis",
            "term": "Static Code Analysis",
            "definition": "Метод анализа программного кода без его выполнения, включающий построение AST, анализ зависимостей и извлечение структурных характеристик для распознавания паттернов проектирования",
            "category": "Анализ кода",
            "relations": [
                {
                    "target_term_id": "feature_extraction",
                    "relation_type": "включает в себя",
                    "description": None
                }
            ]
        },
        "feature_extraction": {
            "id": "feature_extraction",
            "term": "Feature Extraction",
            "definition": "Процесс извлечения признаков из исходного кода для последующего использования в ML-моделях распознавания паттернов, включает метрики кода, структурные характеристики и семантическую информацию",
            "category": "Machine Learning",
            "relations": [
                {
                    "target_term_id": "embeddings",
                    "relation_type": "производит",
                    "description": None
                }
            ]
        },
        "gof_patterns": {
            "id": "gof_patterns",
            "term": "GoF Design Patterns",
            "definition": "23 классических паттерна проектирования из книги Gang of Four, разделенные на три категории: порождающие, структурные и поведенческие паттерны",
            "category": "Паттерны проектирования",
            "relations": [
                {
                    "target_term_id": "static_analysis",
                    "relation_type": "распознается через",
                    "description": None
                }
            ]
        }
    }

    data = {"terms": terms}

    # Создание директории если не существует
    os.makedirs("app/data", exist_ok=True)

    # Сохранение в файл
    with open("app/data/glossary.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✓ База данных инициализирована с {len(terms)} терминами")
    print(f"✓ Файл создан: app/data/glossary.json")


if __name__ == "__main__":
    create_initial_data()
