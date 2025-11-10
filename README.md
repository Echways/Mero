
# Mero — веб-приложение для событий и билетов

[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/DB-SQLite-lightgrey)]()
[![Pillow](https://img.shields.io/badge/images-Pillow-yellowgreen)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

> **Mero:**
> Mero — аккуратное и практичное Django-приложение для управления событиями, билетами и медиа-контентом. Проект подходит как стартовая база для MVP: готовая админка, поддержка загрузки изображений и простая локальная конфигурация.

---

## Подробное описание возможностей

### 1. Управление событиями (Events)
- Модели событий с основными полями (название, описание, даты начала/окончания, место).  
- Админ-интерфейс для создания/редактирования/удаления событий.  
- Загрузка обложек и вспомогательных изображений для каждого события (через `ImageField`). 

### 2. Билеты и инвентарь (Tickets)
- Модель билета, привязанная к событию (тип билета, цена, количество).  
- Управление наличием билетов в админке.  
- Базовая логика резервирования/продажи

### 3. Пользователи и админ-панель
- Полноценная интеграция с Django Admin — удобное управление сущностями.  
- Возможность создавать суперпользователя и управлять доступом прямо через админку.  
- Формы (Django Forms / ModelForms) для валидации и обработки входящих данных.

### 4. Медиа и файлы
- Поддержка `MEDIA_ROOT` и `MEDIA_URL` — файлы сохраняются в `media/`.  
- Обработка и хранение изображений через Pillow.  

### 5. Формы и валидация
- В проекте присутствуют формы для создания/редактирования сущностей (включая `ModelForm`).  
- Серверная валидация полей и обработка ошибок в шаблонах.

### 6. Простая локальная конфигурация
- По-умолчанию используется SQLite — удобно для разработки и тестирования.  
- Настройка через `settings.py`; при необходимости легко переключиться на PostgreSQL.

---

## Быстрая установка

```bash
git clone git@github.com:Echways/Mero.git
cd Mero

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

export SECRET_KEY="replace_this"
export DEBUG=True

cd TimeTicket

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

---

## Команды разработки
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py shell
```
