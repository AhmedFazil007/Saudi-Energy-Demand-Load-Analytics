"""Validate synthetic energy data and export grouped CSV summaries (stdlib only)."""
from pathlib import Path
from collections import defaultdict
import csv
import statistics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
with (ROOT / "data" / "03_energy_daily_synthetic.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

numeric = ["average_temperature_c", "estimated_consumption_mwh", "estimated_peak_load_mw", "renewable_share_assumption"]
for row in rows:
    for key in numeric:
        row[key] = float(row[key])

keys = [(r["date"], r["city"], r["customer_sector"]) for r in rows]
assert len(keys) == len(set(keys)), "Duplicate date/city/sector keys"
assert all(all(str(v) for v in r.values()) for r in rows), "Missing values"

def export(name, key_fn):
    groups = defaultdict(list)
    for r in rows:
        groups[key_fn(r)].append(r)
    result = []
    for name_key, records in sorted(groups.items()):
        result.append({
            "name": name_key,
            "records": len(records),
            "consumption_mwh": round(sum(r["estimated_consumption_mwh"] for r in records), 2),
            "max_record_peak_mw": max(r["estimated_peak_load_mw"] for r in records),
            "mean_temperature_c": round(statistics.mean(r["average_temperature_c"] for r in records), 2),
            "mean_assumed_renewable_share": round(statistics.mean(r["renewable_share_assumption"] for r in records), 4)
        })
    with (OUT / f"{name}_reproduced.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=result[0].keys())
        writer.writeheader()
        writer.writerows(result)

export("annual", lambda r: r["date"][:4])
export("monthly", lambda r: r["date"][:7])
export("city", lambda r: r["city"])
export("region", lambda r: r["region"])
export("sector", lambda r: r["customer_sector"])
print(f"Validated {len(rows):,} records")
print("Estimated consumption MWh:", round(sum(r["estimated_consumption_mwh"] for r in rows), 2))
