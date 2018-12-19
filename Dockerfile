FROM python:2.7.15-alpine3.7

RUN apk add gcc

ENV LANG C.UTF-8

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN rm -r .pytest_cache && find . -name '*.pyc' -delete

RUN pip install pytest

RUN pytest