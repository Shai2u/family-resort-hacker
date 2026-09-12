from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
origins = pd.read_csv(DATA / "origins.csv")
destinations = pd.read_csv(DATA / "destinations.csv")
airlines = pd.read_csv(DATA / "airlines.csv")
routes = pd.read_csv(DATA / "routes.csv")

errors = []
if origins.origin_iata.duplicated().any(): errors.append("Duplicate origin_iata")
if destinations.destination_iata.duplicated().any(): errors.append("Duplicate destination_iata")
if airlines.airline_id.duplicated().any(): errors.append("Duplicate airline_id")
if routes[["origin_iata","destination_iata","airline_id"]].duplicated().any():
    errors.append("Duplicate route natural key")

valid_airports = set(origins.origin_iata) | set(destinations.destination_iata)
bad_origins = sorted(set(routes.origin_iata) - valid_airports)
bad_destinations = sorted(set(routes.destination_iata) - valid_airports)
bad_airlines = sorted(set(routes.airline_id) - set(airlines.airline_id))
if bad_origins: errors.append(f"Unknown route origins: {bad_origins}")
if bad_destinations: errors.append(f"Unknown route destinations: {bad_destinations}")
if bad_airlines: errors.append(f"Unknown airline IDs: {bad_airlines}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"OK: {len(origins)} origins, {len(destinations)} destinations, "
      f"{len(airlines)} airlines, {len(routes)} route edges")
