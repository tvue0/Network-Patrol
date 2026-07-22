# Progress Report 2

**Course:** ICS 460-50 Networks and Security  
**Project:** Network Patrol  
**Team Members:**  
- Ermias Kassa
- Abdullahi Mohamed

---

# Project Status

The project is approximately **95% complete**. Since Progress Report 1, we have completed the Docker network environment, generated network traffic, captured packet data, analyzed traffic using Zeek, and developed a Python security reporting tool. The remaining work consists of improving documentation, preparing screenshots, and practicing the final project presentation.

---

# Ermias Kassa Contributions

Since Progress Report 1, I completed the core infrastructure of the project by building a Docker-based network environment consisting of a custom Ubuntu attacker container and an Nginx victim web server connected through an isolated Docker network.

I verified communication between the containers using ping, curl, and Nmap to generate both normal and suspicious network traffic. Packet captures were collected using tcpdump and saved as PCAP files for later analysis.

I integrated the official Zeek Docker image into the project and successfully processed captured traffic into Zeek log files including:

- conn.log
- http.log
- dns.log
- files.log
- packet_filter.log

I also updated the project documentation and verified the complete workflow from traffic generation through Zeek analysis.

Several technical challenges were encountered during development, including Docker networking, container configuration, GitHub authentication using Personal Access Tokens, packet capture, and Zeek configuration. These issues were resolved through testing and configuration changes until the environment became stable and repeatable.

---

# Abdullahi Mohamed Contributions

The Python analysis component was expanded into a security reporting tool capable of summarizing Zeek log data.

The Python application now:

- Parses Zeek connection logs
- Counts observed network connections
- Reports unique source hosts
- Reports unique destination hosts
- Identifies detected services
- Displays the most active source hosts
- Displays the most active destination hosts
- Displays the most frequently targeted destination ports
- Detects HTTP traffic
- Detects DNS traffic
- Identifies possible Nmap port scan activity based on the number of destination ports observed

Testing with traffic generated inside the Docker lab confirmed that the analysis tool accurately summarizes network activity and highlights potentially suspicious behavior.

---

# Current Project Workflow

```
Docker Network
      │
      ▼
Generate Traffic
      │
      ▼
Capture Packets (PCAP)
      │
      ▼
Analyze with Zeek
      │
      ▼
Generate Zeek Logs
      │
      ▼
Python Security Report
```

---

# Current Project Features

The project now includes:

- Docker-based network environment
- Custom attacker container
- Nginx victim web server
- Traffic generation using ping, curl, and Nmap
- Packet capture using tcpdump
- Zeek log generation
- Python security reporting
- HTTP traffic detection
- DNS traffic detection
- Basic Nmap port scan detection
- Connection statistics
- Host and port summaries

---

# Remaining Tasks

The remaining work before the final presentation includes:

- Final README revisions
- Organize project screenshots
- Create a network architecture diagram
- Perform final testing
- Prepare the live demonstration

---

# Overall Status

The project objectives have been successfully completed. The Docker networking environment, traffic generation, packet capture, Zeek analysis, and Python reporting components are fully functional and integrated into a complete network monitoring workflow.

The project is now in its final documentation and presentation phase before submission.
