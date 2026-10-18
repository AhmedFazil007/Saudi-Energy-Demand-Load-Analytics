-- SQLite, synthetic energy observations
SELECT COUNT(*) AS observations, SUM(estimated_consumption_mwh) AS total_mwh, MAX(estimated_peak_load_mw) AS max_record_peak_mw FROM energy_daily;
SELECT SUBSTR(date,1,4) AS year, SUM(estimated_consumption_mwh) AS total_mwh FROM energy_daily GROUP BY 1 ORDER BY 1;
SELECT city, region, SUM(estimated_consumption_mwh) AS total_mwh FROM energy_daily GROUP BY city,region ORDER BY total_mwh DESC;
SELECT customer_sector, SUM(estimated_consumption_mwh) AS total_mwh, AVG(renewable_share_assumption) AS mean_assumed_renewable_share FROM energy_daily GROUP BY customer_sector ORDER BY total_mwh DESC;
SELECT SUBSTR(date,1,7) AS month, SUM(estimated_consumption_mwh) AS total_mwh FROM energy_daily GROUP BY 1 ORDER BY 1;
SELECT CASE WHEN average_temperature_c < 15 THEN 'Under 15 C' WHEN average_temperature_c < 25 THEN '15-25 C' WHEN average_temperature_c < 35 THEN '25-35 C' ELSE '35 C+' END AS temperature_band, COUNT(*) AS records, AVG(estimated_consumption_mwh) AS avg_mwh FROM energy_daily GROUP BY 1 ORDER BY 1;
