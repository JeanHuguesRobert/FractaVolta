![FractaVolta logo](./docs/assets/jana.svg)


# FractaVolta

> From photons to inference

> Engineering firm and software publisher for robust Energy Packet Network deployments.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-FractaVolta-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/company/fractavolta)
![Status](https://img.shields.io/badge/status-early--stage-orange)
![Focus](https://img.shields.io/badge/focus-energy%20%2B%20compute%20%2B%20QoS-blue)

🌐 https://fractavolta.com — public entry point
📚 [research/index.md](research/index.md) — published papers and open possibilities
📊 [research/corpus_status.md](research/corpus_status.md) — corpus status

*Part of the [Cogentia Commons](https://github.com/JeanHuguesRobert/cogentia) distributed knowledge corpus.*
*Methodology: [Discours de la seconde méthode](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md)*

---

## What FractaVolta Is

FractaVolta is an engineering firm and software publisher. It designs and implements robust energy and compute infrastructure for clients who need it to work — islands, remote territories, industrial sites, cooperative housing, sovereign AI deployments.

It is the commercial and operational layer of the [MareNostrum](https://github.com/JeanHuguesRobert/marenostrum) strategic framework. MareNostrum defines the architecture. FractaVolta builds it.

**What FractaVolta sells:**
- Feasibility studies and system design for Energy Packet Network deployments
- DC-native node architecture (48V SELV bus, PV, LFP, edge compute)
- Regulatory navigation (IMDG maritime framework for battery containers, SELV electrical codes)
- Proprietary software tools for packet routing, fleet tracking, and energy dispatch (Cogentia)
- Operational training and deployment support

**What FractaVolta does not sell:**
- Electrons on a grid
- Carbon credits
- Generic consulting

The commercial proposition is precise: thirty years of asking "how do autonomous agents coordinate without a capturable centre?" — in programming languages, sensor networks, and governance institutions. We know how to answer it for energy. We charge for that answer.

---

## TL;DR

- The electrical grid is still **circuit-switched**
- Solar energy is **abundant but poorly utilized**
- FractaVolta applies **packet-switching to energy**
- Batteries, vehicles, and containers become **energy packets**
- Result: **resilient, distributed, scalable infrastructure**

---

*Jean Hugues Noël Robert*
Institut Mariani / C.O.R.S.I.C.A. — Corte, Corsica

📧 jhr@baronsmariani.org
🌐 https://fractavolta.com

---

## The Core Insight

In 1964, Paul Baran introduced packet-switching.
By 2000, it had replaced circuit-switched networks.

The electrical grid has not noticed.

It remains, structurally, a circuit-switched network: dedicated paths, continuous synchronisation, saturation that blocks all flow when any segment is full. The SARCO submarine cable connecting Corsica to continental France — saturated for significant portions of each year, while the island receives some of Europe's highest solar irradiation — is a textbook case.

> **FractaVolta applies packet-switching to energy.**

The insight is simple: a charged battery is an energy packet. The person carrying a mobile phone from one location to another is routing an energy packet. A twenty-foot shipping container of lithium iron phosphate cells, loaded onto a roll-on/roll-off ferry in Bastia and unloaded in Livorno, is a 2 MWh energy packet crossing 170 kilometres of sea with no cable, no synchronisation, and no saturated interconnection.

This architecture is fractal — self-similar from the mobile phone battery (0.1 kWh) to the container vessel carrying fifty containers (100 MWh). It is not a proposal. It already exists, practiced unconsciously. What is missing is the conscious protocol.

FractaVolta provides the protocol, the deployment framework, and the expertise to implement it.

---

## Why it matters

Solar energy is no longer scarce.

What is scarce is:
- reliability
- timing
- quality of service

FractaVolta addresses this gap.

---

## The Architecture

FractaVolta is built on three interlocking principles:

### 1. Store-and-Forward at Every Scale

> Energy is not a flow. It is a packet.

Energy packets are discrete, addressable, and physically transportable. The routing decision — which packet goes where, when, at what price — is made locally by the carrying agent responding to price signals, not by a central dispatcher. This is stigmergy: the same coordination mechanism that termite colonies use to build cathedrals without an architect.

| Scale | Packet | Carrier | Range |
|---|---|---|---|
| Personal | 0.1 kWh (phone battery) | Human | km |
| Neighbourhood | 1 kWh (cargo bicycle) | EV | 30 km |
| Mobility | 75 kWh (electric vehicle) | Road | 300 km |
| Regional | 2 MWh (20' container) | Ferry / truck | 500 km |
| Oceanic | 100 MWh (container vessel) | Ship | 2,000+ km |

### 2. Exergy, Not Energy

All accounting in the FractaVolta framework is conducted in **exergy** — the capacity to perform useful work — not raw energy. A container of LFP batteries holds 2 MWh and delivers 1.9 MWh of electrical work. A container of e-diesel holds 150–200 MWh but delivers only 60–70 MWh of electrical work — the Carnot ceiling cannot be engineered away.

The EPN is multi-protocol at the physical layer, selecting the energy medium to match the application. Battery for short-range high-value compute. Synthetic fuels for maritime propulsion and long-haul aviation.

### 3. AI Inference as the Application Layer

The highest-value use of an island's solar energy is not the export of electrons — constrained by cable capacity and priced at wholesale spot rates of €40–80/MWh — but the production of sovereign AI inference services, whose revenue per megawatt-hour is ×10 to ×40 greater.

AI inference converts solar photons into internet-routable data packets. An inference token does not cross the SARCO cable. It crosses the internet. The bottleneck is bypassed entirely.

The Compute eXergy Unit (CXU = E × η_hw × η_sys × η_sla), defined in the [MareNostrum framework](https://github.com/JeanHuguesRobert/marenostrum), is the pricing unit for this transduction.

---

## DC-Native Architecture

EPN packets are naturally DC. Photovoltaics generate DC. Batteries store DC. Electronic loads, LED lighting, telecommunications, electric vehicles, and AI inference nodes consume DC internally. Each avoidable AC/DC conversion stage introduces losses of 2–5%, compounding to 10–20% systemic overhead in conventional AC distribution chains.

FractaVolta nodes are designed DC-first:

```
[PV array] → [MPPT DC/DC] → [LFP battery bank]
                                      ↓
                             [48V DC bus]
                              ├── USB-C PD 3.1 (up to 240W)
                              ├── PoE — cameras, LoRa, WiFi
                              ├── LED lighting (24V via DC/DC)
                              ├── Edge compute / GPU inference
                              └── AC inverter — legacy boundary only
```

The 48V SELV bus is the spine. AC is an adapter protocol at the boundary, not the substrate. The USB-C PD 3.1 connector — operating at exactly 48V DC, up to 240W — becomes the human-facing interface of the DC bus: touch-safe, power-negotiated, and already in every user's pocket.

See `DC_NATIVE_EPN.md` for the full layered analysis.

---

## Mariani Village

Mariani Village is the habitat instance of the EPN thesis — developed by Institut Mariani and commercialised through its spin-off **Dilorta SAS** (*di l'Orta* — of the Orta river, Minesteggio, Corsica).

ISO 20-foot container units configured as DC-native minimal dwellings (<14 m²), deployed on host sites, repositioned annually between student occupancy (Corte, academic year) and tourist occupancy (Corsican coast, summer). No grid connection required. No licensed electrician. No CONSUEL. Total electrical cost per unit: €2,740–4,080.

The 230V AC capability travels as a portable 700 Wh battery packet — borrowed from the shared charging station, tracked by BLE beacon, returned when done. The student carrying it between their unit and the station re-enacts the gesture of a ferry transporting an LFP container between islands. Same protocol, different scale.

See `MARIANI_VILLAGE.md`.

---

## Why Diversity Is the Source

The FractaVolta framework is antifragile — in Taleb's precise sense — because its packet-switched architecture naturally produces diversity, and diversity is the source of resilience.

Diversity of vectors (battery, methanol, ammonia, SAF) means no single price shock collapses the network. Diversity of form factors (phone to vessel) means no single technology failure interrupts service. Diversity of routes (ferry, road, rail, aircraft) means no single closure blocks flow. Diversity of governance (cooperative, municipal, academic, commercial) means no single institutional actor can capture the protocol.

**RAIB — Redundant Array of Inexpensive Batteries.**

Commodity-grade LFP cells cost €80–120/kWh. Second-life cells retired from electric vehicles at 70–80% residual capacity cost €30–60/kWh. A fleet of inexpensive batteries managed by intelligent routing software is more resilient than a single premium system, for the same reason that ARPANET was more resilient than the telephone network: failure is distributed, graceful, and informative rather than catastrophic and silent.

---

## The France Connection

France has been here before.

In 1973, Louis Pouzin at IRIA designed CYCLADES — one of the world's first packet-switched networks, whose datagram architecture directly influenced Cerf and Kahn's TCP/IP. France then chose X.25: packet-switching in form, circuit-switching in spirit. Transpac and the Minitel were brilliant implementations of the wrong abstraction.

The energy sector faces the same choice. The "smart grid" literature proposes the X.25 of energy: smarter cables, better HVDC links, demand-response — all of which preserve the circuit-switched substrate. FractaVolta proposes the datagram: autonomous packets, routerless transport, stigmergic self-organisation.

Pouzin was right. The datagram won for information. It will win for energy.

---

## Repository Contents

| File | Description |
|---|---|
| [UNCONSCIOUS_GRID.md](./UNCONSCIOUS_GRID.md) | **Founding paper** — *The Unconscious Grid: On Store-and-Forward as the Repressed Solution to Energy Sovereignty*. The complete theoretical foundation of FractaVolta. |
| [DC_NATIVE_EPN.md](./DC_NATIVE_EPN.md) | **DC architecture paper** — *DC-Native Energy Packet Networks*. Layered analysis from packet internals to HVDC. Quantitative efficiency case for 48V DC-first node design. |
| [PGN.md](./PGN.md) | **Hydraulic paper** — *Packetized Gravity Networks*. Extending the exergy chain through gravitational storage. Historical canals as PGN substrate. Corsica case study. |
| [MARIANI_VILLAGE.md](./MARIANI_VILLAGE.md) | **Habitat packet paper** — *Mariani Village: A Relocatable DC-Native Housing Fleet*. Single container and multi-unit fleet. Dilorta SAS. BLE packet tracking. |
| [electricity_in_containers.md](./electricity_in_containers.md) | Working note (April 2026) — exploratory precursor to the full paper. |
| [fractavolta_paper.md](./fractavolta_paper.md) | Commercial overview and deployment framework. |
| [partner_brief.md](./partner_brief.md) | Partner engagement brief. |
| [tera.md](./tera.md) | FractaTera reference architecture — multi-scale sensing and territorial mapping. |
| [research/index.md](./research/index.md) | Research index — published papers, open possibilities, corpus map. |

---

## Ecosystem

FractaVolta is the commercial and operational layer of a four-repository ecosystem:

| Repository | Role |
|---|---|
| [MareNostrum](https://github.com/JeanHuguesRobert/marenostrum) | Strategic framework. Sovereign compute infrastructure for France and Europe. CXU. DHITL. Mediterranean solar commons. Circuit-to-packet transition theory. |
| **FractaVolta** | **Engineering firm + software publisher. EPN design and implementation. DC-native nodes. PGN. Mariani Village / Dilorta.** |
| [Cogentia](https://github.com/JeanHuguesRobert/cogentia) | Knowledge methodology. Cogentia Commons framework. `cogentia.js` CLI. Distributed corpus infrastructure. |
| [barons-Mariani](https://github.com/JeanHuguesRobert/barons-Mariani) | Political and institutional framework. Plan 2038. Corsican senatorial candidacy. *Discours de la seconde méthode.* |

---

## Theoretical Foundations

- **[The Unconscious Grid](./UNCONSCIOUS_GRID.md)** (2024) — founding EPN paper.
- **[DC-Native Energy Packet Networks](./DC_NATIVE_EPN.md)** (2026) — DC architecture, 48V node design, amathia of grid engineers.
- **[Packetized Gravity Networks](./PGN.md)** (2026) — hydraulic exergy, IEV nodes, gravity as territorial memory, Corsica case study.
- **[Mariani Village](./MARIANI_VILLAGE.md)** (2026) — habitat packet, Dilorta, BLE tracking, seasonal fleet routing.
- **[The Packet Transition: A Lateral Reading](https://github.com/JeanHuguesRobert/marenostrum/blob/main/PACKET_TRANSITION.md)** (2026) — phronèsis, amathia, transition taxonomy. *In MareNostrum.*
- **[The Packet as Evolutionary Attractor](https://github.com/JeanHuguesRobert/marenostrum/blob/main/PACKET_ATTRACTOR.md)** (2026) — complexity theory, open question. *In MareNostrum.*
- **[DHITL](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md)** (2025–2026) — Democratic Humans in the Loop. *In MareNostrum.*
- **[Discours de la seconde méthode](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md)** (2026-05-08) — methodological foundation of the corpus. *In barons-Mariani.*

All papers: CC BY-SA 4.0.

---

## Contact

**Email:** jhr@baronsmariani.org · institutmariani@gmail.com
**Web:** fractavolta.com
**GitHub:** github.com/JeanHuguesRobert/FractaVolta

---

## Optimized condensed version for AI agents

**FractaVolta** is an engineering firm and software publisher that designs and implements Energy Packet Network (EPN) deployments — the application of packet-switching principles to physical energy flows.

**Core architecture**: fractal electrochemical packets (0.1 kWh phone battery → 2 MWh ISO container → 100 MWh vessel) routed via conventional logistics. DC-native 48V SELV bus inside every autonomous node. USB-C PD 3.1 as human interface. AC as boundary adapter only.

**Extended exergy chain**: photons → pumps → altitude → turbines → electrons → inference. Gravitational storage via Packetized Gravity Networks (PGN) — historical irrigation canals repurposed as programmable hydro-energetic infrastructure.

**Software**: Cogentia — open-source energy routing, BLE fleet tracking, edge AI inference dispatch.

**Flagship deployment**: Mariani Village — relocatable DC-native student/tourist housing in ISO containers, operated by Dilorta SAS, seasonal routing between Corte (students) and Corsican coast (tourists).

**Strategic parent**: [MareNostrum](https://github.com/JeanHuguesRobert/marenostrum) — sovereign compute infrastructure framework for France/Europe. FractaVolta implements what MareNostrum specifies.

**Value proposition**: stranded Mediterranean solar exergy → sovereign AI inference tokens → ×10–×40 revenue premium over grid electricity export, bypassing cable bottlenecks entirely via internet routing.

**RAIB** (Redundant Array of Inexpensive Batteries): commodity LFP cells (€80–120/kWh) + intelligent routing > single premium system. Antifragile by architecture, not by contract.

**Knowledge methodology**: [Cogentia Commons](https://github.com/JeanHuguesRobert/cogentia) — traceable, auditable, AI-connectable. Governed by living persons alone.

---

*© 2026 Jean Hugues Noël Robert — Institut Mariani / C.O.R.S.I.C.A.*
*Documentation: CC BY-SA 4.0 · Software: MIT (Cogentia)*
