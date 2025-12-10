import csv
import re
from typing import List


def parse_sic_file(input_path: str) -> list[dict]:
    rows = []

    group_id = None
    industry_code = None
    industry_name = None

    header_pattern = re.compile(r"^(\d+)\s+([A-Za-z]+)\s{2,}(.*)$")
    range_pattern = re.compile(r"^(\d{4})-(\d{4})(?:\s+(.*))?$")

    with open(input_path, "r", encoding="utf-8") as file:
        for raw_line in file:
            if not raw_line.strip():
                continue

            stripped = raw_line.lstrip()

            # ✅ SIC ranges first
            range_match = range_pattern.match(stripped)
            if range_match and group_id is not None:
                rows.append({
                    "group_id": group_id,
                    "industry_code": industry_code,
                    "industry_name": industry_name,
                    "sic_start": int(range_match.group(1)),
                    "sic_end": int(range_match.group(2)),
                    "sic_description": range_match.group(3) or ""
                })
                continue

            # ✅ Headers second
            header_match = header_pattern.match(stripped)
            if header_match:
                group_id = int(header_match.group(1))
                industry_code = header_match.group(2)
                industry_name = header_match.group(3)

    return rows


def write_csv(data: list[dict], output_path: str) -> None:
    if not data:
        return

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    classification_list: List[int] = [5, 10, 12, 17, 30, 38, 48, 49]
    for category in classification_list:
        INPUT_FILE = f"Siccodes{category}.txt"
        OUTPUT_FILE = f"sic_codes{category}.csv"
        records = parse_sic_file(INPUT_FILE)
        write_csv(records, OUTPUT_FILE)
        print(f"✅ Converted {len(records)} rows to {OUTPUT_FILE}")
