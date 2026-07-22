FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
    iputils-ping \
    curl \
    nmap \
    tcpdump && \
    rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]
