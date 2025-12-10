import csv
import re
import pandas as pd
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
                sic_description = range_match.group(3) or ""
                industry_name_full = f"{industry_name}: {sic_description}".strip()
                rows.append({
                    "group_id": group_id,
                    "industry_code": industry_code,
                    "sic_start": int(range_match.group(1)),
                    "sic_end": int(range_match.group(2)),
                    "sic_description": industry_name_full
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

    # ✅ Convert TXT → CSV once
    for category in classification_list:
        INPUT_FILE = f"Siccodes{category}.txt"
        OUTPUT_FILE = f"sic_codes{category}.csv"
        records = parse_sic_file(INPUT_FILE)
        write_csv(records, OUTPUT_FILE)
        print(f"✅ Converted {len(records)} rows to {OUTPUT_FILE}")

    # ✅ Load all CSVs once
    category_dfs: dict[int, pd.DataFrame] = {
        category: pd.read_csv(f"sic_codes{category}.csv")
        for category in classification_list
    }

    rows = []

    # ✅ Build ONE row per SIC
    for industry_index in range(100, 10000):
        row = {"sic": industry_index}

        # Default descriptions for unmatched categories
        default_descriptions = {
            5: "Other -- Mines, Constr, BldMt, Trans, Hotels, Bus Serv, Entertainment, Finance",
            10: "Other -- Mines, Constr, BldMt, Trans, Hotels, Bus Serv, Entertainment, Finance",
            12: "Other -- Mines, Constr, BldMt, Trans, Hotels, Bus Serv, Entertainment, Finance",
            17: "Other",
            30: "Everything Else",
            38: "Almost Nothing",
            48: "Almost Nothing",
            49: "Almost Nothing"
        }

        for category, df in category_dfs.items():
            match = df[(df["sic_start"] <= industry_index) & (df["sic_end"] >= industry_index)]
            
            if not match.empty:
                row[f"sic_ff{category}_group"] = int(match["group_id"].iloc[0])
                row[f"sic_ff{category}_desc"] = match["sic_description"].iloc[0]
            elif category in default_descriptions:
                # Apply default values for unmatched categories
                row[f"sic_ff{category}_group"] = category
                row[f"sic_ff{category}_desc"] = default_descriptions[category]



        rows.append(row)

    # ✅ Final merged dataframe
    final_df = pd.DataFrame(rows)
    group_cols = [c for c in final_df.columns if c.endswith("_group")]

    for col in group_cols:
        final_df[group_cols] = final_df[group_cols].fillna(0).astype(int)
    
    final_df = final_df.rename(columns=lambda c: c.replace("_group", ""))


    final_df.to_csv("sic_final_crosswalk.csv", index=False)
    print(f"✅ Final crosswalk written with {len(final_df)} rows")
