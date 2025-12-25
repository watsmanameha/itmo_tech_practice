FROM python:3.11-slim

WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app ./app

# Создаем директорию для данных (если вдруг glossary.json отсутствует)
RUN mkdir -p app/data

EXPOSE 8000

# Запуск uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
