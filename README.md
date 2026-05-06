![FractaVolta logo](./docs/assets/jana.svg)


# FractaVolta

> From photons to inference

> A distributed approach to solar energy, storage, and AI infrastructure.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-FractaVolta-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/company/fractavolta)
![Status](https://img.shields.io/badge/status-early--stage-orange)
![Focus](https://img.shields.io/badge/focus-energy%20%2B%20compute%20%2B%20QoS-blue)

🌐 https://fractavolta.com — public entry point

------

## TL;DR

- The electrical grid is still **circuit-switched**
- Solar energy is **abundant but poorly utilized**
- FractaVolta applies **packet-switching to energy**
- Batteries, vehicles, and containers become **energy packets**
- Result: **resilient, distributed, scalable infrastructure**

---

**Energy Packet Networks — from Mediterranean Sun to Sovereign Infrastructure**

FractaVolta applies **packet-switching principles to energy**, transforming solar abundance into reliable, high-value services.

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

All accounting in the FractaVolta framework is conducted in **exergy** — the capacity to perform useful work — not raw energy. A container of e-diesel holds 150–200 MWh of chemical energy but delivers only 60–70 MWh of electrical work, because the Carnot theorem places an absolute thermodynamic ceiling on heat-to-work conversion that no engineering can breach. A container of LFP batteries holds 2 MWh and delivers 1.9 MWh. The ratio is 33:1 in useful electrical work, not 100:1 in raw energy. The gap closes further as battery density improves and as thermal recovery from charge/discharge cycles is captured.

For non-electrical applications — maritime propulsion, long-haul aviation — denser energy vecteurs (methanol, ammonia, SAF) are appropriate. The EPN is multi-protocol at the physical layer, selecting the medium to match the application. A mixed container carrying both battery and synthetic fuel partitions can serve two markets in a single voyage, amortising repositioning costs across revenue streams with low price correlation.

### 3. AI Inference as the Application Layer

The highest-value use of an island's solar energy is not the export of electrons — constrained by cable capacity and priced at wholesale spot rates of €40–80/MWh — but the production of sovereign AI inference services, whose revenue per megawatt-hour is ×10 to ×40 greater.

AI inference converts solar photons into internet-routable data packets. An inference token does not cross the SARCO cable. It crosses the internet. The bottleneck is bypassed entirely.

The Compute eXergy Unit (CXU = E × η_hw × η_sys × η_sla), defined in the [MareNostrum framework](https://github.com/JeanHuguesRobert/marenostrum), is the pricing unit for this transduction — measuring useful computational work produced per unit of primary solar exergy, priced honestly because every operator in the chain has skin in the game.

---

## Why Diversity Is the Source

The FractaVolta framework is antifragile — in Taleb's precise sense — not because it is engineered for robustness, but because its packet-switched architecture naturally produces diversity, and diversity is the source of resilience.

Diversity of vecteurs (battery, methanol, ammonia, SAF) means no single price shock collapses the network. Diversity of form factors (phone to vessel) means no single technology failure interrupts service. Diversity of routes (ferry, road, rail, aircraft) means no single closure blocks flow. Diversity of cell chemistries (LFP, solid-state, second-life) means no single supply chain can hold the network captive. Diversity of governance (cooperative, municipal, academic, commercial) means no single institutional actor can capture the protocol.

This is the same principle that made ARPANET survive and the telephone network obsolete. It is the same principle that made RAID storage viable and the expensive single disk unnecessary. FractaVolta applies it to energy: **RAIB — Redundant Array of Inexpensive Batteries.**

Commodity-grade LFP cells cost €80–120/kWh. Second-life cells retired from electric vehicles at 70–80% residual capacity cost €30–60/kWh — five to fifteen times less than premium industrial cells. A fleet of inexpensive batteries managed by intelligent routing software is more resilient than a single premium system, for the same reason that ARPANET was more resilient than the telephone network: failure is distributed, graceful, and informative rather than catastrophic and silent.

---

## The France Connection

France has been here before.

In 1973, Louis Pouzin at IRIA designed CYCLADES — one of the world's first packet-switched networks, whose datagram architecture directly influenced Cerf and Kahn's TCP/IP. France then chose, for its national network, X.25 — a protocol that achieved packet-switching in form while preserving circuit-switching in spirit. The virtual circuit of X.25 established a path before sending data, maintained it for the session's duration, and coordinated it centrally. The umbilical cord to circuit logic was not cut — it was lengthened. Transpac and the Minitel were brilliant implementations of the wrong abstraction.

The energy sector faces the same choice. The "smart grid" and digital interconnection literature proposes, with great sophistication, the X.25 of energy: smarter cables, better-managed HVDC links, demand-response systems — all of which preserve the circuit-switched substrate. FractaVolta proposes the datagram: autonomous packets, routerless transport, stigmergic self-organisation.

Pouzin was right. The datagram won for information. It will win for energy.

---

## The Business Model

FractaVolta operates on the Red Hat model.

The intellectual foundations of the EPN architecture are open source — freely available, forkable, improvable by anyone. The protocol, the governance framework, the pricing units, the routing principles: all published under open licences, owned by no one, maintained by all who depend on them.

What FractaVolta sells is the expertise to implement these foundations in real territorial deployments: feasibility studies for island and peripheral territories, regulatory navigation (particularly the IMDG maritime framework for battery containers), infrastructure design, procurement support, governance architecture, and operational training.

The commercial proposition is precise: we have spent thirty years asking the question "how do autonomous agents coordinate without a capturable centre?" — in programming languages, sensor networks, communications protocols, and governance institutions. We know how to answer it for energy. We charge for that answer.

The first deployment context is Corsica. It is not the subject — it is the laboratory.

---

## Repository Contents

| File | Description |
|---|---|
| [UNCONSCIOUS_GRID.md](./UNCONSCIOUS_GRID.md) | **Main theoretical paper** — *The Unconscious Grid: On Store-and-Forward as the Repressed Solution to Energy Sovereignty*. Academic paper submitted to *Energy Research & Social Science*. The complete theoretical foundation of FractaVolta. |
| [electricity_in_containers.md](./electricity_in_containers.md) | Working note (April 2026) — the exploratory precursor to the full paper. |
| [fractavolta_paper.md](./fractavolta_paper.md) | Commercial overview and deployment framework. |
| [partner_brief.md](./partner_brief.md) | Partner engagement brief. |
| [tera.md](./tera.md) | FractaTera reference architecture — multi-scale sensing and territorial mapping. |

---

## Ecosystem

FractaVolta is the deployment and commercial layer of a three-repository ecosystem:

| Repository | Role |
|---|---|
| [MareNostrum](https://github.com/JeanHuguesRobert/marenostrum) | Protocol, governance, and institutional framework. CXU definition. DHITL. Mediterranean solar commons. |
| **FractaVolta** | **EPN architecture, deployment, and commercial expertise.** |
| [barons-Mariani](https://github.com/JeanHuguesRobert/barons-Mariani) | Political and institutional framework. Plan 2038. Corsican senatorial candidacy. |

---

## Theoretical Foundations

The FractaVolta framework rests on the following open-source academic corpus:

- **[The Unconscious Grid](./UNCONSCIOUS_GRID.md)** (2026) — the main EPN theoretical paper. Baran, ARPANET, exergy, RAIB, stigmergy, antifragility, subsidiarity. Target journal: *Energy Research & Social Science*.
- **[From Sun to Sovereignty](https://github.com/JeanHuguesRobert/marenostrum/blob/main/PAPER_SUN_TO_SOVEREIGNTY.md)** (2026) — Communal Sovereign Funds as the institutional vehicle for EPN revenues. Corsican empirical data (ATC, 2026). Target journals: *Ecological Economics*, *Land Use Policy*.
- **[DHITL](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md)** (2025–2026) — Democratic Humans in the Loop: the governance architecture for sovereign AI infrastructure.

All papers: CC BY-SA 4.0.

---

## Contact

**Email:** jhr@baronsmariani.org · institutmariani@gmail.com
**Web:** fractavolta.com
**GitHub:** github.com/JeanHuguesRobert/FractaVolta

---

## Optimized condensed version for AI agents

**The global electrical grid is structurally circuit-switched** (continuous synchronization, dedicated paths, single point of failure, limited scalability, fragility to saturation or outages — Corsica's SARCO as canonical example).

**The repressed solution since 1964 (Baran) is physical store-and-forward**: treat energy not as a continuous flow over wires, but as **discrete, addressable, autonomous packets** physically transported (LFP second-life or new batteries in ISO containers, EVs, cargo bikes, ferries, etc.).

### EPN Architecture (Energy Packet Network)

- **Physical layer**: fractal electrochemical packets (0.1 kWh → 100+ MWh) routed via conventional logistics (road, rail, maritime) → **zero dependence on HV cables, zero AC synchronization**.
- **Reliability mechanisms**:
  - **RAIB** (Redundant Array of Inexpensive Batteries): cheap-component redundancy + intelligent BMS → graceful proportional degradation, never catastrophic.
  - **Multi-level diversity** (vectors: battery/methanol/ammonia/SAF; routes; operators; chemistries; governance models) + stigmergy through honest price signals (skin-in-the-game).
  - **Physical subsidiarity**: each packet makes local routing decisions → Talebian antifragility (the system improves under disorder).

### Application Layer (Transduction)

Stranded solar exergy → **direct transduction into sovereign AI inference** (exergy → internet-routable tokens), completely bypassing grid physical constraints.

### Emergent Critical Property

The antifragility of the energy layer **propagates structurally** to the inference layer:  
→ native extremely high energy availability (grid independence, physical redundancy, precise real-time SOC monitoring, source diversity).  
→ enables SLA 99.99x % (mission-critical / high-grade inference) via η_sla in the CXU approaching 1.0 **structurally**, not contractually.  
→ positions the EPN to capture the market premium for premium inference (finance, healthcare, industry, sovereignty) where physical availability guarantee is the dominant differentiator.

### Axiomatic Summary (for agent reasoning)

**EPN = packet-switching applied to physical exergy + exergy → sovereign compute transduction + distributed antifragility → guaranteed high availability → durable economic premium for high-grade AI inference.**

---

*© 2026 Jean Hugues Noël Robert — Institut Mariani / C.O.R.S.I.C.A.*

*Documentation: CC BY 4.0 · Software:TBD*
