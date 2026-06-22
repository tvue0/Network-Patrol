"""

Basic Zeek log parser for Progress Report 1.
This script reads a Zeek log file and prints the records with a short summary.
"""

import sys


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
    path = sys.argv[1] if len(sys.argv) > 1 else "conn.log"
    fields, rows = read_zeek_log(path)

    print(f"Parsed {path}: {len(rows)} record(s), {len(fields)} fields\n")

    for number, row in enumerate(rows, 1):
        print(f"Record {number}:")
        width = max((len(key) for key in row), default=0)

        for key, value in row.items():
            if value not in ("-", "(empty)"):
                print(f"   {key:{width}} = {value}")

        print()

    print("Summary")
    print(f"   records: {len(rows)}")

    # These fields are useful for conn.log because they show traffic sources
    # and the ports that were contacted.
    if any("id.orig_h" in row for row in rows):
        source_ips = sorted({row["id.orig_h"] for row in rows if row.get("id.orig_h")})
        print(f"   source IPs: {len(source_ips)} {source_ips}")

    if any("id.resp_p" in row for row in rows):
        destination_ports = sorted({row["id.resp_p"] for row in rows if row.get("id.resp_p")})
        print(f"   destination ports: {len(destination_ports)} {destination_ports}")


if __name__ == "__main__":
    main()