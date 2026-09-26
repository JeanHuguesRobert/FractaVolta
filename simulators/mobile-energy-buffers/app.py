import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from fractasim import Assumptions, Producer, simulate, PRODUCERS, STATIONS, FIXED_HUB, MOBILE_BUFFERS

st.set_page_config(page_title="FractaVolta — Buffers mobiles", page_icon="⚡", layout="wide")
st.title("FractaVolta — chaîne agile de buffers énergétiques")
st.caption("MVP : producteurs Seconde Vie → PV5 → buffers mobiles → tracteurs → stations.")

with st.sidebar:
    st.header("Hypothèses")
    packet_kwh = st.slider("Energy Packet (kWh)", 20, 100, 50, 5)
    pv5_payload = st.slider("Charge énergie / rotation PV5 (kWh)", 50, 200, 150, 10)
    container_kwh = st.slider("Capacité utile conteneur (kWh)", 1500, 4000, 3000, 100)
    efficiency = st.slider("Rendement source → borne", 0.75, 0.98, 0.90, 0.01)
    producer_price = st.slider("Prix producteur par défaut (€/kWh)", 0.05, 0.20, 0.10, 0.005)
    pv5_driver = st.slider("Coût conducteur PV5 (€/h)", 15, 45, 28, 1)
    pv5_consumption = st.slider("Conso PV5 + remorque (kWh/km)", 0.20, 0.60, 0.35, 0.01)
    truck_consumption = st.slider("Conso tracteur (kWh/km)", 0.8, 2.2, 1.20, 0.05)
    battery_cycle = st.slider("Usure batterie (€/kWh livré)", 0.00, 0.10, 0.04, 0.005)
    charger_ops = st.slider("Borne + exploitation (€/kWh)", 0.00, 0.15, 0.05, 0.005)

a = Assumptions(
    packet_kwh=float(packet_kwh),
    pv5_payload_kwh=float(pv5_payload),
    container_kwh=float(container_kwh),
    source_to_charger_efficiency=float(efficiency),
    pv5_driver_eur_h=float(pv5_driver),
    pv5_consumption_kwh_km=float(pv5_consumption),
    truck_consumption_kwh_km=float(truck_consumption),
    battery_cycle_eur_kwh_delivered=float(battery_cycle),
    charger_ops_eur_kwh_delivered=float(charger_ops),
)

producers = [
    Producer(
        p.id, p.cluster, p.x, p.y, p.production_kwh_day,
        p.alternative_eur_kwh,
        max(float(producer_price), p.alternative_eur_kwh + 0.001)
    )
    for p in PRODUCERS
]

fixed = simulate(producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, a, "fixed")
mobile = simulate(producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, a, "mobile")

d_cost = fixed.total_cost_eur_kwh - mobile.total_cost_eur_kwh
d_km = fixed.pv5_km_day - mobile.pv5_km_day

c1,c2,c3,c4 = st.columns(4)
c1.metric("Coût mobile", f"{mobile.total_cost_eur_kwh:.3f} €/kWh", f"{-d_cost:.3f} vs hub fixe", delta_color="inverse")
c2.metric("Marge mobile", f"{mobile.margin_eur_kwh:.3f} €/kWh", f"{mobile.margin_day:,.0f} €/j")
c3.metric("Kilomètres PV5", f"{mobile.pv5_km_day:,.0f} km/j", f"{-d_km:,.0f} vs hub fixe", delta_color="inverse")
c4.metric("Énergie livrée", f"{mobile.delivered_kwh_day/1000:.2f} MWh/j", f"{mobile.gross_kwh_day/1000:.2f} MWh bruts")

tab_map, tab_fin, tab_sens, tab_data = st.tabs(["Carte réseau","Économie","Sensibilité","Données"])

with tab_map:
    st.subheader("Topologie simplifiée")
    st.info("Coordonnées synthétiques dans ce MVP ; elles seront remplacées par de vrais sites corses.")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[p.x for p in producers], y=[p.y for p in producers],
        mode="markers+text", text=[p.id for p in producers],
        textposition="top center", name="Producteurs",
        marker=dict(size=[8+p.production_kwh_day/80 for p in producers], symbol="circle"),
        customdata=[[p.cluster,p.production_kwh_day,p.fracta_price_eur_kwh] for p in producers],
        hovertemplate="<b>%{text}</b><br>%{customdata[0]}<br>%{customdata[1]:.0f} kWh/j<br>Achat %{customdata[2]:.3f} €/kWh<extra></extra>"
    ))
    fig.add_trace(go.Scatter(
        x=[b.x for b in MOBILE_BUFFERS.values()], y=[b.y for b in MOBILE_BUFFERS.values()],
        mode="markers+text", text=[b.id for b in MOBILE_BUFFERS.values()],
        textposition="bottom center", name="Buffers mobiles",
        marker=dict(size=20, symbol="square")
    ))
    fig.add_trace(go.Scatter(
        x=[s.x for s in STATIONS], y=[s.y for s in STATIONS],
        mode="markers+text", text=[s.id for s in STATIONS],
        textposition="top center", name="Stations",
        marker=dict(size=22, symbol="diamond"),
        customdata=[[s.public_price_ttc_eur_kwh,s.demand_kwh_day] for s in STATIONS],
        hovertemplate="<b>%{text}</b><br>%{customdata[0]:.2f} €/kWh TTC<br>%{customdata[1]:.0f} kWh/j<extra></extra>"
    ))
    for p in producers:
        b=MOBILE_BUFFERS[p.cluster]
        fig.add_trace(go.Scatter(x=[p.x,b.x],y=[p.y,b.y],mode="lines",line=dict(width=1),showlegend=False,hoverinfo="skip"))
    station_by_cluster={s.cluster:s for s in STATIONS}
    for cl,b in MOBILE_BUFFERS.items():
        s=station_by_cluster[cl]
        fig.add_trace(go.Scatter(x=[b.x,s.x],y=[b.y,s.y],mode="lines",line=dict(width=3,dash="dash"),showlegend=False,hoverinfo="skip"))
    fig.update_layout(height=650,legend=dict(orientation="h"),margin=dict(l=20,r=20,t=20,b=20))
    fig.update_yaxes(scaleanchor="x",scaleratio=1)
    st.plotly_chart(fig,use_container_width=True)

with tab_fin:
    df=pd.DataFrame([
        {"Scénario":fixed.name,"Coût €/kWh":fixed.total_cost_eur_kwh,"Marge €/kWh":fixed.margin_eur_kwh,"Marge €/j":fixed.margin_day,"km PV5/j":fixed.pv5_km_day,"km PL/j":fixed.truck_km_day},
        {"Scénario":mobile.name,"Coût €/kWh":mobile.total_cost_eur_kwh,"Marge €/kWh":mobile.margin_eur_kwh,"Marge €/j":mobile.margin_day,"km PV5/j":mobile.pv5_km_day,"km PL/j":mobile.truck_km_day},
    ])
    st.dataframe(df,use_container_width=True,hide_index=True)
    bar=go.Figure()
    bar.add_bar(name="Hub fixe",x=["Coût","Marge"],y=[fixed.total_cost_eur_kwh,fixed.margin_eur_kwh])
    bar.add_bar(name="Buffers mobiles",x=["Coût","Marge"],y=[mobile.total_cost_eur_kwh,mobile.margin_eur_kwh])
    bar.update_layout(barmode="group",yaxis_title="€/kWh",height=420)
    st.plotly_chart(bar,use_container_width=True)

    costs=pd.DataFrame({
        "Poste":["Achat producteurs","Collecte PV5","Backbone PL","Cycle batterie + borne"],
        "€/jour":[mobile.purchase_cost_day,mobile.pv5_cost_day,mobile.truck_cost_day,mobile.storage_charger_cost_day],
    })
    pie=go.Figure(data=[go.Pie(labels=costs["Poste"],values=costs["€/jour"],hole=.45)])
    pie.update_layout(height=420)
    st.plotly_chart(pie,use_container_width=True)

with tab_sens:
    points=[]
    for price in [0.05+i*0.005 for i in range(31)]:
        ps=[
            Producer(p.id,p.cluster,p.x,p.y,p.production_kwh_day,p.alternative_eur_kwh,max(price,p.alternative_eur_kwh+0.001))
            for p in PRODUCERS
        ]
        rf=simulate(ps,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a,"fixed")
        rm=simulate(ps,STATIONS,FIXED_HUB,MOBILE_BUFFERS,a,"mobile")
        points.append({"Prix producteur":price,"Hub fixe":rf.margin_eur_kwh,"Buffers mobiles":rm.margin_eur_kwh})
    sens=pd.DataFrame(points)
    f=go.Figure()
    f.add_scatter(x=sens["Prix producteur"],y=sens["Hub fixe"],mode="lines",name="Hub fixe")
    f.add_scatter(x=sens["Prix producteur"],y=sens["Buffers mobiles"],mode="lines",name="Buffers mobiles")
    f.add_hline(y=0,line_dash="dash")
    f.update_layout(xaxis_title="Prix producteur (€/kWh)",yaxis_title="Marge contributive (€/kWh)",height=500)
    st.plotly_chart(f,use_container_width=True)

with tab_data:
    st.dataframe(pd.DataFrame([p.__dict__ for p in producers]),use_container_width=True,hide_index=True)
    export=pd.DataFrame([fixed.to_dict(),mobile.to_dict()])
    st.download_button("Télécharger résultats CSV",export.to_csv(index=False).encode("utf-8"),"fractavolta_simulation.csv","text/csv")

st.divider()
st.caption("MVP exploratoire — hypothèses synthétiques ; aucune promesse commerciale ou validation réglementaire.")
