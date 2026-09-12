# Phase 1 schema

## origins.csv
Strategic starting airports and positioning hubs.

## destinations.csv
Spatial airport points to plot in QGIS. `destination_iata` is the primary key.

## airlines.csv
Airline master data. `airline_id` is the primary key.

## routes.csv
Junction/edge table. Natural key: (`origin_iata`, `destination_iata`, `airline_id`).
One row means: this airline is a candidate/verified edge from origin to destination.
Evidence status is mandatory because route availability is temporal.

Later tables can add dated schedule observations, weekday coverage, prices, resorts,
hotel observations, packages and cancellation terms without changing this core graph.
