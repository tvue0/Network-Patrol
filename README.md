# Network Patrol

ICS 460 - Networks and Security Term Project

## Project Overview

Network Patrol is a Docker-based Network Intrusion Detection System demonstration project.

The project creates an isolated virtual network consisting of an attacker container and a victim web server. Network traffic is generated using tools such as ping, curl, and Nmap. The traffic is captured into a PCAP file, analyzed with Zeek, and then processed by a custom Python detector.

The project demonstrates an end-to-end intrusion detection workflow from traffic generation to detection results.

---

## Features

- Docker-based virtual network
- Custom Ubuntu attacker container
- Nginx victim web server
- Traffic generation using ping, curl, and Nmap
- Packet capture using tcpdump
- Zeek log generation
- Python-based connection analysis
- Nmap port-scan detection
- Normal and suspicious traffic classification
- CSV result files
- Testing comparison graph

---

## Project Architecture

```text
Attacker Container
        |
        | Ping / Curl / Nmap
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
Zeek conn.log
        |
        V
Python Detection Program
        |
        V
CSV Results and Comparison Graph
```

---

## Project Structure

```text
Network-Patrol/
│
├── docker/
│   └── attacker.Dockerfile
│
├── docs/
│   └── final_results.md
│
├── python/
│   ├── detection_analysis.py
│   └── log_analysis.py
│
├── results/
│   ├── normal-traffic-conn_results.csv
│   ├── attack_conn_results.csv
│   └── network_patrol_comparison_graph.png
│
├── screenshots/
│   ├── normal_traffic_detection_result.png
│   └── attack_detection_result.png
│
├── zeek/
│   ├── captures/
│   │   └── network-patrol-demo.pcap
│   └── logs/
│       ├── normal-traffic-conn.log
│       └── attack_conn.log
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
- Zeek Docker image

---

## Starting the Lab

Start the Docker environment:

```bash
docker compose up --build -d
```

Verify that the containers are running:

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

Generate the normal or attack traffic while tcpdump is running.

Stop packet capture:

```bash
docker exec attacker pkill tcpdump
```

---

## Run Zeek

Use Zeek to process the captured PCAP file:

```bash
docker run --rm \
-v "$(pwd)/zeek/captures:/captures" \
-v "$(pwd)/zeek/logs:/logs" \
-w /logs \
zeek/zeek \
zeek -C -r /captures/network-patrol-demo.pcap
```

Zeek creates connection logs that can be analyzed by the Python program.

---

## Run the Python Detector

Run these commands from the main `Network-Patrol` folder.

Normal traffic test:

```bash
python python/detection_analysis.py zeek/logs/normal-traffic-conn.log
```

Nmap attack test:

```bash
python python/detection_analysis.py zeek/logs/attack_conn.log
```

On systems that use `python3`, replace `python` with `python3`.

---

## Detection Rules

The Python program groups connection records by source IP and calculates:

- Total connections
- Unique destination IPs
- Unique destination ports
- Failed connections

A source IP is labeled `SUSPICIOUS` when at least one of these rules is triggered:

- 10 or more unique destination ports
- 20 or more connections
- 10 or more failed connections

If no rule is triggered, the source is labeled `NORMAL`.

---

## Testing Results

| Test | Connections | Unique Ports | Failed Connections | Result |
|---|---:|---:|---:|---|
| Normal Traffic | 4 | 2 | 0 | NORMAL |
| Nmap Port Scan | 1,010 | 1,001 | 1,001 | SUSPICIOUS |

### Normal Traffic Test

The normal traffic file contained:

- 8 Zeek records
- 4 source IPs
- 0 suspicious source IPs

All source IPs were correctly labeled `NORMAL`.

### Nmap Attack Test

The attack file contained:

- 1,014 Zeek records
- 4 source IPs
- 1 suspicious source IP

The main attack source was `172.28.0.20`. It created 1,010 connections, contacted 1,001 destination ports, and had 1,001 failed connections.

The source triggered all three detection rules and was correctly labeled `SUSPICIOUS`.

---

## Evaluation

The project used one normal-traffic scenario and one simulated Nmap attack scenario.

| Measurement | Result |
|---|---:|
| True Positives | 1 |
| True Negatives | 1 |
| False Positives | 0 |
| False Negatives | 0 |

The detector correctly identified the Nmap scan and did not generate a false alarm for the normal-traffic test.

---

## Output Files

The Python detector creates separate CSV files for each test:

```text
results/normal-traffic-conn_results.csv
results/attack_conn_results.csv
```

The comparison graph is saved as:

```text
results/network_patrol_comparison_graph.png
```

The detailed testing summary is located at:

```text
docs/final_results.md
```

---

## Technologies Used

- Docker
- Docker Compose
- Ubuntu
- Nginx
- Nmap
- tcpdump
- Zeek
- Python 3

---

## Team Members

- Ermias Kassa
- Abdullahi Mohamed
---

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