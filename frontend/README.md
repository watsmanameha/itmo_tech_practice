# Frontend - Glossary Application

React приложение для визуализации глоссария терминов и семантического графа.

## Технологии

- **React 18** - UI библиотека
- **TypeScript** - типизация
- **Vite** - сборщик и dev сервер
- **TailwindCSS** - утилитарные CSS стили
- **React Flow** - визуализация графов
- **Axios** - HTTP клиент
- **Dagre** - алгоритмы раскладки графов

## Установка

```bash
npm install
```

## Запуск

### Development

```bash
npm run dev
```

Приложение будет доступно на http://localhost:3000

### Production Build

```bash
npm run build
```

Собранные файлы будут в директории `dist/`

### Preview Production Build

```bash
npm run preview
```

## Структура компонентов

```
src/
├── components/
│   ├── glossary/
│   │   ├── TermCard.tsx          # Карточка термина
│   │   ├── GlossaryGrid.tsx      # Сетка терминов
│   │   └── SearchFilter.tsx      # Поиск и фильтры
│   ├── mindmap/
│   │   ├── MindMap.tsx           # Граф терминов
│   │   └── CustomNode.tsx        # Кастомный узел графа
│   └── layout/
│       └── Header.tsx            # Шапка приложения
├── services/
│   └── api.ts                    # API клиент
├── types/
│   └── term.ts                   # TypeScript типы
├── App.tsx                       # Главный компонент
├── main.tsx                      # Точка входа
└── index.css                     # Глобальные стили
```

## Переменные окружения

Создайте файл `.env` на основе `.env.example`:

```
VITE_API_URL=http://localhost:8000
```

## Docker

### Сборка образа

```bash
docker build -t glossary-frontend .
```

### Запуск контейнера

```bash
docker run -p 3000:80 glossary-frontend
```

## Деплой на GitHub Pages

1. Обновите `vite.config.ts`:

```typescript
export default defineConfig({
  base: '/repository-name/',
  // ...
})
```

2. Соберите проект:

```bash
npm run build
```

3. Загрузите содержимое `dist/` на GitHub Pages

## Особенности реализации

### Глоссарий

- Карточное представление терминов
- Живой поиск по названию и определению
- Фильтрация по категориям
- Выделение выбранного термина

### Семантический граф

- Автоматическая раскладка узлов с помощью Dagre
- Интерактивная навигация (зум, перемещение)
- Визуализация связей между терминами
- Кастомные узлы с поддержкой центрального элемента

## Лицензия

MIT
