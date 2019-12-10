# Author:  DINDIN Meryll
# Date:    10 December 2019
# Project: aster-website

FROM ubuntu:18.04

MAINTAINER Meryll Dindin "meryll_dindin@berkeley.edu"

RUN apt-get update -y
RUN apt-get install --no-install-recommends build-essential python3-pip python3.6 --fix-missing -y

RUN mkdir -p /website-app
VOLUME /website-app
WORKDIR /website-app

COPY ./requirements.txt /website-app/requirements.txt
RUN pip3 install wheel setuptools
RUN pip3 install -r requirements.txt

COPY . /website-app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "application.py" ]