# Saudi Energy Demand & Load Analytics (2022–2025)

**Excel · SQL · Python · Interactive Visualization | 58,440 synthetic observations**

> **Portfolio disclosure:** This project uses fictional Saudi energy data, not measured national electricity-grid data. Consumption is estimated, renewable share is assumed, and record-level peak loads do not represent a simultaneous national grid peak.

## Business challenge (STAR-D)

**Situation:** A fictional energy planning team needs visibility into electricity demand across Saudi cities, customer sectors, and seasons.

**Task:** Validate and analyze 58,440 daily city-sector records from 2022–2025, investigate demand and temperature patterns, and develop management-ready reporting.

**Approach:** Python validation and aggregation → SQLite SQL queries → Excel KPI summaries and charts → interactive HTML dashboards.

**Results:** The dataset indicates demand concentration in Industrial and Residential sectors and Riyadh, while annual total consumption varies relatively little.

## Executive KPIs

| Metric | Result |
|---|---:|
| Observations | **58,440** |
| Estimated total consumption | **23.56M MWh** |
| Maximum individual-record peak load | **2,059 MW** |
| Mean recorded temperature | **24.98°C** |
| Mean assumed renewable share | **48.46%** |
| Cities / sectors | **10 / 4** |

## Three key findings

1. **Sector concentration:** Industrial accounts for **8,936,834 MWh (37.93%)**, and Residential **7,861,691 MWh (33.37%)**. **Recommendation:** Prioritize forecasting and peak-management scenarios for these sectors.
2. **City concentration:** Riyadh leads with **3,943,155 MWh (16.74%)**. **Recommendation:** Evaluate Riyadh's seasonal demand profile before considering operational investments.
3. **Annual stability:** Annual consumption ranges from approximately **5.88M to 5.90M MWh**. **Recommendation:** Analyze within-year fluctuations rather than relying solely on annual totals.

These are descriptive observations, not evidence of real-world financial savings or causal effects.

## Interactive dashboard — redesigned energy theme

The redesigned dashboard uses **grid green, solar gold, hydro blue, and light neutral backgrounds**, with a fixed **1920 × 1080** canvas and page navigation below the canvas.

- **01 Executive Overview:** demand KPIs, monthly trends, city, sector and annual comparisons.
- **02 Demand & Temperature:** seasonal demand, temperature bands and record-level peak-load comparisons.
- **03 Geographic & Sector Performance:** regional and city demand, customer sectors, and assumed renewable shares.

The HTML dashboard is interactive and works offline when downloaded. It is **not a PBIX or Tableau workbook**.

## Repository files

| Path | Purpose |
|---|---|
| `data/03_energy_daily_synthetic.csv` | Synthetic source dataset |
| `excel/Saudi_Energy_Demand_Analysis.xlsx` | Excel KPI analysis, summaries and charts |
| `sql/energy_analysis.sql` | SQLite analytical queries |
| `python/load_sqlite.py` | Data import and SQL execution |
| `python/analyze_energy.py` | Data quality and grouped summaries |
| `dashboard/index.html` | Redesigned three-page interactive dashboard |
| `outputs/` | Exported analytical summaries |

**Upload status:** The files listed above are included in the complete project ZIP provided in the ChatGPT conversation from the ChatGPT conversation. They must be uploaded to this repository before these relative paths become clickable. The README alone does not contain the dashboard or dataset.

## How to run locally

1. Download the complete project ZIP and extract it.
2. Open `dashboard/index.html` in Chrome or Edge to explore the offline interactive dashboard.
3. Open `excel/Saudi_Energy_Demand_Analysis.xlsx` in Excel.
4. Run `python python/load_sqlite.py` and `python python/analyze_energy.py` from the project root with Python 3.

## Interpretation and limitations

- MWh is energy and may be aggregated across observations. MW is power; summing record-level peaks is not a valid simultaneous system peak.
- `renewable_share_assumption` is a modeled assumption, not measured renewable generation.
- The data is synthetic and no actual business or energy-system impact is claimed.

**Project focus:** Data cleaning · SQL · Python · Excel · Business intelligence · Energy demand analysis · Visualization
