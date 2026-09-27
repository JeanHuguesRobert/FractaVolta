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
    light_payload_kwh: float = 150.0
    container_kwh: float = 3000.0
    source_to_charger_efficiency: float = 0.90
    light_energy_eur_kwh: float = 0.14
    light_consumption_kwh_km: float = 0.35
    light_vehicle_eur_km: float = 0.25
    light_driver_eur_h: float = 28.0
    light_speed_kmh: float = 35.0
    light_handling_h_trip: float = 0.25
    heavy_energy_eur_kwh: float = 0.14
    heavy_consumption_kwh_km: float = 1.20
    heavy_vehicle_eur_km: float = 0.45
    heavy_driver_eur_h: float = 32.0
    heavy_speed_kmh: float = 50.0
    heavy_handling_h_move: float = 0.50
    battery_cycle_eur_kwh_delivered: float = 0.04
    charger_ops_eur_kwh_delivered: float = 0.05
    vat: float = 0.20
    vehicle_autonomy: float = 0.0  # 0..1; reduces driving labour only, not handling
    light_towing_capacity_kg: float = 1500.0  # declared towing capability; not converted to kWh automatically
    heavy_towing_capacity_kg: float = 30000.0  # declared towing capability; not converted to kWh automatically
    retail_price_ttc_eur_kwh: float | None = None  # optional uniform client price override

@dataclass
class ScenarioResult:
    name: str
    gross_kwh_day: float
    delivered_kwh_day: float
    light_km_day: float
    light_cost_day: float
    heavy_km_day: float
    heavy_cost_day: float
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

def light_cost_km(a: Assumptions) -> float:
    driving_labour = (1.0 - a.vehicle_autonomy) * a.light_driver_eur_h / a.light_speed_kmh
    return a.light_vehicle_eur_km + a.light_consumption_kwh_km*a.light_energy_eur_kwh + driving_labour

def heavy_cost_km(a: Assumptions) -> float:
    driving_labour = (1.0 - a.vehicle_autonomy) * a.heavy_driver_eur_h / a.heavy_speed_kmh
    return a.heavy_vehicle_eur_km + a.heavy_consumption_kwh_km*a.heavy_energy_eur_kwh + driving_labour

def simulate(producers, stations, fixed_hub, mobile_buffers, assumptions, mode):
    gross = sum(p.production_kwh_day for p in producers)
    delivered = gross * assumptions.source_to_charger_efficiency
    pv5_km = pv5_cost = purchase = 0.0
    cluster_gross = {}

    for p in producers:
        target = fixed_hub if mode == "fixed" else mobile_buffers[p.cluster]
        d = distance((p.x,p.y),(target.x,target.y))
        trips = p.production_kwh_day / assumptions.light_payload_kwh
        km = 2*d*trips
        pv5_km += km
        pv5_cost += km*light_cost_km(assumptions) + trips*assumptions.light_driver_eur_h*assumptions.light_handling_h_trip
        cluster_gross[p.cluster] = cluster_gross.get(p.cluster,0) + p.production_kwh_day
        purchase += p.production_kwh_day*p.fracta_price_eur_kwh

    station_by_cluster = {s.cluster:s for s in stations}
    heavy_km = departures = 0.0
    for cluster, energy in cluster_gross.items():
        s = station_by_cluster[cluster]
        origin = fixed_hub if mode == "fixed" else mobile_buffers[cluster]
        dep = energy / assumptions.container_kwh
        departures += dep
        heavy_km += 2*distance((origin.x,origin.y),(s.x,s.y))*dep

    heavy_cost = heavy_km*heavy_cost_km(assumptions) + departures*assumptions.heavy_driver_eur_h*assumptions.heavy_handling_h_move
    storage_charger = delivered*(assumptions.battery_cycle_eur_kwh_delivered + assumptions.charger_ops_eur_kwh_delivered)
    total = pv5_cost + heavy_cost + purchase + storage_charger
    total_kwh = total/delivered if delivered else 0.0

    demand = sum(s.demand_kwh_day for s in stations)
    weighted_ttc = assumptions.retail_price_ttc_eur_kwh if assumptions.retail_price_ttc_eur_kwh is not None else sum(s.demand_kwh_day*s.public_price_ttc_eur_kwh for s in stations)/demand
    sell_ht = weighted_ttc/(1+assumptions.vat)
    revenue = delivered*sell_ht
    margin = revenue-total

    return ScenarioResult("Hub fixe" if mode=="fixed" else "Buffers mobiles", gross, delivered, pv5_km, pv5_cost, heavy_km, heavy_cost, purchase, storage_charger, total, total_kwh, revenue, margin, margin/delivered)
