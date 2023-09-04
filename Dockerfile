# Container image that runs your code
#FROM alpine:3.10

# Copies your code file from your action repository to the filesystem path `/` of the container
#COPY entrypoint.sh /entrypoint.sh


# Code file to execute when the docker container starts up (`entrypoint.sh`)
#ENTRYPOINT ["/entrypoint.sh"]


# base image  
FROM python:3.10.13-alpine

# setup environment variable  
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]