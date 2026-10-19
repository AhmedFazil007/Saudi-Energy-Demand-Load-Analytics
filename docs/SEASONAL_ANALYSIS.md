# Seasonal Demand and Temperature Analysis

I wanted to look beyond annual energy totals to see how consumption changes between seasons. This analysis uses the **58,440 synthetic city-sector records** already in the repository.

## What the data shows

| Season | Observations | Total modeled consumption | Mean consumption per record | Mean temperature |
|---|---:|---:|---:|---:|
| Winter | 14,440 | 5,072,611 MWh | 351.29 MWh | 15.07°C |
| Spring | 14,720 | 5,573,789 MWh | 378.65 MWh | 24.28°C |
| Summer | 14,720 | 7,279,759 MWh | 494.55 MWh | 34.86°C |
| Autumn | 14,560 | 5,632,431 MWh | 386.84 MWh | 25.53°C |

Summer has the highest average modeled consumption per record. The overall Pearson correlation between temperature and consumption is about **0.234**.

The relationship varies by sector: **Commercial 0.533**, **Residential 0.466**, **Government 0.376**, **Industrial 0.196**.

## How I'd use it

For a real demand-planning team, this would be a reason to explore **sector-specific temperature sensitivity** and seasonal forecasting, rather than applying one temperature adjustment to every customer type.

These are associations in simulated observations, **not causal estimates or validated forecasts**. Season, city, sector and data-generation assumptions may influence the relationships.

## Reproduce

Run `python python/seasonal_demand.py` from the repository root. It uses the Python standard library and exports `outputs/seasonal_summary.csv` and `outputs/sector_temperature_association.csv`.

I checked the figures above against the local synthetic CSV; they should be reproducible with the script.
