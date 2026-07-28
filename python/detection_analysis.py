import csv
import os
import sys


PORT_THRESHOLD = 10
CONNECTION_THRESHOLD = 20
FAILED_CONNECTION_THRESHOLD = 10

FAILED_STATES = ["S0", "REJ", "RSTO", "RSTRH", "SH", "SHR"]


def read_zeek_log(file_path):
    records = []
    fields = []

    with open(file_path, "r", encoding="utf-8", errors="replace") as log_file:
        for line in log_file:
            line = line.strip()

            if line.startswith("#fields"):
                fields = line.split("\t")[1:]
                continue

            if not line or line.startswith("#"):
                continue

            values = line.split("\t")

            if len(values) < len(fields):
                values.extend(["-"] * (len(fields) - len(values)))

            records.append(dict(zip(fields, values)))

    return records


def analyze_connections(records):
    source_data = {}

    for record in records:
        source_ip = record.get("id.orig_h", "unknown")
        destination_ip = record.get("id.resp_h", "unknown")
        destination_port = record.get("id.resp_p", "-")
        connection_state = record.get("conn_state", "-")

        if source_ip not in source_data:
            source_data[source_ip] = {
                "connections": 0,
                "destination_ips": set(),
                "destination_ports": set(),
                "failed_connections": 0,
            }

        source_data[source_ip]["connections"] += 1
        source_data[source_ip]["destination_ips"].add(destination_ip)
        source_data[source_ip]["destination_ports"].add(destination_port)

        if connection_state in FAILED_STATES:
            source_data[source_ip]["failed_connections"] += 1

    results = []

    for source_ip, data in source_data.items():
        connections = data["connections"]
        unique_ips = len(data["destination_ips"])
        unique_ports = len(data["destination_ports"])
        failed_connections = data["failed_connections"]

        reasons = []

        if unique_ports >= PORT_THRESHOLD:
            reasons.append("Contacted many destination ports")

        if connections >= CONNECTION_THRESHOLD:
            reasons.append("Created many connections")

        if failed_connections >= FAILED_CONNECTION_THRESHOLD:
            reasons.append("Had many failed connections")

        if reasons:
            status = "SUSPICIOUS"
            reason = "; ".join(reasons)
        else:
            status = "NORMAL"
            reason = "No detection rule was triggered"

        results.append(
            {
                "source_ip": source_ip,
                "connections": connections,
                "unique_destination_ips": unique_ips,
                "unique_destination_ports": unique_ports,
                "failed_connections": failed_connections,
                "status": status,
                "reason": reason,
            }
        )

    return results


def save_results(results, log_path):
    os.makedirs("results", exist_ok=True)

    log_name = os.path.splitext(os.path.basename(log_path))[0]
    output_file = os.path.join("results", f"{log_name}_results.csv")

    columns = [
        "source_ip",
        "connections",
        "unique_destination_ips",
        "unique_destination_ports",
        "failed_connections",
        "status",
        "reason",
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(results)

    return output_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python detection_analysis.py path/to/conn.log")
        return

    log_path = sys.argv[1]

    if not os.path.exists(log_path):
        print("Error: Zeek conn.log was not found.")
        print("Path entered:", log_path)
        return

    records = read_zeek_log(log_path)

    if not records:
        print("No traffic records were found in:", log_path)
        return

    results = analyze_connections(records)
    output_file = save_results(results, log_path)

    suspicious_count = 0

    print("\nNetwork Patrol Analysis")
    print("-" * 45)
    print("Log file:", log_path)
    print("Total Zeek records:", len(records))
    print("Unique source IPs:", len(results))

    print("\nDetection Rules")
    print("-" * 45)
    print("Unique ports threshold:", PORT_THRESHOLD)
    print("Connections threshold:", CONNECTION_THRESHOLD)
    print("Failed connections threshold:", FAILED_CONNECTION_THRESHOLD)

    print("\nSource Summary")
    print("-" * 45)

    for result in results:
        print(
            result["source_ip"],
            "-",
            result["connections"],
            "connections,",
            result["unique_destination_ports"],
            "ports,",
            result["failed_connections"],
            "failed,",
            result["status"],
        )

        print("Reason:", result["reason"])

        if result["status"] == "SUSPICIOUS":
            suspicious_count += 1

    print("\nSuspicious source IPs:", suspicious_count)
    print("Results saved to:", output_file)


if __name__ == "__main__":
    main() 