---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/PGN.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-05-26
title: "Packetized Gravity Networks: Distributed Hydro-Energetic Infrastructure for Resilient Renewable Integration"
date: "2026-05-08"
status: "draft — auto-filled (frontmatter cleanup)"
---
# Packetized Gravity Networks: Distributed Hydro-Energetic Infrastructure for Resilient Renewable Integration

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani — C.O.R.S.I.C.A.

1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org | fractavolta.com

*Priority established by first public commit. License: CC BY-SA 4.0.*
*Repository: github.com/JeanHuguesRobert/fractavolta*

---

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

Cascade architectures link multiple IEV nodes along the same watercourse, with each node managing a portion of the total head. A watercourse descending 200 meters over 10 kilometers might host four IEV nodes at 50-meter intervals, each extracting 10–30 kW of opportunistic power while maintaining full irrigation delivery to fields at each elevation level. The cascade as a whole behaves as a single logical storage and generation unit, with the distributed IEV mesh providing coordinated scheduling.

### 4.3 Solar Coupling: The Absorption-Release Cycle

The fundamental operational cycle of a PGN node under solar integration is:

**Absorption phase** (solar surplus, typically 10:00–15:00 in Mediterranean summer):
$$solar_{excess} \rightarrow IEV_{pump} \rightarrow \Delta H_{reservoir}$$

**Storage phase** (evening and night):
$$\Delta H_{reservoir} \text{ maintained passively, zero energy cost}$$

**Release phase** (morning peak, evening peak, compute load):
$$\Delta H_{reservoir} \rightarrow IEV_{turbine} \rightarrow P_{local}$$

The efficiency of this cycle depends on pump-turbine round-trip efficiency (typically 70–85% for small units), hydraulic head losses in the canal, and the operational efficiency of the IEV's local scheduler. At the territorial scale, the cycle's economic value is determined not by round-trip efficiency alone but by the *price spread* between absorption and release — which, in markets with strong solar midday depression (the duck curve effect), can be substantial.

---

## 5. Multi-Use Storage and the Economics of Functional Overlap

### 5.1 Beyond the Single-Use Battery

The economic case for PGN rests not on energy storage economics alone but on the *functional overlap* between hydraulic storage and other territorial water needs. A battery stores electrons and serves no other purpose. A hydraulic buffer at elevation simultaneously provides:

- **Energy storage**: release through turbine when grid needs it
- **Irrigation reserve**: release on agricultural schedule regardless of grid state
- **Fire-resilience buffer**: rapid discharge to downstream cisterns during wildfire risk
- **Ecological support**: maintained minimum flow through the watercourse during drought
- **Thermal inertia**: buffered temperature in mountain streams, relevant for downstream ecosystems
- **Tourism and amenity**: maintained water flow in landscapes that depend on visible rivers and streams

Each of these functions has an independent economic value. The energy function is the marginal addition that PGN enables on top of an infrastructure that water management would require anyway. This changes the investment calculus fundamentally: the question is not whether energy storage alone justifies the IEV installation cost, but whether the energy function covers the *marginal* cost of adding measurement, control, and generation to water infrastructure that would be built regardless.

### 5.2 Seasonal Complementarity in Mediterranean Climates

Mediterranean mountain territories exhibit a seasonal pattern that makes PGN particularly well-suited. Solar generation peaks in summer (June–August), when snowmelt and spring rains have already filled upstream reservoirs, irrigation demand is highest, and fire risk is at its maximum. This apparent conflict — water is needed for agriculture and fire fighting precisely when solar generation is highest — is resolved by PGN's priority structure: solar surplus fills reservoirs, irrigation and fire reserves are maintained at priority, and the energy extraction function operates on whatever is available at the margin.

In winter, the pattern reverses: solar generation is lower, but precipitation recharges hydraulic reservoirs and reduces wildfire risk. The energy function gains priority over irrigation (which is minimal in winter), and micro-turbines can run at higher duty cycles. This seasonal complementarity is the hydraulic analogue of the wind-solar complementarity that grid planners exploit at the regional level — except that hydraulic storage provides the buffering that bridges the two seasons rather than requiring overbuilding of either source.

---

## 6. Governance: Water Rights as Programmable Constraints

### 6.1 The Regulatory Gap

Water rights in most jurisdictions are defined in documents — prefectural decrees, irrigation association bylaws, ecological flow requirements established by hydrological surveys — but enforced through inspections, complaints, and legal proceedings. The gap between the written allocation and the actual flow is often wide, and contested precisely because measurement is expensive and intermittent.

IEV nodes provide continuous, traceable measurement of diverted flows, restituted flows, ecological thresholds, and energy extracted at each point. This measurement infrastructure does not merely support governance — it *constitutes* governance, in the sense that the operational rules of each node are a direct encoding of the applicable water rights.

### 6.2 Software-Defined Water Rights

The IEV operational logic implements water rights as executable invariants. Consider a simplified regulatory requirement: a watercourse must maintain a minimum ecological flow of *Q_eco* = 0.02 m³/s at all times; irrigation association A has priority claim to 0.05 m³/s between 06:00 and 20:00 during the April–September season; energy extraction may use the remainder.

```python
def iev_allocation(Q_total, time, season):
    Q_eco = 0.020  # m³/s — regulatory invariant, never violated
    Q_irrigation = 0.050 if is_irrigation_season(season) and is_day(time) else 0
    Q_energy = max(0, Q_total - Q_eco - Q_irrigation)
    return Q_eco, Q_irrigation, Q_energy
```

This encoding is not a simplification — it is a faithful representation of the actual regulatory framework. What it adds is: auditability (every allocation decision is logged), enforceability (the node cannot violate the invariant regardless of external instructions), and transparency (any stakeholder can inspect the allocation logic and verify it against the regulatory text).

The implication is significant: *water rights become programmable operational constraints*, enforceable in real time without relying on the goodwill of operators or the availability of inspectors. This is the governance contribution of PGN, distinct from and complementary to its technical contributions.

### 6.3 Traceable Exergy and Democratic Accountability

The combination of continuous measurement and programmable allocation enables a new form of democratic accountability over shared water resources. Every cubic meter diverted, every watt-hour extracted, every ecological exceedance event is recorded in a tamper-evident log anchored to the same blockchain-based attestation infrastructure used for CXU accounting in MareNostrum.

This means that the citizens of a watershed — not an abstract regulatory authority, but the farmers, the municipal governments, the environmental associations — can directly inspect the operational record of every IEV node in their territory. The water commons becomes observable, and observability is the precondition for democratic governance of any shared resource (Ostrom, 1990).

---

## 7. Corsica as a Case Study

### 7.1 Territorial Endowment

Corsica presents an unusual combination of characteristics that make it a representative and tractable case study for PGN. The island rises to 2,706 meters (Monte Cinto) within 25 kilometers of the sea, generating relief of 100–800 meters over distances of 2–15 kilometers in most inland valleys. Mean solar irradiance on the western slopes is approximately 1,700 kWh/m²/year, among the highest in metropolitan France. Annual precipitation ranges from 600 mm on the coast to over 1,800 mm at altitude, with significant snowpack in the central massif providing spring and early summer discharge.

The island's water infrastructure includes several hundred kilometers of historical irrigation canals — the *chjole*, *piove*, and *matre* of the traditional agricultural system — many of which remain partially operational or intact as physical structures despite the collapse of the traditional agriculture that built them. These canals were engineered to convey gravitational head over long distances with minimal loss; they are, already, latent PGN infrastructure awaiting the installation of IEV nodes and measurement systems.

### 7.2 The ZNI Constraint as a Driver

Corsica operates as a Zone Non Interconnectée (ZNI) — an isolated electrical system not synchronized with the continental French grid. This isolation, which is a regulatory and economic constraint in conventional energy terms, is a technical opportunity for PGN deployment. In an interconnected grid, the value of local storage depends on wholesale market prices and transmission capacity; in a ZNI, every kilowatt-hour stored locally is worth exactly what it would cost to generate from diesel or import via submarine cable.

The island's current energy mix includes significant diesel generation for thermal backup, with a cost that the CRE (Commission de Régulation de l'Énergie) estimates at several hundred euros per MWh in marginal terms during peak periods. Every unit of gravitational storage that displaces this marginal diesel generation has a quantified value that justifies IEV deployment on purely economic grounds, before any ecological or resilience benefits are counted.

### 7.3 Historical Infrastructure as Substrate

The repurposing of historical canals as PGN substrate is not merely a technical convenience — it carries a governance logic. The *associations syndicales* that historically managed these canals established, over centuries, a body of customary water rights, usage calendars, and maintenance obligations that represents one of the most sophisticated pre-industrial commons governance systems in the Mediterranean (Robert, 2026; Ostrom, 1990).

PGN deployment on this substrate does not replace this governance — it extends it into the digital domain. The same associations that historically allocated irrigation turns can govern IEV priority schedules; the same customary minimum flows that protected downstream users can be encoded as ecological invariants. The technology becomes an implementation layer for institutional wisdom that predates it by centuries.

---

## 8. Connection to MareNostrum: From Photons to Inference via Gravity

### 8.1 The Extended Exergy Chain

The MareNostrum framework (Robert, 2025) proposes that Mediterranean solar irradiance, treated as a commons rather than a private resource, can fund a sovereign computation infrastructure through the chain: photons → electricity → Compute eXergy Units (CXU) → inference services. This chain is direct but fragile: solar generation is intermittent, and inference workloads require stable power.

PGN inserts a resilience layer into this chain by interposing gravitational storage between generation and computation:

$$\text{photons} \rightarrow \text{pumps} \rightarrow \Delta H \rightarrow \text{turbines} \rightarrow \text{electrons} \rightarrow \text{inference}$$

The gravitational buffer is not a detour — it is the mechanism that transforms intermittent photovoltaic generation into firm, dispatchable power suitable for datacentre operation. A datacentre powered entirely by direct solar generation requires either massive battery backup or significant grid connection; a datacentre powered by PGN-buffered hydraulic generation can operate at higher duty cycles with smaller battery systems, because the gravitational buffer smooths the solar duck curve over hours and the seasonal complementarity smooths it over months.

### 8.2 Hydraulic CXU

The CXU framework can be extended to incorporate hydraulic exergy. A *hydraulic CXU* is defined as:

$$CXU_{hydro} = E_{grav} \cdot \eta_{turbine} \cdot \eta_{sys} \cdot \eta_{sla}$$

where *E_grav* = ρVgH is the gravitational energy stored in volume *V* at head *H*, *η_turbine* is the turbine efficiency, *η_sys* is the system efficiency (accounting for distribution losses), and *η_sla* is the service-level availability factor of the downstream compute infrastructure.

This formulation allows direct comparison between solar-derived CXU and hydraulic-derived CXU, enabling optimal dispatch of compute workloads across mixed-source power infrastructures. When solar generation is abundant, CXU is derived primarily from direct photovoltaic generation and excess power is directed to pumping. When solar generation is scarce, CXU is derived from stored hydraulic exergy. The sovereign computation infrastructure becomes, in this sense, a second-order battery: it absorbs power when it is cheap and produces cognitive services when they are needed.

### 8.3 Sovereignty Implications

The sovereignty argument for MareNostrum rests on the proposition that Mediterranean nations own their solar irradiance as a commons, and that this ownership can fund sovereign AI infrastructure. PGN strengthens this argument by adding relief — another commons — to the asset base. A territory that owns its sunlight and its mountains owns, by extension, a dispatchable energy infrastructure that requires no imported fuel, no centralized grid operator, and no foreign capital for operation.

This is the physical foundation of the *nustrale* sovereignty claim in the Plan 2038 framework: Corsican sunlight, stored in Corsican mountains, released through Corsican canals, powering Corsican datacentres, providing inference services to the world. The token is the gold of the future; the mountain is the vault.

---

## 9. Deployment Strategy and Future Work

### 9.1 Pilot Architecture

The first FractaVolta PGN pilot is proposed for deployment in the Tavignano valley upstream of Corte, where: (i) existing irrigation canal infrastructure provides a substrate with 150–300 meters of available gravitational head over 8 kilometers; (ii) the proximity to the Université de Corse provides a research partner for instrumentation and monitoring; (iii) the ZNI constraint makes the economic case for local storage strongest; and (iv) the historical *association syndicale* governance structure provides a proven institutional framework.

The pilot architecture comprises three IEV nodes in cascade, each rated for 15–50 kW of generation capacity, with LoRaWAN mesh communication, local solar panels for IEV self-powering, and integration with a micro-datacentre load at the Université de Corse. This configuration tests all major elements of the PGN framework — generation, pumped storage, priority scheduling, ecological compliance, and CXU accounting — at a scale that is deployable within a 12-month timeframe.

### 9.2 Research Agenda

The PGN framework raises several open research questions that will be pursued in subsequent work. The first concerns hydraulic simulation: the interaction between IEV packet scheduling and watercourse hydraulics involves non-linear dynamics that cannot be fully captured by the simplified linear models presented in this paper, and requires finite-element simulation of canal flow under variable boundary conditions.

The second concerns distributed optimization: optimal packet scheduling across a network of IEV nodes is a combinatorial problem with real-time constraints, and the interaction between local ML schedulers and network-level coordination protocols requires formal analysis. The third concerns legal frameworks: the encoding of water rights as software constraints requires a precise mapping between regulatory text and executable logic that must be validated against the applicable law in each jurisdiction.

Finally, environmental assessment of PGN deployment on historical canals — particularly regarding fish passage, sediment transport, and riparian habitat — requires field study that cannot be completed at the design stage. The FractaVolta pilot will incorporate continuous ecological monitoring as a primary output, not a secondary compliance exercise.

---

## 10. Conclusion

Packetized Gravity Networks represent a reframing, rather than an invention, of existing hydraulic infrastructure. The water is already there, the relief is already there, the canals are already there. What is missing is the conceptual framework that recognizes distributed gravitational storage as a programmable exergy network, and the IEV hardware that makes that programmability physical.

The contribution of this paper is threefold. First, it proposes the packet-switching analogy as a productive conceptual framework for hydraulic energy routing, drawing on the structural parallel between Baran's insight in communication networks and the fragility of centralized energy balancing in distributed solar systems. Second, it formalizes the IEV as a node model that unifies turbine, pump, measurement, control, and communication functions in a single deployable unit whose operational logic encodes water rights as executable invariants. Third, it connects PGN to the broader MareNostrum exergy chain, demonstrating that gravitational storage is not merely an energy technology but a sovereignty infrastructure — a physical vault for the computational wealth that Mediterranean solar irradiance can generate.

The future of resilient infrastructure lies not in larger centralized systems but in programmable networks of small, locally-owned, locally-governed nodes cooperating through software-defined routing. In communication networks, this insight transformed a fragile circuit-switched world into the internet. In energy and water networks, the transformation has yet to fully occur. PGN is a proposal for how to begin.

---

## References

- McNabola, A., Coughlan, P., Corcoran, L., Power, C., Williams, A. P., Harris, I., ... & Gallagher, J. (2014). Energy recovery in the water industry using micro-hydropower: An opportunity to improve sustainability. *Water Policy*, 16(1), 168–183.
- Quaranta, E., Aggidis, G., Boes, R. M., Comoglio, C., De Michele, C., Doble, M., ... & Pistocchi, A. (2022). *Hydropower and Pumped Storage Hydropower in the European Green Deal*. JRC Publications Repository. JRC143929.
- Ramos, H. M., Morillo, J. G., Díaz, J. A. R., Pavĩco, I., Coronado-Hernández, O. E., & McNabola, A. (2022). Inline pumped storage hydropower towards smart and flexible energy recovery in water networks. *Water*, 14(15), 2401.
- Silva-Rodriguez, J., & Li, Z. (2022). Centralized networked micro water-energy nexus with proportional exchange among participants. *arXiv preprint*, arXiv:2207.02110.
- Li, Z., Wen, G., & Duan, Z. (2018). Micro water-energy nexus: Optimal demand-side management and quasi-convex hull relaxation. *arXiv preprint*, arXiv:1805.07626.
- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Robert, J.-H. N. (2025). *MareNostrum: Mediterranean Solar Irradiance as a Democratic Commons*. github.com/JeanHuguesRobert/marenostrum. CC BY-SA 4.0.
- Robert, J.-H. N. (2026). *Invidia, envie et désir mimétique: pour une anthropologie de la disqualification de la réussite en contexte méditerranéen*. Institut Mariani, Corte. github.com/JeanHuguesRobert/barons-mariani.
- UNESCO (2014). *The Water-Energy Nexus: An Introduction*. UNESCO Documents, pf0000227061.
- Wikipedia contributors. (2024). *Conduit hydroelectricity*. Wikipedia.
- Wikipedia contributors. (2024). *Micro hydro*. Wikipedia.

---

*Institut Mariani — C.O.R.S.I.C.A.*
*1 cours Paoli, F-20250 Corte, Corsica*
*Priority: first public commit timestamp*
*License: CC BY-SA 4.0 — Fork to explore alternatives, challenge via issues*


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Concept Index — FractaVolta](research/concepts.md)
- [Corpus Status — FractaVolta](research/corpus-status.md)
- [Research Index — FractaVolta](research/index.md)

<!-- END_AUTO: backlinks -->
