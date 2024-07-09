FROM python:3.11-alpine as web
WORKDIR /home/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add python3-dev

COPY ./requirements.txt ./

RUN pip install --upgrade pip

RUN pip install gunicorn
RUN pip install --no-cache-dir -r ./requirements.txt

COPY . .