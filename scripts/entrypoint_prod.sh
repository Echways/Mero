#!/bin/sh
set -e

python TimeTicket/manage.py migrate
python TimeTicket/manage.py collectstatic --noinput

exec gunicorn TimeTicket.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 60
