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
