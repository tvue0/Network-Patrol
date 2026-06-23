# Network-Patrol
 Su26 ICS 460-50 Networks and Security Term Project


# Zeek Setup and Usage (Docker-Based)
## Overview

This project uses the official Zeek Docker image rather than a traditional operating system installation of Zeek. Docker provides an isolated environment containing Zeek and its dependencies, allowing the same commands and workflow to be used across Windows, Linux, and VirtualBox environments.

## Requirements

- Docker
- Git
- A packet capture file (`.pcap`)

---

## Verify Docker Installation

### Windows (Docker Desktop)

Open and use either:

- PowerShell
- Windows Terminal
- Command Prompt (cmd)

### Linux / VirtualBox VM

Open a terminal inside the VM.

Run:

```bash
docker run hello-world
```

Expected output:

```text
Hello from Docker!
```

---

## Install Zeek (Docker Image)

Download the official Zeek Docker image:

```bash
docker pull zeek/zeek
```

Verify the image was downloaded:

```bash
docker images
```

Example output:

```text
REPOSITORY   TAG       IMAGE ID
zeek/zeek    latest    xxxxxxxxxxxx
```

Verify Zeek is available inside the container:

```bash
docker run --rm zeek/zeek zeek --version
```


---

## Project Directory Structure

```text
Network-Patrol/
├── docs/
├── docker/
├── python/
├── zeek/
│   ├── captures/
│   └── logs/
└── README.md
```

Place PCAP files inside:

```text
zeek/captures/
```

---

## Run Zeek Against a PCAP

### Linux / VirtualBox

```bash
docker run --rm \
-v $(pwd)/zeek/captures:/captures \
-v $(pwd)/zeek/logs:/logs \
zeek/zeek \
zeek -C -r /captures/<your-file>.pcap # replace with your PCAP filename
```

### Windows PowerShell

```powershell
docker run --rm `
-v "${PWD}\zeek\captures:/captures" `
-v "${PWD}\zeek\logs:/logs" `
zeek/zeek `
zeek -C -r /captures/<your-file>.pcap # replace with your PCAP filename
```

### Command Explanation

| Option | Purpose |
|----------|----------|
| `--rm` | Removes container after execution |
| `-v` | Mounts local folders into the container |
| `-C` | Ignores checksum issues common in sample captures |
| `-r` | Reads a PCAP file |

---

## Verify Log Generation

After Zeek completes, the following logs should appear in:

```text
zeek/logs/
```

Typical outputs:

```text
conn.log
http.log
files.log
packet_filter.log
```

---

## Log Overview

### conn.log

Contains:

- Source IP
- Destination IP
- Ports
- Protocol
- Connection duration

Useful for:

- Port scan detection
- Unusual connection analysis

---

### http.log

Contains:

- HTTP requests
- URLs
- Request methods

Useful for:

- Web traffic analysis

---

### files.log

Contains:

- File transfer metadata

Useful for:

- Monitoring transferred files

---

