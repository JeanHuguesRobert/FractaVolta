from fractasim import Assumptions, simulate, PRODUCERS, STATIONS, FIXED_HUB, MOBILE_BUFFERS
a=Assumptions()
f=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a,"fixed")
m=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a,"mobile")
assert m.delivered_kwh_day == f.delivered_kwh_day
assert m.pv5_km_day < f.pv5_km_day
assert m.total_cost_eur_kwh < f.total_cost_eur_kwh
print("OK")
print(round(f.total_cost_eur_kwh,4), round(m.total_cost_eur_kwh,4))


a_auto=Assumptions(vehicle_autonomy=1.0)
m_auto=simulate(PRODUCERS,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a_auto,"mobile")
assert m_auto.total_cost_eur_kwh < m.total_cost_eur_kwh
assert m_auto.pv5_cost_day > 0  # handling and vehicle/energy costs remain
print("AUTO",round(m_auto.total_cost_eur_kwh,4))
