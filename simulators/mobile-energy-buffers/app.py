import json
import os
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from fractasim import (
    Assumptions,
    Producer,
    simulate,
    user_fuel_savings,
    PRODUCERS,
    STATIONS,
    FIXED_HUB,
    MOBILE_BUFFERS,
)
from fractasim.data import CORRIDORS

st.set_page_config(page_title="FractaVolta — Buffers mobiles Corse", page_icon="⚡", layout="wide")
st.title("FractaVolta — Chaîne agile de buffers énergétiques")
st.caption("Modélisation insulaire corse : producteurs Seconde Vie → collecte légère → buffers mobiles → corridors T20/T10/T50 → stations urbaines.")

@st.cache_data
def load_solar_register():
    path = os.path.join(os.path.dirname(__file__), "data", "registre_producteurs_edf_corse.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

solar_register = load_solar_register()

with st.sidebar:
    st.header("1. Périmètre de simulation")
    scope_options = [
        "Échantillon pilote (12 sites témoins MVP — 4,5 MWh/j)",
        "Seconde Vie Imminente ≤ 2030 (61 sites — 24,1 MWc)",
        "Seconde Vie Court terme 2031–2035 (145 sites — 99,9 MWc)",
        "Total Seconde Vie ≤ 2035 (206 sites — 124,1 MWc)",
        "Grandes centrales HTA sol (34 parcs — 154,6 MWc)",
        "Bassin Plaine Orientale (255 sites — 86,6 MWc)",
        "Bassin Ajaccio (157 sites — 46,9 MWc)",
        "Bassin Bastia (139 sites — 42,3 MWc)",
        "Bassin Corte (183 sites — 56,6 MWc)",
    ]
    if "custom_producers" in st.session_state and st.session_state["custom_producers"]:
        custom_label = f"Sélection personnalisée ({len(st.session_state['custom_producers'])} sites)"
        if custom_label not in scope_options:
            scope_options.append(custom_label)
        default_scope_idx = scope_options.index(custom_label) if st.session_state.get("simulation_scope") == custom_label else 0
    else:
        default_scope_idx = 0

    selected_scope = st.selectbox(
        "Échelle modélisée :",
        scope_options,
        index=default_scope_idx,
        help="Passez de l'échantillon pilote à l'échelle macro du registre des producteurs solaires en Corse."
    )

    st.header("2. Hypothèses techno-économiques")
    packet_kwh = st.slider("Energy Packet (kWh)", 20, 100, 50, 5)
    light_payload = st.slider("Énergie transportée par rotation légère (kWh)", 50, 300, 150, 10)
    container_kwh = st.slider("Capacité utile conteneur (kWh)", 1500, 4000, 3000, 100)
    efficiency = st.slider("Rendement source → borne", 0.75, 0.98, 0.90, 0.01)
    producer_price = st.slider("Prix d'achat producteur par défaut (€/kWh)", 0.05, 0.20, 0.10, 0.005)
    retail_price_ttc = st.slider("Prix client final TTC (€/kWh)", 0.30, 1.00, 0.65, 0.01)
    light_driver = st.slider("Coût conducteur tracteur léger (€/h)", 15, 45, 28, 1)
    light_consumption = st.slider("Conso tracteur léger + remorque (kWh/km)", 0.20, 0.80, 0.35, 0.01)
    light_towing_kg = st.slider("Capacité de tractage — tracteur léger (kg)", 500, 5000, 1500, 100)
    heavy_consumption = st.slider("Conso tracteur lourd (kWh/km)", 0.8, 2.5, 1.20, 0.05)
    heavy_towing_kg = st.slider("Capacité de tractage — tracteur lourd (kg)", 10000, 50000, 30000, 1000)
    autonomy_pct = st.slider("Autonomie de conduite des véhicules (%)", 0, 100, 0, 5)
    st.caption("Scénario prospectif : ce paramètre réduit le coût de conduite des tracteurs légers et lourds. La manutention reste humaine.")
    battery_cycle = st.slider("Usure batterie (€/kWh livré)", 0.00, 0.10, 0.04, 0.005)
    charger_ops = st.slider("Borne + exploitation (€/kWh)", 0.00, 0.15, 0.05, 0.005)

    st.header("3. Gain usager — carburant seulement")
    fuel_price = st.slider("Prix carburant thermique (€/L)", 1.20, 3.00, 2.00, 0.01)
    thermal_consumption = st.slider("Conso véhicule thermique (L/100 km)", 3.0, 12.0, 6.5, 0.1)
    ev_consumption = st.slider("Conso véhicule électrique (kWh/100 km)", 10.0, 30.0, 17.0, 0.5)
    small_km = st.slider("Petit rouleur (km/mois)", 100, 1500, 500, 50)
    medium_km = st.slider("Rouleur moyen (km/mois)", 500, 2500, 1000, 50)
    st.header("4. Flexibilité réseau & Écrêtement EDF-SEI")
    curtailment_pct = st.slider("Taux d'écrêtement solaire évité (%)", 0, 50, 20, 5, help="Part de la production solaire aux heures de midi qui serait bridée ou déconnectée par EDF-SEI sans nos conteneurs.")
    thermal_fuel_eur = st.slider("Coût fioul évité centrales EDF (€/kWh)", 0.10, 0.35, 0.18, 0.01, help="Coût du combustible fossile évité aux centrales thermiques de Lucciana et du Vazzio lors de la pointe du soir.")
    flexibility_fee = st.slider("Prime de flexibilité rémunérée (€/kWh)", 0.00, 0.15, 0.04, 0.005, help="Rémunération de flexibilité/réserve versée par l'opérateur (EDF-SEI / CRE) pour l'évitement de combustible fossile et la tenue de réseau.")

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
    curtailment_rate=float(curtailment_pct) / 100.0,
    thermal_avoided_fuel_eur_kwh=float(thermal_fuel_eur),
    flexibility_remuneration_eur_kwh=float(flexibility_fee),
)

# Résolution des producteurs selon le périmètre sélectionné
if selected_scope == "Échantillon pilote (12 sites témoins MVP — 4,5 MWh/j)":
    active_producers = [
        Producer(
            p.id, p.cluster, p.x, p.y, p.production_kwh_day,
            p.alternative_eur_kwh,
            max(float(producer_price), p.alternative_eur_kwh + 0.001),
            tension=getattr(p, "tension", "BT"),
        )
        for p in PRODUCERS
    ]
    scope_desc = "12 sites représentatifs répartis sur Bastia, Ajaccio, Corte et Plaine Orientale."
elif selected_scope.startswith("Sélection personnalisée"):
    records = st.session_state.get("custom_producers", [])
    active_producers = [
        Producer(
            id=r["id"],
            cluster=r["cluster"],
            x=r["longitude"],
            y=r["latitude"],
            production_kwh_day=float(r.get("production_estimee_kwh_jour", 300)),
            alternative_eur_kwh=0.085,
            fracta_price_eur_kwh=max(float(producer_price), 0.085 + 0.001),
            tension=r.get("tension", "BT"),
        )
        for r in records
    ]
    scope_desc = f"{len(records)} sites filtrés sur mesure depuis l'explorateur du Registre."
else:
    if "≤ 2030" in selected_scope:
        subset = [r for r in solar_register if r.get("horizon_seconde_vie") == "Imminent (<= 2030)"]
    elif "2031–2035" in selected_scope:
        subset = [r for r in solar_register if r.get("horizon_seconde_vie") == "Court terme (2031-2035)"]
    elif "Total Seconde Vie" in selected_scope:
        subset = [r for r in solar_register if r.get("horizon_seconde_vie") in ["Imminent (<= 2030)", "Court terme (2031-2035)"]]
    elif "Grandes centrales HTA" in selected_scope:
        subset = [r for r in solar_register if r.get("tension") == "HTA"]
    elif "Plaine Orientale" in selected_scope:
        subset = [r for r in solar_register if r.get("cluster") == "Plaine Orientale"]
    elif "Ajaccio" in selected_scope:
        subset = [r for r in solar_register if r.get("cluster") == "Ajaccio"]
    elif "Bastia" in selected_scope:
        subset = [r for r in solar_register if r.get("cluster") == "Bastia"]
    elif "Corte" in selected_scope:
        subset = [r for r in solar_register if r.get("cluster") == "Corte"]
    else:
        subset = solar_register

    active_producers = [
        Producer(
            id=r["id"],
            cluster=r["cluster"],
            x=r["longitude"],
            y=r["latitude"],
            production_kwh_day=float(r.get("production_estimee_kwh_jour", 300)),
            alternative_eur_kwh=0.085,
            fracta_price_eur_kwh=max(float(producer_price), 0.085 + 0.001),
            tension=r.get("tension", "BT"),
        )
        for r in subset
    ]
    scope_desc = f"{len(subset)} sites issus de l'extraction officielle ODRÉ / EDF-SEI."

fixed = simulate(active_producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, a, "fixed")
mobile = simulate(active_producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, a, "mobile")

d_cost = fixed.total_cost_eur_kwh - mobile.total_cost_eur_kwh
d_km = fixed.light_km_day - mobile.light_km_day
break_even_ttc = mobile.total_cost_eur_kwh * (1.0 + a.vat)

# Bandeau de synthèse du périmètre
st.info(f"📍 **Périmètre actif : {selected_scope}** — {len(active_producers)} producteurs simulés ({mobile.gross_kwh_day/1000:.2f} MWh/j bruts, {mobile.delivered_kwh_day/1000:.2f} MWh/j livrés). *{scope_desc}*")

# Ligne 1 : Indicateurs Économiques
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Coût de revient mobile", f"{mobile.total_cost_eur_kwh:.3f} €/kWh", f"{-d_cost:.3f} vs hub fixe", delta_color="inverse")
c2.metric("Marge contributive", f"{mobile.margin_eur_kwh:.3f} €/kWh livré", f"{mobile.margin_day:,.0f} €/j")
c3.metric("Marge globale annuelle", f"{mobile.margin_day * 365 / 1000:,.1f} k€/an", f"recette : {mobile.revenue_ht_day * 365 / 1000:,.0f} k€ HT/an")
c4.metric("Énergie livrée", f"{mobile.delivered_kwh_day/1000:.2f} MWh/j", f"{mobile.gross_kwh_day/1000:.2f} MWh bruts")
c5.metric("Prix d'équilibre TTC", f"{break_even_ttc:.3f} €/kWh", f"prix client {retail_price_ttc:.2f} €")

# Ligne 2 : Dimensionnement de la Flotte & Impact Environnemental
f1, f2, f3, f4, f5 = st.columns(5)
f1.metric("Conteneurs 3 MWh requis", f"{mobile.containers_needed} unités", f"{mobile.containers_needed * 3:.0f} MWh de stockage tampon")
f2.metric("Tracteurs lourds", f"{mobile.heavy_tractors_needed} en rotation", f"{mobile.heavy_km_day:,.0f} km/j de conteneurs")
f3.metric("Tracteurs légers", f"{mobile.light_tractors_needed} en rotation", f"{-d_km:,.0f} km vs hub", delta_color="inverse", help=f"{mobile.light_km_day:,.0f} km/j de navettes capillaires")
f4.metric("CO₂ fossile évité", f"{mobile.co2_avoided_tons_year:,.0f} t/an", "remplacement fossile insulaire")
f5.metric("Sites solaires modélisés", f"{len(active_producers)}", f"{sum(1 for p in active_producers if getattr(p, 'tension', 'BT')=='HTA')} HTA, {sum(1 for p in active_producers if getattr(p, 'tension', 'BT')=='BT')} BT")

# Ligne 3 : Flexibilité insulaire & Évitement de carburant thermique EDF-SEI
fx1, fx2, fx3, fx4, fx5 = st.columns(5)
fx1.metric("Énergie fatale sauvée", f"{mobile.curtailed_kwh_day/1000:.2f} MWh/j", f"{mobile.curtailed_kwh_day*365/1000:,.0f} MWh/an sauvés d'écrêtement")
fx2.metric("Fioul EDF économisé", f"{mobile.thermal_fuel_saved_eur_day:,.0f} €/j", f"{mobile.thermal_fuel_saved_eur_day*365/1000:,.0f} k€/an économisés par EDF")
fx3.metric("Carburant fossile évité", f"{mobile.fuel_liters_saved_year:,.0f} L/an", f"{mobile.fuel_liters_saved_year/1000:.1f} m³ de fioul Lucciana/Vazzio")
fx4.metric("Prime de flexibilité", f"{mobile.flexibility_revenue_day*365/1000:,.1f} k€/an", f"+{mobile.flexibility_revenue_day:,.0f} €/j pour FractaVolta")
fx5.metric("Marge bonifiée", f"{mobile.margin_with_flexibility_eur_kwh:.3f} €/kWh", f"+{mobile.flexibility_revenue_day:,.0f} €/j", delta_color="normal", help=f"{mobile.margin_with_flexibility_day:,.0f} €/j avec prime flexibilité")


user_profiles = [
    ("Petit rouleur", small_km),
    ("Rouleur moyen", medium_km),
    ("Gros rouleur", large_km),
]
user_savings = [
    (label, user_fuel_savings(km, thermal_consumption, fuel_price, ev_consumption, retail_price_ttc))
    for label, km in user_profiles
]

st.subheader("Gain usager : passer du thermique à l'électrique")
g1, g2, g3 = st.columns(3)
for col, (label, r) in zip((g1, g2, g3), user_savings):
    col.metric(label, f"{r['saving_month']:.0f} €/mois", f"{r['saving_year']:.0f} €/an")
st.caption(
    f"À {fuel_price:.2f} €/L et {thermal_consumption:.1f} L/100 km, le thermique coûte "
    f"{user_savings[0][1]['thermal_cost_100km']:.2f} €/100 km. "
    f"À {retail_price_ttc:.2f} €/kWh et {ev_consumption:.1f} kWh/100 km, l'électrique coûte "
    f"{user_savings[0][1]['electric_cost_100km']:.2f} €/100 km."
)

with st.expander("Comment lire les métriques de flotte et de dimensionnement ?"):
    st.markdown(f"""
- **Conteneurs 3 MWh** : Nombre d'unités de stockage nécessaires pour tamponner la production journalière (**{mobile.containers_needed} conteneurs** pour **{mobile.gross_kwh_day/1000:.1f} MWh/jour**).
- **Massification HTA vs Capillarité BT** : Les parcs au sol HTA (> 1 MW) hébergent directement les conteneurs mobiles (aucun trajet léger). Les toitures et hangars BT (< 250 kW) sont collectés par tracteurs légers en rotation de **{light_payload:.0f} kWh**.
- **Tracteurs légers et lourds** : Nombre de véhicules équivalents calculé sur la base de vacations de conduite de 7h/jour.
- **CO₂ évité** : Émissions évitées par rapport à un mix thermique insulaire ou du carburant diesel de transport routier (~0,70 kg CO₂ / kWh décarboné).
""")

with st.expander("Pourquoi EDF-SEI devrait rémunérer cette flexibilité ?"):
    st.markdown(f"""
En Corse (Zone Non Interconnectée au réseau continental), le système électrique présente une double asymétrie quotidienne :

1. **L'écrêtement solaire méridien (Énergie fatale)** :
   Aux heures de pointe d'ensoleillement (11h–15h), l'injection solaire combinée aux autres EnR excède le plafond technique de pénétration instantanée (fixé à **35 %** par le code de l'énergie pour garantir la stabilité de fréquence). Faute de capacité de stockage suffisante, EDF-SEI est contraint de brider ou déconnecter les parcs solaires. Sans conteneurs mobiles, cette énergie propre est **définitivement perdue**.

2. **La pointe du soir aux hydrocarbures importés (Centrales de Lucciana et du Vazzio)** :
   Entre 18h et 22h, la demande explose alors que la production solaire est nulle. EDF-SEI compense en démarrant les moteurs thermiques de Lucciana (Bastia) et du Vazzio (Ajaccio), brûlant des hydrocarbures importés avec un coût marginal de combustible de **{thermal_fuel_eur:.2f} €/kWh**. Ce surcoût colossal est historiquement compensé par la solidarité nationale via les Charges de Service Public de l'Énergie (CSPE).

3. **L'économie directe créée pour EDF-SEI** :
   En absorbant l'énergie fatale de midi dans ses conteneurs de 3 MWh pour la restituer le soir aux bornes urbaines, FractaVolta évite à EDF-SEI de brûler **{mobile.fuel_liters_saved_year:,.0f} litres de fioul par an**, générant une économie brute de carburant de **{mobile.thermal_fuel_saved_eur_day * 365 / 1000:,.0f} k€ par an**.

4. **L'alignement économique de la prime de flexibilité** :
   Une rémunération de réserve/flexibilité de **{flexibility_fee:.3f} €/kWh** versée par l'opérateur de réseau ne représente qu'une fraction de l'économie réalisée par EDF-SEI (**{thermal_fuel_eur:.2f} €/kWh** de combustible évité). Cette prime génère **+{mobile.flexibility_revenue_day * 365 / 1000:,.1f} k€/an** de chiffre d'affaires additionnel pour FractaVolta, rendant le réseau mobile pérenne tout en allégeant les charges de service public.
""")

with st.expander("Prix final et marge par kWh"):
    st.markdown(f"""
Le curseur **Prix client final TTC** représente le prix affiché au client final à la borne, l'équivalent du prix « à la pompe » pour l'électricité.

Le modèle retire la TVA avant de calculer la recette opérateur. Avec le périmètre actif :

- prix client TTC : **{retail_price_ttc:.2f} €/kWh** ;
- coût modélisé : **{mobile.total_cost_eur_kwh:.3f} €/kWh livré** ;
- marge contributive : **{mobile.margin_eur_kwh:.3f} €/kWh livré** ;
- prix d'équilibre TTC : **{break_even_ttc:.3f} €/kWh**.
""")

with st.expander("Capacités de tractage"):
    st.markdown(f"""
Le modèle distingue deux classes génériques : **tracteur léger** et **tracteur lourd**.

- Tracteur léger : capacité déclarée **{light_towing_kg:,.0f} kg**
- Tracteur lourd : capacité déclarée **{heavy_towing_kg:,.0f} kg**

Ces valeurs expriment une contrainte physique de véhicule.
""")

with st.expander("Pourquoi tester la conduite autonome ?"):
    st.markdown("""
La collecte capillaire multiplie les petites rotations et donc les heures de conduite. Si, à l'avenir, les utilitaires et les poids lourds peuvent circuler de façon autonome, ce poste de coût peut fortement diminuer.
""")

tab_map, tab_reg, tab_fin, tab_sens, tab_data = st.tabs([
    "Carte de Corse",
    "Registre Seconde Vie EDF",
    "Économie",
    "Sensibilité",
    "Données",
])

with tab_map:
    st.subheader("Réseau insulaire et corridors de transport")
    st.caption("Fond de carte OpenStreetMap : hubs de distribution urbains (Bastia, Corte, Ajaccio, Porto-Vecchio), corridors routiers T20, T10, T50, buffers mobiles et sources solaires.")

    col_m1, col_m2 = st.columns([2, 1])
    with col_m1:
        solar_view = st.radio(
            "Sources solaires affichées :",
            [f"Producteurs du périmètre simulé ({len(active_producers)} sites)", "Grandes centrales solaires HTA (34 parcs)", "Tous les sites de production (742 sites)"],
            horizontal=True,
        )
    with col_m2:
        show_flows = st.checkbox("Afficher les flux logistiques (légers & lourds)", value=True)

    fig_map = go.Figure()

    # Corridors routiers majeurs
    corridor_colors = {
        "T20 (Ajaccio–Corte–Bastia)": "#2563EB",
        "T10 (Bastia–Aléria–Porto-Vecchio)": "#0D9488",
        "T50 (Corte–Aléria)": "#EA580C",
    }
    for c_name, coords in CORRIDORS.items():
        lons = [pt[0] for pt in coords]
        lats = [pt[1] for pt in coords]
        fig_map.add_trace(go.Scattermap(
            lon=lons,
            lat=lats,
            mode="lines",
            line=dict(width=4, color=corridor_colors.get(c_name, "#475569")),
            name=c_name,
            hoverinfo="name",
        ))

    # Flux logistiques (si activés)
    if show_flows:
        # Collecte capillaire légère pour sites BT
        for p in active_producers:
            if getattr(p, "tension", "BT") != "HTA":
                b = MOBILE_BUFFERS[p.cluster]
                fig_map.add_trace(go.Scattermap(
                    lon=[p.x, b.x],
                    lat=[p.y, b.y],
                    mode="lines",
                    line=dict(width=1.2, color="#94A3B8"),
                    showlegend=False,
                    hoverinfo="skip",
                ))

        # Navettes lourdes conteneurs (Buffer mobile -> Station urbaine)
        station_by_cluster = {s.cluster: s for s in STATIONS}
        for cl, b in MOBILE_BUFFERS.items():
            s = station_by_cluster[cl]
            fig_map.add_trace(go.Scattermap(
                lon=[b.x, s.x],
                lat=[b.y, s.y],
                mode="lines",
                line=dict(width=3, color="#7C3AED"),
                showlegend=False,
                hoverinfo="skip",
            ))

    # Sources solaires
    if solar_view.startswith("Producteurs du périmètre simulé"):
        fig_map.add_trace(go.Scattermap(
            lon=[p.x for p in active_producers],
            lat=[p.y for p in active_producers],
            mode="markers",
            name=f"Simulés ({len(active_producers)} sites)",
            marker=dict(
                size=[14 if getattr(p, "tension", "BT") == "HTA" else 8 for p in active_producers],
                color=["#DC2626" if getattr(p, "tension", "BT") == "HTA" else "#F59E0B" for p in active_producers],
                opacity=0.85,
            ),
            customdata=[[p.id, p.cluster, p.production_kwh_day, getattr(p, "tension", "BT")] for p in active_producers],
            hovertemplate="<b>%{customdata[0]}</b> (%{customdata[3]})<br>Bassin : %{customdata[1]}<br>Production : %{customdata[2]:,.0f} kWh/j<extra></extra>",
        ))
    elif solar_view == "Grandes centrales solaires HTA (34 parcs)":
        hta_sites = [r for r in solar_register if r.get("tension") == "HTA"]
        fig_map.add_trace(go.Scattermap(
            lon=[r["longitude"] for r in hta_sites],
            lat=[r["latitude"] for r in hta_sites],
            mode="markers",
            name="Centrales HTA (grand sol)",
            marker=dict(
                size=[max(8, min(24, int(r["puissance_kw"] / 500) + 8)) for r in hta_sites],
                color="#D97706",
                opacity=0.85,
            ),
            customdata=[[r["commune"], r["nom"], r["puissance_kw"], r["annee_fin_oa"], r["horizon_seconde_vie"]] for r in hta_sites],
            hovertemplate="<b>%{customdata[0]}</b><br>%{customdata[1]}<br>Puissance : %{customdata[2]:,.0f} kWc<br>Échéance OA : %{customdata[3]}<br>Statut : %{customdata[4]}<extra></extra>",
        ))
    else:
        # All 742 sites
        fig_map.add_trace(go.Scattermap(
            lon=[r["longitude"] for r in solar_register],
            lat=[r["latitude"] for r in solar_register],
            mode="markers",
            name="Tous sites solaires (ODRÉ)",
            marker=dict(
                size=[6 if r["tension"] == "BT" else 14 for r in solar_register],
                color=["#F59E0B" if r["tension"] == "BT" else "#DC2626" for r in solar_register],
                opacity=0.65,
            ),
            customdata=[[r["commune"], r["nom"], r["puissance_kw"], r["tension"], r["annee_fin_oa"]] for r in solar_register],
            hovertemplate="<b>%{customdata[0]}</b> (%{customdata[3]})<br>%{customdata[1]}<br>%{customdata[2]:,.0f} kWc<br>Fin OA : %{customdata[4]}<extra></extra>",
        ))

    # Buffers mobiles (conteneurs régionaux)
    fig_map.add_trace(go.Scattermap(
        lon=[b.x for b in MOBILE_BUFFERS.values()],
        lat=[b.y for b in MOBILE_BUFFERS.values()],
        mode="markers+text",
        text=[b.id for b in MOBILE_BUFFERS.values()],
        textposition="bottom center",
        name="Buffers mobiles (3 MWh)",
        marker=dict(size=18, color="#7C3AED", symbol="square"),
        customdata=[[b.cluster, b.capacity_kwh] for b in MOBILE_BUFFERS.values()],
        hovertemplate="<b>%{text}</b><br>Bassin : %{customdata[0]}<br>Capacité : %{customdata[1]:,.0f} kWh<extra></extra>",
    ))

    # Hub fixe (Corte)
    fig_map.add_trace(go.Scattermap(
        lon=[FIXED_HUB.x],
        lat=[FIXED_HUB.y],
        mode="markers+text",
        text=[FIXED_HUB.id],
        textposition="top left",
        name="Hub central fixe (Corte)",
        marker=dict(size=14, color="#64748B", symbol="circle"),
        hoverinfo="text",
    ))

    # Stations de distribution urbaines / Hubs de recharge
    fig_map.add_trace(go.Scattermap(
        lon=[s.x for s in STATIONS],
        lat=[s.y for s in STATIONS],
        mode="markers+text",
        text=[f"{s.id} ({s.cluster})" for s in STATIONS],
        textposition="top center",
        name="Hubs urbains & Bornes rapides",
        marker=dict(size=20, color="#059669", symbol="diamond"),
        customdata=[[s.public_price_ttc_eur_kwh, s.demand_kwh_day] for s in STATIONS],
        hovertemplate="<b>%{text}</b><br>Prix borne : %{customdata[0]:.2f} €/kWh TTC<br>Demande : %{customdata[1]:,.0f} kWh/j<extra></extra>",
    ))

    fig_map.update_layout(
        map=dict(
            style="open-street-map",
            center=dict(lat=42.15, lon=9.15),
            zoom=7.8,
        ),
        margin=dict(l=0, r=0, t=10, b=0),
        height=680,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
        ),
    )
    st.plotly_chart(fig_map, use_container_width=True)

with tab_reg:
    st.subheader("Registre officiel des producteurs d'électricité vendant à EDF en Corse")
    st.markdown("""
Données consolidées issues du **Registre national des installations de production d'électricité (ODRÉ / EDF-SEI)** au 31 décembre 2023.

En Corse (zone non interconnectée au réseau continental), les producteurs photovoltaïques disposent historiquement de contrats d'**Obligation d'Achat (OA)** d'une durée de 20 ans avec EDF.
À l'échéance de ce contrat, les installations entrent en **Seconde Vie** : elles perdent leur tarif d'achat garanti et s'exposent à des contraintes d'écrêtement sévères imposées par EDF-SEI pour préserver la stabilité du réseau insulaire.
""")

    if solar_register:
        df_reg = pd.DataFrame(solar_register)

        # Calcul des métriques globales
        total_sites = len(df_reg)
        total_p_mwc = df_reg["puissance_kw"].sum() / 1000.0

        p_imminent_mwc = df_reg[df_reg["horizon_seconde_vie"] == "Imminent (<= 2030)"]["puissance_kw"].sum() / 1000.0
        n_imminent = len(df_reg[df_reg["horizon_seconde_vie"] == "Imminent (<= 2030)"])

        p_court_mwc = df_reg[df_reg["horizon_seconde_vie"] == "Court terme (2031-2035)"]["puissance_kw"].sum() / 1000.0
        n_court = len(df_reg[df_reg["horizon_seconde_vie"] == "Court terme (2031-2035)"])

        p_2035_total = p_imminent_mwc + p_court_mwc
        pct_2035 = (p_2035_total / total_p_mwc * 100.0) if total_p_mwc else 0.0

        # KPI Cards
        rk1, rk2, rk3, rk4 = st.columns(4)
        rk1.metric("Puissance totale installée", f"{total_p_mwc:.1f} MWc", f"{total_sites} installations")
        rk2.metric("Fin OA ≤ 2030 (Imminent)", f"{p_imminent_mwc:.1f} MWc", f"{n_imminent} sites prioritaires")
        rk3.metric("Fin OA 2031–2035 (Court terme)", f"{p_court_mwc:.1f} MWc", f"{n_court} sites identifiés")
        rk4.metric("Potentiel Seconde Vie ≤ 2035", f"{p_2035_total:.1f} MWc", f"{pct_2035:.1f} % du parc corse")

        st.divider()

        # Filtres interactifs
        st.markdown("##### Filtres du registre")
        rf1, rf2, rf3, rf4 = st.columns(4)
        with rf1:
            clusters_list = ["Tous"] + sorted(list(df_reg["cluster"].unique()))
            sel_cluster = st.selectbox("Bassin / Hub", clusters_list)
        with rf2:
            tensions_list = ["Toutes", "HTA (Grandes centrales)", "BT (Toitures / Hangars)"]
            sel_tension = st.selectbox("Niveau de tension", tensions_list)
        with rf3:
            horizons_list = ["Tous", "Imminent (<= 2030)", "Court terme (2031-2035)", "Moyen/Long terme (> 2035)"]
            sel_horizon = st.selectbox("Horizon Seconde Vie", horizons_list)
        with rf4:
            search_query = st.text_input("Recherche (commune ou installation)", "")

        filtered_df = df_reg.copy()
        if sel_cluster != "Tous":
            filtered_df = filtered_df[filtered_df["cluster"] == sel_cluster]
        if sel_tension == "HTA (Grandes centrales)":
            filtered_df = filtered_df[filtered_df["tension"] == "HTA"]
        elif sel_tension == "BT (Toitures / Hangars)":
            filtered_df = filtered_df[filtered_df["tension"] == "BT"]
        if sel_horizon != "Tous":
            filtered_df = filtered_df[filtered_df["horizon_seconde_vie"] == sel_horizon]
        if search_query:
            q = search_query.strip().lower()
            filtered_df = filtered_df[
                filtered_df["commune"].str.lower().str.contains(q, na=False) |
                filtered_df["nom"].str.lower().str.contains(q, na=False)
            ]

        # Action d'injection directe dans la simulation
        col_act1, col_act2 = st.columns([3, 1])
        with col_act1:
            st.info(f"💡 Ce filtre isole **{len(filtered_df)}** installations ({filtered_df['puissance_kw'].sum()/1000:.2f} MWc, production estimée : {filtered_df['production_estimee_kwh_jour'].sum()/1000:.1f} MWh/jour).")
        with col_act2:
            if st.button("🚀 Simuler cette sélection", type="primary", use_container_width=True):
                custom_lbl = f"Sélection personnalisée ({len(filtered_df)} sites)"
                st.session_state["simulation_scope"] = custom_lbl
                st.session_state["custom_producers"] = filtered_df.to_dict(orient="records")
                st.rerun()

        # Table d'affichage
        display_cols = [
            "commune",
            "nom",
            "tension",
            "puissance_kw",
            "puissance_mw",
            "date_mise_en_service",
            "annee_fin_oa",
            "horizon_seconde_vie",
            "cluster",
            "production_estimee_kwh_an",
        ]
        rename_map = {
            "commune": "Commune",
            "nom": "Installation",
            "tension": "Tension",
            "puissance_kw": "Puissance (kWc)",
            "puissance_mw": "Puissance (MWc)",
            "date_mise_en_service": "Mise en service",
            "annee_fin_oa": "Fin de contrat OA",
            "horizon_seconde_vie": "Horizon Seconde Vie",
            "cluster": "Bassin",
            "production_estimee_kwh_an": "Prod. estimée (kWh/an)",
        }
        sub_df = filtered_df[display_cols].rename(columns=rename_map)

        st.caption(f"Affichage de **{len(sub_df)}** installations sur {total_sites} (puissance cumulée : {sub_df['Puissance (kWc)'].sum()/1000:.2f} MWc)")
        st.dataframe(sub_df, use_container_width=True, hide_index=True)

        # Export CSV
        csv_bytes = sub_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Télécharger le registre filtré (CSV)",
            csv_bytes,
            "registre_producteurs_edf_corse.csv",
            "text/csv",
        )
    else:
        st.warning("Le fichier de données du registre n'est pas disponible.")

with tab_fin:
    st.subheader("Bilan économique & Valorisation de la flexibilité insulaire")
    
    df_fin = pd.DataFrame([
        {
            "Scénario": fixed.name,
            "Coût (€/kWh)": fixed.total_cost_eur_kwh,
            "Marge brute (€/kWh)": fixed.margin_eur_kwh,
            "Prime flex. (€/kWh)": a.flexibility_remuneration_eur_kwh,
            "Marge bonifiée (€/kWh)": fixed.margin_with_flexibility_eur_kwh,
            "Marge brute (€/j)": fixed.margin_day,
            "Marge bonifiée (€/j)": fixed.margin_with_flexibility_day,
            "Économie fioul EDF (€/j)": fixed.thermal_fuel_saved_eur_day,
            "Conteneurs 3 MWh": fixed.containers_needed,
            "Tracteurs lourds": fixed.heavy_tractors_needed,
            "Tracteurs légers": fixed.light_tractors_needed,
        },
        {
            "Scénario": mobile.name,
            "Coût (€/kWh)": mobile.total_cost_eur_kwh,
            "Marge brute (€/kWh)": mobile.margin_eur_kwh,
            "Prime flex. (€/kWh)": a.flexibility_remuneration_eur_kwh,
            "Marge bonifiée (€/kWh)": mobile.margin_with_flexibility_eur_kwh,
            "Marge brute (€/j)": mobile.margin_day,
            "Marge bonifiée (€/j)": mobile.margin_with_flexibility_day,
            "Économie fioul EDF (€/j)": mobile.thermal_fuel_saved_eur_day,
            "Conteneurs 3 MWh": mobile.containers_needed,
            "Tracteurs lourds": mobile.heavy_tractors_needed,
            "Tracteurs légers": mobile.light_tractors_needed,
        },
    ])
    st.dataframe(df_fin, use_container_width=True, hide_index=True)

    col_b1, col_b2 = st.columns([3, 2])
    with col_b1:
        bar = go.Figure()
        bar.add_bar(name="Hub central fixe (Corte)", x=["Coût de revient", "Marge d'arbitrage", "Marge + Prime Flexibilité"], y=[fixed.total_cost_eur_kwh, fixed.margin_eur_kwh, fixed.margin_with_flexibility_eur_kwh], marker_color="#64748B")
        bar.add_bar(name="Buffers mobiles (Corridors)", x=["Coût de revient", "Marge d'arbitrage", "Marge + Prime Flexibilité"], y=[mobile.total_cost_eur_kwh, mobile.margin_eur_kwh, mobile.margin_with_flexibility_eur_kwh], marker_color="#059669")
        bar.update_layout(barmode="group", yaxis_title="€/kWh livré", height=400, legend=dict(orientation="h", yanchor="bottom", y=1.02))
        st.plotly_chart(bar, use_container_width=True)

    with col_b2:
        costs = pd.DataFrame({
            "Poste": ["Achat producteurs", "Collecte légère", "Transport lourd", "Cycle batterie + borne"],
            "€/jour": [mobile.purchase_cost_day, mobile.light_cost_day, mobile.heavy_cost_day, mobile.storage_charger_cost_day],
        })
        pie = go.Figure(data=[go.Pie(labels=costs["Poste"], values=costs["€/jour"], hole=0.45)])
        pie.update_layout(height=400, margin=dict(l=10, r=10, t=20, b=10))
        st.plotly_chart(pie, use_container_width=True)

    st.subheader("Profil horaire journalier : absorption de l'écrêtement méridien & restitution en pointe du soir")
    st.caption("Modélisation de la courbe journalière type en Corse : absorption de l'excédent solaire (11h–15h) et restitution aux bornes urbaines (18h–23h), évitant le démarrage des moteurs fioul de Lucciana et du Vazzio.")

    hours = list(range(24))
    # Normalized solar production profile (bell curve between 6h and 19h, peak at 13h)
    solar_weights = [max(0.0, math.sin(math.pi * (h - 6) / 13.0))**1.8 if 6 <= h <= 19 else 0.0 for h in hours]
    sum_weights = sum(solar_weights) or 1.0
    solar_hourly_kwh = [(w / sum_weights) * mobile.gross_kwh_day for w in solar_weights]

    # Curtailed energy absorbed by mobile buffers (peaks between 10h and 15h)
    curtailed_hourly_kwh = [p * a.curtailment_rate if 10 <= h <= 15 else 0.0 for h, p in zip(hours, solar_hourly_kwh)]

    # Grid direct injection
    grid_injection_kwh = [p - c for p, c in zip(solar_hourly_kwh, curtailed_hourly_kwh)]

    # Discharged energy at urban charging stations during evening mobility peak (17h to 23h)
    ev_evening_weights = [0.0]*17 + [0.12, 0.22, 0.26, 0.22, 0.12, 0.06] + [0.0]
    ev_hourly_kwh = [w * mobile.delivered_kwh_day for w in ev_evening_weights]

    fig_flex = go.Figure()
    fig_flex.add_trace(go.Scatter(
        x=[f"{h:02d}h" for h in hours],
        y=[k / 1000.0 for k in grid_injection_kwh],
        name="Injection réseau autorisée (EnR)",
        mode="lines",
        line=dict(color="#10B981", width=2.5),
        stackgroup="solar",
    ))
    fig_flex.add_trace(go.Scatter(
        x=[f"{h:02d}h" for h in hours],
        y=[k / 1000.0 for k in curtailed_hourly_kwh],
        name="Énergie fatale absorbée dans les buffers mobiles",
        mode="lines",
        line=dict(color="#F59E0B", width=2.5),
        fillcolor="rgba(245, 158, 11, 0.45)",
        stackgroup="solar",
    ))
    fig_flex.add_trace(go.Scatter(
        x=[f"{h:02d}h" for h in hours],
        y=[k / 1000.0 for k in ev_hourly_kwh],
        name="Restitution aux bornes le soir (Fioul EDF évité)",
        mode="lines+markers",
        line=dict(color="#7C3AED", width=3, dash="dash"),
    ))
    fig_flex.update_layout(
        xaxis_title="Heure de la journée (00h - 23h)",
        yaxis_title="Énergie horaire (MWh)",
        height=450,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        margin=dict(l=20, r=20, t=30, b=20),
    )
    st.plotly_chart(fig_flex, use_container_width=True)


with tab_sens:
    points = []
    # Sample producers for fast interactive response if fleet is very large
    sample_producers = active_producers[:30] if len(active_producers) > 30 else active_producers
    for price in [0.05 + i * 0.005 for i in range(31)]:
        ps = [
            Producer(p.id, p.cluster, p.x, p.y, p.production_kwh_day, p.alternative_eur_kwh, max(price, p.alternative_eur_kwh + 0.001), getattr(p, "tension", "BT"))
            for p in sample_producers
        ]
        rf = simulate(ps, STATIONS, FIXED_HUB, MOBILE_BUFFERS, a, "fixed")
        rm = simulate(ps, STATIONS, FIXED_HUB, MOBILE_BUFFERS, a, "mobile")
        points.append({"Prix producteur": price, "Hub fixe": rf.margin_eur_kwh, "Buffers mobiles": rm.margin_eur_kwh})
    sens = pd.DataFrame(points)
    f = go.Figure()
    f.add_scatter(x=sens["Prix producteur"], y=sens["Hub fixe"], mode="lines", name="Hub fixe")
    f.add_scatter(x=sens["Prix producteur"], y=sens["Buffers mobiles"], mode="lines", name="Buffers mobiles")
    f.add_hline(y=0, line_dash="dash")
    f.update_layout(xaxis_title="Prix producteur (€/kWh)", yaxis_title="Marge contributive (€/kWh)", height=500)
    st.plotly_chart(f, use_container_width=True)

    st.subheader("Gain usager selon le kilométrage")
    km_points = []
    for km in range(250, 3001, 250):
        r = user_fuel_savings(km, thermal_consumption, fuel_price, ev_consumption, retail_price_ttc)
        km_points.append({"Kilométrage mensuel": km, "Gain mensuel": r["saving_month"]})
    kdf = pd.DataFrame(km_points)
    kf = go.Figure()
    kf.add_scatter(x=kdf["Kilométrage mensuel"], y=kdf["Gain mensuel"], mode="lines+markers", name="Gain usager")
    kf.add_hline(y=0, line_dash="dash")
    kf.update_layout(xaxis_title="Kilométrage mensuel (km)", yaxis_title="Économie carburant (€/mois)", height=500)
    st.plotly_chart(kf, use_container_width=True)

    st.subheader("Sensibilité au prix client final")
    retail_points = []
    for price in [0.30 + i * 0.025 for i in range(29)]:
        aa = Assumptions(**{**a.__dict__, "retail_price_ttc_eur_kwh": price})
        rf = simulate(sample_producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, aa, "fixed")
        rm = simulate(sample_producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, aa, "mobile")
        retail_points.append({"Prix client TTC": price, "Hub fixe": rf.margin_eur_kwh, "Buffers mobiles": rm.margin_eur_kwh})
    rdf = pd.DataFrame(retail_points)
    pf = go.Figure()
    pf.add_scatter(x=rdf["Prix client TTC"], y=rdf["Hub fixe"], mode="lines", name="Hub fixe")
    pf.add_scatter(x=rdf["Prix client TTC"], y=rdf["Buffers mobiles"], mode="lines", name="Buffers mobiles")
    pf.add_hline(y=0, line_dash="dash")
    pf.update_layout(xaxis_title="Prix client final TTC (€/kWh)", yaxis_title="Marge contributive (€/kWh livré)", height=500)
    st.plotly_chart(pf, use_container_width=True)

    st.subheader("Sensibilité à la conduite autonome")
    autonomy_points = []
    for pct in range(0, 101, 10):
        aa = Assumptions(**{**a.__dict__, "vehicle_autonomy": pct / 100.0})
        rf = simulate(sample_producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, aa, "fixed")
        rm = simulate(sample_producers, STATIONS, FIXED_HUB, MOBILE_BUFFERS, aa, "mobile")
        autonomy_points.append({"Autonomie (%)": pct, "Hub fixe": rf.total_cost_eur_kwh, "Buffers mobiles": rm.total_cost_eur_kwh})
    adf = pd.DataFrame(autonomy_points)
    af = go.Figure()
    af.add_scatter(x=adf["Autonomie (%)"], y=adf["Hub fixe"], mode="lines+markers", name="Hub fixe")
    af.add_scatter(x=adf["Autonomie (%)"], y=adf["Buffers mobiles"], mode="lines+markers", name="Buffers mobiles")
    af.update_layout(xaxis_title="Autonomie de conduite (%)", yaxis_title="Coût total (€/kWh)", height=500)
    st.plotly_chart(af, use_container_width=True)

with tab_data:
    st.subheader(f"Producteurs modélisés dans le scénario actif ({len(active_producers)} sites)")
    st.dataframe(pd.DataFrame([p.__dict__ for p in active_producers]), use_container_width=True, hide_index=True)
    
    st.subheader("Bilan comparatif et dimensionnement de flotte")
    export = pd.DataFrame([fixed.to_dict(), mobile.to_dict()])
    st.dataframe(export, use_container_width=True, hide_index=True)
    st.download_button("Télécharger résultats CSV", export.to_csv(index=False).encode("utf-8"), "fractavolta_simulation.csv", "text/csv")

st.divider()
st.caption("Modélisation exploratoire Corsica — données solaires ODRÉ / EDF-SEI 2023 ; aucune promesse commerciale ou validation réglementaire.")
