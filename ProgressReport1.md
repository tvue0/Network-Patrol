# Progress Report 1
## Project Status Summary

Current completion is estimated at 30–35% of the overall project.

The project now has a working Docker-based network environment, Zeek log generation, and an initial Python parser for Zeek output. Team roles and workflow have been defined around shared PCAP files to support testing across different environments. Next steps include generating attack traffic, capturing PCAPs, expanding detection logic, and adding evaluation metrics such as true positives, false positives, true negatives, and false negatives.

---
# Ermias Kassa – Network patrol progress

For my part of the project, I worked on setting up the Docker lab environment. I created an attacker container and a victim container and connected them through the same Docker network. I tested the setup using `ping`, `curl`, and `nmap` to make sure the containers could communicate and generate traffic. 
I also added Docker setup and usage instructions to the README so other group members can run the same environment. The current Docker setup is working, but PCAP capture has not been fully added yet. The traffic can be captured later using tools like tcpdump or Zeek. 
Some issues I ran into were Docker Compose setup problems, GitHub authentication using a Personal Access Token, and container name conflicts. I was able to resolve these issues and continue development on a separate branch to avoid affecting the main branch.
Before Progress Report 2, my next steps are to implement PCAP capture from Docker-generated traffic, create additional test traffic, and work with the team to ensure the Docker environment integrates properly with Zeek for monitoring and analysis.
---
# Tony Vue – Zeek Analysis Component

A functional Zeek-based network intrusion detection pipeline was successfully deployed using Docker, and initial packet capture analysis demonstrates the system’s ability to generate structured logs for network traffic inspection. Zeek was tested against sample PCAP files and successfully produced logs including:

* `conn.log`
* `http.log`
* `files.log`
* `packet_filter.log`

Project documentation was also created to describe the installation, configuration, and usage process.

## Challenges Encountered

Several challenges were encountered during initial setup and testing:

* Configuring Zeek to run correctly within a Docker environment.
* Processing sample PCAP files that generated checksum and trace-related warnings.
* Coordinating development across different environments, as team members are using separate Docker installations and operating systems (Windows and VirtualBox/Linux).

The Zeek setup and analysis workflow were documented in the project README to support reproducibility across multiple operating systems and Docker environments

---
## Abdullahi Mohamed - Python Analysis & Reporting

Estimated Completion: ~30%

So far, I created an initial Python parser that reads Zeek log files and tested it using "conn.log" The script can read Zeek logs, display the records, and generate a basic summary including record count, source IPs, and destination ports. I also tested it with other Zeek logs and uploaded example output screenshots to the repository.
One challenge was learning the structure of Zeek logs and getting familiar with GitHub since I had limited experience with both. Because of that, I decided to focus on conn.log first since it contains the main connection information we will need later. Before Progress Report 2, I plan to expand the parser to generate more statistics, begin combining information from multiple Zeek logs, and start building the reporting and evaluation features needed for the final project.

---
## Adjustments Made

To address these challenges, the project workflow was adjusted to standardize around shared PCAP files as the primary input for analysis. This allows traffic generated in one environment to be analyzed consistently in another environment without requiring identical Docker configurations.

The project architecture was also refined to separate responsibilities among team members:

* **Member 1:** Docker network setup, traffic generation, and PCAP capture.
* **Member 2:** Zeek setup, log generation, documentation, and detection design.
* **Member 3:** Python-based log analysis, reporting, and evaluation metrics.

This separation reduces overlap and creates a clear end-to-end workflow:

```text
Traffic Generation
        ↓
PCAP Capture
        ↓
Zeek Analysis
        ↓
Log Generation
        ↓
Python Analysis & Metrics
```

## Next Steps

The next phase of development will focus on:

* Generating project-specific network traffic from the Docker environment.
* Capturing traffic into PCAP files.
* Simulating attack scenarios such as:

    * Port scans
    * Ping sweeps
    * SSH brute-force attempts
* Expanding detection logic using Zeek-generated logs.
* Integrating Python-based analysis to support evaluation metrics, including:

    * True Positives (TP)
    * False Positives (FP)
    * True Negatives (TN)
    * False Negatives (FN)
* Preparing datasets and scenarios for performance evaluation and final demonstrations.
---