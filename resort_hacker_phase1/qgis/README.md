# QGIS setup

1. Load `data/destinations.csv` as Delimited Text:
   - X = longitude
   - Y = latitude
   - CRS = EPSG:4326
2. Load `data/origins.csv` the same way.
3. Load `data/routes.csv` and `data/airlines.csv` as non-spatial tables.
4. Create relations:
   - destinations.destination_iata -> routes.destination_iata
   - origins.origin_iata -> routes.origin_iata
   - airlines.airline_id -> routes.airline_id
5. Save QML styles in `qgis/styles/`.
