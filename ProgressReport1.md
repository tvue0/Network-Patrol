This should capture the team's progress report 1 as a whole.



as of right now

A functional Zeek-based network intrusion detection pipeline was successfully deployed using Docker,
and initial packet capture analysis demonstrates the system’s ability to generate structured logs for network traffic inspection.
The project architecture and evaluation approach have been defined, and future work will focus on attack simulation and automated log analysis.

Python Analysis & Reporting

Estimated Completion: ~30%

So far, I created an initial Python parser that reads Zeek log files and tested it using "conn.log" The script can read Zeek logs, display the records, and generate a basic summary including record count, source IPs, and destination ports. I also tested it with other Zeek logs and uploaded example output screenshots to the repository.

One challenge was learning the structure of Zeek logs and getting familiar with GitHub since I had limited experience with both. Because of that, I decided to focus on `conn.log` first since it contains the main connection information we will need later.

Before Progress Report 2, I plan to expand the parser to generate more statistics, begin combining information from multiple Zeek logs, and start building the reporting and evaluation features needed for the final project.
