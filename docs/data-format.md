# 🗂️ Data Formats

## targets.csv

`id,ra,dec,mag,teff,logL,priority,duration,sun`

## bright-stars.csv

Calibrators for photometry zero-points.

## example-lightcurve.csv

`time_days,flux` — 10 d, 1.2% dip at day 5. Validate with `scripts/check_data.py`.

All CSVs UTF-8, LF, header row required.
