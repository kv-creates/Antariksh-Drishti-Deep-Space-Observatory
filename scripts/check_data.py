"""Check data CSVs for header + row sanity (used in CI)."""
import csv, sys, os
ok=True
for path in ["data/targets.csv","data/bright-stars.csv","data/example-lightcurve.csv"]:
    if not os.path.exists(path):
        print(f"missing {path}"); ok=False; continue
    with open(path, newline="", encoding="utf-8") as f:
        r=list(csv.DictReader(f))
        if not r:
            print(f"empty {path}"); ok=False
        else:
            print(f"{path}: {len(r)} rows, cols={list(r[0].keys())[:6]}")
if not ok:
    sys.exit(1)
print("check_data: OK")
