FROM python:latest

COPY . /lethe

WORKDIR /lethe 

RUN pip install --no-cache-dir -r requirements.txt