## Docker Lab Setup

### Overview

The Docker environment consists of two containers connected on the same network:

- attacker (Ubuntu)
- victim (Nginx web server)

The purpose of this setup is to generate normal and attack traffic for later analysis.

### Start the Lab

```bash
docker compose up -d

### Verify Containers

Run:

```bash
docker ps
```

Expected output should show:

- attacker
- victim

### Enter the Attacker Container

```bash
docker exec -it attacker bash
```

### Test Connectivity

```bash
ping -c 4 victim
```

Expected:
- Replies from victim
- 0% packet loss

### Access Victim Web Server

```bash
curl http://victim
```

Expected:
- Nginx welcome page HTML

### Scan Victim

```bash
nmap victim
```

Expected:
- Port 80/tcp open
- Service: http

### Exit Container

```bash
exit
```

### Stop the Lab

```bash
docker compose down
```

### Generate Traffic for Packet Capture

The following commands generate network traffic that can be captured by tools such as tcpdump, Wireshark, or Zeek:

```bash
ping -c 4 victim
curl http://victim
nmap victim
```

These commands produce ICMP, HTTP, and TCP scan traffic suitable for PCAP generation and analysis.
```
