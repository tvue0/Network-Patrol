This should capture the team's progress report 1 as a whole.



as of right now

# Progress Report 1 – Zeek Analysis Component

## Completion Status

Current completion is estimated at **30–35%** of the overall project.

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
