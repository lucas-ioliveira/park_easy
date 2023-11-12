FROM python:3.10.12-slim-buster

WORKDIR /app
COPY . /app

EXPOSE 8000

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt