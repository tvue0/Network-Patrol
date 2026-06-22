# Network-Patrol
 Su26 ICS 460-50 Networks and Security Term Project


# Zeek Setup and Usage

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

## Pull the Zeek Docker Image

Download the Zeek image:

```bash
docker pull zeek/zeek
```

Verify the image is installed:

```bash
docker images
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
zeek -C -r /captures/sample.pcap
```

### Windows PowerShell

```powershell
docker run --rm `
-v "${PWD}\zeek\captures:/captures" `
-v "${PWD}\zeek\logs:/logs" `
zeek/zeek `
zeek -C -r /captures/sample.pcap
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

