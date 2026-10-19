# Saudi Energy Demand & Load Analytics

**Excel · Python · SQL · Interactive dashboard | 2022–2025**

I built this project around a practical energy-planning question: **How can consumption, peak load, temperature and customer-sector data be brought together to make demand patterns easier to understand?**

The dataset contains **58,440 synthetic daily city-sector observations** across **10 Saudi cities** and **four customer sectors**. It's a fictional scenario for analytics practice—not actual grid measurements or official energy statistics.

## Explore the dashboard

**[Open the interactive dashboard](https://ahmedfazil007.github.io/Saudi-Energy-Demand-Load-Analytics/)**

![Energy executive dashboard](assets/SEDI_Executive-Summary.png)

### Demand and temperature

![Demand and temperature](assets/SEDI_Demand&Temparature.png)

### Geographic and sector comparison

![Geographic and sector](assets/SEDI_Geographic&Sector.png)

The three-page dashboard runs in a browser. It's an HTML report, **not a Power BI (.pbix) file**.

## A few numbers from the simulated dataset

| Measure | Result |
|---|---:|
| Estimated energy consumption | **23.56 million MWh** |
| Daily city-sector observations | **58,440** |
| Highest individual-record peak load | **2,059 MW** |
| Mean recorded temperature | **24.98°C** |
| Mean assumed renewable share | **48.46%** |

The **2,059 MW** figure is the maximum for a single record, not the simultaneous peak demand of the whole grid. Renewable share is a modeled assumption, not measured generation.

## Seasonal analysis

I also explored [seasonal demand and temperature relationships](docs/SEASONAL_ANALYSIS.md), with a [reproducible Python script](python/seasonal_demand.py). In the synthetic data, summer has the highest average consumption per record (**494.55 MWh**), and the overall temperature-consumption correlation is about **0.234**. These are descriptive relationships, not forecasts.

## What stood out to me

**Industrial and residential demand account for most consumption.** Industrial contributes about **8.94M MWh (37.93%)**, followed by residential at **7.86M MWh (33.37%)**. If I were planning a forecasting exercise, these are the sectors I'd examine first.

**Riyadh has the largest city-level share in this scenario.** Its estimated consumption is around **3.94M MWh (16.74%)**. I'd break that down by month, sector and temperature before drawing any planning conclusions.

**Annual totals look fairly steady.** Consumption stays around **5.88–5.90M MWh per year**. That makes the monthly and seasonal patterns especially worth examining; stable annual totals can hide meaningful variation.

These are descriptive findings from synthetic data, not evidence of real grid conditions or operational savings.

## How I'd use this in a planning discussion

I'd focus on three things: identifying which sectors contribute most to demand, checking how consumption changes with temperature and season, and separating **energy consumption (MWh)** from **power demand (MW)**.

A real utility would need verified meter data, operational load measurements and forecasting validation before using these results to make capacity or investment decisions.

## Tools and files

| File | Purpose |
|---|---|
| [Interactive HTML dashboard](dashboard/index.html) | Three-page browser report |
| [Excel analysis workbook](excel/Saudi_Energy_Demand_Analysis.xlsx) | KPI summaries and charts |
| [Synthetic source data](data/03_energy_daily_synthetic.csv) | Daily city-sector observations |
| [Python loader](python/load_sqlite.py) | CSV to SQLite |
| [Python analysis](python/analyze_energy.py) | Checks and grouped summaries |
| [SQL queries](sql/energy_analysis.sql) | Six SQLite-compatible queries |

## Reproduce the analysis

From the repository root:

```bash
python python/load_sqlite.py
python python/analyze_energy.py
```

Both scripts use Python's standard library. Open `dashboard/index.html` in a browser to explore the dashboard, or use the live link above.

## What this project does—and doesn't—show

It demonstrates data preparation, KPI design, SQL analysis, reporting and energy-sector storytelling. It doesn't forecast actual Saudi electricity demand, measure real renewable generation or show verified operating improvements.

---

[Ahmed Fazil](https://github.com/AhmedFazil007)
