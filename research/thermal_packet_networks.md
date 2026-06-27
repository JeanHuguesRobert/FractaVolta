---
title: "Thermal Packet Networks"
subtitle: "A Multi-Scale Store-and-Forward Architecture for Low-Exergy Heat and Cold Distribution"
description: "Working paper v0.2 defining Thermal Packet Networks as a multi-scale store-and-forward architecture in which heat and cold are stored, transported, addressed, exchanged, and delivered as discrete thermal packets."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
x-address: "1 cours Paoli, F-20250 Corte, Corsica, France"
x-email: "jhr@baronsmariani.org"
x-website: "https://fractavolta.com"
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/thermal_packet_networks.md
version: "0.2"
status: "working-paper"
date: "2026-05-22"
last_modified_at: "2026-05-22"
last_stamped_at: 2026-06-01
license: "CC BY-SA 4.0"
layout: default
tags:
  - thermal-packet-networks
  - fractavolta
  - fractanet
  - energy-packet-networks
  - heat-logistics
  - cold-storage
  - mobile-thermal-energy-storage
  - exergy
  - district-heating
  - low-temperature-heating
  - thermal-traffic-intensity
  - seconde-methode
x-keywords:
  - Thermal Packet Networks
  - mobile thermal energy storage
  - heat logistics
  - cold storage
  - Energy Packet Networks
  - packetized energy
  - exergy
  - district heating
  - low-temperature heating
  - waste heat recovery
  - thermal traffic intensity
  - Erlang
  - storage hierarchy
  - freshness
  - CXU
  - FractaVolta
  - Mariani Village
  - Seconde méthode
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
---

# Thermal Packet Networks

## A Multi-Scale Store-and-Forward Architecture for Low-Exergy Heat and Cold Distribution

---

## Abstract

Energy infrastructures are still largely designed around continuous flows: electricity through wires, heat through pipes, fuels through supply chains. While electrochemical storage has made distributed *electrical* packets familiar, thermal energy remains framed either as a local by-product, a buffering problem, or a continuous flow through fixed district heating and cooling networks. This paper proposes the concept of **Thermal Packet Networks (TPN)**: a multi-scale store-and-forward architecture in which heat and cold are stored, transported, addressed, exchanged, and delivered as discrete thermal packets.

The minimal packet is the insulated bottle. The same operational grammar — *charge, store, route, transfer, discharge, measure, reuse* — extends to domestic hot-water tanks, building thermal mass, neighborhood buffer tanks, mobile thermal containers, and territorial thermal logistics. The architecture is *complementary* to district heating, not a substitute for it: pipes remain optimal where thermal density, demand stability, and long-term utilization justify high fixed infrastructure costs.

The paper makes three contributions. First, it formalizes the thermal packet through a definition, a functional grammar, and a six-scale architecture. Second, it introduces service metrics — thermal traffic intensity (TTI), congestion elasticity, packet decay, and a **Thermal Compute eXergy Unit (CXU_th)** that extends the CXU framework of the MareNostrum project to thermal exergy chains. Third, it grounds the framework in two worked examples: the insulated bottle quantified as a minimal packet, and the Mariani Village portable air-conditioning packet as a deployable instance.

The proposal is positioned as a testable architectural hypothesis under the *Seconde méthode*: claims are versioned, distinguished by epistemic status, and offered for adversarial review.

---

## Keywords

Thermal Packet Networks; mobile thermal energy storage; heat logistics; cold storage; Energy Packet Networks; packetized energy; exergy; district heating; low-temperature heating; waste heat recovery; thermal traffic intensity; Erlang; storage hierarchy; freshness; CXU; FractaVolta; Mariani Village; Seconde méthode.

---

## 1. Introduction

### 1.1 The thermal share of final energy demand

Energy-transition discussion privileges electricity. This is understandable: electricity is versatile, increasingly renewable, and central to mobility, computation, and artificial intelligence. Yet a large share of final energy demand remains thermal: domestic hot water, space heating, industrial process heat, refrigeration, cooling, and comfort regulation account for roughly half of European final energy consumption [1].

Thermal needs are usually addressed through one of three dominant architectures:

1. **Local production** — boilers, heat pumps, solar thermal panels, electric resistance heating.
2. **Continuous thermal networks** — district heating or cooling with buried pipes.
3. **Stationary thermal storage** — local buffer between production and consumption.

A fourth architecture deserves explicit formalization: **packetized thermal distribution**.

### 1.2 Three architectures, one gap

The conventional district heating network is a **circuit-based infrastructure**: a continuous physical path is established between producers and consumers through pipes, pumps, and heat-transfer fluids. By contrast, a **Thermal Packet Network** treats heat and cold as discrete packets that can be charged, stored, moved, addressed, exchanged, and discharged.

The simplest instance is not a truck, a container, or an industrial device. It is an insulated bottle.

An insulated bottle stores a finite amount of heat or cold in a portable, identifiable container. It allows temporal delay, spatial displacement, and controlled discharge. It is to heat what a mobile phone battery is to electricity: a small packet of useful energy carried by a person.

From this primitive object, the same operational logic scales upward through six levels:

```text
insulated bottle
→ domestic hot-water tank
→ building thermal mass / low-temperature floor
→ neighborhood buffer tank
→ mobile thermal container
→ territorial thermal logistics
```

These objects are not merely similar by analogy. They share a functional grammar that can be formalized, measured, and integrated into energy systems planning.

### 1.3 Research gap and contribution

The literature on thermal energy storage is extensive. Mobile thermal energy storage (M-TES) has been comprehensively reviewed [2, 3], phase-change materials are well characterized [4], waste-heat recovery is the subject of recent policy reports [5], and the economics of district heating is mature [6]. Energy Packet Networks (EPN) have been proposed by Gelenbe for electrical energy [7, 8], and Packetized Energy Management has been developed under the ARPA-E NODES program [9, 10].

To our knowledge, however, no existing framework proposes:

1. a unified **multi-scale formalization** of heat and cold as discrete packets across the full range from insulated bottle to territorial logistics;
2. a service-metric layer — **thermal traffic intensity, congestion elasticity, packet decay** — drawn from teletraffic engineering and computer architecture and adapted to thermal physics;
3. an **exergy-aware service unit** (CXU_th) extending the Compute eXergy Unit framework of MareNostrum to the thermal substrate;
4. an explicit positioning of thermal packets as one of three physical substrates in a wider packet-energy program (alongside Energy Packet Networks for electricity and Packetized Gravity Networks for hydraulics [11]).

These four contributions define the scope of the present paper.

### 1.4 Methodological status

This paper is published as a working draft under the *Seconde méthode* [12]. Three framings follow.

First, claims are *versioned*. v0.1 was an intuitive exposition. v0.2 introduces formal definitions, service metrics, CXU_th, the Mariani Village worked example, and a claim manifest. Subsequent versions are expected.

Second, *objections are first-class contributions*. The repository at `github.com/JeanHuguesRobert/FractaVolta` accepts issues and pull requests. An unrefuted objection is itself a discovery.

Third, the *corpus is the evidence*. This paper does not claim authority on its own; it claims a place in a corpus of cross-referenced documents [11, 12, 13, 14, 15] whose internal consistency and external testability constitute the demonstration.

### 1.5 What this paper does not claim

Precision requires explicit non-claims.

**This paper does not claim** that thermal packets should replace district heating pipes. Where thermal density, demand stability, and long-term utilization justify the capital cost of buried infrastructure, pipes remain optimal. TPN is *complementary*.

**This paper does not claim** that heat behaves like information. Heat dissipates physically. Cold packets warm. A thermal packet is constrained by mass, volume, temperature, insulation, surface-to-volume ratio, and exergy quality in ways that data packets are not. The architectural analogies (cache, buffer, hot/cold data) are operational vocabulary, not physical identity.

**This paper does not claim** to solve the volumetric energy-density problem. A 1,000 L hot-water tank at ΔT = 50 °C stores roughly 58 kWh_th — two orders of magnitude below diesel. TPN does not compete on density. It competes on adequacy, modularity, and avoided infrastructure.

**This paper does not claim** the full theory of generalized packet networks. The general framework is developed separately [13]. The present paper enters the general theory through the particular case of heat and cold.

**This paper does not claim** that all thermal logistics is low-carbon. Vehicle emissions are a function of energy source, route, and utilization. The full life-cycle assessment is part of the research agenda (§13).

### 1.6 Two disclosures

**On the author's formation.** The author's training is in computer science. The computer scientist sees discrete state transitions everywhere. This may be a sensitivity that detects real architectural recurrences across substrates, or it may be a projection bias. The bias is declared. The reader weighs accordingly.

**On the author's interests.** FractaVolta and the Mariani Village project — both cited in this paper as instances — are projects in which the author holds direct commercial and institutional interests. The conflict is not hidden. The hypothesis stands or falls on independent scrutiny, not on the author's interests. The thermos as a worked example (§11.1) is offered precisely because it requires no commercial buy-in to evaluate.

---

## 2. From Circuit-Based to Packet-Based Thermal Systems

### 2.1 The circuit logic of district heating

District heating and cooling networks are powerful infrastructures when thermal density is high, demand is stable, and the capital cost of buried pipes is justified by long-term utilization [6]. They reduce local emissions, aggregate diverse heat sources, and can integrate renewable or recovered heat.

Pipe-based networks also carry structural constraints:

- high upfront capital expenditure;
- civil engineering disruption;
- fixed topology;
- vulnerability to underutilization;
- long payback periods;
- limited reversibility;
- difficulty serving dispersed or uncertain demand;
- strong dependence on thermal density along the route.

In network-theoretic terms, the pipe is a dedicated or semi-dedicated *circuit*. This is rational when the circuit is heavily used. It is less rational when demand is sparse, seasonal, uncertain, temporary, or geographically fragmented.

### 2.2 The packet logic

A Thermal Packet Network proposes a complementary model:

```text
source of heat or cold
→ thermal packet generation
→ storage / buffering
→ transport or local addressing
→ delivery / discharge
→ reuse / return / recharge
```

The key shift:

> Heat does not always need to travel through a pipe, just as electrical energy does not always need to travel through a wire.

This restates, for thermal systems, the move that Baran, Davies, and Kleinrock made for communications in the 1960s [16, 17, 18]: replace dedicated circuits with discrete, addressable, storable, routable units that share infrastructure opportunistically. The pattern recurs across the corpus: information [16], money [19], electricity [7, 8], gravitational potential [11], and habitat [14].

### 2.3 Domain of complementarity

Thermal packets do not displace district heating. They define a domain of complementarity:

- low-density settlements;
- rural or mountainous territories;
- islands and isolated systems (ZNI);
- temporary or construction sites;
- emergency heating or cooling;
- waste-heat sources too distant from demand to justify pipes;
- prefiguration of future heat networks;
- resilience backup for critical buildings;
- short-distance autonomous thermal shuttles;
- seasonal or intermittent thermal flows.

The central design question becomes:

> At which scale should thermal demand be served by continuous flows, and at which scale by discrete packets?

The answer is empirical and contextual. The conceptual contribution of TPN is to make the question askable.

---

## 3. Definition and Functional Grammar

### 3.1 Definition

A **thermal packet** is a finite amount of heat or cold stored in an identifiable medium and container, capable of being charged, stored, transported or locally addressed, discharged, measured, and reused for a specific thermal service.

A thermal packet has six necessary properties:

1. **bounded energy content** — a measurable quantity of thermal energy, typically in kWh_th or MWh_th;
2. **identifiable medium and container** — water, ice, phase-change material, sand, brick, salt, oil, or any thermal storage substrate held in a bounded enclosure;
3. **transferable interface** — a defined mode for charge and discharge (conductive, convective, radiative, or sanitary);
4. **addressability** — either physical mobility or stationary identification within a network;
5. **measurable state** — instantaneous energy content, temperature level, exergy quality, time-since-charge, and where applicable sanitary status and ownership;
6. **reusability** — the container, medium, and interface support cyclic operation.

### 3.2 Functional grammar

Thermal packets share a sequence:

```text
charge → store → route → transfer → discharge → measure → recover/reuse
```

This grammar applies at all scales. Table 1 illustrates.

**Table 1.** Functional grammar across thermal packet scales.

| Scale | Example | Charge | Store | Discharge |
|---|---|---|---|---|
| Object | insulated bottle | hot/cold liquid | vacuum-insulated container | drink, pour |
| Appliance | domestic hot-water tank | heat pump, solar, electricity | water tank | sanitary use |
| Building | low-temperature floor | low-grade source | building thermal mass | space heating |
| Cluster | neighborhood buffer | solar, heat pump, waste heat | collective tank | micro-network |
| Mobile | thermal tanker | source station | insulated tank | delivery port |
| Territorial | thermal container | industrial / renewable | containerized PCM | district node |

A packet is not merely a substance. It is an *operational unit*.

### 3.3 The insulated bottle as minimal worked example

The insulated bottle is conceptually important because it prevents the concept from being over-engineered.

A standard 1 L vacuum-insulated bottle filled with water at 90 °C, with ambient temperature at 20 °C and a typical 6 h cooling time-constant for high-quality models:

$$
E_0 = m \cdot c_p \cdot \Delta T = 1\,\text{kg} \cdot 4{,}186\,\text{J/kg·K} \cdot 70\,\text{K} \approx 293\,\text{kJ} \approx 81\,\text{Wh}_{th}
$$

Newtonian cooling gives, after 6 h:

$$
T(6\text{h}) = T_a + (T_0 - T_a) \cdot e^{-6/\tau}
$$

For τ = 8 h (high-quality bottle), T(6h) ≈ 53 °C — still usable for hot beverage or low-grade heat. For τ = 4 h (mediocre bottle), T(6h) ≈ 36 °C — no longer useful.

The thermos thus exhibits all defining properties of a thermal packet: bounded content (~81 Wh_th), measurable state (T(t)), known decay (τ), defined transfer interface (pour, exchange), addressability (the carrier), reusability (rinse and refill). It also exhibits the central limitation of thermal packets: low energy density and temperature decay set the operational envelope.

This minimal case grounds the entire architecture. Every claim about larger packets must remain consistent with the physics visible in the bottle.

---

## 4. Multi-Scale Architecture

### 4.1 Six scales

Thermal packets operate at six characteristic scales. Each scale shares the functional grammar of §3 while exhibiting domain-specific constraints.

**Object scale.** Insulated bottles, hot/cold packs, portable coolers. Capacity: 0.05–0.5 kWh_th. Decay time-constant: hours.

**Appliance scale.** Domestic hot-water tanks (200 L, ΔT = 40 °C → ~9.3 kWh_th), heat-pump water tanks, electric water heaters. Capacity: 5–30 kWh_th. Standing losses: 1–3 kWh per 24 h.

**Building scale.** Low-temperature heated floors, thermal mass, walls, slabs, PCM-loaded panels. Capacity: 10–200 kWh_th depending on mass and ΔT.

**Building-cluster scale.** Shared hot-water tanks, neighborhood buffer tanks, low-temperature micro-networks. Capacity: 100 kWh_th–10 MWh_th.

**Mobile-logistics scale.** Hot-water tankers, PCM containers, mobile thermal batteries, ice containers. Capacity: 0.5–5 MWh_th per vehicle [2, 3].

**Territorial scale.** Fleets of autonomous thermal shuttles, waste-heat logistics, cold-chain integration, island or mountain thermal resilience systems. Capacity: aggregated.

### 4.2 What "multi-scale" means here

This paper deliberately uses **multi-scale** rather than **fractal**.

*Fractal* in the geometric or statistical sense requires scale-invariant statistics (power-law distributions, Hausdorff dimension). The thermal packet architecture is not fractal in that strong sense. What it exhibits is a *structural recurrence*: the same operational grammar (charge–store–route–transfer–discharge–measure–reuse) applies at each scale, with scale-specific physical constraints.

This is the same distinction maintained in the corpus paper on the packet as evolutionary attractor [15]: structural recurrence is an *observation*; scale-invariance in any formal sense is a *hypothesis* requiring separate mathematical investigation. TPN claims the observation, not the hypothesis.

---

## 5. Exergy, Quality, and Direct vs. Indirect Packets

### 5.1 Exergy mismatch in current systems

Electricity is a high-exergy carrier. It can produce motion, computation, light, electrochemistry, high-temperature heat, and digital services. Yet many final uses are low-exergy thermal needs: domestic hot water, low-temperature space heating, drying, washing, comfort heating, refrigeration.

Using high-exergy electricity to produce low-temperature heat is practical, especially with heat pumps. Conceptually, however, energy systems should match the *quality* of the energy carrier to the quality required by the final use.

Thermal Packet Networks make this visible. They store and deliver the final-use thermal service directly, rather than treating heat as a secondary residue of electricity.

> Do not store only energy. Store useful end-use capacity.

In winter, this means heat packets. In summer, cold packets.

### 5.2 Heat packets and cold packets

A TPN includes both polarities.

*Heat packets*: hot water, low-temperature thermal tanks, high-temperature PCM modules, sand or brick thermal storage, industrial heat containers.

*Cold packets*: ice, chilled water, cold packs, cold PCM modules, refrigerated containers, building cold storage, nighttime cold for daytime cooling.

The symmetry matters. Cold packets are especially relevant in electricity systems stressed by air-conditioning peaks. Producing cold when electricity is abundant and releasing it during peak demand is a direct thermal equivalent of demand shifting. The Mariani Village AC packet (§11.2) is one such instance.

### 5.3 Direct sanitary packets vs. indirect technical packets

Thermal packets divide further by transferred medium.

**Indirect technical packets** deliver heat through an exchanger. The transported fluid is not consumed. Advantages: sanitary separation, reusable technical fluid, controlled chemistry. Limitations: exchangers add cost; heat-transfer power may limit service speed.

**Direct sanitary packets** deliver hot or cold potable water itself. Advantages: simpler interface, no exchanger required. Limitations: stronger sanitary requirements, residence-time constraints, risk of stagnation at unsafe temperatures, regulated certification.

A direct hot-water packet is in fact a **hybrid hydric–thermal–sanitary packet**:

```text
water + heat + sanitary status + container + traceability
```

This is not a problem to be eliminated. It is a reclassification: the packet is regulated under sanitary norms as well as thermal ones.

---

## 6. Quantitative Limits

### 6.1 Volumetric energy density

Thermal packets face a major physical limitation: low volumetric energy density compared with chemical fuels.

**Table 2.** Approximate volumetric energy densities.

| Carrier | Energy density |
|---|---:|
| Fuel oil / diesel | ~10 kWh/L |
| Liquid propane | ~6.5 kWh/L |
| Hot water, ΔT = 80 °C | ~0.093 kWh/L |
| Hot water, ΔT = 50 °C | ~0.058 kWh/L |
| Latent PCM (representative) | 0.05–0.15 kWh/L |
| Lithium-ion battery (electrical) | ~0.4–0.7 kWh/L |

A 1,000 L hot-water tank at ΔT = 50 °C stores ~58 kWh_th — two orders of magnitude below a fuel-oil tank of the same volume.

This limitation must be made explicit. TPN is *not* a volumetric replacement for fuel oil or gas. It is relevant when:

- distances are short;
- heat is low-cost or otherwise wasted;
- demand is low-temperature (where exergy match favors low-grade storage);
- fixed pipe infrastructure is uneconomic;
- modularity and reversibility have value;
- thermal storage aligns with renewable intermittency;
- automated logistics reduce operational cost per cycle.

The correct comparison is not only kWh per litre. It is *adequacy* between energy quality, end use, location, timing, and infrastructure cost.

### 6.2 Transfer rate and thermal C-rate

A packet is useful only if it can be charged or discharged at an operationally acceptable rate.

$$
t = \frac{E}{P_{\text{transfer}}}
$$

where E is packet capacity (kWh_th) and P is transfer power (kW_th).

By analogy with batteries, a thermal packet can be described by a charge or discharge rate relative to its capacity:

$$
\text{C-rate}_{th} = \frac{P_{\text{transfer}}}{E_{\text{capacity}}}
$$

A 50 kWh_th packet discharged at 50 kW_th has a 1-hour discharge time. Discharged at 250 kW_th, 12 minutes. Two transfer modes are relevant:

1. **Thermal recharge** — heat is transferred into stationary storage. Throughput limited by exchanger power.
2. **Packet exchange** — a discharged packet is replaced by a charged one. Analogous to battery swapping or gas-cylinder exchange. Relevant for standardized thermal modules.

### 6.3 Cycle economics

A packet logistics system depends on cycle time and per-cycle cost:

$$
\text{Cost}_{\text{per kWh}_{th}} = \frac{C_{\text{cycle}}}{E_{\text{packet}} \cdot (1 - \ell_{\text{cycle}})}
$$

where C_cycle is the all-in cost of one round trip (energy, labor, depreciation, maintenance, interface time) and ℓ_cycle is the fractional loss per cycle (standing + transport + transfer losses).

Two consequences. First, large packets and short cycles reduce cost. Second, losses appear in the denominator: a system tolerating 20 % cycle losses doubles the relative impact of all other costs. Insulation quality, surface-to-volume ratio, and waiting-time discipline are not optional refinements; they are first-order economic levers.

---

## 7. Topology, Logistics, Autonomous Operation

### 7.1 Backbone and last mile

The distinction between **backbone** and **last mile**, common in telecommunications and logistics, generalizes to TPN:

```text
central or regional sources
→ backbone transport corridors
→ local hubs
→ last-mile delivery
→ end-use storage or interface
```

The backbone may consist of high-capacity heat sources, industrial waste-heat sites, renewable hubs, thermal charging stations, container routes, autonomous shuttle corridors, ports, rail terminals.

The last mile may consist of domestic tanks, building buffer tanks, micro-district loops, thermal ports, mobile modules, neighborhood exchange points, emergency delivery interfaces.

This decomposition avoids a false binary between buried pipes and trucks. A mature architecture combines pipe-based local loops, mobile backbone logistics, stationary buffers, and packet exchange at the edge.

### 7.2 Topology: chain, hub, ring, tree, mesh

**Table 3.** Topology trade-offs.

| Topology | Strength | Weakness |
|---|---|---|
| Linear chain | simple | fragile, no rerouting |
| Hub-and-spoke | efficient aggregation | hub vulnerability |
| Tree | hierarchical clarity | branch isolation |
| Ring | alternative path | limited redundancy |
| Mesh | high resilience | coordination complexity |
| Hybrid | practical compromise | governance complexity |

A **mesh TPN** does not require every node to connect to every other node. It requires sufficient alternative paths, storage buffers, and standardized interfaces to maintain service when part of the system fails. This places TPN closer to resilient communication networks [16, 18] than to a single-purpose delivery chain.

### 7.3 Heterogeneous packet carriers

Thermal vehicles should not be restricted to a single packet type. A delivery platform may carry, in different configurations:

- hot water or other thermal medium;
- cold packets, ice, or chilled-water modules;
- electrical batteries or power modules;
- potable water;
- material goods;
- mobile compute or inference equipment;
- emergency supplies.

This broadens the concept from thermal logistics to **packetized transport infrastructure**. In normal operation a route delivers hot-water packets or charged batteries. In degraded operation the same logistics backbone delivers potable water, cold storage, emergency power, communication equipment, or medical supplies. The packet generalization is developed in [13].

### 7.4 Virtual pipes: autonomous thermal shuttles

Autonomous vehicles may significantly alter TPN economics. The relevant scenario is not general autonomous driving but a *constrained operational domain*: fixed routes, low to moderate speed, mapped corridors, predictable schedules, supervised operation, controlled loading/unloading.

Such routes constitute **virtual rails**. A thermal tanker operating repeatedly between a source and a demand node becomes a discontinuous pipe:

$$
\bar{\Phi}_{th} = E_{\text{packet}} \cdot f_{\text{rotation}}
$$

If a vehicle carries 1.5 MWh_th and completes one cycle per hour, it provides an average thermal flow of 1.5 MW_th. Two vehicles double the flow. Slower cycles reduce it.

Autonomy reduces the labor penalty of repeated short trips, night operations, waiting times, and low-speed service. It does not solve the energy-density problem. It can make short-distance packet logistics competitive against high-CAPEX buried networks.

> The buried pipe is a physical rail for heat. The autonomous route is a virtual rail for thermal packets.

---

## 8. Service Metrics

### 8.1 Thermal traffic intensity (TTI)

TPN are service systems. Vehicles, loading stations, unloading ports, storage tanks, routes, and thermal interfaces are *resources occupied for finite durations by packet flows*. Teletraffic and queueing theory apply [20, 21].

In teletraffic engineering, the Erlang measures traffic intensity:

$$
A = \lambda \cdot h
$$

where λ is arrival rate (arrivals per unit time), h is mean holding time, and A is the average number of resources continuously occupied. The Erlang B formula

$$
B(A, c) = \frac{A^c / c!}{\sum_{k=0}^{c} A^k / k!}
$$

gives the loss probability for c servers under Poisson arrivals.

We introduce **Thermal Traffic Intensity** as the thermal analogue:

$$
TTI = \lambda_{\text{packet}} \cdot \bar{h}_{\text{port}}
$$

with λ_packet the arrival rate of thermal packets at a port and h̄_port the mean unloading time. If six tankers arrive per hour and each occupies a port for 10 minutes, TTI = 6 × (1/6) = 1: with one port the system is saturated; with two ports, mean utilization is 50 %.

The same construction yields occupancy metrics for vehicles, charging stations, exchangers, and storage buffers.

### 8.2 Congestion elasticity

Average occupancy is insufficient. Two systems can carry the same average load with very different responses to fluctuation.

**Congestion elasticity** measures sensitivity:

$$
\varepsilon_C = \frac{\Delta C / C}{\Delta A / A}
$$

where C is a congestion measure (waiting time, delivery delay, port saturation, queue length, cost per delivered MWh_th, loss probability) and A is traffic intensity.

A robust system absorbs a 10 % increase in load with a small increase in delay. A fragile system near saturation experiences a disproportionate degradation. The general framing:

> Intensity measures pressure. Occupancy measures load. Elasticity measures fragility.

### 8.3 Packet decay, time-to-live, useful-life metadata

Packets are bounded not only by capacity, routing, and transfer rate, but by *time*.

Heat dissipates through imperfect insulation. Newtonian cooling gives:

$$
T(t) = T_a + (T_0 - T_a) \cdot e^{-t/\tau}
$$

where τ is the thermal time-constant (insulation × thermal mass / surface area). Cold packets warm by the same law.

A packet's *thermal usefulness* is not energy alone but a joint function:

$$
U(t) = f(E(t), T(t), T_{\text{required}}, T_a, \text{end-use threshold})
$$

A hot-water packet that has lost little energy but fallen below a useful temperature threshold may no longer be adequate. The same applies to cold packets warming above a preservation threshold.

This makes time a routing variable. Each packet should carry metadata:

- time of charge;
- initial temperature;
- current or estimated temperature (sensor or model);
- maximum acceptable delay;
- end-use temperature threshold;
- reheating or recooling possibility;
- sanitary validity where relevant.

Information networks already use this construct under the name **time-to-live (TTL)**. TPN needs the same. The generalization to other packet types — informational, biological, monetary, mandate-bearing — is developed in [13].

> A packet is not only what it contains. It is what remains useful at delivery.

---

## 9. Storage Hierarchies and Cache-Like Layers

### 9.1 The computer-architecture analogy: scope and limits

Computer systems use multiple memory levels because no single storage layer optimizes all criteria at once [22]. Fast caches sit close to computation but are expensive and limited. Main memory is larger but slower. Persistent storage is larger and slower still. Archival storage is densest, cheapest, and slowest.

Thermal systems exhibit a comparable hierarchy. The analogy is architectural, not physical. Heat is constrained by mass, volume, temperature, insulation, losses, and exergy in ways that bits are not. The borrowing concerns layered storage, locality, access latency, priority, and replacement policy — *not* the claim that heat behaves like data.

### 9.2 Thermal hierarchy

**Table 4.** Storage-hierarchy mapping.

| Computing layer | Thermal analogue | Function |
|---|---|---|
| Register / L1 cache | immediately available thermal mass, small buffer | very fast response |
| L2/L3 cache | domestic hot-water tank, local buffer tank | local smoothing |
| Main memory | building-scale or neighborhood thermal storage | operational flexibility |
| Persistent storage | large tank, borehole, seasonal store, container yard | long-duration storage |
| Archival storage | low-grade residual heat, remote slow-access thermal resource | low-priority/delayed use |

Two adjacent concepts:

- A **buffer** absorbs short-term mismatch between inflow and outflow.
- A **cache** keeps useful capacity close to likely demand, reducing access time.

A domestic hot-water tank is both. It absorbs mismatch between heat production and use, and it keeps useful heat close to the user.

---

## 10. Thermal CXU: An Exergy-Aware Service Metric

### 10.1 Formal definition

The MareNostrum project defines the **Compute eXergy Unit (CXU)** as a service metric for sovereign compute infrastructure [23]:

$$
\text{CXU} = E \cdot \eta_{\text{hw}} \cdot \eta_{\text{sys}} \cdot \eta_{\text{sla}}
$$

where E is electrical energy delivered to the compute substrate and the η factors capture hardware, system, and service-level efficiency.

We define the **Thermal Compute eXergy Unit (CXU_th)** as the thermal analogue:

$$
\text{CXU}_{th} = E_{th} \cdot \eta_{\text{storage}} \cdot \eta_{\text{transport}} \cdot \eta_{\text{transfer}} \cdot \eta_{\text{match}}
$$

where:

- E_th is the thermal energy charged into the packet at source (kWh_th);
- η_storage captures losses during storage (standing losses, decay);
- η_transport captures losses during routing (insulation losses while moving);
- η_transfer captures losses at charge and discharge interfaces;
- η_match is the **exergy-match factor**, capturing the adequacy between delivered temperature and end-use requirement.

### 10.2 The exergy-match factor

η_match is the contribution that distinguishes CXU_th from a naive end-to-end efficiency. It encodes the principle "store useful end-use capacity, not just energy."

A simple parameterization:

$$
\eta_{\text{match}} = \min\left(1, \frac{T_{\text{delivered}} - T_a}{T_{\text{required}} - T_a}\right)
$$

If a packet arrives at the required temperature or above, η_match = 1 (full match). If it arrives below, η_match < 1 in proportion to the shortfall above ambient. A packet that has cooled to ambient delivers nominal energy but zero useful exergy: η_match = 0, and CXU_th = 0 regardless of E_th.

For cold packets the inequality reverses; the formula is symmetric in (T_a − T) for cooling applications.

### 10.3 Comparison with the electrical CXU

The two units differ in one essential way: electricity has near-unit exergy quality at the point of delivery (high-grade work-equivalent energy), so the electrical CXU's η factors are dominated by hardware and system terms. Thermal exergy is graded — temperature level matters as much as energy quantity — so CXU_th cannot omit η_match without misrepresenting the service.

This makes CXU_th a *service unit*, not a thermodynamic unit. It is intended for contracts, pricing, and continuity SLA design, not for thermodynamic accounting.

---

## 11. Worked Examples

### 11.1 The thermos as primitive packet

We return to the case introduced in §3.3. Parameters:

- m = 1 kg water, c_p = 4,186 J/kg·K
- T_0 = 90 °C, T_a = 20 °C, T_required = 50 °C (hot beverage threshold)
- τ = 8 h (high-quality bottle)

At t = 0: E_0 ≈ 81 Wh_th; T_0 = 90 °C.

After 6 h: T = 20 + 70·e^(−6/8) = 53 °C. T > T_required, so η_match = (53−20)/(50−20) = 1.10 → clamped to 1. The packet remains fully useful.

After 12 h: T = 20 + 70·e^(−12/8) = 35.6 °C. T < T_required: η_match = (35.6−20)/(50−20) = 0.52. Half the exergy service is lost despite the bottle still being warm.

After 24 h: T = 20 + 70·e^(−24/8) = 23.5 °C. η_match ≈ 0.12. Effectively expired.

The thermos thus exhibits all the formal properties developed above: decay-aware routing applies (the packet should be consumed within τ); time-to-live metadata is essential; η_match captures the operational truth that "still warm" and "still useful" are different states.

### 11.2 The Mariani Village portable AC packet

The Mariani Village concept [14] proposes ISO-container–based housing units serving students in Corte (Corsican interior) and tourists on the coast in alternation across seasons. Cooling needs concentrate on the coast in summer; heating needs concentrate inland in winter.

A central design element is a **shared portable air-conditioning packet**: a transportable refrigeration unit standardized across the container housing stock. Treated as a TPN component:

- *Content*: a sealed refrigerant loop coupled to a small PCM cold-storage buffer.
- *Capacity*: order of 3–10 kWh_th of cold per packet.
- *Carrier*: a wheeled unit moved between containers as occupancy shifts; periodically returned to a service hub for inspection, refrigerant top-up, and PCM recharge.
- *Network*: the Mariani Village hub serves as a local exchange point; the regional logistics layer provides seasonal redistribution.

Applied CXU_th: under typical coastal summer use, η_storage ≈ 0.9 (PCM hold), η_transport ≈ 0.95 (short distances within the village), η_transfer ≈ 0.9 (heat-exchanger coupling to interior air), η_match ≈ 1 when delivered above the target cooling threshold. Overall CXU_th ≈ 0.77 · E_th_charged.

This worked example does three things. It demonstrates that the architecture is deployable, not merely descriptive. It connects TPN to a wider project [14] which itself instantiates the packet transition in habitat. And it makes the framework testable: a Mariani Village pilot generates measurable data on each η factor.

### 11.3 Waste heat recovery from a small datacenter

A complementary example. A 100 kW IT-load edge datacenter releases roughly 100 kW of low-grade waste heat (typically 35–55 °C return temperature). Over 24 h that is ~2.4 MWh_th — non-trivial.

Without a packet layer this heat is rejected. With a packet layer, a 1.5 MWh_th PCM container parked at the datacenter could absorb 15 hours of waste heat and shuttle it to a nearby greenhouse, district loop, or laundry. Cycle time, distance, η_match against the receiving end-use temperature, and the carbon footprint of the shuttle determine viability.

This is a candidate pilot configuration under the FractaVolta research agenda.

---

## 12. Use Cases, Failure Modes, Scope

### 12.1 Use cases

- **Domestic hot water** — stationary thermal packets already deployed at scale.
- **Low-temperature floor heating** — building thermal mass as slow-release packet.
- **Waste heat recovery** — connecting industrial or datacenter heat to nearby demand without permanent pipes.
- **Rural, mountainous, island territories** — intermediate between isolated systems and full district heating.
- **Temporary sites and events** — construction, refugee camps, festivals, military deployments, field hospitals.
- **Emergency and resilience** — critical buildings during grid failures, fuel shortages, pipe outages, storms.
- **Hybrid district heating** — prefiguring future networks, serving peripheral users, providing backup, balancing peaks, bridging non-economic pipe gaps, testing demand before capital-intensive works.

### 12.2 Failure modes

TPN fails when:

- distances are too long;
- temperature losses exceed acceptable thresholds;
- energy density is too low for the use case;
- interface power is too slow;
- labor or vehicle costs dominate;
- traffic congestion erodes reliability;
- sanitary constraints become disproportionately costly;
- demand is high and stable enough to justify pipes;
- standardization is absent;
- carbon savings are negated by fossil transport emissions;
- governance is unclear (ownership, responsibility, traceability).

### 12.3 The proper scope claim

> Thermal Packet Networks are not a universal substitute for district heating. They are a complementary architecture for low-density, uncertain, intermittent, temporary, resilient, or geographically fragmented thermal demand.

This is the only claim defended in this paper.

---

## 13. Research Agenda

**13.1 Formal modeling.** Develop full mathematical models linking packet capacity, transfer power, cycle time, route length, topology, loss rate, service load, queueing delay, congestion elasticity, and delivered thermal quality. Integrate with established teletraffic and queueing theory [20, 21].

**13.2 Interface standards.** Define standardized thermal ports, connectors, metering systems, safety protocols, and sanitary classifications. Without standards, packet exchange is impossible at network scale.

**13.3 Hybrid optimization.** Compare pipes, stationary storage, mobile thermal packets, and autonomous thermal shuttles under realistic demand profiles. The output is a decision framework: "at this density, demand stability, and distance, choose architecture X."

**13.4 Autonomous thermal logistics.** Model constrained-route autonomous shuttles as virtual pipes (§7.4). Evaluate operational design domains.

**13.5 Exergy-aware planning.** Integrate exergy analysis and CXU_th into packet routing and end-use matching algorithms.

**13.6 Sanitary thermal packets.** Study direct hot-water packets as hybrid hydric–thermal–sanitary systems. Regulatory pathway analysis.

**13.7 Pilot deployments.** Mariani Village AC packet (§11.2), waste-heat-to-greenhouse shuttle (§11.3), or a Corsican island municipality micro-network are candidate pilots.

**13.8 Connection to generalized packet theory.** TPN is one of several packet substrates. The general framework — including data, electricity, gravitational potential, inference, cognition, value, and mandate — is developed separately [13].

---

## 14. Claim Manifest

```yaml
paper_id: thermal_packet_networks
version: 0.2

claims:
  - id: C1
    statement: "Heat and cold can be usefully formalized as discrete packets with a shared functional grammar (charge, store, route, transfer, discharge, measure, reuse) across six scales from insulated bottle to territorial logistics."
    status: definitional

  - id: C2
    statement: "TPN is complementary to district heating, not a substitute. The boundary between the two is set by thermal density, demand stability, distance, and infrastructure-cost amortization."
    status: argued

  - id: C3
    statement: "Service metrics from teletraffic engineering (Erlang-form traffic intensity, congestion elasticity) and computer architecture (storage hierarchy, freshness, TTL) can be adapted to thermal physics without erasing thermal specificity."
    status: argued

  - id: C4
    statement: "The Thermal Compute eXergy Unit (CXU_th = E_th · η_storage · η_transport · η_transfer · η_match) extends the MareNostrum CXU framework to thermal substrates and is suitable as a service-pricing unit."
    status: hypothesis

  - id: C5
    statement: "The Mariani Village portable air-conditioning packet is a deployable TPN instance whose performance can be measured against CXU_th in a pilot."
    status: empirical_hypothesis

  - id: C6
    statement: "Waste-heat recovery via mobile thermal packets is economically viable at distances and demand profiles where district heating is uneconomic."
    status: empirical_hypothesis

  - id: C7
    statement: "TPN is one of three physical substrates of a wider packet-energy architecture, alongside Energy Packet Networks (electricity, Gelenbe) and Packetized Gravity Networks (hydraulics, this corpus)."
    status: terminological

  - id: C8
    statement: "The use of 'multi-scale' rather than 'fractal' is deliberate: structural recurrence of an operational grammar is claimed; mathematical scale-invariance is not."
    status: scope
```

---

## 15. Conclusion

The insulated bottle, the domestic hot-water tank, the heated floor, the mobile thermal tanker, and the territorial thermal container belong to different categories of object. This paper has argued that they share a common operational grammar. Each can be interpreted as a thermal packet: a finite quantity of heat or cold stored in an identifiable medium and container, charged, stored, transported or addressed, discharged, measured, and reused.

This perspective does not reject pipe-based district heating. It clarifies its domain. Pipes are excellent when thermal density, demand stability, and long-term utilization justify high fixed infrastructure costs. Thermal packets become relevant when modularity, reversibility, resilience, short-distance logistics, low-exergy demand, waste-heat recovery, or uncertainty dominate.

Three contributions have been made. First, a formal definition of the thermal packet with a six-property characterization and a multi-scale architecture. Second, a service-metric layer — TTI, congestion elasticity, packet decay — drawn carefully from teletraffic and computer architecture without metaphorical overreach. Third, a Thermal Compute eXergy Unit (CXU_th) that extends the MareNostrum CXU framework and makes thermal service contractually pricable, illustrated by two worked examples — the thermos and the Mariani Village AC packet.

TPN is one instance of a broader pattern. The general theory of generalized packet networks is developed in a companion paper [13]. The companion papers on Energy Packet Networks [7, 8], Packetized Gravity Networks [11], cognitive packets [24], and the packet transition [25, 15] form the corpus in which this paper takes its place.

Whether TPN is a useful architecture will be determined by deployment, measurement, and external scrutiny. The thermos is not merely an analogy. It is the smallest visible instance of a larger architecture that the corpus — public, versioned, falsifiable — is designed to test.

---

## References

[1] Eurostat, *Energy balances and final energy consumption by sector*, latest annual release. Thermal demand accounts for approximately half of EU final energy consumption.

[2] M. Kuta, "Mobile Thermal Energy Storage — A Review and Analysis," *Energies*, vol. 18, 2025.

[3] B. Zalba, J. M. Marín, L. F. Cabeza, and H. Mehling, "Review on thermal energy storage with phase change materials, heat transfer analysis and applications," *Applied Thermal Engineering*, vol. 23, no. 3, 2003.

[4] IRENA, *Innovation Outlook: Thermal Energy Storage*, 2020.

[5] Royal Society, *Unlocking thermal energy: industrial thermal energy efficiency and waste heat reuse*, 2026.

[6] H. Lund et al., "4th Generation District Heating (4GDH): Integrating smart thermal grids into future sustainable energy systems," *Energy*, 2014.

[7] E. Gelenbe, "Energy Packet Networks: ICT based energy allocation and storage," *Lecture Notes in Computer Science*, 2011.

[8] E. Gelenbe, "Energy Packet Networks: adaptive energy management for the cloud," *Proceedings of the 2nd International Workshop on Cloud Computing Platforms*, 2012.

[9] M. R. Almassalkhi et al., "Packetized Energy Management," research conducted under the ARPA-E NODES program.

[10] L. A. Duffaut Espinosa, M. Almassalkhi, P. Hines, and J. Frolik, "System properties of Packetized Energy Management for aggregated diverse resources," *Power Systems Computation Conference*.

[11] J. H. N. Robert, *Packetized Gravity Networks: Distributed Hydro-Energetic Infrastructure for Resilient Renewable Integration*, FractaVolta working paper, 2026. `github.com/JeanHuguesRobert/FractaVolta/blob/main/research/PGN.md`.

[12] J. H. N. Robert, *Discours de la seconde méthode*, Institut Mariani, 2026. `github.com/JeanHuguesRobert/barons-Mariani`.

[13] J. H. N. Robert, *Generalized Packet Networks: A Framework for Heterogeneous Packets, Resource Occupancy, and Cross-Domain Operational Recurrence*, FractaVolta working paper, 2026.

[14] J. H. N. Robert, *Mariani Village: Relocatable ISO-Container Habitat as Energy Packet Network Instance*, working paper, 2026.

[15] J. H. N. Robert, *The Packet as Evolutionary Attractor: Scale-Invariant Transitions in Complex Networks*, FractaVolta working paper, 2026.

[16] P. Baran, *On Distributed Communications*, RAND Corporation, 1964.

[17] D. Davies, *Proposal for a Digital Communication Network*, National Physical Laboratory, 1965–1967.

[18] L. Kleinrock, *Communication Nets: Stochastic Message Flow and Delay*, McGraw-Hill, 1964.

[19] S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," 2008.

[20] V. B. Iversen, *Teletraffic Engineering Handbook*, ITU-D, 2001.

[21] L. Kleinrock, *Queueing Systems, Volume I: Theory*, Wiley, 1975.

[22] J. L. Hennessy and D. A. Patterson, *Computer Architecture: A Quantitative Approach*, 6th ed., Morgan Kaufmann, 2017, esp. Chapters 2 and 5.

[23] J. H. N. Robert, *CXU Specification: The Compute eXergy Unit*, MareNostrum repository, 2026. `github.com/JeanHuguesRobert/marenostrum/blob/main/research/CXU_SPEC.md`.

[24] J. H. N. Robert, *Cognitive Packets: A Minimal Continuation Payload for Human–AI and Multi-Agent Cooperation*, Institut Mariani working paper, 2026.

[25] J. H. N. Robert, *The Packet Transition: A Lateral Reading of Circuit Networks*, FractaVolta working paper, 2026. `github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_transition.md`.

---

*Comments, objections, and contributions are invited via the project repository. Each will be recorded and addressed in subsequent versions, per the Seconde méthode (Rule 2).*

*Process note: This document results from an iterative drafting process. v0.1 was an intuitive exposition. v0.2 introduces methodological framing, scope claims, formal definitions, service metrics (TTI, congestion elasticity, packet decay), the CXU_th unit, two worked examples (thermos, Mariani Village), and a claim manifest. The history is in the repository.*

*The next version will be better. That is the point.*
<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Rendre capable — noyau doctrinal provisoire](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/noyau_doctrinal_rendre_capable.md)
- [For researchers](../docs/for-researchers.md)
- [Fractanet — Generalized Control Planes for Heterogeneous Packet Networks](fractanet.md)
- [FractaVolta](../README.md)
- [Research Index — FractaVolta](index.md)
<!-- END_AUTO: backlinks -->
