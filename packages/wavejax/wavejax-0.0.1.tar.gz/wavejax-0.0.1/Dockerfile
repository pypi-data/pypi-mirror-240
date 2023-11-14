# syntax=docker/dockerfile:1

FROM ubuntu:22.04

RUN apt-get update && apt-get install --yes \
    build-essential \
    python3-pip 

COPY ./requirements.txt /requirements.txt 
RUN python3 -m pip install -r /requirements.txt && rm -f /requirements.txt 

CMD ["/bin/bash"]
