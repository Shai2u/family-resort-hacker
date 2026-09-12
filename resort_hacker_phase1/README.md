# Resort Hacker — Phase 1

A deliberately small Git/CSV/QGIS seed for mapping family-resort access.

## Current scope
- Strategic origins/hubs: TLV, HFA, ETM, LCA, PFO
- Candidate final resort gateway airports
- Airline master table
- Vertical route junction table (origin + destination + airline)
- No flight numbers, detailed schedules, fares, or hotel tables yet

## Source-of-truth
- Git/CSV: normalized structured facts used by QGIS/code
- Notion: methodology, decisions, interpretation, research notes
- QGIS: spatial exploration and visualization

## Evidence statuses
- `verified_bookable`: official airline pages showed bookable route examples when checked
- `verified_current_network`: official airline/network evidence supports the route
- `airport_airline_verified_destination_seed`: airline presence is verified but this row is only an initial structural seed
- `candidate_needs_route_verification`: plausible/useful edge intentionally retained as a research candidate; do not treat as confirmed

The dataset is a seed, not an exhaustive schedule.
