from __future__ import annotations
from dataclasses import dataclass, asdict
from math import hypot
from typing import Tuple

@dataclass(frozen=True)
class Producer:
    id: str
    cluster: str
    x: float
    y: float
    production_kwh_day: float
    alternative_eur_kwh: float
    fracta_price_eur_kwh: float

@dataclass(frozen=True)
class Station:
    id: str
    cluster: str
    x: float
    y: float
    demand_kwh_day: float
    public_price_ttc_eur_kwh: float

@dataclass(frozen=True)
class Buffer:
    id: str
    cluster: str
    x: float
    y: float
    capacity_kwh: float

@dataclass
class Assumptions:
    packet_kwh: float = 50.0
    pv5_payload_kwh: float = 150.0
    container_kwh: float = 3000.0
    source_to_charger_efficiency: float = 0.90
    pv5_energy_eur_kwh: float = 0.14
    pv5_consumption_kwh_km: float = 0.35
    pv5_vehicle_eur_km: float = 0.25
    pv5_driver_eur_h: float = 28.0
    pv5_speed_kmh: float = 35.0
    pv5_handling_h_trip: float = 0.25
    truck_energy_eur_kwh: float = 0.14
    truck_consumption_kwh_km: float = 1.20
    truck_vehicle_eur_km: float = 0.45
    truck_driver_eur_h: float = 32.0
    truck_speed_kmh: float = 50.0
    truck_handling_h_move: float = 0.50
    battery_cycle_eur_kwh_delivered: float = 0.04
    charger_ops_eur_kwh_delivered: float = 0.05
    vat: float = 0.20
    vehicle_autonomy: float = 0.0  # 0..1; reduces driving labour only, not handling

@dataclass
class ScenarioResult:
    name: str
    gross_kwh_day: float
    delivered_kwh_day: float
    pv5_km_day: float
    pv5_cost_day: float
    truck_km_day: float
    truck_cost_day: float
    purchase_cost_day: float
    storage_charger_cost_day: float
    total_cost_day: float
    total_cost_eur_kwh: float
    revenue_ht_day: float
    margin_day: float
    margin_eur_kwh: float

    def to_dict(self):
        return asdict(self)

def distance(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    return hypot(a[0]-b[0], a[1]-b[1])

def pv5_cost_km(a: Assumptions) -> float:
    driving_labour = (1.0 - a.vehicle_autonomy) * a.pv5_driver_eur_h / a.pv5_speed_kmh
    return a.pv5_vehicle_eur_km + a.pv5_consumption_kwh_km*a.pv5_energy_eur_kwh + driving_labour

def truck_cost_km(a: Assumptions) -> float:
    driving_labour = (1.0 - a.vehicle_autonomy) * a.truck_driver_eur_h / a.truck_speed_kmh
    return a.truck_vehicle_eur_km + a.truck_consumption_kwh_km*a.truck_energy_eur_kwh + driving_labour

def simulate(producers, stations, fixed_hub, mobile_buffers, assumptions, mode):
    gross = sum(p.production_kwh_day for p in producers)
    delivered = gross * assumptions.source_to_charger_efficiency
    pv5_km = pv5_cost = purchase = 0.0
    cluster_gross = {}

    for p in producers:
        target = fixed_hub if mode == "fixed" else mobile_buffers[p.cluster]
        d = distance((p.x,p.y),(target.x,target.y))
        trips = p.production_kwh_day / assumptions.pv5_payload_kwh
        km = 2*d*trips
        pv5_km += km
        pv5_cost += km*pv5_cost_km(assumptions) + trips*assumptions.pv5_driver_eur_h*assumptions.pv5_handling_h_trip
        cluster_gross[p.cluster] = cluster_gross.get(p.cluster,0) + p.production_kwh_day
        purchase += p.production_kwh_day*p.fracta_price_eur_kwh

    station_by_cluster = {s.cluster:s for s in stations}
    truck_km = departures = 0.0
    for cluster, energy in cluster_gross.items():
        s = station_by_cluster[cluster]
        origin = fixed_hub if mode == "fixed" else mobile_buffers[cluster]
        dep = energy / assumptions.container_kwh
        departures += dep
        truck_km += 2*distance((origin.x,origin.y),(s.x,s.y))*dep

    truck_cost = truck_km*truck_cost_km(assumptions) + departures*assumptions.truck_driver_eur_h*assumptions.truck_handling_h_move
    storage_charger = delivered*(assumptions.battery_cycle_eur_kwh_delivered + assumptions.charger_ops_eur_kwh_delivered)
    total = pv5_cost + truck_cost + purchase + storage_charger
    total_kwh = total/delivered if delivered else 0.0

    demand = sum(s.demand_kwh_day for s in stations)
    weighted_ttc = sum(s.demand_kwh_day*s.public_price_ttc_eur_kwh for s in stations)/demand
    sell_ht = weighted_ttc/(1+assumptions.vat)
    revenue = delivered*sell_ht
    margin = revenue-total

    return ScenarioResult("Hub fixe" if mode=="fixed" else "Buffers mobiles", gross, delivered, pv5_km, pv5_cost, truck_km, truck_cost, purchase, storage_charger, total, total_kwh, revenue, margin, margin/delivered)
