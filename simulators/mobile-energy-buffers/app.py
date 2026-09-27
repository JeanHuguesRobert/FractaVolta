import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from fractasim import Assumptions, Producer, simulate, user_fuel_savings, PRODUCERS, STATIONS, FIXED_HUB, MOBILE_BUFFERS

st.set_page_config(page_title="FractaVolta — Buffers mobiles", page_icon="⚡", layout="wide")
st.title("FractaVolta — chaîne agile de buffers énergétiques")
st.caption("MVP : producteurs Seconde Vie → tracteur léger → buffers mobiles → tracteurs → stations.")

with st.sidebar:
    st.header("Hypothèses")
    packet_kwh = st.slider("Energy Packet (kWh)", 20, 100, 50, 5)
    light_payload = st.slider("Énergie transportée par rotation légère (kWh)", 50, 300, 150, 10)
    container_kwh = st.slider("Capacité utile conteneur (kWh)", 1500, 4000, 3000, 100)
    efficiency = st.slider("Rendement source → borne", 0.75, 0.98, 0.90, 0.01)
    producer_price = st.slider("Prix producteur par défaut (€/kWh)", 0.05, 0.20, 0.10, 0.005)
    retail_price_ttc = st.slider("Prix client final TTC (€/kWh)", 0.30, 1.00, 0.65, 0.01)
    light_driver = st.slider("Coût conducteur tracteur léger (€/h)", 15, 45, 28, 1)
    light_consumption = st.slider("Conso tracteur léger + remorque (kWh/km)", 0.20, 0.80, 0.35, 0.01)
    light_towing_kg = st.slider("Capacité de tractage — tracteur léger (kg)", 500, 5000, 1500, 100)
    heavy_consumption = st.slider("Conso tracteur lourd (kWh/km)", 0.8, 2.5, 1.20, 0.05)
    heavy_towing_kg = st.slider("Capacité de tractage — tracteur lourd (kg)", 10000, 50000, 30000, 1000)
    autonomy_pct = st.slider("Autonomie de conduite des véhicules (%)", 0, 100, 0, 5)
    st.caption("Scénario prospectif : ce paramètre réduit le coût de conduite des tracteurs légers et lourds. La manutention reste humaine dans ce modèle.")
    battery_cycle = st.slider("Usure batterie (€/kWh livré)", 0.00, 0.10, 0.04, 0.005)
    charger_ops = st.slider("Borne + exploitation (€/kWh)", 0.00, 0.15, 0.05, 0.005)

    st.header("Gain usager — carburant seulement")
    fuel_price = st.slider("Prix carburant thermique (€/L)", 1.20, 3.00, 2.17, 0.01)
    thermal_consumption = st.slider("Conso véhicule thermique (L/100 km)", 3.0, 12.0, 6.5, 0.1)
    ev_consumption = st.slider("Conso véhicule électrique (kWh/100 km)", 10.0, 30.0, 17.0, 0.5)
    small_km = st.slider("Petit rouleur (km/mois)", 100, 1500, 500, 50)
    medium_km = st.slider("Rouleur moyen (km/mois)", 500, 2500, 1000, 50)
    large_km = st.slider("Gros rouleur (km/mois)", 1000, 5000, 2000, 100)
    st.caption("Comparaison limitée au coût d’énergie d’usage : carburant liquide vs électricité. Achat, entretien, assurance et financement du véhicule sont exclus.")

a = Assumptions(
    packet_kwh=float(packet_kwh),
    light_payload_kwh=float(light_payload),
    container_kwh=float(container_kwh),
    source_to_charger_efficiency=float(efficiency),
    light_driver_eur_h=float(light_driver),
    light_consumption_kwh_km=float(light_consumption),
    heavy_consumption_kwh_km=float(heavy_consumption),
    light_towing_capacity_kg=float(light_towing_kg),
    heavy_towing_capacity_kg=float(heavy_towing_kg),
    battery_cycle_eur_kwh_delivered=float(battery_cycle),
    charger_ops_eur_kwh_delivered=float(charger_ops),
    vehicle_autonomy=float(autonomy_pct) / 100.0,
    retail_price_ttc_eur_kwh=float(retail_price_ttc),
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
d_km = fixed.light_km_day - mobile.light_km_day

break_even_ttc = mobile.total_cost_eur_kwh * (1.0 + a.vat)

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Coût mobile", f"{mobile.total_cost_eur_kwh:.3f} €/kWh", f"{-d_cost:.3f} vs hub fixe", delta_color="inverse")
c2.metric("Marge contributive", f"{mobile.margin_eur_kwh:.3f} €/kWh livré", f"{mobile.margin_day:,.0f} €/j")
c3.metric("Kilomètres tracteur léger", f"{mobile.light_km_day:,.0f} km/j", f"{-d_km:,.0f} vs hub fixe", delta_color="inverse")
c4.metric("Énergie livrée", f"{mobile.delivered_kwh_day/1000:.2f} MWh/j", f"{mobile.gross_kwh_day/1000:.2f} MWh bruts")
c5.metric("Prix d’équilibre TTC", f"{break_even_ttc:.3f} €/kWh", f"prix client {retail_price_ttc:.2f} €")

user_profiles = [
    ("Petit rouleur", small_km),
    ("Rouleur moyen", medium_km),
    ("Gros rouleur", large_km),
]
user_savings = [
    (label, user_fuel_savings(km, thermal_consumption, fuel_price, ev_consumption, retail_price_ttc))
    for label, km in user_profiles
]

st.subheader("Gain usager : passer du thermique à l’électrique")
g1,g2,g3 = st.columns(3)
for col, (label, r) in zip((g1,g2,g3), user_savings):
    col.metric(label, f"{r['saving_month']:.0f} €/mois", f"{r['saving_year']:.0f} €/an")
st.caption(
    f"À {fuel_price:.2f} €/L et {thermal_consumption:.1f} L/100 km, le thermique coûte "
    f"{user_savings[0][1]['thermal_cost_100km']:.2f} €/100 km. "
    f"À {retail_price_ttc:.2f} €/kWh et {ev_consumption:.1f} kWh/100 km, l’électrique coûte "
    f"{user_savings[0][1]['electric_cost_100km']:.2f} €/100 km."
)

with st.expander("Comment lire le gain usager ?"):
    st.markdown("""
Ce calcul répond à une question volontairement étroite : **combien l’usager économise-t-il chaque mois sur l’énergie nécessaire pour rouler ?**

Il compare le coût d’un véhicule thermique en litres/100 km au coût d’un véhicule électrique en kWh/100 km, au prix client final choisi dans le simulateur.

Les trois profils servent seulement de repères de kilométrage et restent modifiables. Le résultat n’inclut pas le prix d’achat du véhicule, le financement, l’entretien, l’assurance, les pneus, les taxes ou la valeur de revente.
""")

with st.expander("Prix final et marge par kWh"):
    st.markdown(f"""
Le curseur **Prix client final TTC** représente le prix affiché au client final à la borne, l’équivalent du prix « à la pompe » pour l’électricité.

Le modèle retire la TVA avant de calculer la recette opérateur. Avec les hypothèses actuelles :

- prix client TTC : **{retail_price_ttc:.2f} €/kWh** ;
- coût modélisé : **{mobile.total_cost_eur_kwh:.3f} €/kWh livré** ;
- marge contributive : **{mobile.margin_eur_kwh:.3f} €/kWh livré** ;
- prix d’équilibre TTC : **{break_even_ttc:.3f} €/kWh**.

Cette marge n’est pas encore une rentabilité comptable complète : le prototype ne modélise pas encore tous les CAPEX, coûts financiers, assurances, fiscalités spécifiques ou taux d’utilisation réels des actifs.
""")

with st.expander("Capacités de tractage"):
    st.markdown(f"""
Le modèle distingue deux classes génériques : **tracteur léger** et **tracteur lourd**.

- Tracteur léger : capacité déclarée **{light_towing_kg:,.0f} kg**
- Tracteur lourd : capacité déclarée **{heavy_towing_kg:,.0f} kg**

Ces valeurs expriment une contrainte physique de véhicule. Elles ne sont pas converties automatiquement en kWh, car il faut connaître la masse réelle de la batterie, de sa structure, de la remorque et des équipements. Un modèle comme le Kia PV5 peut servir d’exemple de tracteur léger, mais il n’est pas la définition de la catégorie.
""")

with st.expander("Pourquoi tester la conduite autonome ?"):
    st.markdown("""
La collecte capillaire multiplie les petites rotations et donc les heures de conduite. Si, à l’avenir, les utilitaires et les poids lourds peuvent circuler de façon autonome, ce poste de coût peut fortement diminuer.

Le curseur **Autonomie de conduite** ne suppose pas que toute la chaîne est robotisée : il réduit uniquement le coût de conduite. Le chargement, le déchargement et les autres opérations de manutention restent comptés comme aujourd’hui.

Cela permet d’explorer une conséquence importante du modèle FractaVolta : **plus le transport devient autonome, plus des paquets énergétiques petits et nombreux peuvent devenir économiquement intéressants**, ce qui favorise un réseau distribué et agile.
""")

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
        {"Scénario":fixed.name,"Coût €/kWh":fixed.total_cost_eur_kwh,"Marge €/kWh":fixed.margin_eur_kwh,"Marge €/j":fixed.margin_day,"km tracteur léger/j":fixed.light_km_day,"km tracteur lourd/j":fixed.heavy_km_day},
        {"Scénario":mobile.name,"Coût €/kWh":mobile.total_cost_eur_kwh,"Marge €/kWh":mobile.margin_eur_kwh,"Marge €/j":mobile.margin_day,"km tracteur léger/j":mobile.light_km_day,"km tracteur lourd/j":mobile.heavy_km_day},
    ])
    st.dataframe(df,use_container_width=True,hide_index=True)
    bar=go.Figure()
    bar.add_bar(name="Hub fixe",x=["Coût","Marge"],y=[fixed.total_cost_eur_kwh,fixed.margin_eur_kwh])
    bar.add_bar(name="Buffers mobiles",x=["Coût","Marge"],y=[mobile.total_cost_eur_kwh,mobile.margin_eur_kwh])
    bar.update_layout(barmode="group",yaxis_title="€/kWh",height=420)
    st.plotly_chart(bar,use_container_width=True)

    costs=pd.DataFrame({
        "Poste":["Achat producteurs","Collecte légère","Transport lourd","Cycle batterie + borne"],
        "€/jour":[mobile.purchase_cost_day,mobile.light_cost_day,mobile.heavy_cost_day,mobile.storage_charger_cost_day],
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

    st.subheader("Gain usager selon le kilométrage")
    km_points=[]
    for km in range(250,3001,250):
        r=user_fuel_savings(km,thermal_consumption,fuel_price,ev_consumption,retail_price_ttc)
        km_points.append({"Kilométrage mensuel":km,"Gain mensuel":r["saving_month"]})
    kdf=pd.DataFrame(km_points)
    kf=go.Figure()
    kf.add_scatter(x=kdf["Kilométrage mensuel"],y=kdf["Gain mensuel"],mode="lines+markers",name="Gain usager")
    kf.add_hline(y=0,line_dash="dash")
    kf.update_layout(xaxis_title="Kilométrage mensuel (km)",yaxis_title="Économie carburant (€/mois)",height=500)
    st.plotly_chart(kf,use_container_width=True)

    st.subheader("Sensibilité au prix client final")
    retail_points=[]
    for price in [0.30+i*0.025 for i in range(29)]:
        aa = Assumptions(**{**a.__dict__, "retail_price_ttc_eur_kwh": price})
        rf=simulate(producers,STATIONS,FIXED_HUB,MOBILE_BUFFERS,aa,"fixed")
        rm=simulate(producers,STATIONS,FIXED_HUB,MOBILE_BUFFERS,aa,"mobile")
        retail_points.append({"Prix client TTC":price,"Hub fixe":rf.margin_eur_kwh,"Buffers mobiles":rm.margin_eur_kwh})
    rdf=pd.DataFrame(retail_points)
    pf=go.Figure()
    pf.add_scatter(x=rdf["Prix client TTC"],y=rdf["Hub fixe"],mode="lines",name="Hub fixe")
    pf.add_scatter(x=rdf["Prix client TTC"],y=rdf["Buffers mobiles"],mode="lines",name="Buffers mobiles")
    pf.add_hline(y=0,line_dash="dash")
    pf.update_layout(xaxis_title="Prix client final TTC (€/kWh)",yaxis_title="Marge contributive (€/kWh livré)",height=500)
    st.plotly_chart(pf,use_container_width=True)

    st.subheader("Sensibilité à la conduite autonome")
    autonomy_points=[]
    for pct in range(0,101,10):
        aa = Assumptions(**{**a.__dict__, "vehicle_autonomy": pct/100.0})
        rf=simulate(producers,STATIONS,FIXED_HUB,MOBILE_BUFFERS,aa,"fixed")
        rm=simulate(producers,STATIONS,FIXED_HUB,MOBILE_BUFFERS,aa,"mobile")
        autonomy_points.append({"Autonomie (%)":pct,"Hub fixe":rf.total_cost_eur_kwh,"Buffers mobiles":rm.total_cost_eur_kwh})
    adf=pd.DataFrame(autonomy_points)
    af=go.Figure()
    af.add_scatter(x=adf["Autonomie (%)"],y=adf["Hub fixe"],mode="lines+markers",name="Hub fixe")
    af.add_scatter(x=adf["Autonomie (%)"],y=adf["Buffers mobiles"],mode="lines+markers",name="Buffers mobiles")
    af.update_layout(xaxis_title="Autonomie de conduite (%)",yaxis_title="Coût total (€/kWh)",height=500)
    st.plotly_chart(af,use_container_width=True)

with tab_data:
    st.dataframe(pd.DataFrame([p.__dict__ for p in producers]),use_container_width=True,hide_index=True)
    export=pd.DataFrame([fixed.to_dict(),mobile.to_dict()])
    st.download_button("Télécharger résultats CSV",export.to_csv(index=False).encode("utf-8"),"fractavolta_simulation.csv","text/csv")

st.divider()
st.caption("MVP exploratoire — hypothèses synthétiques ; aucune promesse commerciale ou validation réglementaire.")
