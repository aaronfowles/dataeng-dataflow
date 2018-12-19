FROM python:3.6-alpine3.6

ENV LANG C.UTF-8

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN rm -r .pytest_cache && find . -name '*.pyc' -delete

RUN pip install -e .

RUN pytest