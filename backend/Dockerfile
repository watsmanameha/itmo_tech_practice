FROM python:3.11-slim

WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app ./app

# Создаем директорию для данных
RUN mkdir -p app/data

# Копируем файл базы данных если он есть
COPY app/data/glossary.json ./app/data/glossary.json 2>/dev/null || true

EXPOSE 8000

# Запуск uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
