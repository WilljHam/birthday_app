#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput --clear
gunicorn birthdays.wsgi:application --bind 0.0.0.0:8890 --access-logfile - --error-logfile -
