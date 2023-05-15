FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1


RUN pip install --upgrade pip && \
    apt-get update && apt-get install -y \
    python3-dev default-libmysqlclient-dev build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y postgresql-server-dev-all

RUN mkdir /AbhrilSoft_app
WORKDIR /AbhrilSoft_app

COPY requirements.txt /AbhrilSoft_app/
RUN pip install -r requirements.txt
RUN pip install Django

ENV DJANGO_SETTINGS_MODULE=core.settings

COPY . /AbhrilSoft_app

