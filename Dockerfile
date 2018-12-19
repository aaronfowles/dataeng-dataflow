FROM python:2.7-alpine2.7

ENV LANG C.UTF-8

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN rm -r .pytest_cache && find . -name '*.pyc' -delete

RUN pip install -e .

RUN pytest