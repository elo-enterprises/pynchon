# a dockerfile that builds this repository from a hash rather than the current contents of this folder

FROM python:3.11

ARG REPO_URL=https://github.com/elo-enterprises/pynchon.git
ARG BRANCH=master
ARG HASH
# docker build --build-arg HASH=abc123def456
#RUN curl -fsSL https://get.docker.com -o get-docker.sh && bash get-docker.sh
RUN mkdir -p /opt/
RUN apt-get update && apt-get install -y curl git 
RUN git clone ${REPO_URL} /opt/pynchon && cd /opt/pynchon && git checkout ${HASH:-$BRANCH}
RUN cd /opt/pynchon && pip install -q . && rm -rf /opt/pynchon
ENTRYPOINT pynchon