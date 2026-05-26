---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/mariani_village.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-05-26
---
# Mariani Village: A Relocatable DC-Native Housing Fleet
## From Single Container to Regional Cooperative Mesh

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A. / FractaVolta

1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org | fractavolta.com

---

## Abstract

Mariani Village is a relocatable housing system based on the ISO 20-foot container as its irreducible physical unit. Conceived over many years within Institut Mariani and commercialised through its spin-off Dilorta SAS, it targets short- to medium-term occupancy by students, seasonal workers, and tourists. Its core architectural thesis is threefold: the container is the packet, the fleet is the network, and the site is the context. A Mariani Village unit carries its own energy infrastructure when the host site provides none, and gracefully integrates available grid connections — electricity, water, sewage, internet — when the site provides some or all of them. Two configurations are described: a single autonomous container unit, and a multi-unit cooperative fleet deployment. Both configurations instantiate the Energy Packet Network concept at human scale.

**Keywords:** relocatable housing; ISO container; DC microgrid; SELV; EPN; FractaVolta; Dilorta; Mariani Village; 48V; fleet management; cooperative; student housing; seasonal tourism

---

## 1. Institutional Context

### 1.1 The lineage

Mariani Village originates within **C.O.R.S.I.C.A.** (Collectif pour l'Organisation de Ressources et de Services en Intelligence Coopérative et Autonome, association loi 1901, founded Corte 1995) and its applied research arm, **Institut Mariani**. The Institut conducts R&D across energy, compute, cooperative governance, and territorial sovereignty — without commercial clients or invoicing.

**Dilorta SAS** is the commercial spin-off of Institut Mariani, currently in formation. Its name derives from *di l'Orta* — "of the Orta", the river running below the Mariani family property at Minesteggio, Corsica. Dilorta will do what the Institut cannot: sign contracts, issue invoices, license intellectual property, and engage clients. It will hold the Mariani Village operational model, the container specifications, and the deployment methodology.

**Mariani Village** is the first regional instance of the Dilorta model, deployed in Corsica. Its capital structure brings together a regional sovereign fund (majority) and C.O.R.S.I.C.A. (minority), consistent with the Plan 2038 framework of sovereign cooperative asset accumulation. Future instances — in other Mediterranean regions or French territories — would replicate the same capital structure with local sovereign partners.

```
C.O.R.S.I.C.A. (loi 1901, non-commercial)
        │
        └── Institut Mariani (R&D, non-commercial)
                    │
                    └── DILORTA SAS (commercial spin-off)
                         "Di l'Orta" — Minesteggio, Corsica
                         Holds: IP, specs, methodology, licences
                                │
                    ┌───────────┴─────────────────┐
                    │                             │
             MARIANI VILLAGE               Future instances
             (Corsica instance)             (other regions)
             Regional Sovereign Fund        same model
             + C.O.R.S.I.C.A.              local sovereign partner
```

### 1.2 The target market

Mariani Village serves two primary occupancy profiles:

- **Students** — academic year occupancy, fixed address, cooperative membership, voter registration in host commune. Reference deployment: Corte, near the Università di Corsica Pasquale Paoli.
- **Visitors** — seasonal occupancy, tourist or seasonal worker, flexible duration. Reference deployment: Corsican coastal sites, summer season.

Each container performs at most one return journey per year. A container occupied by a student in Corte from October to June may move to a coastal site for the summer season, then return in September. The container does not change. The occupant profile, the site infrastructure, and the tariff do.

This deliberate annual repositioning — not a frequent rotation — is the operational expression of the Energy Packet Network principle at its slowest tempo: **the container is a packet, the annual move is the routing event, demand is the routing metric.** The low frequency of moves is a constraint that imposes discipline on site selection: each deployment is a considered commitment, not an opportunistic placement.

---

## 2. The Container as Housing Packet

### 2.1 Physical constraints

The ISO 20-foot container imposes hard constraints that are also design virtues:

- **External dimensions**: 6.058 m × 2.438 m × 2.591 m
- **Internal usable area**: approximately 13.8 m² (after insulation and fit-out)
- **Transport compatibility**: standard flatbed truck, crane lift, forklift, ship — no special permit required below 40 tonnes
- **Structural integrity**: stackable, weatherproof, lockable, certified for international transport

Every design decision is subordinated to these constraints. The electrical system, plumbing, furniture, and HVAC must fit inside, survive transport, and reconnect reliably at the next site.

### 2.2 Site-adaptive electrical architecture

The core design challenge is graceful adaptation to variable site infrastructure. A Mariani Village container must operate correctly across four site classes:

| Site class | Available connections | Container response |
|---|---|---|
| **Class 0** — bare land | None | Full autonomous operation |
| **Class 1** — partial | Water and/or internet only | Autonomous energy, connected services |
| **Class 2** — partial+ | Water + internet + AC grid | Hybrid: grid supplements autonomous |
| **Class 3** — full | All networks available | Integrated: autonomous systems as backup |

The electrical architecture resolves this through a **48V DC SELV bus as permanent spine**, with optional grid connection as an additive layer rather than a prerequisite.

---

## 3. Electrical Architecture — The DC-Native Spine

### 3.1 Why 48V DC

The 48V DC bus is chosen for four converging reasons:

1. **SELV compliance**: ≤50V DC places the fixed installation outside NF C 15-100 scope — no CONSUEL, no licensed electrician mandatory, installation performable by cooperative members
2. **Ecosystem maturity**: 48V is the global telecom standard (Bell System, 1960s), the Open Rack v3 server standard, and the USB Power Delivery 3.1 ceiling — vast certified component supply
3. **Transport safety**: 48V LFP battery packs are classified UN 38.3, transportable by road and sea without special permit at typical container capacities
4. **Efficiency**: at 48V, cable cross-sections and resistive losses are manageable over container-length runs without heavy copper

### 3.2 The 230V AC question

A container unit smaller than 14m² occupied by a student or tourist has a daily energy consumption of approximately 1.7 kWh — dominated by a small DC refrigerator, laptop, phone, lighting, and WiFi router. Every significant load in this profile is natively DC or powered through a switching supply that accepts DC input.

230V AC is not eliminated. It is **demoted to an on-demand service**, provided by a portable power station (700–1000 Wh, integrated inverter, 500–1000W AC output) that lives at the site charging station and is borrowed by residents for punctual needs: hair dryer, drill, legacy charger.

This portable pack is the smallest viable EPN packet: a discrete, addressed, routable unit of stored exergy, physically carried between the charging station and the point of use. Its location is tracked in real time via a BLE beacon.

```
BUS 48V DC (permanent spine inside container)
│
├── USB-C PD 3.1 outlets (×4, up to 240W each)
│   laptop, phone, tablet, small appliances
│
├── Fixed DC loads (hard-wired)
│   mini-fridge brushless DC
│   LED lighting (via DC/DC 24V)
│   ventilation fan DC
│   WiFi router (PoE 48V)
│   IP camera (PoE 48V)
│   LoRaWAN gateway
│
└── [Optional] Grid connection input
    AC 230V → rectifier → 48V bus top-up
    (Class 2 and 3 sites only)

PORTABLE PACK (shared, not fixed)
700 Wh + integrated inverter + BLE beacon
→ borrowed from charging station
→ provides 230V AC inside unit when needed
→ returned and recharged on 48V bus
```

---

## 4. Configuration A — Single Autonomous Container

### 4.1 Use case

A single Mariani Village container deployed on a Class 0 or Class 1 site: bare land, a farm, a remote commune, a festival site. No grid connection. Full energy autonomy required.

### 4.2 Architecture

```
[2 × PV 400Wc — roof mounted]
            ↓
    [MPPT controller 48V/40A]
    Victron SmartSolar 100/40
            ↓
    [LFP battery 48V 100Ah = 4.8 kWh]
    Pylontech US3000C or equivalent
            ↓
    [48V DC busbar — inside container]
            │
    ┌───────┼────────────────────────┐
    │       │                        │
[USB-C  [PoE 48V]           [DC/DC 48→24V]
 PD 3.1  router WiFi          LED lighting
 ×4      IP camera            ventilation
 240W]   LoRa gateway               │
                              [DC/DC 48→12V]
                               mini-fridge
                               brushless DC
```

### 4.3 Bill of materials

| Item | Reference | Cost |
|---|---|---|
| PV panels 2 × 400 Wc | Tier-1 monocrystalline | 400–600 € |
| MPPT controller 48V/40A | Victron SmartSolar 100/40 | 150–200 € |
| LFP battery 48V 100Ah | Pylontech US3000C | 800–1 100 € |
| DC busbar + fuses + wiring | Marine DC hardware | 150–250 € |
| USB-C PD 3.1 outlets ×4 | Baseus / Anker 140W GaN | 120–200 € |
| PoE switch 48V | TP-Link TL-SG1005P | 50–80 € |
| WiFi router PoE | Ubiquiti UniFi AP | 80–150 € |
| DC/DC 48→24V 10A | Victron Orion 48/24-8A | 60–90 € |
| DC/DC 48→12V 10A | Victron Orion 48/12-8A | 50–80 € |
| LED lighting 24V | Strip + fixtures | 80–150 € |
| Mini-fridge brushless DC | Vitrifrigo C42i | 300–500 € |
| **Total electrical** | | **2 240–3 400 €** |

**Portable pack (amortised, shared):**

| Item | Reference | Cost |
|---|---|---|
| Portable power station 768 Wh | EcoFlow RIVER 2 Pro | 450–600 € |
| BLE beacon | Tile Pro | 30–40 € |
| 48V DC charging cable | Compatible input | 20–40 € |
| **Total pack** | | **500–680 €** |

**Single container total: 2 740 – 4 080 €** for complete electrical installation.

Compare with grid connection (raccordement ERDF) alone: 2 000–8 000 €.

### 4.4 Daily energy balance (Class 0 site, Corsica irradiance)

```
Production: 800 Wc × 5h × 0.80 efficiency = 3 200 Wh/day

Consumption:
  Mini-fridge brushless DC      40W × 24h =   960 Wh
  Laptop + phone (USB-C PD)     60W ×  4h =   240 Wh
  WiFi router (PoE)              8W × 24h =   192 Wh
  LED lighting                  20W ×  6h =   120 Wh
  Ventilation fan               15W ×  8h =   120 Wh
  IP camera (PoE)                5W × 24h =   120 Wh
  Total                                   = 1 752 Wh/day

Surplus available                         = 1 448 Wh/day
Production/consumption ratio              = ×1.83
Battery autonomy without generation       = 2.7 days
```

### 4.5 Class 2–3 site adaptation

When AC grid is available, a single additional component is added:

**Victron MultiPlus-II 48/800** (~400€): bidirectional charger/inverter that tops up the 48V bus from grid AC when battery falls below threshold, and optionally exports surplus to grid when battery is full.

The occupant experience does not change. The 48V bus remains the spine. The grid becomes a background supplement, invisible in normal operation.

---

## 5. Configuration B — Multi-Unit Fleet Deployment

### 5.1 Use case

Five to seven Mariani Village containers deployed together on a single site: student housing in Corte, a cooperative campsite on the coast, a rural commune hosting seasonal workers. The fleet is managed by Mariani Village SAS, leased to the site operator.

### 5.2 The cooperative DC mesh

Individual container buses connect to a **shared 48V DC backbone** running across the site. This creates a local energy mesh with three operational benefits:

1. **Surplus sharing**: a container with excess solar production feeds neighbours with depleted batteries
2. **Resilience**: no single container's failure affects others
3. **Shared packet station**: two portable packs permanently on the backbone, always charged, always available to any resident

```
[C1]──[C2]──[C3]──[C4]──[C5]──[C6]──[C7]
  │     │     │     │     │     │     │
  └─────┴─────┴────[48V DC BACKBONE]──┴──┘
                          │
              ┌───────────┴────────────┐
              │                        │
       [Shared PV array]        [Cogentia node]
       [Shared LFP bank]        [Dashboard]
       [Packet station]         [BLE aggregator]
              │
       [Pack A 🔋 charged]
       [Pack B 🔋 charging]
```

### 5.3 Fleet shared infrastructure

| Item | Specification | Cost |
|---|---|---|
| Shared PV supplement | 4 × 400 Wc on common structure | 600–900 € |
| Shared LFP bank | 48V 200Ah = 9.6 kWh | 1 400–1 800 € |
| DC backbone cable 35mm² | ~60m across site | 200–400 € |
| DC distribution hub | Busbar + breaker per container | 300–500 € |
| Cogentia edge node | Raspberry Pi 4 + 48V UPS | 150–250 € |
| Portable pack A + BLE | EcoFlow RIVER 2 Pro + Tile | 480–640 € |
| Portable pack B + BLE | EcoFlow RIVER 2 Pro + Tile | 480–640 € |
| Charging station enclosure | Weatherproof IP65 cabinet | 150–250 € |
| BLE detection nodes ×7 | Raspberry Pi Zero 2W each | 105–175 € |
| **Total shared** | | **3 865–5 555 €** |
| **Per container (÷7)** | | **552–793 €** |

### 5.4 Total cost per container in fleet configuration

| Component | Cost |
|---|---|
| Individual container electrical | 2 240–3 400 € |
| Shared infrastructure share (÷7) | 552–793 € |
| **Total per container** | **2 792–4 193 €** |

The fleet configuration is marginally cheaper per unit than single deployment, while providing surplus sharing, redundancy, and shared services.

### 5.5 The portable pack as EPN packet

The portable power station circulating between containers and charging station is the operational core of the fleet's AC strategy. Two packs serve seven containers because AC usage is brief and rarely simultaneous.

Its location is tracked via BLE beacon, detected by a Raspberry Pi Zero 2W in each container (powered from the 48V bus), aggregated by the Cogentia node:

```json
{
  "timestamp": "2026-09-01T14:32:11Z",
  "pack_id": "PACK-A",
  "soc_percent": 87,
  "location": "container_03",
  "since": "14:18:00",
  "status": "in_use",
  "pack_b": {
    "location": "station",
    "soc_percent": 100,
    "status": "available"
  }
}
```

A local web dashboard served by the Cogentia node — accessible on the shared WiFi from any browser — shows availability at a glance. No app installation required.

### 5.6 Annual fleet repositioning

Each container performs at most one return journey per year — a deliberate constraint imposed by transport cost and site logistics. The annual calendar is therefore a strategic document, not an operational schedule:

```
ACADEMIC YEAR (October → June)
Fleet deployed at student site (e.g. Corte)
Occupants: students, SCIC associates, voter registration
Tariff: monthly cooperative rent

SUMMER SEASON (July → September)
Fleet deployed at tourist or coastal site
Occupants: visitors, seasonal workers
Tariff: nightly or weekly rate

ANNUAL TRANSITION (June — 1 to 2 weeks)
Containers lifted by crane truck, transported to summer site
Backbone reconnected, Cogentia node restarted
Duration: 3–5 days per full fleet move

RETURN (September — 1 to 2 weeks)
Fleet returns to student site for academic year
```

The Cogentia node travels with the fleet, preserving all energy performance data, occupancy history, and maintenance records across deployments. Site operators at both ends must pre-provision the 48V backbone connection points — standardised by Dilorta's site specification — so reconnection on arrival requires no configuration beyond physical cable connection.

---

## 6. Regulatory and Legal Position

### 6.1 Electrical safety

The 48V SELV fixed installation is outside NF C 15-100 scope (IEC 60364-4-41). No CONSUEL inspection required. Installation is performable by cooperative members or Dilorta technicians without licensed electrician certification for the SELV components.

The portable pack is a CE-marked consumer electronics product (UN 38.3 transport certified). Its 230V AC output is governed by product safety law — identical in legal status to using any portable generator or power bank.

### 6.2 Housing and transport classification

An ISO container adapted as housing is classified in France as a **résidence démontable** or mobile dwelling when it retains transport capability. Electrical requirements follow vehicle and product directives rather than residential building regulations. Long-term placement on a site under bail à construction does not automatically reclassify the unit as a fixed building provided the container remains structurally transportable.

### 6.3 Dilorta's commercial role

Once formed, Dilorta SAS will hold:
- the Mariani Village container specification and electrical design
- the Cogentia software licence for fleet management
- the deployment methodology and training programme for site operators
- the commercial relationship with site operators (lease contracts, SLA)

Mariani Village SAS (Corsica instance) will licence the model from Dilorta and own the physical fleet. Site operators (SCIC Corte, campings, communes) lease containers from Mariani Village on terms defined by Dilorta's standard contracts.

This three-tier structure cleanly separates:
- **IP and methodology** (Dilorta) — protected, replicable
- **Fleet ownership and regional operation** (Mariani Village instance) — capitalised with sovereign fund
- **Site operation** (local operator) — no capital requirement, leases the service

---

## 7. The EPN Correspondence

Mariani Village is the Energy Packet Network at human scale. Every element of the EPN architecture has a direct correspondent:

| EPN concept | Mariani Village equivalent |
|---|---|
| Energy packet | ISO 20-foot container unit |
| Packet metadata | Container spec sheet, electrical config, occupancy profile |
| Fleet routing | Seasonal deployment: Corte ↔ coastal site |
| Routing metric | Demand (students in winter, tourists in summer) |
| Store-and-forward | Container stored at site, energy stored in LFP, AC stored in portable pack |
| Smallest packet | Portable 700 Wh pack, carried by resident |
| Human router | Resident carrying portable pack between unit and station |
| Network operations | Cogentia edge node + BLE tracking dashboard |
| Application layer | Housing service, tourist accommodation, student cooperative |

> *The resident who borrows the portable pack to charge a legacy device re-enacts exactly the gesture of a ferry transporting an LFP container between islands. It is the same protocol at a different scale: a discrete packet of stored exergy, routed by a human, tracked by the network, discharged at the point of need.*

---

## 8. Roadmap

### Phase 1 — Single container demonstrator (2026)

- Deploy one container unit at reference site in Corte
- Full DC-native electrical installation, Cogentia node commissioned
- Document installation procedure, costs, energy performance
- Portable pack circulation protocol tested with first occupants
- Open to student occupancy: September 2026

### Phase 2 — First fleet deployment (2027)

- Deploy 5–7 containers at Corte student site (parcel AB 0120 reference)
- Shared DC backbone and cooperative charging station installed
- First cohort of SCIC student associates onboarded
- Summer 2027: first seasonal relocation to coastal site, performance documented

### Phase 3 — Dilorta licence replication (2028–2030)

- Publish open deployment guide (Dilorta white label)
- First licence to non-Corsican instance (Sardinia, Réunion, or French mountain commune)
- Position Mariani Village as reference demonstrator for FractaVolta Mediterranean rollout
- Submit energy and social performance data to Horizon Europe / PRIMA funding calls

---

## 9. Conclusion

Mariani Village is a relocatable housing fleet built on three converging theses.

**Architecturally**, the ISO 20-foot container is the natural housing packet: standardised, transportable by any carrier, structurally certified, and large enough to constitute a complete living unit while small enough to require only DC-native loads.

**Electrically**, the 48V SELV DC bus is the natural spine: outside regulatory scope for fixed wiring, compatible with the full modern consumer electronics ecosystem via USB-C PD 3.1, and safe enough for cooperative self-installation. The 230V AC capability travels with the resident as a portable packet, not through the walls as permanent infrastructure.

**Operationally**, the fleet is a network. Demand routes containers between student and tourist profiles seasonally. Dilorta holds the protocol. Mariani Village instances hold the physical assets. Site operators provide the terrain.

The single container proves the concept at minimum scale: one unit, one occupant, full autonomy, 2 740–4 080 € total electrical cost, no grid connection, no licensed electrician, no CONSUEL.

The fleet deployment proves the concept at cooperative scale: shared DC backbone, surplus routing between containers, portable pack circulation tracked by BLE, seasonal relocation between sites.

In both configurations, the packet model works. It will work at the scale of a Mediterranean territorial energy commons.

The persistence of the fixed, grid-connected dwelling as the only conceivable form of housing is not a technical necessity. It is a case of what the companion paper [1] calls *amathia* — the Aristotelian term for the ignorance of one's own ignorance. Housing professionals, urban planners, and cooperative developers possess every element required to conceive the relocatable DC-native dwelling: the ISO container standard, the LFP battery, the USB-C PD connector, the SCIC legal form. What is missing is not information but the synthetic intelligence that assembles these elements across domain boundaries into a coherent packet.

The first Mariani Village container deployed in Corte is not a pilot project in the conventional sense. It is an epistemological intervention: a physical object that should not exist according to the housing circuit paradigm — and does.

---

## References

[1] Robert, J.H.N. *The Unconscious Grid: On Store-and-Forward as the Repressed Solution to Energy Sovereignty*. FractaVolta, 2024.
https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md

[2] Robert, J.H.N. *DC-Native Energy Packet Networks: How Far Can Electricity Return from Alternating Current to Direct Current?* Institut Mariani / FractaVolta, 2026.

[3] IEC 60364-4-41. *Low-voltage Electrical Installations — Protection for Safety — Protection Against Electric Shock*. IEC, 2005 (amended 2017).

[4] USB Implementers Forum. *USB Power Delivery Specification Revision 3.1*. USB-IF, 2021.

[5] Victron Energy. *SmartSolar MPPT and MultiPlus-II Technical Documentation*. Victron Energy BV, 2024. https://www.victronenergy.com

[6] Open Compute Project. *DCF Power Distribution LVDC White Paper*. OCP, 2026.

[7] Loi n° 2001-624 du 17 juillet 2001 instituant les sociétés coopératives d'intérêt collectif. Journal officiel de la République française.

[8] Loi Huwart, novembre 2025. Dispositions dérogatoires pour l'habitat coopératif et les structures SCIC.

[9] github.com/JeanHuguesRobert/cogentia — Cogentia open-source energy routing and inference layer, MIT licence.

[10] ISO 668:2020. *Series 1 Freight Containers — Classification, Dimensions and Ratings*. ISO, 2020.


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Corpus Status — FractaVolta](research/corpus-status.md)
- [Research Index — FractaVolta](research/index.md)

<!-- END_AUTO: backlinks -->
