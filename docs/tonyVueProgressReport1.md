Progress Report 1 — Member Contribution (Zeek + IDS Setup)
Work Completed (Your Contribution)
Established the local development environment using Docker on Windows
Successfully installed and verified Docker functionality (hello-world container test)
Pulled and validated the Zeek network security monitoring tool inside a Docker container
Created a structured project directory within the Git repository:
zeek/captures/ for packet capture files
zeek/logs/ for Zeek-generated output logs
Supporting documentation and project folders for organization
Obtained and imported a sample packet capture file (.pcap) from Wireshark sample datasets
Executed Zeek analysis on the packet capture using Docker with proper volume mounting
Resolved initial execution issues (command formatting and checksum warnings)
Successfully generated Zeek log outputs:
conn.log (connection-level network activity)
http.log (HTTP traffic data)
files.log (file transfer activity)
packet_filter.log (capture filtering metadata)
Technical Requirements Met (Course Alignment)

✔ Virtualization / Deployment

Docker used to containerize and run Zeek in an isolated environment

✔ Network Security Tooling

Zeek deployed as the primary Intrusion Detection System (IDS)
Packet capture analysis performed using real network traffic samples

✔ Programming / Automation (initial stage)

Environment prepared for Python-based log analysis (next phase)
Structured pipeline established for automated processing:
PCAP → Zeek → Log generation → Python analysis (planned)

✔ Experimental Evaluation (early foundation)

Successfully processed real packet capture data
Verified system ability to generate structured network logs for later analysis
Established baseline “normal traffic” dataset for future attack comparison
Observations / Initial Findings
Zeek successfully processes packet capture files and produces structured logs describing network activity between hosts
Initial warnings encountered (TCP checksum and filtered trace warnings) were expected in virtualized/sample environments and do not affect core functionality
Generated logs confirm visibility into:
Host-to-host communication patterns (conn.log)
Application-layer traffic (http.log)
File transfer behavior (files.log)
Current Status in Project Pipeline
PCAP Input → Zeek (Docker IDS) → Structured Logs Generated → Python Analysis (next phase)
Next Steps (Planned Contribution)
Develop Python-based parser for conn.log
Extract key network features (IP communication patterns, port usage, connection frequency)
Define baseline “normal traffic” behavior
Begin defining detection logic for:
Port scans
Unusual connection patterns
Support team in preparing attack simulation scenarios for evaluation (TP/FP/FN metrics)
Summary Statement (for report inclusion)

A functional Zeek-based intrusion detection pipeline was successfully implemented using Docker and tested with sample network traffic. The system is now capable of generating structured network logs that will serve as the foundation for anomaly detection and security analysis in later phases of the project. This establishes the core monitoring component of the Network Patrol IDS and enables future integration with Python-based analysis and attack evaluation metrics.