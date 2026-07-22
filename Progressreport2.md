# Progress Report 2

**Course:** ICS 460-50 Networks and Security  
**Project:** Network Patrol  
**Group Members:**
- Ermias Kassa
- Abdullahi Mohamed

---

# Project Status

The project is approximately **95% complete**. Since Progress Report 1, we have completed the major technical components of the project. The Docker lab environment is fully operational, network traffic can be generated and captured, Zeek successfully analyzes the traffic, and the Python program produces a security report summarizing the results. The remaining work consists of improving documentation, preparing screenshots, performing final testing, and practicing our presentation.

---

# Ermias Kassa work

Since Progress Report 1, I completed the core infrastructure of the project by building a Docker-based network environment consisting of a custom Ubuntu attacker container and an Nginx victim web server connected through an isolated Docker network.

I verified communication between the containers using ping, curl, and Nmap to generate both normal and suspicious network traffic. Packet captures were collected using tcpdump and saved as PCAP files for later analysis.

I integrated the official Zeek Docker image into the project and successfully processed captured traffic into Zeek log files including:

- conn.log
- http.log
- dns.log
- files.log
- packet_filter.log

I also expanded the project documentation, updated the GitHub repository, and tested the complete workflow from Docker traffic generation through Zeek analysis and the Python reporting tool.

During the project I honestly thought both of my teammates had left, so I worked on a lot of the project by myself because I wanted to make sure I would still have a complete project to present.I focused on getting the Docker environment, packet capture, Zeek integration, testing, GitHub updates, and documentation working together as one complete system.

---

# Abdullahi Mohamed – Python Analysis and Reporting 

For this report, I updated my earlier Python file so it does more than print the Zeek log. I tested it with the conn.log already in our repository. The test only had one HTTP connection, so the program labeled it normal. It also created a CSV file in the results folder. I still need a larger attack log from our Docker testing before I can properly test the suspicious-traffic rules. 

 For the Final presentation

I will get separate normal-traffic and port-scan conn.log files from my teammate, run my Python detection program on both, compare the number of connections, unique ports, and failed connections, and adjust the detection thresholds if needed. After testing, I will record the TP, FP, TN, and FN results, create an Excel evaluation table and graph, update the GitHub README and results files, and help complete the final report and presentation.


---

# Current Project Workflow

```
Docker Network
      │
      ▼
Generate Network Traffic
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
- Custom Ubuntu attacker container
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

Before the final presentation we plan to:

- Complete the final README.
- Organize project screenshots.
- Create a simple network architecture diagram.
- Perform final testing.
- Practice and prepare the live demonstration.

---

# Overall Status

Progress Report 1 was at 35% complete. Since then, we have completed the major implementation work and successfully integrated Docker networking, traffic generation, packet capture, Zeek analysis, and Python security reporting into one complete workflow.

The project is at 95% complete and is in the final documentation and presentation phase before submission.
