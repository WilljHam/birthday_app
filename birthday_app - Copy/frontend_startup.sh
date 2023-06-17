#!/bin/sh
ls -l
python manage.py migrate
python manage.py collectstatic --noinput --clear
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
gunicorn --bind 0.0.0.0:8890 birthday_app.wsgi:application  --access-logfile - --error-logfile -
