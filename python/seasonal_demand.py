"""Seasonal demand and temperature association, synthetic data only.
Run: python python/seasonal_demand.py
Standard library only. Produces outputs/seasonal_summary.csv and
outputs/sector_temperature_association.csv.
"""
from pathlib import Path
from collections import defaultdict
import csv, math
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
SEASONS = {12:"Winter",1:"Winter",2:"Winter",3:"Spring",4:"Spring",5:"Spring",
           6:"Summer",7:"Summer",8:"Summer",9:"Autumn",10:"Autumn",11:"Autumn"}
with (ROOT / "data/03_energy_daily_synthetic.csv").open(encoding="utf-8-sig",newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    r["consumption"] = float(r["estimated_consumption_mwh"])
    r["temperature"] = float(r["average_temperature_c"])
    r["season"] = SEASONS[int(r["date"][5:7])]
def correlation(pairs):
    n=len(pairs)
    if n<3: return None
    mx=sum(x for x,y in pairs)/n; my=sum(y for x,y in pairs)/n
    num=sum((x-mx)*(y-my) for x,y in pairs)
    xx=sum((x-mx)**2 for x,y in pairs); yy=sum((y-my)**2 for x,y in pairs)
    return num/math.sqrt(xx*yy) if xx>0 and yy>0 else None
groups=defaultdict(list)
for r in rows: groups[r["season"]].append(r)
with (OUT/"seasonal_summary.csv").open("w",newline="") as f:
    w=csv.writer(f);w.writerow(["season","records","total_consumption_mwh","mean_consumption_mwh","mean_temperature_c"])
    for season in ("Winter","Spring","Summer","Autumn"):
        subset=groups[season];n=len(subset)
        w.writerow([season,n,round(sum(r["consumption"] for r in subset),2),
                    round(sum(r["consumption"] for r in subset)/n,2),
                    round(sum(r["temperature"] for r in subset)/n,2)])
sectors=defaultdict(list)
for r in rows: sectors[r["customer_sector"]].append((r["temperature"],r["consumption"]))
with (OUT/"sector_temperature_association.csv").open("w",newline="") as f:
    w=csv.writer(f);w.writerow(["sector","observations","pearson_r_temperature_vs_consumption"])
    for sector,pairs in sorted(sectors.items()):
        value=correlation(pairs)
        w.writerow([sector,len(pairs),round(value,4) if value is not None else ""])
print(f"Analyzed {len(rows):,} synthetic records. Output saved in outputs/.")
print("Associations are descriptive and do not establish causal temperature effects.")
