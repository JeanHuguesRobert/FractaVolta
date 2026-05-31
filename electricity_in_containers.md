---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/electricity_in_containers.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-05-26
title: "Electricity in Containers"
date: "2026-04-27"
status: "working-paper — auto-filled (frontmatter cleanup)"
---
# Electricity in Containers

**Store-and-Forward Energy Logistics: A Complementary Infrastructure Layer**

*Jean Hugues Noël Robert, baron Mariani*

*Institut Mariani — C.O.R.S.I.C.A. — Corte, Corsica*  

*Working Paper — MareNostrum Working Paper Series — April 2026*

> Living document. Priority established by commit timestamp.  
> Challenge via issues. Fork to explore alternatives.

---

## The Core Idea

Electricity is conventionally conceived as a continuous flow transmitted through fixed conductors. This ontology is incomplete.

Wired grids presuppose permanent infrastructure, network operator authorization, regulated tariffing, and a physical topology that is expensive to build, slow to authorize, and impossible to reconfigure. These presuppositions are invisible when the grid works. They become visible when it does not — or when the regulatory and economic constraints it carries are themselves the obstacle.

This paper proposes a complementary modality: **electricity as a transportable stock**, moved in modular containers across multiple scales. Not instead of grids — alongside them, in the spaces and use cases where grids are too costly, too slow, too regulated, or structurally absent.

The key insight is not technical. It is **regulatory and commercial**: transporting a physical container of stored electrical energy is a logistics operation, not a network operation. The applicable legal framework is contract law and transport law, not energy network regulation. This distinction changes everything about what business models are possible.

---

## 1. From Flow to Container: The Ontological Shift

Standard energy economics treats electricity as a commodity flow: produced at a source, transmitted through a network, consumed at a destination. The value of a kilowatt-hour is determined by its position in this flow — time of production, location, and marginal cost.

Containerized electricity breaks this ontology. A charged battery is not a flow — it is a stock. It has a physical location, a transport cost, and a delivery schedule. Its value depends not on network position but on the contract under which it is delivered.

This distinction enables a different commercial structure entirely:

> **Selling containerized electricity as a service commitment — not as a commodity — removes the regulated seller-of-electricity status and replaces it with a service provider status.**

The client does not buy kilowatt-hours. They buy a guaranteed outcome: thermal comfort, lighting availability, vehicle charge readiness, process continuity. The container is the vehicle of delivery, invisible to the contract object.

This is not a legal trick. It is a genuine reframing of what is being sold — one that aligns commercial incentives correctly. A service provider whose contract specifies "indoor temperature between 19°C and 22°C" has an economic incentive to optimize the client's energy efficiency, install sensors, reduce waste, and shift loads intelligently. A commodity seller has no such incentive: they profit from consumption, not from its optimization.

---

## 2. The Store-and-Forward Analogy

Packet-switched networks introduced store-and-forward logic: information is buffered at a node, then forwarded when the next link is available. This architecture made the internet resilient to partial failures and enabled asynchronous communication across heterogeneous networks.

The analogy to containerized electricity is structural, not decorative:

| Packet switching | Store-and-forward power |
|-----------------|------------------------|
| Packet buffered at router | Energy stored in container |
| Forwarded when link available | Delivered when vehicle available |
| Routing adapts to congestion | Logistics adapts to grid stress |
| No dedicated circuit required | No dedicated wire required |
| Asynchronous, best-effort or QoS | Service contract specifies guarantee |

The analogy has limits: electrons cannot be error-corrected, and energy storage has self-discharge losses that data does not. But the structural logic holds: store-and-forward power enables **asynchronous energy logistics** that complements synchronous grid distribution.

This is also, in an ironic sense, the practical realization of wireless power transmission — not through resonant fields as Nikola Tesla imagined, but through logistics.

---

## 3. Fractal Form Factors

Containerized electricity appears naturally across multiple scales. This is not a coincidence — it reflects the fact that the store-and-forward architecture is scale-invariant, much like the memory hierarchy in computing.

| Scale | Container form | Typical capacity | Mobility |
|-------|---------------|-----------------|---------|
| Personal | Portable battery pack | 10–100 Wh | Hand-carried |
| Household | Modular home battery | 5–20 kWh | Trolley/van |
| Vehicle | EV battery (V2H/V2G) | 40–100 kWh | Self-propelled |
| Neighborhood | Swappable battery module | 100–500 kWh | Light truck |
| District | Containerized storage unit | 500 kWh–5 MWh | Heavy truck |
| Regional | Mobile battery plant | 5–50 MWh | Rail/barge |

Each scale level has different economics, different logistics constraints, and different regulatory exposure. The personal and vehicle scales are already widespread; the neighborhood and district scales are emerging; the regional scale is demonstrated but not yet deployed at volume.

The fractal property: the same store-and-forward logic operates at every scale. A service provider can enter at any scale, demonstrate the model, and extend upward or downward as density and economics allow.

---

## 4. Use Case Taxonomy

The following taxonomy organizes use cases by maturity and by the nature of the gap that containerized electricity fills. It is deliberately non-exhaustive — the point is to identify the structural categories, not to list every possible application.

### 4.1 Off-Grid Customers — High Maturity, High Motivation

**The case**: a customer who chooses to disconnect from the wired grid, or who is located where connection is prohibitively expensive, has already internalized the trade-off. They are not a passive consumer — they are actively managing their energy relationship. This makes them the natural early adopter of a service model.

**The gap filled**: permanent grid connection requires authorization, infrastructure investment, network tariffs, and regulatory status as a connected customer. Off-grid operation with containerized resupply requires none of these. The customer receives a service guarantee (comfort, lighting, appliance availability) and pays a subscription. The provider optimizes delivery logistics and on-site management.

**Maturity**: high. Solar + battery off-grid systems are well-established. The innovation is the service contract structure and the logistics resupply model, not the hardware.

**Density requirement**: low — even a single isolated customer can be served, if logistics cost is priced into the contract.

### 4.2 Electric Vehicle Owners — High Maturity, Structurally Underexploited

**The case**: a typical EV battery contains 60–100 kWh. A typical household consumes 10–15 kWh/day. A vehicle parked 20+ hours per day is a large, underutilized storage asset sitting in the customer's driveway.

**The gap filled**: V2H (Vehicle to Home) and V2G (Vehicle to Grid) technology exists and is commercially available on several platforms (Nissan Leaf, Hyundai Ioniq 5/6, Kia EV6, some Mitsubishi models). The barrier is not hardware — it is the commercial and regulatory model. Current electricity tariffs do not compensate the vehicle owner for the storage service they provide to the grid or their own home. A service contract model changes this: the provider manages the vehicle battery as part of the client's energy system, guarantees the outcome (home comfort + vehicle departure charge), and captures the optimization value.

**The gap filled (regulatory)**: the provider does not sell electricity from the vehicle to the grid — they manage the client's energy system as a service. The vehicle battery is an asset in the service contract, not a generation source.

**Maturity**: medium-high. The hardware is ready; the commercial model is nascent. Several European startups are attempting V2G as a service; none has yet combined it with full off-grid or off-network service positioning.

**Density requirement**: medium — a cluster of 20–50 VE owners in a geographic area creates sufficient aggregate storage for meaningful logistics optimization.

### 4.3 Rural and Peri-Urban Households — Medium Maturity

**The case**: rural households with grid connection but poor power quality (voltage fluctuations, frequent outages, high network tariffs for low consumption) benefit from a local storage buffer that smooths the grid supply and enables self-consumption from rooftop solar.

**The gap filled**: unlike off-grid customers, these clients do not want to disconnect — they want resilience that the grid cannot provide at reasonable cost. A containerized buffer, delivered and managed as a service, provides this without requiring the client to own or maintain any hardware.

**Maturity**: medium. The use case is well-understood; the service model is less developed. The regulatory positioning (service, not electricity resale) is the key enabler.

**Density requirement**: medium — route-based logistics require sufficient client density to be economically viable. Corsican village clusters are a plausible initial geography.

### 4.4 Temporary and Seasonal Installations — Medium Maturity

**The case**: construction sites, seasonal agricultural operations, outdoor events, temporary medical facilities, disaster relief operations. These require reliable power for a defined period, after which the installation is dismantled.

**The gap filled**: temporary grid connection is expensive and slow to authorize. Diesel generators are the current default — costly, noisy, polluting, and logistically complex (fuel delivery, maintenance). A containerized battery service provides clean, quiet, low-maintenance power with a predictable service cost and no permanent infrastructure.

**Maturity**: medium. Several companies offer battery rental for events and construction. The innovation in the service model is the outcome guarantee (guaranteed power availability for defined equipment loads) rather than simple hardware rental.

**Density requirement**: low per site, but geographic concentration of sites reduces logistics cost.

### 4.5 Islands and Isolated Communities — Medium Maturity, High Strategic Value

**The case**: islands and remote communities with undersized or unreliable grid connections that cannot justify the investment in cable reinforcement. The Mediterranean context (Corsica, Sardinia, Sicily) makes this structurally relevant to the MareNostrum framework.

**The gap filled**: mobile battery fleets can provide peak-shaving and backup capacity without requiring cable upgrades. At sufficient scale, they enable local solar generation to reach higher penetration by absorbing surplus that would otherwise be curtailed.

**Maturity**: medium. Several Mediterranean islands have experimented with mobile storage as grid support. The service model layer is underdeveloped.

**Strategic value**: high — this is where containerized electricity connects directly to the MareNostrum energy governance model. Mobile storage units are traceable assets whose energy provenance can be certified (see [`safe_compute_exergy.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/safe_compute_exergy.md)). A battery charged from certified Corsican solar, delivered to a household, creates a traceable provenance chain for the service rendered.

### 4.6 Industrial and Commercial Demand Response — Lower Maturity for Service Model

**The case**: industrial customers with large, flexible loads (refrigeration, HVAC, compressed air, electrochemical processes) can shift consumption in response to grid signals. Containerized storage enables this shift without requiring the customer to install permanent infrastructure.

**The gap filled**: demand response programs typically require the customer to manage the response themselves. A service model externalizes this management: the provider monitors grid signals and manages on-site storage, guaranteeing the customer's process continuity while optimizing grid interaction.

**Maturity**: lower for the service model specifically. Demand response as a concept is mature; combining it with containerized storage as a service is less developed.

### 4.7 Emerging and Speculative Cases

Several use cases are at lower maturity but structurally coherent with the model:

**Boat and marina supply**: leisure boats consume significant power at berth (hotel load). Shore power connections are standardized but expensive to install at new marinas. A containerized delivery model, with battery swap at berth, is logistically simpler.

**Mountain refuges and remote tourism**: alpine and maritime refuges with solar+battery systems that need seasonal resupply or winter backup. The service model (guaranteed lighting and heating through the season) replaces the current practice of diesel generator maintenance.

**Humanitarian and development contexts**: off-grid communities in developing regions where grid extension is decades away. The service model, adapted to local payment infrastructure (mobile money, cooperative subscription), provides a pathway to reliable electricity access without the grid timeline.

**Data center UPS as a service**: uninterruptible power for edge computing nodes where grid reliability is insufficient for Sovereign-tier CXU certification. The containerized battery provides the physical backup that the certification requires — and its provenance chain contributes to η_traceability.

---

## 5. The Service Model as Regulatory Strategy

The commercial and regulatory framing deserves explicit statement, because it is the key enabler for all the use cases above.

In France and most EU jurisdictions, selling electricity requires authorization as a supplier, subjects the seller to network tariffs (TURPE in France), and creates obligations under the energy code that are designed for large, established operators. These requirements effectively exclude small operators and novel business models.

Selling a **service whose delivery happens to involve energy** does not. A contract to maintain indoor temperature between 19°C and 22°C is a service contract governed by the French Code civil. The provider's obligation is the outcome; the means — including the energy used to achieve it — are the provider's operational concern, not the object of the contract.

This is not a regulatory loophole. It is the correct legal characterization of what is genuinely being sold. The distinction tracks a real economic difference: a commodity seller optimizes for volume (more kilowatt-hours sold = more revenue); a service provider optimizes for outcome efficiency (fewer kilowatt-hours needed = lower cost for the provider, same revenue). The incentive alignment is entirely different.

The analogy to settled practice: Butagaz and Total do not hold electricity supplier licenses. They deliver energy in containers (gas cylinders) under service contracts. The legal category is logistics and service, not network energy supply. Containerized electricity occupies the same legal space.

---

## 6. Connection to the MareNostrum Stack

Containerized electricity is not an isolated concept. It connects to the broader MareNostrum architecture at multiple points:

**FractaTera** ([`tera.md`](tera.md)): mobile battery containers are nodes in the FractaTera network. Their GPS trajectory, detected by vehicles and fixed infrastructure, provides the physical tracking layer. VIGILIA-type beacon detection can be applied to container tracking. The logistics network is the physical instantiation of the mobile node layer.

**Operational exergy** ([`MODEL.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/MODEL.md)): a container charged during surplus (R(t) = 0, w(t) = 1) and delivered during scarcity (R(t) > 0, w(t) > 1) performs a time-shift that directly increases operational exergy E. The container is a physical arbitrageur of temporal value.

**Safe Compute Exergy** ([`safe_compute_exergy.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/safe_compute_exergy.md)): a battery charged from certified Corsican solar, tracked through the logistics chain, and discharged into a compute node creates a provenance link in the τ-chain. The container's journey is a segment of the photon-to-inference chain. Its traceability contributes to η_traceability for the inference it ultimately powers.

**Traceable governance** ([`traceable_governance.md`](traceable_governance.md)): each container delivery is a signed trace event — charged at location X, delivered to location Y, discharged for service Z. The logistics register is an append-only record of energy provenance at the service level.

---

## 7. What Remains Speculative

The core logistical claim — that terrestrial delivery of containerized electricity can be economically viable for certain use cases — is not yet empirically validated at scale. The key unknowns:

**Break-even logistics density**: below what client concentration per route does the logistics cost exceed the value of the service premium? This varies by container scale, vehicle cost, and local geography. Corsica's combination of geographic concentration and isolation may be favorable; this requires quantification.

**Battery cycle economics**: battery containers have finite cycle life. The service pricing must recover the battery replacement cost over the contract period. At current battery costs (declining), the economics are improving; at 2020 costs, they were marginal for most use cases.

**Client acceptance of outcome contracts**: selling comfort rather than kilowatt-hours requires clients to trust the provider's measurement of the outcome. Sensor-based verification (indoor temperature logs, lighting availability records) makes this auditable — but client acceptance of remote monitoring varies.

**Regulatory evolution**: the service model framing is robust under current French and EU law, but regulatory bodies may reclassify containerized energy delivery as network operation if the scale becomes significant. The legal boundary should be monitored.

---

## 8. Research Questions

- Under what conditions does the logistics cost of container delivery become competitive with grid connection cost? What is the geographic and demographic profile of the viable service territory?
- How does battery cycle degradation interact with service contract duration and pricing? What is the minimum viable contract length for different container scales?
- Can V2H/V2G integration with a service contract model be structured to satisfy both the client's vehicle use requirements and the provider's energy management needs? What are the failure modes?
- What is the carbon accounting of containerized electricity delivery relative to grid supply, accounting for transport emissions? Under what conditions is the certified renewable premium sufficient to offset logistics emissions?
- How does the provenance chain for containerized electricity interact with existing renewable energy certificate (REC) and guarantee-of-origin (GO) frameworks in the EU?

---

*Related documents: [`tera.md`](tera.md) (mobile node architecture), [`MODEL.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/MODEL.md) (operational exergy), [`safe_compute_exergy.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/safe_compute_exergy.md) (provenance certification), [`traceable_governance.md`](traceable_governance.md) (logistics register).*  
*License: CC BY-SA 4.0 — Priority established by first commit timestamp.*


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Concept Index — FractaVolta](research/concepts.md)
- [Corpus Status — FractaVolta](research/corpus-status.md)
- [Research Index — FractaVolta](research/index.md)
- [FractaTera](tera.md)
- [FractaVolta traceable gouvernance](traceable_governance.md)

<!-- END_AUTO: backlinks -->
