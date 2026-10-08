FROM ubuntu:22.04

RUN apt update && apt install -y \
    build-essential \
    valgrind \
    curl \
    netcat \
    python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /webserv

CMD ["/bin/bash"]