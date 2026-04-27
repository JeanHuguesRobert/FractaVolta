# Electricity in Containers

## A Note on Store-and-Forward Energy Logistics

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani — C.O.R.S.I.C.A.

1 cours Paoli, F-20250 Corte. jhr@baronsmariani.org institutmariani@gmail.com

Working Paper — April 2026

*Part of the FractaVolta & Mare Nostrum research program.*
[github.com/JeanHuguesRobert/FractaVolta](github.com/JeanHuguesRobert/FractaVolta)
[github.com/JeanHuguesRobert/marenostrum](github.com/JeanHuguesRobert/marenostrum)

*Cross-reference: Robert & Valdes (2026), "Constellia: A Fractal Architecture for Energy,
Food, and Digital Sovereignty in Island Territories."
[github.com/JeanHuguesRobert/marenostrum/blob/main/constellia.md](github.com/JeanHuguesRobert/marenostrum/blob/main/constellia.md).
---

## Working Status Note

This is an exploratory conceptual note, inviting critique rather than asserting a completed theory. It is offered as a working paper in the spirit of the FractaVolta research program: physical systems are richer than their standard descriptions, and that richness has infrastructure consequences.

---

## Abstract

Electricity is conventionally conceived as a continuous flow transmitted through fixed conductors. This paper argues that this ontology is incomplete.

As electrification expands across mobility, heating, and digital infrastructure, a complementary possibility emerges: electricity may also be treated as a transportable stock — stored in modular containers, moved across space by ordinary logistics, and discharged at point of need. Electric vehicles, battery trailers, and containerised battery systems already instantiate this model at commercial scale. Yet the theoretical and regulatory infrastructure appropriate to this modality has not been developed.

This paper proposes a conceptual framework for **containerised electricity** and the notion of **store-and-forward energy logistics**, drawing cautious analogies with buffering and packetised communication architectures. It argues that this perspective may illuminate neglected pathways for resilience, distributed flexibility, and reduced marginal pressure on conventional network reinforcement — and that the FractaVolta distributed inference architecture provides a natural routing and management layer for mobile energy assets.

The paper is positioned as the theoretical substrate for the energy storage and mobility choices made in the Constellia architecture (Robert & Valdes, 2026), in which V2G fleets, mobile battery containers, and Power-to-X reserves constitute the resilience and arbitrage layer of a Mediterranean distributed energy system.

---

## 1. Introduction

Modern electrical systems are built upon an implicit ontological assumption:

**electricity moves through wires.**

Even decentralised energy discourse — smart grids, distributed generation, demand response, storage — largely preserves this premise. Storage is discussed as a way to *temporally* buffer flows that still move through conductors; distributed generation as a way to relocate the *source* of flows that still move through conductors.

Yet electrification may be destabilising this assumption from below.

Electric vehicles carry batteries of 40–100+ kWh across road networks. Long-haul electric trucks carry 600–900 kWh. Containerised battery energy storage systems (BESS) of 2–8 MWh fit in a standard 20- or 40-foot shipping container and can be moved by flatbed truck, rail, or ship. Swappable battery systems for two-wheelers and light vehicles are deployed at scale in China, Taiwan, and growing markets globally.

These systems are typically discussed as devices — tools for solving specific charging or grid problems. Here they are viewed differently: as elements of an emerging **infrastructure layer** for electricity, one that is logistical rather than conductive in character.

This is not a claim that wired grids become obsolete. It is a claim that electrical infrastructure may be architecturally richer than currently assumed — and that the missing layer has consequences for resilience design, regulatory frameworks, and territorial energy sovereignty.

---

## 2. Electricity as Flow and as Container

Historically, electricity has been treated as an instantaneous flux — it cannot be stored in the wire, must be consumed at the moment of production, and moves at a speed that makes spatial buffering seem paradoxical. This is not wrong; it is a description of how most electricity systems currently function.

This paper proposes a complementary ontology by distinguishing two infrastructural modalities:

### Flow Electricity

Transport through conductive networks. The dominant modality. Requires simultaneous physical connection between source and sink. Governed by voltage, impedance, and frequency. Managed by grid operators through real-time balancing.

### Containerised Electricity

Transport through movable stored energy units. The emerging modality. Decouples production from consumption in both *time* and *space*. Requires no continuous physical connection. Managed by logistics operators through scheduling, routing, and inventory.

Both modalities convert electrical energy into useful work at the point of consumption. They differ in the physical medium of transport and in the temporal structure they impose on supply chains.

The distinction is not merely theoretical. It has practical consequences for how infrastructure is designed, regulated, and governed. A world in which a significant fraction of electricity moves through logistics networks rather than conductor networks requires different planning tools, different regulatory regimes, and different governance structures than a world in which all electricity flows through wires.

---

## 3. Store-and-Forward Power

The most illuminating conceptual analogy comes from communication systems.

The circuit-switched telephone network — the dominant telecommunications paradigm until the late twentieth century — assumed continuous, dedicated physical connections between communicating parties. End-to-end paths had to be established and maintained for the duration of a call. The capacity was dedicated; if unused, it was wasted; if the path broke, the connection failed.

Packet-switched networks — pioneered in the ARPANET project and formalised by Baran (1964) and Davies (1965) — introduced a fundamentally different architecture: **store-and-forward**. Information is broken into packets, each buffered at intermediate nodes, routed opportunistically across available paths, and reassembled at the destination. No end-to-end connection is required; packets may take different physical routes; failure of any node redirects traffic rather than dropping it.

The analogy with electricity is imperfect — energy is subject to thermodynamic constraints that information is not — but it is structurally illuminating.

**Flow electricity** is circuit-switched: a continuous, dedicated physical path must be maintained between generator and load. If the path breaks, the power is lost. If the path is unused, the capacity is wasted.

**Containerised electricity** is store-and-forward: energy is accumulated at a source node, physically transported through available logistics infrastructure, and discharged at a destination node. The source and destination need not be simultaneously connected. Failure of a transport route can be compensated by alternative logistics paths.

Under this framing, a diesel generator driving a truck carrying a fully-charged containerised BESS to a remote site is performing a store-and-forward energy delivery — exactly as a postal relay carried a physical message across a circuit that had no wire. And an EV fleet operating V2G protocols, charging during off-peak hours and discharging into buildings or local grids during peak demand, is performing distributed energy buffering — exactly as a CDN cache absorbs upstream traffic to reduce backbone congestion.

In an ironic sense, this realises a practical form of wireless power transmission — not through resonant electromagnetic fields as Tesla envisioned, but through logistics. The physics are mundane; the infrastructure consequence is not.

---

## 4. Fractal Form Factors

A striking property of containerised electricity is **scale recursion**: the pattern appears naturally across at least five orders of magnitude, from personal devices to regional infrastructure.

| Scale | Example | Typical capacity | Mobility mode |
|---|---|---|---|
| Personal | Portable power station (EcoFlow, Jackery) | 1–3 kWh | Hand-carried |
| Household | Home battery + swap system | 5–30 kWh | Manual exchange |
| Vehicle — light | BEV battery (Tesla Model 3, BYD Atto) | 60–100 kWh | Road |
| Vehicle — heavy | Electric truck (Tesla Semi, BYD T9) | 600–900 kWh | Road |
| Neighbourhood | Mobile BESS trailer (20-foot container) | 1–2 MWh | Flatbed truck |
| District | Containerised BESS (40-foot) | 4–8 MWh | Truck / rail / ship |
| Regional | Mobile storage fleet (10–50 units) | 40–400 MWh | Fleet operations |
| Geographic | Pumped hydro (STEP) | 1–100+ GWh | Gravity (fixed) |

The last row is notable: pumped hydro, while spatially fixed, is economically equivalent to containerised electricity at the geographic scale — it decouples the time of generation from the time of consumption, and the "container" is a reservoir of water at elevation. Its inclusion in the fractal suggests that the store-and-forward logic extends further than the mobile instances alone.

This scaling behaviour suggests that containerised electricity is not a collection of isolated technical artefacts but a **latent fractal infrastructure**: the same logical pattern — accumulate, transport, discharge — replicated across multiple physical instantiations at different scales.

Whether this fractal structure is a design principle worth pursuing deliberately, or merely a pattern that happens to recur across independently-developed technologies, is an open question and one of the motivating puzzles of this paper.

---

## 5. Buffers, Caches, and Resilience

Distributed computing provides a second useful family of analogies.

**Buffers** absorb intermittent flows: a buffer at the input of a processing node prevents data loss when production temporarily exceeds consumption. The energy equivalent is a battery absorbing excess solar generation during midday peak irradiance, preventing curtailment.

**Caches** reduce backbone stress: a content delivery network caches popular content at edge nodes, serving most requests locally without traversing the long-haul backbone. The energy equivalent is a neighbourhood BESS charged during off-peak periods and discharged locally during peak demand, reducing peak load on the distribution transformer and potentially the transmission line.

**Graceful degradation** means that failure of nodes reduces performance proportionally rather than catastrophically. Baran (1964) showed that distributed mesh networks tolerate 30–50% node destruction with proportional capacity reduction, while centralised hub-and-spoke networks fail catastrophically above much lower node-loss thresholds. The Constellia/Stella network applies this principle directly to energy-compute infrastructure: each of the 60 nodes is autonomous; loss of any subset reduces capacity proportionally.

The same principle applied to containerised electricity logistics: if ten mobile BESS units are available in a territory, destruction or failure of three reduces mobile storage capacity by 30%, not zero. If electricity could only move through a single transmission line, destruction of that line reduces capacity to zero.

This is not an argument against centralised infrastructure. High-voltage transmission lines are efficient for moving large quantities of energy over long distances, and no logistics system competes with them on that dimension. It is an argument for the *layered* resilience that comes from combining conductive and containerised modalities: the conductor layer handles bulk flows efficiently; the containerised layer absorbs failure modes that the conductor layer cannot.

---

## 6. Economics of Containerised Electricity

The economic case for containerised electricity depends on the comparison between the *levelised cost of energy transport via conductors* and the *levelised cost of energy transport via logistics*. This comparison varies enormously across contexts.

### 6.1 When Conductors Win

Conductors have near-zero marginal transport cost once installed. A 400 kV high-voltage line can transport GWh at a cost of a few euros per MWh over hundreds of kilometres. At this scale, no logistics system is competitive.

For bulk, long-distance, continuous transport of large energy quantities, conductors dominate and will continue to do so.

### 6.2 When Logistics Compete

The containerised logistics layer becomes economically competitive under several specific conditions:

**Last-mile delivery.** The cost of grid reinforcement to serve a single additional customer with high-power demand (e.g., a fast EV charging station in a rural area) may exceed €100,000–500,000 in grid extension, transformer upgrades, and permitting delays. A mobile BESS of 500 kWh–2 MWh, trucked to the site for charging events, may serve the same function at a fraction of the capital cost, particularly during the early period of demand growth before grid investment is warranted.

**Temporary or event-based demand.** Construction sites, outdoor events, disaster response operations, and temporary installations generate high-power demand in locations without adequate grid connection. Mobile BESS units already serve this market commercially (Aggreko, Sunbelt Rentals). The containerised model is not hypothetical here; it is deployed.

**Island or isolated territories.** In territories where grid connection to the mainland is expensive or absent, containerised electricity via ship can supplement or replace undersea cable where the cable would be prohibitively costly. The "fuel ferry" concept — a vessel carrying fully-charged containerised BESS from a solar-rich mainland to a remote island — is already technically feasible with current battery energy densities.

**Arbitrage between price zones.** Where electricity prices vary significantly across time (e.g., day/night spot price spreads of €100–200/MWh) or across geographic zones with limited interconnection, the round-trip economics of charge-transport-discharge can be positive. The constraint is that road transport of a 2 MWh container costs approximately €150–300 for a 100 km round trip, implying a breakeven spread of €75–150/MWh — achievable in high-volatility markets during renewable intermittency events.

**Resilience value beyond cost.** Economic cost alone may understate the case in critical infrastructure contexts, where the value of maintaining service continuity during grid failure — for hospitals, data centres, emergency services — may greatly exceed the transport cost.

### 6.3 The V2G Fleet as Economic Proof-of-Concept

Vehicle-to-Grid (V2G) technology is the most developed instantiation of containerised electricity economics at scale. An electric vehicle battery charges when electricity is cheap and available, and discharges into the grid (or building) when electricity is expensive or unavailable. The vehicle is performing spatial logistics (it moves its battery from charging point to discharge point as part of its ordinary operational cycle) and temporal arbitrage (it decouples purchase from sale of electricity by hours or days).

Commercial V2G deployments are now operating in the Netherlands (Renault Megane E-Tech, EVN), the UK (Nissan Leaf, Octopus Energy), and Denmark. The economic value captured per vehicle per year in grid services ranges from €300–1,500 depending on market design and battery utilisation. A fleet of 2,500 trucks, each carrying 800 kWh, represents 2 GWh of mobile storage — roughly equivalent to the output of a 200 MW gas peaker plant for 10 hours — at a capital cost that is already sunk into the vehicle fleet.

This is not a marginal economic proposition. It is a reclassification of existing assets.

---

## 7. V2G as Proof-of-Concept Infrastructure

Vehicle-to-Grid is conventionally discussed as a grid services technology. This paper reframes it as the first large-scale deployment of containerised electricity infrastructure.

The key insight: an electric vehicle fleet does not merely *consume* electricity. It *carries* electricity as cargo, and the cargo can be discharged at any point along its route where a compatible interface exists.

This means that wherever a fleet of electric vehicles operates — whether cars, vans, buses, or trucks — a distributed mobile energy storage system exists, managed by the fleet's operational schedule. The fleet operator becomes, in effect, a logistics operator for electricity.

The infrastructure implications are significant:

**The charging point is not the only relevant interface.** Any point along a vehicle route where a V2G-capable inverter is installed becomes a potential discharge point. A truck delivering goods to a remote site can simultaneously deliver electricity to that site's local storage, charging a neighbourhood BESS from its on-board battery during the unloading period.

**Fleet optimisation and energy optimisation merge.** The route planning problem for an electric fleet, taking into account V2G opportunities, becomes structurally identical to a logistics optimisation problem with a two-commodity flow (goods and electricity). The FractaVolta distributed inference architecture is designed precisely for this class of problem: routing under uncertainty, with distributed assets and opportunistic connectivity.

**Island territories as natural testbeds.** Corsica has approximately 10,000 registered commercial vehicles. If 2,000 of these were heavy electric with V2G capability and 800 kWh batteries, the mobile storage capacity would be 1.6 GWh — comparable to 3–4 hours of peak island consumption. The fleet would be managed not by a central dispatcher but by a distributed inference system tracking vehicle positions, battery states, and energy prices in real time.

---

## 8. Regulatory Gaps

The regulatory frameworks governing electricity — almost universally designed around the flow modality — do not account for the containerised modality. This creates specific gaps worth identifying:

**Metering and settlement.** Net metering rules assume that electricity moves bidirectionally through a fixed meter at a fixed location. When electricity is carried physically to a location and discharged, it does not appear in any meter. The transaction is invisible to the system operator and to settlement systems.

**V2G billing.** A vehicle discharging into the grid is performing a wholesale electricity sale. Most jurisdictions require a licensed entity to perform such sales. This creates a regulatory barrier for individual vehicle owners and small fleet operators. Regulatory sandboxes for V2G exist in several EU member states (Netherlands, Germany, France) but are not universal.

**Transport-as-energy-service classification.** A truck carrying a charged BESS to a construction site and discharging it is performing an energy delivery service. Whether this constitutes electricity supply (regulated, requiring a licence) or logistics (unregulated) varies by jurisdiction and is frequently unresolved.

**Mobile asset tracking for grid accounting.** System operators require visibility into connected generation and storage to balance the grid. Mobile assets that appear and disappear at different grid connection points create an accounting challenge. The FractaVolta probabilistic asset tracking layer offers a technical solution; the regulatory framework for using such tracking data in grid accounting does not exist.

These gaps are not arguments against containerised electricity. They are arguments that the regulatory infrastructure is lagging behind the physical infrastructure. The standard pattern in infrastructure development.

---

## 9. Connection to Distributed Inference: The FractaVolta Layer

The FractaVolta framework, of which this paper is a part, defines a distributed infrastructure for transforming physical reality into actionable probabilistic inference. Its core principle:

> Physical systems do not need to be fully measured to be understood. They can be inferred from weak signals, motion, and distributed observation.

This principle applies directly to containerised electricity logistics.

A fleet of mobile energy assets — EVs, battery trailers, containerised BESS — is a physical system that cannot be centrally managed at scale without prohibitive communication and computation overhead. But it can be *inferred*: vehicle positions are known with varying precision through GPS and cellular signals; battery states can be estimated from charging patterns and motion data; discharge availability can be predicted from fleet schedules.

The FractaVolta architecture treats this as a standard photon-to-inference problem: distributed weak signals (GPS pings, V2G handshakes, charging session data) are aggregated through distributed nodes, fused into probabilistic state estimates of the mobile energy asset fleet, and used to generate routing recommendations that optimise energy delivery, grid services, and logistics simultaneously.

This creates a natural pairing: the **physical layer** of containerised electricity logistics (vehicles, batteries, inverters) managed by the **inference layer** of FractaVolta (probabilistic tracking, distributed routing, opportunistic V2G dispatch). Neither layer is complete without the other. Mobile energy assets without intelligent routing are logistically inefficient. Distributed inference without mobile energy assets to manage is computation in search of a problem.

The combination defines a new infrastructure category: **intelligent mobile energy logistics** — a convergence of energy systems, logistics, and distributed computing that no existing regulatory or planning framework fully addresses.

---

## 10. Mediterranean Application and Corpus Connection

The Constellia architecture (Robert & Valdes, 2026) provides the most detailed existing instantiation of the ideas developed in this paper. Its energy storage and resilience layer includes:

| Layer | Form | Capacity | Timescale | Role in Constellia |
|---|---|---|---|---|
| Stationary BESS | Li-ion at node | 100–500 MWh | Hours | Primary diurnal buffer |
| V2G fleet | Heavy trucks, 800 kWh | 2 GWh (2,500 units) | Days | Demand response + emergency |
| Mobile BESS | 20-ft containers, 2 MWh | 40–200 MWh (20–100 units) | Days–weeks | Island-to-island transfer, disaster response |
| Power-to-X (e-diesel) | Chemical store | 30 days reserve | Weeks–months | Long-duration resilience, SAF export |
| STEP (pumped hydro) | Gravitational | 1–10 GWh | Hours–days | Frequency regulation + seasonal |

Each of these is a form of containerised electricity at a different scale and timescale, operating on the store-and-forward principle. The fractal structure of the form-factor table in Section 4 is not abstract in the Constellia context — it is the deliberate design choice of a multi-scale resilience architecture.

The economic logic follows from Section 6. In a Mediterranean island context:

- Grid connection to the mainland (Corsica–France submarine cable) costs approximately €1–2 billion per GW of capacity. Mobile BESS transfer via ship at low prices per kWh is competitive for peak shaving and emergency backup at scales below grid reinforcement thresholds.
- The V2G fleet contributes to frequency regulation services currently imported through the undersea cable, reducing the cable's peak loading.
- Power-to-X e-diesel serves as the longest-duration "container" — energy stored in chemical form, transportable by any tanker, dischargeable through any diesel generator, and therefore fully fungible with the global fuel logistics network.

The containerised electricity framework thus provides the theoretical justification for what Constellia treats as practical engineering choices. The two papers are mutually reinforcing: Constellia provides the numbers; this paper provides the conceptual framework that explains why the architecture takes the form it does.

---

## 11. Research Questions

This note raises more questions than it answers. Among those deserving investigation:

**Economic thresholds:**
- At what distance and demand density does mobile BESS logistics become competitive with grid reinforcement for last-mile electrification?
- What is the breakeven V2G spread (charge price minus discharge price) required to cover the logistics cost of deliberate energy transport by vehicle?
- How does the economics change at the scale of a fleet vs. an individual vehicle?

**Systems modelling:**
- How should containerised electricity be integrated into power systems models that currently only represent conductive flows?
- What are the appropriate planning reserve rules for a grid that includes a significant mobile storage component?
- Can the store-and-forward analogy be formalised sufficiently to generate quantitative resilience metrics?

**Distributed inference:**
- What data requirements does the FractaVolta routing layer need to perform reliable real-time routing of mobile energy assets?
- How does inference quality scale with fleet size and node density?
- What are the privacy and security implications of continuous position and battery-state tracking of a mobile energy fleet?

**Regulation:**
- What regulatory changes are required to allow mobile energy assets to participate in wholesale markets?
- How should system operators account for mobile storage in grid balancing?
- What liability regime is appropriate when a V2G discharge contributes to grid instability?

**Territorial sovereignty:**
- Under what conditions can containerised electricity logistics reduce the energy import dependency of island territories below what wired grid connection alone could achieve?
- How does the resilience value of a mobile energy fleet change as a function of territory isolation (response time for external emergency supply)?

These questions appear underexplored in the current literature on energy systems, transport, and distributed computing.

---

## 12. Conclusion

The energy transition is conventionally framed as a transition in generation (from fossil to renewable) and in transmission (from centralised to distributed, with reinforced grids). This paper argues that a third dimension deserves attention: a transition in the **ontology of electricity transport** itself — from exclusively conductive to partially logistical.

Electricity may not only flow. It may be stored, moved, buffered, routed, and traded through logistics infrastructure. This is not a future possibility; it is an emerging present — in V2G fleets, in mobile battery trailers, in containerised BESS deployments, in swappable battery systems for two-wheelers.

What is missing is the conceptual framework that treats this as an infrastructure category worthy of deliberate design — rather than a collection of device-level technical solutions. This paper proposes that framework, and situates it within two research programs:

- **FractaVolta**, which provides the distributed inference layer for routing mobile energy assets;
- **Constellia / MareNostrum**, which provides the physical and institutional architecture within which containerised electricity operates as a resilience and sovereignty layer for Mediterranean island territories.

The theoretical substrate is modest: electricity has two transport modalities, not one. The infrastructure consequences may be substantial.

---

## Keywords

Containerised electricity; store-and-forward power; vehicle-to-grid; V2G; distributed energy systems; mobile battery storage; BESS; electric vehicles; resilience; energy logistics; infrastructure theory; FractaVolta; Mediterranean energy sovereignty; agrivoltaics; fractal infrastructure.

---

## References

Baran, P. (1964). On distributed communications networks. RAND Corporation Memorandum RM-3420-PR, Santa Monica, CA.

Davies, D. W. (1965). Proposal for a digital communication network. Internal note, National Physical Laboratory, Teddington, UK.

Jacobson, M. Z., Delucchi, M. A., et al. (2017). 100% clean and renewable wind, water, and sunlight all-sector energy roadmaps for 139 countries of the world. *Joule* 1(1), 108–121.

Kempton, W., & Tomić, J. (2005). Vehicle-to-grid power fundamentals: Calculating capacity and net revenue. *Journal of Power Sources* 144(1), 268–279.

Noel, L., Zarazua de Rubens, G., Kester, J., Sovacool, B. K. (2019). *Vehicle-to-Grid: A Sociotechnical Transition Beyond Electric Vehicles*. Palgrave Macmillan.

OREGES. (2023). *Bilan énergétique de la Corse 2022*. Observatoire Régional de l'Énergie, des Gaz à effet de serre et de l'Air de Corse, Ajaccio.

Robert, J.-H. N. (2026). FractaVolta: Distributed infrastructure for physical flow, sensing, and probabilistic inference. [github.com/JeanHuguesRobert/FractaVolta/blob/main/fractavolta_paper.md](github.com/JeanHuguesRobert/FractaVolta/blob/main/fractavolta_paper.md)

Robert, J.-H. N., & Valdes, G. (2026). Constellia: A fractal architecture for energy, food, and digital sovereignty in island territories. *Proceedings of ICOME'26* (submitted, not accepted yet). Université de Corse Pasquale Paoli, Corte. [github.com/JeanHuguesRobert/marenostrum/blob/main/constellia.md](github.com/JeanHuguesRobert/marenostrum/blob/main/constellia.md).

Sioshansi, R., Denholm, P., & Jenkin, T. (2012). Market and policy barriers to deployment of energy storage. *Economics of Energy & Environmental Policy* 1(2), 47–63.

*(Full BibTeX to be added before release.)*

---

*© 2026 Jean Hugues Noël Robert, baron Mariani — Institut Mariani / C.O.R.S.I.C.A.*
*Published under CC0-1.0 .*
*Repository: https://github.com/JeanHuguesRobert/FractaVolta*
*Contact: jhr@baronsmariani.org*
