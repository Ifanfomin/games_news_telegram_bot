FROM python:3.11

RUN pip install --upgrade pip setuptools wheel
# Установка системных зависимостей: Redis client + PostgreSQL
RUN apt-get update && apt-get install -y \
    postgresql-client \
    netcat-openbsd \
    redis-tools \
    libpq-dev \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app
ENV PYTHONPATH=/app

# Копируем зависимости
COPY requirements.txt ./

# Установка pip-зависимостей
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Копируем весь код
# COPY . .
COPY bot .
COPY .env .
COPY main.py .

# # Копируем и делаем исполняемым стартовый скрипт
# COPY start.sh /app/start.sh
# RUN chmod +x /app/start.sh

# # Запуск стартового скрипта
# CMD ["/app/start.sh"]
