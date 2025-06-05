#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn -b 0.0.0.0 -p 8000 vchdbuxoroback.wsgi:application