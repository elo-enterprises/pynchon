FROM python:3.11
COPY . /opt/pynchon
RUN cd /opt/pynchon && pip install -q -e .
RUN apt-get update && apt-get install -y curl docker make
ENTRYPOINT pynchon