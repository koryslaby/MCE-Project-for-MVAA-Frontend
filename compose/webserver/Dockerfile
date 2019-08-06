FROM python:3
ENV PYTHONUNBUFFERED 1

COPY . /code/
WORKDIR /code/www

RUN apt update
RUN apt install -y imagemagick tesseract-ocr=3.04.01-5 libtesseract-dev ghostscript

RUN pip install -r ../requirements.txt