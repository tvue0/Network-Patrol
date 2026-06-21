Network Patrol
Group members: Ermias Kassa, Abdullahi Mohamed, Tony Vue
Leader: Tony Vue
Our project is to build a Network Intrusion Detection system (NIDS) using Docker, Zeek and Python. Using Docker, we will create several small, simulated networks with multiple devices communicating with each other. Zeek will monitor the network traffic and generate logs showing the activity between devices.
We will then use Python scripts to analyze the Zeek logs and identify suspicious behavior such as port scans, unusual connections, and any other potential attacks. WE will also simulate 2 different trafficking networks, one being normal usage between devices and one being attacked by a malicious device to test how well the system can detect threats.
Docker is going to be used to create and manage the different network hosts in a stimulating environment. Using docker will allow us to simulate multiple devices without needing separate physical machines and OS.
The goal of the project is to demonstrate how intrusion detection systems help monitor network activity, detect security threats and provide useful information for security network administrators. We will evaluate the system by measuring detection rates, alert generations and the overall performance under different network conditions

Recent research in network intrusion detection shows that combining signature-based and behavior-based methods works well for spotting malicious activity in real time. Studies also show that tools like Zeek are commonly used for monitoring network traffic, detecting unusual behavior, and analyzing security events in modern systems. In addition, prior work has looked at how well intrusion detection systems perform in terms of accuracy, false positives, and system load under different network conditions. These findings support our project idea, where we use Zeek for traffic monitoring and Python scripts to analyze logs and detect suspicious behavior in a controlled Docker-based setup.

References
Spring et al., “Evaluation of Intrusion Detection Systems in Modern Network Environments,” Empirical Software Engineering, 2021.
https://link.springer.com/article/10.1007/s10664-021-10046-w

Sharma et al., “A Survey on Intrusion Detection Systems and Techniques,” Journal of Big Data, 2020.
https://link.springer.com/article/10.1186/s40537-020-00382-x

https://docs.zeek.org/en/current/get-started.html

