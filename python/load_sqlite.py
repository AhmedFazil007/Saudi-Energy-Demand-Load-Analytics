"""Load the synthetic energy CSV into SQLite using the Python standard library."""
from pathlib import Path
import csv
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "outputs" / "energy_analytics.sqlite"
DB.parent.mkdir(exist_ok=True)

with sqlite3.connect(DB) as conn:
    conn.execute("DROP TABLE IF EXISTS energy_daily")
    conn.execute("""CREATE TABLE energy_daily (
        date TEXT, city TEXT, region TEXT, customer_sector TEXT,
        average_temperature_c REAL, estimated_consumption_mwh REAL,
        estimated_peak_load_mw REAL, renewable_share_assumption REAL
    )""")
    with (ROOT / "data" / "03_energy_daily_synthetic.csv").open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        fields = ["date", "city", "region", "customer_sector", "average_temperature_c",
                  "estimated_consumption_mwh", "estimated_peak_load_mw", "renewable_share_assumption"]
        conn.executemany("INSERT INTO energy_daily VALUES (?,?,?,?,?,?,?,?)",
                         ([row[k] for k in fields] for row in reader))
    conn.execute("CREATE INDEX idx_energy_date_city_sector ON energy_daily(date,city,customer_sector)")
    print("Loaded rows:", conn.execute("SELECT COUNT(*) FROM energy_daily").fetchone()[0])
print("Database:", DB)
