#!/bin/sh
set -e

python TimeTicket/manage.py makemigrations
python TimeTicket/manage.py migrate

python TimeTicket/manage.py ensure_superuser

exec python TimeTicket/manage.py runserver 0.0.0.0:8000
