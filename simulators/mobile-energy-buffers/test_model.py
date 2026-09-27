from fractasim import Assumptions, simulate, PRODUCERS, STATIONS, FIXED_HUB, MOBILE_BUFFERS
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
