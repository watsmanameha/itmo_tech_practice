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
            "term": "Одиночка (Singleton)",
            "definition": "Порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа",
            "category": "Порождающие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "abstract_factory": {
            "id": "abstract_factory",
            "term": "Абстрактная фабрика (Abstract Factory)",
            "definition": "Порождающий паттерн проектирования, который позволяет создавать семейства связанных объектов, не привязываясь к конкретным классам создаваемых объектов",
            "category": "Порождающие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                },
                {
                    "target_term_id": "factory_method",
                    "relation_type": "связан с"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "factory_method": {
            "id": "factory_method",
            "term": "Фабричный метод (Factory Method)",
            "definition": "Порождающий паттерн проектирования, который определяет общий интерфейс для создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов",
            "category": "Порождающие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "strategy": {
            "id": "strategy",
            "term": "Стратегия (Strategy)",
            "definition": "Поведенческий паттерн проектирования, который определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми",
            "category": "Поведенческие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "observer": {
            "id": "observer",
            "term": "Наблюдатель (Observer)",
            "definition": "Поведенческий паттерн проектирования, который создает механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах",
            "category": "Поведенческие паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "decorator": {
            "id": "decorator",
            "term": "Декоратор (Decorator)",
            "definition": "Структурный паттерн проектирования, который позволяет динамически добавлять объектам новую функциональность, оборачивая их в полезные обёртки",
            "category": "Структурные паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "adapter": {
            "id": "adapter",
            "term": "Адаптер (Adapter)",
            "definition": "Структурный паттерн проектирования, который позволяет объектам с несовместимыми интерфейсами работать вместе",
            "category": "Структурные паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "composite": {
            "id": "composite",
            "term": "Компоновщик (Composite)",
            "definition": "Структурный паттерн проектирования, который позволяет сгруппировать объекты в древовидную структуру, а затем работать с ними так, как будто это единичный объект",
            "category": "Структурные паттерны",
            "relations": [
                {
                    "target_term_id": "gof_patterns",
                    "relation_type": "является частью"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268."
            ]
        },
        "ast": {
            "id": "ast",
            "term": "Абстрактное синтаксическое дерево (AST)",
            "definition": "Древовидное представление абстрактной синтаксической структуры исходного кода, используемое в статическом анализе для распознавания паттернов проектирования",
            "category": "Анализ кода",
            "relations": [
                {
                    "target_term_id": "static_analysis",
                    "relation_type": "используется в"
                },
                {
                    "target_term_id": "gnn",
                    "relation_type": "преобразуется в"
                }
            ],
            "sources": [
                "Spinellis D. Code Reading: The Open Source Perspective. – Addison-Wesley, 2003. – 512 с.",
                "Mou L., Li G., Zhang L., Wang T., Jin Z. Convolutional Neural Networks over Tree Structures for Programming Language Processing // AAAI. – 2016. – С. 1287–1293."
            ]
        },
        "gnn": {
            "id": "gnn",
            "term": "Графовая нейронная сеть (GNN)",
            "definition": "Класс нейронных сетей для обработки данных, представленных в виде графов, применяется для анализа AST и распознавания паттернов в коде",
            "category": "Машинное обучение",
            "relations": [
                {
                    "target_term_id": "embeddings",
                    "relation_type": "создает"
                },
                {
                    "target_term_id": "static_analysis",
                    "relation_type": "используется в"
                }
            ],
            "sources": [
                "Mou L., Li G., Zhang L., Wang T., Jin Z. Convolutional Neural Networks over Tree Structures for Programming Language Processing // AAAI. – 2016. – С. 1287–1293.",
                "Zhang Y., Wang H., et al. A survey on deep learning-based software vulnerability detection // IEEE Access. – 2020. – Т. 7. – С. 103251–103272."
            ]
        },
        "embeddings": {
            "id": "embeddings",
            "term": "Векторные представления (Code Embeddings)",
            "definition": "Векторные представления фрагментов кода, полученные с помощью моделей машинного обучения (CodeLlama, DeepSeek Coder), используются для семантического анализа и распознавания паттернов",
            "category": "Машинное обучение",
            "relations": [
                {
                    "target_term_id": "feature_extraction",
                    "relation_type": "является результатом"
                }
            ],
            "sources": [
                "Alon U., Zilberstein M., Levy O., Yahav E. code2vec: Learning Distributed Representations of Code // POPL. – 2019.",
                "Vaswani A., Shazeer N., Parmar N., et al. Attention is All You Need // Proc. NeurIPS. – 2017.",
                "Devlin J., Chang M. W., Lee K., Toutanova K. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding // NAACL. – 2019."
            ]
        },
        "static_analysis": {
            "id": "static_analysis",
            "term": "Статический анализ кода (Static Code Analysis)",
            "definition": "Метод анализа программного кода без его выполнения, включающий построение AST, анализ зависимостей и извлечение структурных характеристик для распознавания паттернов проектирования",
            "category": "Анализ кода",
            "relations": [
                {
                    "target_term_id": "feature_extraction",
                    "relation_type": "включает в себя"
                }
            ],
            "sources": [
                "Spinellis D. Code Reading: The Open Source Perspective. – Addison-Wesley, 2003. – 512 с.",
                "Poshyvanyk D., Marcus A. The Conceptual Cohesion of Classes // ICSE. – 2006. – С. 320–329.",
                "Tsantalis N., Chatzigeorgiou A. Identification of Move Method Refactoring Opportunities // IEEE Trans. Software Eng. – 2011."
            ]
        },
        "feature_extraction": {
            "id": "feature_extraction",
            "term": "Извлечение признаков (Feature Extraction)",
            "definition": "Процесс извлечения признаков из исходного кода для последующего использования в ML-моделях распознавания паттернов, включает метрики кода, структурные характеристики и семантическую информацию",
            "category": "Машинное обучение",
            "relations": [],
            "sources": [
                "Allamanis M., Barr E. T., Bird C., Sutton C. Learning natural coding conventions // Proc. of the 22nd ACM SIGSOFT Int. Symp. on Foundations of Software Engineering. – 2014. – С. 281–293.",
                "Gu X., Zhang H., Kim S., Kim K. Deep Code Search // ICSE. – 2018. – С. 933–944.",
                "Reiss S. P. Semantics-based code search // ICSE. – 2009. – С. 243–253."
            ]
        },
        "gof_patterns": {
            "id": "gof_patterns",
            "term": "Паттерны проектирования GoF",
            "definition": "23 классических паттерна проектирования из книги Gang of Four, разделенные на три категории: порождающие, структурные и поведенческие паттерны",
            "category": "Паттерны проектирования",
            "relations": [
                {
                    "target_term_id": "static_analysis",
                    "relation_type": "распознается через"
                }
            ],
            "sources": [
                "Gamma E., Helm R., Johnson R., Vlissides J. Design Patterns: Elements of Reusable Object-Oriented Software. – Addison-Wesley, 1994. – 395 с.",
                "Ferreira F., Vale D., Saraiva J., Cruz D. Detection of Design Patterns in Java Projects Using Static Analysis and Machine Learning // IEEE Access. – 2021. – Т. 9. – С. 147254–147268.",
                "Bajracharya S. K., Lopes C. Sourcerer: Infrastructure for Large-scale Collection and Analysis of Open-source Code // Sci. Comput. Program. – 2009."
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
