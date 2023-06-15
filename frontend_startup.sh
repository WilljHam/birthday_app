#!/bin/sh
ls -l
python manage.py migrate
python manage.py collectstatic --noinput --clear
gunicorn --bind 0.0.0.0:8890 birthday_app.wsgi:application  --access-logfile - --error-logfile -
