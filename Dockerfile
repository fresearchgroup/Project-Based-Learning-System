FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /PBL-server
WORKDIR /PBL-server
COPY  . /PBL-server
RUN pip install -r requirements.txt