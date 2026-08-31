---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/PGN.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-06-01
title: "Packetized Gravity Networks: Distributed Hydro-Energetic Infrastructure for Resilient Renewable Integration"
date: "2026-05-08"
status: "draft — auto-filled (frontmatter cleanup)"
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
---
# Packetized Gravity Networks: Distributed Hydro-Energetic Infrastructure for Resilient Renewable Integration

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani — C.O.R.S.I.C.A.

1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org | fractavolta.com

*Priority established by first public commit. License: CC BY-SA 4.0.*
*Repository: github.com/JeanHuguesRobert/fractavolta*

---

## Orientation

Status: sovereign source document in draft form.

Function in the corpus: introduce Packetized Gravity Networks as the hydraulic and energetic substrate that can buffer solar exergy before it becomes sovereign compute.

Read before: [Carte globale du Corpus](https://github.com/JeanHuguesRobert/JeanHuguesRobert/blob/main/research/corpus-map.md), [DHITL](https://github.com/JeanHuguesRobert/marenostrum/blob/main/research/DHITL.md), and [Infrastructure is All You Need](https://github.com/JeanHuguesRobert/marenostrum/blob/main/research/infrastructure_is_all_you_need.md).

Read after: [Inference Packet Network](research/inference_packet_network.md) and the FractaVolta research index.

Depends on: the packet-switching analogy, distributed water infrastructure, territorial exergy storage, and the MareNostrum compute-governance layer.

Continuation: clarify the connection from PGN to EPN/IPN and to concrete Mediterranean pilot sites.

Last consolidation: 2026-06-09 — orientation block added during corpus digestion.

## Abstract

This paper introduces Packetized Gravity Networks (PGN), a distributed hydro-energetic infrastructure architecture that repurposes existing water systems — irrigation canals, mountain reservoirs, gravity-fed conduits — as programmable exergy networks. The central claim is that gravitational potential energy, distributed across territorial relief, can function as a passive, multi-purpose memory layer for intermittent solar generation, provided it is governed through software-defined hydraulic routing nodes we term Intelligent Energy Valves (IEV).

The PGN framework is inspired structurally by packet-switched communication networks: where Baran and Davies replaced fragile point-to-point circuits with resilient asynchronous routing, PGN replaces fragile centralized energy balancing with opportunistic local exergy extraction and distributed gravitational buffering. Unlike batteries, stored water simultaneously satisfies energy, irrigation, fire-resilience, and ecological objectives — making PGN a rare case of infrastructure whose resilience compounds rather than specializes.

We argue that this framework addresses a genuine gap in the water-energy nexus literature, which has extensively explored micro-hydropower recovery, inline pumped storage, and distributed water-energy systems, but has not proposed a unified packet-switched architecture for hydraulic exergy routing. Corsica is introduced as a representative mountainous, solar-rich, hydraulically-rich case study. The paper is positioned within the broader MareNostrum framework, in which the exergy chain extends from photovoltaic generation through gravitational storage to sovereign computation: photons → pumps → altitude → turbines → electrons → inference.

---

## 1. Introduction

### 1.1 The Storage Problem in Distributed Solar Energy

The accelerating deployment of solar photovoltaics has made the mismatch between generation and consumption — rather than raw generation capacity — the binding constraint on decarbonization. In solar-rich, mountainous territories, this mismatch has a peculiar structure: peak generation occurs at midday under full sun, while peak demand occurs in the morning and evening, and the seasonal surplus in summer precedes the greatest thermal storage need in winter. No battery technology currently addresses this temporal scale economically at the territorial level.

Conventional responses have concentrated on large pumped storage hydropower (PSH), grid-scale lithium batteries, and demand-side management. Each of these approaches inherits what this paper calls the *circuit-switched paradigm*: the assumption that energy infrastructure must continuously balance synchronized flows from large, centralized sources to large, centralized sinks, with limited local buffering and strong coupling between production and consumption. This paradigm maximizes steady-state efficiency but systematically reduces resilience. A single large reservoir fails as a unit; a centralized grid collapses when its balancing authority fails.

Meanwhile, in virtually every mountainous Mediterranean territory, there exists a distributed hydraulic infrastructure — irrigation canals, gravity-fed water distribution systems, mountain micro-reservoirs, historical conduits — that already implements territorial gravitational transport at scales ranging from a few kilowatts to several megawatts of latent hydraulic head. This infrastructure is almost entirely underexploited energetically. It was built to move water; the fact that moving water downhill is thermodynamically equivalent to discharging a battery has never been structurally integrated into its operational logic.

### 1.2 From Circuits to Packets

The transformation this paper proposes is conceptually analogous to the shift from circuit-switched to packet-switched communication networks. In circuit-switched telephony, a dedicated physical path was established end-to-end before any data could flow; the path was held for the duration of the call regardless of whether information was being transmitted. This maximized the quality of any given connection but made the infrastructure fragile and wasteful at low utilization.

Paul Baran's insight was that information did not require a dedicated circuit — it could be decomposed into discrete packets, each independently routed through a distributed mesh, with local nodes making routing decisions based on available paths. The result was a network that degraded gracefully under partial failure rather than catastrophically, and that made efficient use of available capacity across the whole mesh.

Packetized Gravity Networks apply the analogous principle to water and energy. A *hydraulic packet* is a bounded quantum of water temporarily stored at a given elevation, available for release through a micro-turbine when downstream demand or grid conditions justify it. An Intelligent Energy Valve (IEV) is a programmable node that routes, stores, measures, and arbitrates hydraulic flows, making local decisions based on its own sensor data, communication with adjacent nodes, and grid state signals. The network of IEVs constitutes a software-defined hydraulic mesh whose aggregate behavior can compensate solar intermittency, enforce water rights, preserve ecological flows, and maintain irrigation schedules — simultaneously, without central coordination.

### 1.3 Research Gap and Contribution

The water-energy nexus literature is extensive and includes work on micro-hydropower energy recovery in water supply systems (McNabola et al., 2014), inline pumped storage hydropower (Ramos et al., 2022), conduit hydroelectricity, distributed micro-hydro and pico-hydro systems, and co-optimization of water and energy networks (Silva-Rodriguez & Li, 2022; Li et al., 2018). The JRC has reviewed pumped storage hydropower comprehensively within European energy systems (Quaranta et al., 2022).

However, no existing framework proposes, to our knowledge: (i) a packet-switched conceptual architecture for hydraulic exergy routing; (ii) the IEV as a unified node model combining turbine, pump, measurement, control, and communication functions; (iii) the integration of distributed gravitational buffering with solar intermittency compensation as a primary design objective; or (iv) the explicit formal treatment of gravity as *territorial memory* — a passive, multi-purpose storage substrate whose capacity is defined by terrain, water availability, and relief, rather than by capital investment in purpose-built storage infrastructure.

This paper makes these contributions. It is positioned within the FractaVolta architecture, and connects to the broader MareNostrum framework through the concept of Compute eXergy Units (CXU), in which gravitational storage constitutes one physical realization of the exergy chain from solar generation to sovereign inference infrastructure.

---

## 2. Theoretical Framework: Gravity as Territorial Memory

### 2.1 Exergy of Elevated Water

The gravitational potential energy stored in a mass *m* of water at height *h* above a reference level is:

$$E_{grav} = mgh$$

where *g* is gravitational acceleration (9.81 m/s²). The extractable hydraulic power from a flow *Q* (m³/s) at head *H* (m) through a turbine of efficiency *η* is:

$$P = \rho \cdot Q \cdot g \cdot H \cdot \eta$$

where *ρ* is water density (≈ 1000 kg/m³). For a micro-turbine installation with *Q* = 0.1 m³/s, *H* = 50 m, and *η* = 0.75, this yields *P* ≈ 36.8 kW — a meaningful contribution at the level of an agricultural hamlet or a small datacentre load.

The key insight is that existing irrigation infrastructure already concentrates gravitational head. A canal that descends 100 meters over 5 kilometers in order to reach lower fields contains, at any given moment, a hydraulic head that could be harvested rather than dissipated. The water must flow for irrigation; the energy can be extracted *en passant* before the water reaches its agricultural destination.

Within the CXU (Compute eXergy Unit) framework of MareNostrum, defined as:

$$CXU = E \cdot \eta_{hw} \cdot \eta_{sys} \cdot \eta_{sla}$$

gravitational storage extends the exergy chain: solar photons generate electricity; electricity drives pumps; pumps elevate water; elevated water stores exergy; exergy is released through micro-turbines; electricity runs compute infrastructure. Each conversion stage has a measurable efficiency, and the product of efficiencies bounds the sovereign computational capacity extractable from a given solar irradiance and relief endowment.

### 2.2 The Packet Abstraction

In a PGN, a *hydraulic packet* is formally defined as a tuple:

$$p = \langle V, H, t_{release}, \theta, \pi \rangle$$

where *V* is the volume (m³) of water, *H* is the net head available at the release node, *t_release* is the scheduled release time, *θ* is the destination node identifier (irrigation point, turbine, or ecological discharge), and *π* is the priority class (irrigation > ecological > energy > compute).

This formalization makes explicit what is implicit in any irrigation network: water stored at elevation is already a packet, awaiting a routing decision. What PGN adds is the *programmability* of that routing decision, the *measurability* of the exergy extracted at each step, and the *communication infrastructure* that allows nodes to coordinate release schedules without central dispatch.

### 2.3 Gravity as Memory: Comparison with Other Storage Modalities

The proposition that gravity constitutes territorial memory deserves careful qualification. Table 1 compares gravitational storage with lithium-ion batteries and hydrogen on the dimensions relevant to distributed territorial deployment.

**Table 1. Comparison of Storage Modalities for Distributed Territorial Deployment**

| Dimension | Gravitational (PGN) | Li-ion Battery | Hydrogen |
|---|---|---|---|
| Energy density (Wh/kg) | 0.003–0.03 | 150–300 | 33,000 |
| Round-trip efficiency | 70–85% | 90–95% | 30–45% |
| Multi-use value | Energy + water + fire + ecology | Energy only | Energy only |
| Capital cost per kWh | Low (existing infrastructure) | 150–400 €/kWh | High |
| Degradation | None (water is reusable) | ~20% over 10 years | Material fatigue |
| Temporal scale | Minutes to months (seasonal) | Hours to days | Weeks to months |
| Geographic constraint | Relief + water resources | None | None |
| Governance complexity | Water rights, ecology | Ownership | Safety regulation |

The gravitational modality is not superior on any single dimension but is uniquely competitive on multi-use value and marginal cost where existing infrastructure is present. A battery stores energy; a hydraulic buffer stores energy *and* delivers irrigation *and* maintains fire-break water reserves *and* supports ecological minimum flows. This multi-functionality is not a secondary benefit — it is the primary economic justification for PGN deployment in territories where water infrastructure already exists.

---

## 3. The Intelligent Energy Valve: Node Architecture

### 3.1 Functional Definition

The Intelligent Energy Valve (IEV) is the elementary node of a Packetized Gravity Network. Its design integrates, in a single modular unit, the functions that existing water-energy systems distribute across separate, non-communicating devices: turbines, pumps, flow meters, pressure sensors, actuated gates, and SCADA interfaces.

Formally, an IEV node *n* is characterized by its state vector:

$$s_n = \langle Q_{in}, Q_{out}, H_{up}, H_{down}, P_{extract}, P_{pump}, \sigma, C_{eco} \rangle$$

where *Q_in* and *Q_out* are upstream and downstream flow rates, *H_up* and *H_down* are upstream and downstream heads, *P_extract* is the current power extraction rate, *P_pump* is the current pumping rate, *σ* is the operational mode, and *C_eco* is the current ecological compliance state.

The IEV implements the following priority ordering for hydraulic allocation:

1. Ecological minimum flow (*C_eco* must never be violated)
2. Drinking water and sanitation
3. Agricultural irrigation (time-scheduled)
4. Fire-resilience buffer maintenance
5. Energy extraction (opportunistic)
6. Compute load serving (lowest priority, highest value per kWh)

This priority structure is not merely a software configuration — it is a formal encoding of the water rights and regulatory obligations that govern any given watershed. By making these priorities explicit in software, PGN transforms water rights from paper constraints into operational invariants.

### 3.2 Operational Modes

An IEV transitions between five operational modes based on sensor state and network signals:

**Bypass mode** routes water without energy interaction, preserving full flow for downstream purposes. This is the default when irrigation demand is high or ecological thresholds are at risk.

**Energy extraction mode** activates the micro-turbine, extracting power from the available hydraulic head at a rate determined by the current grid signal and downstream availability.

**Pumped storage mode** reverses the turbine to act as a pump, lifting water to upstream reservoirs during periods of solar overproduction. This closes the storage loop, enabling the node to function as both a battery charger and a battery discharger depending on grid state.

**Maintenance isolation mode** gracefully removes the node from the network by activating bypass while signaling adjacent nodes to redistribute routing.

**Emergency fire reserve mode** overrides all other priorities to rapidly fill downstream cisterns from available upstream storage, triggered by atmospheric risk signals or local fire detection.

### 3.3 Communication Stack

The IEV communication stack is designed for low-power, low-bandwidth mesh operation in mountainous terrain where cellular connectivity is intermittent and fiber infrastructure absent. The proposed stack is:

- **Physical layer**: LoRaWAN (868 MHz in Europe) for long-range, low-power mesh
- **Messaging protocol**: MQTT over LoRaWAN bridge, with local broker at each IEV
- **Routing protocol**: Gossip-based state sharing with 30-second heartbeat
- **Optimization layer**: Local ML model (trained offline, updated monthly) for predictive release scheduling based on weather forecast and irrigation calendar
- **Security**: Hardware attestation at each node, traceable via blockchain-anchored measurement log

The key design constraint is that each IEV must be capable of *local autonomous operation* in the absence of network connectivity. An IEV that fails when its internet connection drops is not a resilient infrastructure component. The communication stack therefore implements only optimization at the network level; safety, priority enforcement, and ecological compliance operate entirely locally.

---

## 4. Distributed Micro-Pumped Storage: From One Dam to Many Buffers

### 4.1 The Fragility of Centralized PSH

Pumped Storage Hydropower (PSH) currently dominates global long-duration energy storage capacity, with over 9,000 TWh of global installed capacity (Quaranta et al., 2022). Its operational logic is straightforward: during low-demand periods, cheap electricity lifts water to an upper reservoir; during high-demand periods, water releases through turbines to generate premium electricity.

However, PSH in its conventional form requires large dedicated infrastructure — reservoirs with capacities measured in millions of cubic meters, head differences of hundreds of meters, turbine-pump units of hundreds of megawatts. These requirements make PSH economically viable only at scales that exclude the vast majority of mountainous territories with moderate relief and distributed water resources. In Corsica, for instance, the largest PSH installation at Alesiani operates at 90 MW, serves the entire island, and took decades to permit and build. It is a single point of failure.

PGN proposes a complementary, not competing, architecture: instead of one 90 MW installation, hundreds of 50–500 kW micro-installations, each locally owned, locally governed, and locally maintained. Their aggregate capacity may approach or exceed the centralized alternative; their resilience is categorically superior because failure of any single node causes graceful degradation rather than system-wide blackout.

### 4.2 Inline and Cascade Architectures

Ramos et al. (2022) have demonstrated the feasibility of *inline pumped storage hydropower* in water supply networks — installations that extract energy from pressure-relief points where excess pressure would otherwise be dissipated through pressure-reducing valves. PGN generalizes this concept to irrigation and gravity-fed distribution networks, where the equivalent of a pressure-relief valve is an uncontrolled drop in the canal profile.

### 4.3 Beyond Water: Solid and Opportunistic Gravitational Packets

The gravitational packet abstraction is not intrinsically hydraulic. The physical invariant is mass at elevation:

$$E_{grav}=mgh$$

Water is often the preferred medium because it is fluid, easily routed through conduits, and frequently provides additional territorial services. But where water storage is expensive, environmentally constrained, unavailable, or mechanically inconvenient, another mass may be preferable. Dense local materials such as granite, quarry rejects, aggregate, or other low-value mineral mass can therefore serve as a **solid gravitational packet** when moved between elevations by cable, rail, inclined-plane, shaft, or related lifting systems.

The relevant design question is not "water or rock?" in the abstract. It is whether a given site minimizes lifetime cost and territorial burden by using a hydraulic packet or a solid mass packet. Water gains from fluid routing and mature turbine technology; solid mass can avoid reservoirs, leakage, evaporation, hydraulic works, and water-right constraints. In mountainous territories, the two forms should be treated as complementary implementations of the same PGN primitive.

A second extension appears when the vertical movement exists for a reason independent of energy storage. An electric vehicle, freight tractor, cable carrier, or other mobile asset that must climb and later descend already performs the transformation:

```text
electrical energy -> altitude (mgh) -> regenerative electrical energy
```

If the trip would occur anyway, the gravitational cycle is **opportunistic**: transport is the primary service and energy buffering is a co-product. The relevant packet is then coupled to a logistical mission rather than created solely for storage.

A useful mobile packet state can be written provisionally as:

$$p_m=\langle m,h,SOC,C_{bat},\theta,t,\pi \rangle$$

where *m* is total moving mass, *h* is altitude, *SOC* and *C_bat* describe electrochemical state and capacity, *θ* is logistical destination, *t* is timing, and *π* represents service or routing priority. The immediately available energy state is then approximately:

$$E_{state}=E_{battery}+mgh$$

subject to route constraints and conversion efficiencies.

This representation exposes a practical variable that ordinary charging logic ignores: **regenerative headroom**. A vehicle approaching a long descent must preserve enough empty battery capacity to absorb the gravitational energy that will be recovered. Charging it to 100% immediately before descending can therefore destroy useful exergy.

### 4.4 Store-and-Forward Across Logistics and Energy

Mobile gravitational packets naturally connect PGN to the broader Generalized Packet Network and Energy Packet Network frameworks. A logistical hub can buffer both material and energy asynchronously:

```text
vehicle A descends
  -> regenerative energy
  -> local DC buffer
  -> wait / route / account
  -> vehicle B departs uphill
```

The energy therefore passes conceptually from one tractor to another without requiring their simultaneous presence. The station performs the same architectural function as a store-and-forward router: receive, buffer, inspect state, choose an outgoing path, and forward later.

The packetization can occur at several coupled layers:

```text
cargo packet      : what must reach the destination
trailer packet    : transportable physical carrier
energy packet     : measured transferable kWh
vehicle state     : battery + altitude + route capability
continuation      : the remaining logistical mission
```

At an intermediate mountain hub, the cargo or trailer may continue with a different tractor while the incoming tractor returns to its own valley. The mission persists while the execution resource changes. In this sense, a mountain logistics hub is not merely a charging station; it is a **physical continuation router**.

This suggests a new class of PGN node: the **Gravitational Packet Exchange Node (GPEN)**. A GPEN may combine bidirectional high-power charging, a stationary buffer, logistics handoff, route scheduling, state-of-charge management, and grid interaction. It does not create energy. Its value comes from reducing synchronization requirements, recovering gravitational exergy that would otherwise be dissipated, and routing that recovered capacity toward the next useful ascent or local grid need.

### 4.5 Corsican Mountain-Pass Case Pattern

Corsica provides a natural test environment because major transport corridors repeatedly cross large elevation differences over short horizontal distances. A representative pattern is a sea-level origin, a mountain pass near the midpoint, and a sea-level destination. For a 40-tonne vehicle climbing approximately 1,160 m, the theoretical gravitational energy change is about 127 kWh. A substantial fraction can be recovered regeneratively during descent if sufficient battery headroom is preserved.

The important research question is therefore not simply the energy consumption of one vehicle, but the aggregate behavior of a fleet:

- how much recoverable gravitational energy crosses each pass per day;
- whether arrival and departure flows are temporally balanced;
- how much stationary buffering is needed to decouple them;
- whether tractor/trailer handoff reduces required battery capacity;
- whether the same infrastructure can provide grid services during evening constraints;
- where a dedicated hydraulic or solid PGN remains preferable to opportunistic mobile storage.

This mobile extension does not replace distributed pumped storage. It adds another substrate to the same territorial gravity network: **water where fluid routing is best, solid mass where reservoirs are poor, and mobile mass where transport already pays for the movement.**
