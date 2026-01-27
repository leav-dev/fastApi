FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip 
RUN mkdir data && cd /data && mkdir code && cd /data
WORKDIR /data
COPY ./complements/ /data/complements
COPY ./complements/requirements.txt requirements.txt
COPY ./main /data/code/

RUN python3 -m pip install virtualenv
RUN  cd /data && virtualenv -p /usr/bin/python3 entornoVirtual
USER root
RUN . /data/entornoVirtual/bin/activate && pip install -r requirements.txt

EXPOSE 8000

CMD ["tail","-f", "/dev/null"]

SHELL ["/bin/bash", "-c"]