# Mero — платформа для событий и билетов

Современное Django‑приложение для управления событиями, регистрациями и медиа‑контентом. Проект обновлён до актуального стека, использует PostgreSQL и подготовлен для разработки и продакшн‑деплоя.

## Быстрый старт (Docker)

```bash
docker compose down -v
docker compose up --build
```

Открой: `http://localhost:8000`

## Production (docker-compose.prod.yml)

```bash
docker compose -f docker-compose.prod.yml up --build
```

Открой: `http://localhost`

## Локальный запуск без Docker

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
export ENV_FILE=.env

cd TimeTicket
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

## Разработка

```bash
pip install -r requirements-dev.txt

black .
ruff check .
pytest
```

## Основные переменные окружения

- `SECRET_KEY` — секрет Django
- `DEBUG` — режим отладки
- `ALLOWED_HOSTS` — список хостов
- `DATABASE_URL` — строка подключения к PostgreSQL
- `EMAIL_*` — SMTP конфигурация
- `CREATE_SUPERUSER` — автосоздание админа в Docker
- `SUPERUSER_*` — данные суперпользователя

## Архитектура

- `TimeTicket/TimeTicket/settings/` — настройки (base/dev/prod)
- `TimeTicket/main/` — приложение событий
- `TimeTicket/main/services/` — внешние побочные эффекты (email, экспорт)
- `TimeTicket/main/templates/` — шаблоны и partials
- `TimeTicket/static/css/` — CSS разделён на base/components/pages
- `deploy/` — nginx конфигурация
