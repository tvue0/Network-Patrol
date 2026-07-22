"""

Basic Zeek log parser for Progress Report 1.
This script reads a Zeek log file and prints the records with a short summary.
"""

import sys
from collections import Counter

def read_zeek_log(path):
    fields = []
    rows = []

    with open(path, encoding="utf-8", errors="replace") as file:
        for line in file:
            line = line.rstrip("\n")

            # Zeek uses the #fields line to list the column names.
            if line.startswith("#fields"):
                fields = line.split("\t")[1:]

            # Other lines starting with # are metadata, not traffic records.
            elif line.startswith("#") or not line.strip():
                continue

            else:
                values = line.split("\t")

                # Match each value to its field name so the data is easier to read.
                rows.append(dict(zip(fields, values)))

    return fields, rows


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "zeek/logs/conn.log"
    fields, rows = read_zeek_log(path)

   # print(f"Parsed {path}: {len(rows)} record(s), {len(fields)} fields\n")

   # for number, row in enumerate(rows, 1):
       # print(f"Record {number}:")
       # width = max((len(key) for key in row), default=0)

       # for key, value in row.items():
           # if value not in ("-", "(empty)"):
               # print(f"   {key:{width}} = {value}")

       # print()

    print("Summary")
    print("=" * 40)
    print("Network Patrol Security Report")
    print("=" * 40)

    print(f"\nLog File: {path}")

    print(f"\nConnections Observed: {len(rows)}")

    source_ips = sorted(
        {row["id.orig_h"] for row in rows if row.get("id.orig_h")}
    )

    destination_ips = sorted(
        {row["id.resp_h"] for row in rows if row.get("id.resp_h")}
    )

    destination_ports = sorted(
        {row["id.resp_p"] for row in rows if row.get("id.resp_p")}
    )

    services = sorted(
        {row["service"] for row in rows
         if row.get("service") not in ("", "-", "(empty)")}
    )

    source_counter = Counter(
        row["id.orig_h"]
        for row in rows
        if row.get("id.orig_h")
    )

    destination_counter = Counter(
        row["id.resp_h"]
        for row in rows
        if row.get("id.resp_h")
    )

    port_counter = Counter(
        row["id.resp_p"]
        for row in rows
        if row.get("id.resp_p")
    )

    print(f"Unique Source Hosts: {len(source_ips)}")
    print(f"Unique Destination Hosts: {len(destination_ips)}")

    print(f"\nSource Hosts:")
    for ip in source_ips:
        print(f"  - {ip}")

    print(f"\nDestination Hosts:")
    for ip in destination_ips:
        print(f"  - {ip}")

    print(f"\nUnique Destination Ports: {len(destination_ports)}")

    print(f"\nServices Detected:")
    if services:
        for service in services:
            print(f"  - {service}")
    else:
        print("  None")

    print("\nTop Source Hosts")
    print("----------------")

    for host, count in source_counter.most_common(5):
        print(f"{host:20} {count} connection(s)")


    print("\nTop Destination Hosts")
    print("---------------------")

    for host, count in destination_counter.most_common(5):
        print(f"{host:20} {count} connection(s)")


    print("\nTop Destination Ports")
    print("---------------------")

    for port, count in port_counter.most_common(10):
        print(f"{port:20} {count} connection(s)")


    print("\nPotential Findings")
    print("------------------")

    if "http" in services:
        print("✓ HTTP traffic detected.")

    if "dns" in services:
	print("DNS traffic detected.")

    if len(destination_ports) > 10:
        print("✓ Possible Nmap port scan detected ({len(destination_ports)} unique destination ports observed.")
    else:
        print("✓ No obvious large port scan detected.")

    print("\nAnalysis Complete.")

if __name__=="__main__":
    main()
