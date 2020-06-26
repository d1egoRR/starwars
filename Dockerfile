FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PORT 8001

RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN pip install -r requirements.txt

CMD gunicorn starwars.wsgi:application --bind 0.0.0.0:$PORT
