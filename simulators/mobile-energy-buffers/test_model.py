from fractasim import Assumptions, Producer, simulate, PRODUCERS, STATIONS, FIXED_HUB, MOBILE_BUFFERS
a=Assumptions()
f=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a,"fixed")
m=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a,"mobile")
assert m.delivered_kwh_day == f.delivered_kwh_day
assert m.light_km_day < f.light_km_day
assert m.total_cost_eur_kwh < f.total_cost_eur_kwh
print("OK")
print(round(f.total_cost_eur_kwh,4), round(m.total_cost_eur_kwh,4))


a_auto=Assumptions(vehicle_autonomy=1.0)
m_auto=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a_auto,"mobile")
assert m_auto.total_cost_eur_kwh < m.total_cost_eur_kwh
assert m_auto.light_cost_day > 0  # handling and vehicle/energy costs remain
print("AUTO",round(m_auto.total_cost_eur_kwh,4))


caps=Assumptions(light_towing_capacity_kg=1800, heavy_towing_capacity_kg=32000)
assert caps.light_towing_capacity_kg == 1800
assert caps.heavy_towing_capacity_kg == 32000
assert caps.light_payload_kwh == 150.0
print("TOWING", int(caps.light_towing_capacity_kg), int(caps.heavy_towing_capacity_kg))


retail_low=Assumptions(retail_price_ttc_eur_kwh=0.50)
retail_high=Assumptions(retail_price_ttc_eur_kwh=0.80)
m_low=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,retail_low,"mobile")
m_high=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,retail_high,"mobile")
assert m_high.margin_eur_kwh > m_low.margin_eur_kwh

break_even_ttc = m.total_cost_eur_kwh * (1.0 + a.vat)
retail_be=Assumptions(retail_price_ttc_eur_kwh=break_even_ttc)
m_be=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,retail_be,"mobile")
assert abs(m_be.margin_eur_kwh) < 1e-9
print("RETAIL", round(m_low.margin_eur_kwh,4), round(m_high.margin_eur_kwh,4), round(break_even_ttc,4))


from fractasim import user_fuel_savings
u_small=user_fuel_savings(500,6.5,2.0,17.0,0.65)
u_medium=user_fuel_savings(1000,6.5,2.0,17.0,0.65)
u_large=user_fuel_savings(2000,6.5,2.0,17.0,0.65)
assert u_small["saving_month"] > 0
assert abs(u_medium["saving_month"] - 2*u_small["saving_month"]) < 1e-9
assert abs(u_large["saving_month"] - 4*u_small["saving_month"]) < 1e-9
print("USER_SAVINGS", round(u_small["saving_month"],2), round(u_medium["saving_month"],2), round(u_large["saving_month"],2))


from fractasim.data import CORRIDORS
from fractasim.model import distance
import json, os

assert "T20 (Ajaccio–Corte–Bastia)" in CORRIDORS
assert len(CORRIDORS["T20 (Ajaccio–Corte–Bastia)"]) > 5
d_corte_bastia = distance((9.1490, 42.3094), (9.4509, 42.6973))
assert 55.0 <= d_corte_bastia <= 75.0  # realistic road km Corte-Bastia

reg_path = os.path.join(os.path.dirname(__file__), "data", "registre_producteurs_edf_corse.json")
assert os.path.exists(reg_path), "Register file must exist"
with open(reg_path, "r", encoding="utf-8") as f:
    reg = json.load(f)
assert len(reg) >= 700
hta_count = sum(1 for r in reg if r.get("tension") == "HTA")
assert hta_count >= 30
total_p = sum(r.get("puissance_kw", 0) for r in reg)
assert 200_000 <= total_p <= 250_000  # ~233 MWc
assert m.containers_needed == 2
assert m.light_tractors_needed >= 1
assert m.heavy_tractors_needed >= 1
assert m.co2_avoided_tons_year > 0

# Test HTA producer direct buffering (no light km generated)
p_hta = [Producer("P_HTA", "Bastia", 9.42, 42.42, 10000, 0.08, 0.10, "HTA")]
m_hta = simulate(p_hta, STATIONS, FIXED_HUB, MOBILE_BUFFERS, a, "mobile")
assert m_hta.light_km_day == 0.0
assert m_hta.heavy_km_day > 0.0
assert m_hta.containers_needed == 4

print("CORSICA_GIS_OK", round(d_corte_bastia, 1), "km", len(reg), "producers", round(total_p/1000, 1), "MWc")
print("FLEET_SIZING_OK", m.containers_needed, "containers", m.light_tractors_needed, "light", m.heavy_tractors_needed, "heavy")


