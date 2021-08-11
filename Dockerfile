FROM python:3.9.6-slim as base

ADD . /flask_demo

WORKDIR /flask_demo

RUN pip install -r requirements.txt
