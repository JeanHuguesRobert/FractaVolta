#!/usr/bin/env python3
"""
Generate the enriched Corsican Solar Producers Register selling to EDF (EDF-SEI / Obligation d'Achat).
Reads raw dataset from ODRÉ national open data registry and enriches with IGN/INSEE geo coordinates,
department, Seconde Vie contract expiration horizons (mise en service + 20 years), and geographic clusters.
"""

import json
import math
import os
import ssl
import sys
import urllib.request

HUBS = {
    "Ajaccio": (41.9192, 8.7386),
    "Bastia": (42.6973, 9.4509),
    "Corte": (42.3094, 9.1490),
    "Plaine Orientale": (42.1100, 9.5100),
}

def dist_approx(p1, p2):
    return math.hypot(p1[0] - p2[0], (p1[1] - p2[1]) * math.cos(math.radians(42.0)))

def fetch_communes_geo():
    ctx = ssl._create_unverified_context()
    communes_geo = {}
    for dep in ["2A", "2B"]:
        url = f"https://geo.api.gouv.fr/departements/{dep}/communes?fields=nom,code,centre"
        req = urllib.request.Request(url, headers={"User-Agent": "FractaVolta/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            for c in json.loads(resp.read().decode("utf-8")):
                code = c["code"]
                coords = c.get("centre", {}).get("coordinates", [None, None])
                communes_geo[code] = {
                    "nom": c["nom"],
                    "lon": coords[0],
                    "lat": coords[1],
                }
    return communes_geo

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "data_raw.json")
    out_dir = os.path.join(base_dir, "data")
    out_path = os.path.join(out_dir, "registre_producteurs_edf_corse.json")

    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found.", file=sys.stderr)
        sys.exit(1)

    os.makedirs(out_dir, exist_ok=True)
    print("Loading commune coordinates from geo.api.gouv.fr...")
    communes_geo = fetch_communes_geo()
    print(f"Loaded {len(communes_geo)} communes.")

    with open(raw_path, "r", encoding="utf-8") as f:
        data_raw = json.load(f)

    enriched = []
    for idx, d in enumerate(data_raw, 1):
        insee = d.get("codeinseecommune")
        commune_nom = d.get("commune") or ""
        geo = communes_geo.get(insee)
        lat = geo["lat"] if geo else None
        lon = geo["lon"] if geo else None

        if not lat or not lon:
            epci = str(d.get("epci") or "")
            if "Calvi" in epci:
                lat, lon, commune_nom = 42.5667, 8.7572, "Calvi (EPCI)"
            elif "Cap Corse" in epci:
                lat, lon, commune_nom = 42.8500, 9.4000, "Cap Corse (EPCI)"
            elif "Alta Rocca" in epci:
                lat, lon, commune_nom = 41.7400, 9.1200, "Levie (EPCI Alta Rocca)"
            elif "Taravo" in epci or "Ornano" in epci:
                lat, lon, commune_nom = 41.8700, 8.9500, "Grosseto-Prugna (EPCI)"
            elif "Liamone" in epci or "Spelunca" in epci:
                lat, lon, commune_nom = 42.1600, 8.7500, "Vico (EPCI)"
            elif "Celavu" in epci or "Prunelli" in epci:
                lat, lon, commune_nom = 42.0200, 8.9200, "Bastelicaccia (EPCI)"
            elif "Pasquale Paoli" in epci:
                lat, lon, commune_nom = 42.4500, 9.2000, "Morosaglia (EPCI)"
            else:
                lat, lon, commune_nom = 42.3094, 9.1490, "Corse (Agregation regionale)"

        best_cluster = min(HUBS.keys(), key=lambda h: dist_approx((lat, lon), HUBS[h]))

        p_kw = float(d.get("puismaxinstallee") or 0.0)
        p_mw = round(p_kw / 1000.0, 3)

        tension = d.get("tensionraccordement") or "BT"
        nom = d.get("nominstallation") or "Confidentiel"
        if nom == "Confidentiel":
            if tension == "HTA":
                nom = f"Centrale solaire HTA - {commune_nom}"
            else:
                nom = f"Site solaire BT - {commune_nom}"
        elif "Agr" in nom:
            nom = f"Agregation toitures < 36 kW - {commune_nom}"

        date_mes = d.get("datemiseenservice_date") or d.get("datemiseenservice") or ""
        annee_mes = None
        if date_mes and len(date_mes) >= 4 and date_mes[:4].isdigit():
            annee_mes = int(date_mes[:4])
        annee_fin_oa = (annee_mes + 20) if annee_mes else None

        if annee_fin_oa:
            if annee_fin_oa <= 2030:
                horizon = "Imminent (<= 2030)"
            elif annee_fin_oa <= 2035:
                horizon = "Court terme (2031-2035)"
            else:
                horizon = "Moyen/Long terme (> 2035)"
        else:
            horizon = "Non renseigne"

        annual_kwh = round(p_kw * 1350.0)
        daily_kwh = round(annual_kwh / 365.0)

        rec_id = d.get("codeeicresourceobject") or f"FV-ODRE-{idx:04d}"

        enriched.append({
            "id": rec_id,
            "nom": nom,
            "commune": commune_nom,
            "code_insee": insee or "94000",
            "departement": d.get("departement") or ("2A" if (insee and insee.startswith("2A")) else "2B"),
            "tension": tension,
            "puissance_kw": round(p_kw, 2),
            "puissance_mw": p_mw,
            "production_estimee_kwh_jour": daily_kwh,
            "production_estimee_kwh_an": annual_kwh,
            "date_mise_en_service": date_mes,
            "annee_mise_en_service": annee_mes,
            "annee_fin_oa": annee_fin_oa,
            "horizon_seconde_vie": horizon,
            "cluster": best_cluster,
            "latitude": round(lat, 5),
            "longitude": round(lon, 5),
            "gestionnaire": "EDF-SEI",
            "regime": "En service",
        })

    enriched.sort(key=lambda r: (r["annee_fin_oa"] or 9999, -r["puissance_kw"]))
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)

    print(f"Generated {out_path} with {len(enriched)} records.")

if __name__ == "__main__":
    main()
