# Network Patrol Final Testing Results

## Detection Rules

The Python detector labels a source IP as suspicious when at least one of these rules is triggered:

- 10 or more unique destination ports
- 20 or more connections
- 10 or more failed connections

## Normal Traffic Test

The normal traffic log contained 8 Zeek connection records from 4 source IPs.

All four source IPs were labeled NORMAL, and no suspicious source IPs were detected.

| Measurement | Result |
|---|---:|
| Zeek records | 8 |
| Unique source IPs | 4 |
| Suspicious source IPs | 0 |
| Final classification | NORMAL |

## Nmap Port Scan Test

The attack log contained 1,014 Zeek connection records. The source IP 172.28.0.20 generated the Nmap port scan.

| Measurement | Result |
|---|---:|
| Zeek records | 1,014 |
| Connections from 172.28.0.20 | 1,010 |
| Unique destination ports | 1,001 |
| Failed connections | 1,001 |
| Suspicious source IPs | 1 |
| Final classification | SUSPICIOUS |

The attack source triggered all three detection rules because it contacted many ports, created many connections, and had many failed connections.

## Evaluation

The evaluation treats the normal-traffic file and attack file as two separate test scenarios.

| Measurement | Total |
|---|---:|
| True Positives | 1 |
| True Negatives | 1 |
| False Positives | 0 |
| False Negatives | 0 |

- The attack test was correctly detected as suspicious.
- The normal test was correctly detected as normal.
- No false alarms occurred during these two tests.
- No simulated attacks were missed.

## Conclusion

The detector successfully distinguished normal traffic from the simulated Nmap port scan. Normal traffic remained below the detection thresholds, while the Nmap scan produced more than 1,000 connections, destination ports, and failed connections. These results show that the threshold-based Python detector can identify a large port scan using Zeek conn.log data.