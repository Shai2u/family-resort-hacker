# Agent instructions

1. Read README.md and schema.md before editing data.
2. Preserve stable IDs (IATA and airline_id).
3. Do not convert an expected/unverified route into a confirmed route without evidence.
4. Prefer append/update with `checked_date` and `source_url` rather than deleting uncertainty.
5. Never infer that unpublished future inventory means a route does not exist.
6. Keep CSV files UTF-8, comma-delimited, one header row, no index column.
7. Run `python scripts/validate_data.py` before committing.
8. QML belongs under qgis/styles/ and should reference stable CSV field names.
