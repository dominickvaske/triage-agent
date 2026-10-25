"""Fake data for the triage agent. Just Python dicts - no database needed."""

ASSETS = {
    "GEN-04": {"name": "Diesel generator", "site": "Site 4", "location": "behind Building C", "installed": 2009},
    "GEN-07": {"name": "Diesel generator", "site": "Site 7", "location": "north lot", "installed": 2021},
    "HVAC-12": {"name": "Rooftop HVAC unit", "site": "Site 4", "location": "Building A roof", "installed": 2015},
    "VEH-31": {"name": "Ford F-250 utility truck", "site": "Motor pool", "location": "bay 2", "installed": 2018},
    "PUMP-02": {"name": "Water pump", "site": "Site 7", "location": "pump house", "installed": 2004},
}

PAST_INCIDENTS = [
    {"asset_id": "GEN-04", "date": "2026-03-02", "summary": "Grinding noise, bearing worn", "priority": "high", "team": "electrical"},
    {"asset_id": "GEN-04", "date": "2025-11-19", "summary": "Failed weekly load test", "priority": "high", "team": "electrical"},
    {"asset_id": "HVAC-12", "date": "2026-07-14", "summary": "Not cooling, refrigerant low", "priority": "medium", "team": "hvac"},
    {"asset_id": "VEH-31", "date": "2026-01-08", "summary": "Check engine light", "priority": "low", "team": "fleet"},
    {"asset_id": "PUMP-02", "date": "2026-05-30", "summary": "Leaking at seal", "priority": "medium", "team": "facilities"},
]

TEAMS = {
    "electrical": "Generators, power distribution, lighting",
    "hvac": "Heating, cooling, ventilation",
    "fleet": "Vehicles",
    "facilities": "Plumbing, pumps, buildings, everything else",
}

REPORTS = [
    "big generator behind bldg C is making a grinding sound again, kinda smells like burning??",
    "AC on the roof of building A stopped working, its 95 degrees in the office",
    "truck in bay 2 wont start. no rush, we have the other one",
    "water on the floor in the pump house at site 7. not sure where its coming from",
    "the coffee machine in the break room is broken",
]
