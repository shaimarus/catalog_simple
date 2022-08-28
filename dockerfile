FROM python:3.9
RUN apt-get update
#RUN apt-get update && rm -rf /var/lib/apt/listls/*
RUN mkdir /opt/catalog_simple/
COPY . /opt/catalog_simple/

RUN pip3 install -r /opt/catalog_simple/requirements.txt
#RUN pip3 --no-cache-dir install -r /opt/catalog_simple/requirements.txt

WORKDIR /opt/catalog_simple/