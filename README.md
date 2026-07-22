# Network Patrol

ICS 460 - Networks and Security Term Project

## Project Overview

Network Patrol is a Docker-based Network Intrusion Detection System (NIDS) demonstration project.

The project creates an isolated virtual network consisting of an attacker container and a victim web server. Network traffic is generated using common networking tools such as ping, curl, and Nmap. Traffic is captured into a PCAP file, analyzed with Zeek, and summarized using a custom Python analysis tool.

The project demonstrates an end-to-end intrusion detection workflow from traffic generation through security reporting.

---

## Features

- Docker-based virtual network
- Custom Ubuntu attacker container
- Nginx victim web server
- Traffic generation using ping, curl, and Nmap
- Packet capture using tcpdump
- Zeek log generation
- Python-based security report
- HTTP and DNS traffic detection
- Basic Nmap port scan detection
- Connection statistics and traffic summaries

---

## Project Architecture

```
Attacker Container
        |
        |  Ping / Curl / Nmap
        |
        V
Victim Container
        |
        V
Packet Capture (PCAP)
        |
        V
Zeek Analysis
        |
        V
Zeek Log Files
        |
        V
Python Security Report
```

---

## Project Structure

```
Network-Patrol/
│
├── docker/
│   └── attacker.Dockerfile
│
├── python/
│   └── log_analysis.py
│
├── zeek/
│   ├── captures/
│   └── logs/
│
├── screenshots/
│
├── docker-compose.yml
├── README.md
└── ProgressReport2.md
```

---

## Requirements

- Docker
- Docker Compose
- Python 3
- Zeek Docker Image

---

## Starting the Lab

```bash
docker compose up --build -d
```

Verify the containers:

```bash
docker compose ps
```

---

## Generate Network Traffic

Generate ICMP traffic:

```bash
docker exec attacker ping -c 5 victim
```

Generate HTTP traffic:

```bash
docker exec attacker curl http://victim
```

Generate an Nmap scan:

```bash
docker exec attacker nmap -sS -sV victim
```

---

## Capture Network Traffic

Start packet capture:

```bash
docker exec -d attacker tcpdump -i eth0 -w /captures/network-patrol-demo.pcap
```

Generate traffic.

Stop packet capture:

```bash
docker exec attacker pkill tcpdump
```

---

## Run Zeek

```bash
docker run --rm \
-v "$(pwd)/zeek/captures:/captures" \
-v "$(pwd)/zeek/logs:/logs" \
-w /logs \
zeek/zeek \
zeek -C -r /captures/network-patrol-demo.pcap
```

---

## Generate the Security Report

```bash
python3 python/log_analysis.py
```

Example report:

```
Connections Observed: 1014

Unique Source Hosts: 4

Unique Destination Hosts: 4

Services Detected
- HTTP
- DNS

Possible Nmap Port Scan Detected
```

---

## Technologies Used

- Docker
- Docker Compose
- Ubuntu
- Nginx
- tcpdump
- Zeek
- Python 3

---

## Team Members

- Ermias Kassa
- Abdullahi Mohamed

## References

1. Zeek Project. *Quick Start Guide*.
   https://docs.zeek.org/en/stable/quickstart/

2. Zeek Project. *Invoking Zeek*.
   https://docs.zeek.org/en/master/tutorial/invoking-zeek.html

3. Zeek Project. *Zeek Documentation*.
   https://docs.zeek.org/en/current/

4. Zeek Project. *Get Zeek*.
   https://zeek.org/get-zeek/

5. Zeek Project. *Zeek Tutorial*.
   https://docs.zeek.org/en/current/tutorial/
