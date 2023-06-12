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
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY birthday_app .
COPY birthdays .
COPY static .
COPY templates .
COPY frontend_startup.sh .
COPY manage.py .

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/birthdays/"

RUN dos2unix -o frontend_startup.sh frontend_startup.sh
RUN chmod +x frontend_startup.sh