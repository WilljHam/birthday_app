# pull official base image
FROM python:latest

USER root

RUN apt-get update && apt-get install dos2unix
RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

# install required python packages
COPY requirements.txt .
RUN pip install -r ./requirements.txt

# set work directory
WORKDIR /usr/src/app/
RUN mkdir birthday_app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY birthday_app /usr/src/app/birthday_app/birthday_app
COPY birthdays /usr/src/app/birthday_app/birthdays
COPY static /usr/src/app/birthday_app/static
COPY templates /usr/src/app/birthday_app/templates
COPY gunicorn.conf.py /usr/src/app/gunicorn.conf.py
COPY frontend_startup.sh /usr/src/app/frontend_startup.sh
COPY manage.py /usr/src/app/manage.py

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/birthdays/"
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/birthday_app/"
ENV DJANGO_SUPERUSER_USERNAME "admin"
ENV DJANGO_SUPERUSER_EMAIL  "admin@admin.com"
ENV DJANGO_SUPERUSER_PASSWORD  "admin"


RUN dos2unix -o frontend_startup.sh frontend_startup.sh
RUN chmod +x frontend_startup.sh