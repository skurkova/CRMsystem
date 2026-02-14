FROM python:3.9-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Создание директорий для статики и медиа
RUN mkdir -p staticfiles uploads

# Экспозиция порта
EXPOSE 8000

# Команда для запуска
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "CRMsystеm.wsgi:application"]