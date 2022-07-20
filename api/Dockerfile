FROM python:3.7-slim

WORKDIR /api

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .
RUN apt-get upgrade && apt-get update &&\
    apt-get -y install libc-dev build-essential &&\
    pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run"]