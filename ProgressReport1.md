This should capture the team's progress report 1 as a whole.



as of right now

A functional Zeek-based network intrusion detection pipeline was successfully deployed using Docker,
and initial packet capture analysis demonstrates the system’s ability to generate structured logs for network traffic inspection.
The project architecture and evaluation approach have been defined, and future work will focus on attack simulation and automated log analysis.


### Ermias Kassa – Docker Setup Progress

For my part of the project, I worked on setting up the Docker lab environment. I created an attacker container and a victim container and connected them through the same Docker network. I tested the setup using `ping`, `curl`, and `nmap` to make sure the containers could communicate and generate traffic.

I also added Docker setup and usage instructions to the README so other group members can run the same environment. The current Docker setup is working, but PCAP capture has not been fully added yet. The traffic can be captured later using tools like tcpdump or Zeek.

Some issues I ran into were Docker Compose setup problems, GitHub authentication using a Personal Access Token, and container name conflicts. I was able to resolve these issues and continue development on a separate branch to avoid affecting the main branch.

Before Progress Report 2, my next steps are to implement PCAP capture from Docker-generated traffic, create additional test traffic, and work with the team to ensure the Docker environment integrates properly with Zeek for monitoring and analysis.
