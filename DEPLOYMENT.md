# Инструкция по развертыванию

## Содержание

1. [Локальное развертывание с Docker](#локальное-развертывание-с-docker)
2. [Локальное развертывание для разработки](#локальное-развертывание-для-разработки)
3. [Развертывание на облачных платформах](#развертывание-на-облачных-платформах)
4. [Развертывание на GitHub Pages](#развертывание-на-github-pages)

---

## Локальное развертывание с Docker

### Требования

- Docker 20.10+
- Docker Compose 2.0+

### Инструкция

1. Клонируйте репозиторий:

```bash
git clone <repository-url>
cd itmo_tech_practice
```

2. Запустите контейнеры:

```bash
docker-compose up --build
```

3. Откройте в браузере:
   - Фронтенд: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

4. Остановка:

```bash
docker-compose down
```

5. Очистка всех данных:

```bash
docker-compose down -v
```

---

## Локальное развертывание для разработки

### Backend

#### Требования
- Python 3.9+
- pip

#### Инструкция

```bash
cd backend

# Создание виртуального окружения
python3 -m venv .venv

# Активация (Linux/Mac)
source .venv/bin/activate

# Активация (Windows)
.venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt

# Инициализация базы данных
python init_db.py

# Запуск сервера
uvicorn app.main:app --reload --port 8000
```

Backend будет доступен на http://localhost:8000

### Frontend

#### Требования
- Node.js 18+
- npm 9+

#### Инструкция

```bash
cd frontend

# Установка зависимостей
npm install

# Запуск dev сервера
npm run dev
```

Frontend будет доступен на http://localhost:3000

---

## Развертывание на облачных платформах

### Backend на Railway.app

1. Создайте аккаунт на [Railway.app](https://railway.app)

2. Установите Railway CLI:

```bash
npm i -g @railway/cli
```

3. Войдите в аккаунт:

```bash
railway login
```

4. Разверните backend:

```bash
cd backend
railway init
railway up
```

5. Получите URL вашего API:

```bash
railway domain
```

### Backend на Render.com

1. Создайте аккаунт на [Render.com](https://render.com)

2. Создайте новый Web Service

3. Подключите GitHub репозиторий

4. Настройте сервис:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Root Directory**: `backend`

5. Создайте переменную окружения:
   - `PYTHONUNBUFFERED=1`

### Backend на Fly.io

1. Установите Fly CLI:

```bash
curl -L https://fly.io/install.sh | sh
```

2. Войдите в аккаунт:

```bash
fly auth login
```

3. Разверните приложение:

```bash
cd backend
fly launch
fly deploy
```

---

## Развертывание на GitHub Pages

### Автоматическое развертывание через GitHub Actions

1. Добавьте secrets в GitHub:
   - `API_URL` - URL вашего backend API

2. Включите GitHub Pages в настройках репозитория:
   - Settings → Pages
   - Source: GitHub Actions

3. При пуше в `main` ветку автоматически запустится деплой

### Ручное развертывание

1. Обновите `frontend/vite.config.ts`:

```typescript
export default defineConfig({
  base: '/your-repo-name/',
  // ...
})
```

2. Соберите проект:

```bash
cd frontend
npm install
npm run build
```

3. Установите `gh-pages`:

```bash
npm install -g gh-pages
```

4. Разверните:

```bash
gh-pages -d dist
```

---

## Развертывание Frontend на Vercel

1. Установите Vercel CLI:

```bash
npm i -g vercel
```

2. Разверните:

```bash
cd frontend
vercel
```

3. Настройте переменные окружения в Vercel Dashboard:
   - `VITE_API_URL` - URL вашего backend API

---

## Развертывание Frontend на Netlify

1. Установите Netlify CLI:

```bash
npm i -g netlify-cli
```

2. Разверните:

```bash
cd frontend
netlify deploy --prod
```

3. Настройте переменные окружения в Netlify Dashboard:
   - `VITE_API_URL` - URL вашего backend API

---

## Полное развертывание (Backend + Frontend)

### Вариант 1: Backend на Railway, Frontend на Vercel

1. Разверните backend на Railway (см. выше)
2. Получите URL backend API
3. Разверните frontend на Vercel с переменной `VITE_API_URL`

### Вариант 2: Backend на Render, Frontend на Netlify

1. Разверните backend на Render (см. выше)
2. Получите URL backend API
3. Разверните frontend на Netlify с переменной `VITE_API_URL`

### Вариант 3: Все на одном VPS

```bash
# На сервере
git clone <repository-url>
cd itmo_tech_practice

# Установите Docker и Docker Compose
sudo apt update
sudo apt install docker.io docker-compose -y

# Запустите приложение
docker-compose up -d

# Настройте Nginx как reverse proxy
# Добавьте домен и SSL сертификат
```

---

## Проверка работоспособности

### Backend

```bash
curl http://localhost:8000/health
# Ожидаемый ответ: {"status":"ok"}
```

### Frontend

Откройте http://localhost:3000 в браузере и проверьте:
- [ ] Отображается список терминов
- [ ] Работает поиск
- [ ] Работает фильтрация по категориям
- [ ] Переключение на граф работает
- [ ] Граф отображается корректно

---

## Устранение проблем

### Backend не запускается

```bash
# Проверьте логи
docker-compose logs backend

# Или для локального запуска
cd backend
source .venv/bin/activate
python -c "import uvicorn; print('OK')"
```

### Frontend не видит API

1. Проверьте CORS настройки в `backend/app/main.py`
2. Убедитесь, что `VITE_API_URL` указывает на правильный адрес
3. Проверьте, что backend запущен и доступен

### Ошибки сборки Docker

```bash
# Очистите кэш Docker
docker system prune -a

# Пересоберите образы
docker-compose build --no-cache
```

---

## Мониторинг

### Логи Docker

```bash
# Все логи
docker-compose logs -f

# Только backend
docker-compose logs -f backend

# Только frontend
docker-compose logs -f frontend
```

### Метрики

Backend предоставляет endpoint для проверки работоспособности:

```
GET /health
```

---

## Обновление

### Обновление кода

```bash
git pull origin main
docker-compose down
docker-compose up --build -d
```

### Обновление зависимостей

```bash
# Backend
cd backend
pip install -r requirements.txt --upgrade

# Frontend
cd frontend
npm update
```

---

## Безопасность

### Рекомендации для продакшена

1. Измените CORS настройки в `backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-domain.com"],  # Укажите конкретные домены
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

2. Используйте HTTPS
3. Настройте rate limiting
4. Добавьте аутентификацию (если требуется)
5. Регулярно обновляйте зависимости

---

## Поддержка

При возникновении проблем:
1. Проверьте логи
2. Убедитесь, что используете правильные версии зависимостей
3. Создайте issue в GitHub репозитории
