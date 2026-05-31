---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-05-26
title: "DC-Native Energy Packet Networks"
date: "2026-05-06"
status: "draft — auto-filled (frontmatter cleanup)"
---
# DC-Native Energy Packet Networks
## How Far Can Electricity Return from Alternating Current to Direct Current?

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A.

1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org | fractavolta.com

---

## Abstract

The victory of alternating current over direct current in the late nineteenth century was not a metaphysical truth about electricity. It was a historically contingent engineering settlement: AC won because transformers made voltage conversion simple, cheap, and efficient, allowing long-distance transmission over a shared wired grid. That settlement shaped the electrical system as a synchronized, circuit-like infrastructure operating at a common frequency and phase. The Energy Packet Network (EPN), as introduced in *The Unconscious Grid*, changes the premise. If energy is no longer primarily transmitted through continuous wired circuits, but stored, addressed, transported, and discharged as discrete physical packets, then the most compelling reason for AC disappears over large parts of the system.

This paper argues that EPN architectures are naturally DC-native. Photovoltaics generate DC; batteries store DC; electronic loads, LED lighting, telecommunications, electric vehicles, and AI data centers internally consume DC. Each avoidable AC/DC conversion stage introduces losses of 2–5%, which compound into 10–20% systemic overhead in conventional AC distribution chains. In packetized energy systems, AC becomes a boundary protocol rather than the default substrate. Eliminating three conversion stages from a FractaVolta sovereign inference node recovers roughly 8–12 percentage points of exergy, equivalent — at Mediterranean irradiance levels — to several additional usable kWh per day per node.

The question is not whether society can "return" to DC everywhere. It cannot, and should not. The correct question is how far DC can propagate once electricity is no longer treated as a continuously synchronized carrier but as stored exergy moving through packets. The answer is layered: DC should dominate inside packets, inside microgrids, inside renewable-storage-compute nodes, inside data centers, and across medium-voltage local energy islands. AC should persist as a compatibility layer at legacy interfaces. HVDC should remain a wired bulk-transfer technology where corridors are justified. EPN goes further: it removes the wire itself from part of the transport problem.

**Keywords:** Energy Packet Network; direct current; DC microgrids; HVDC; LVDC; store-and-forward; battery logistics; photovoltaic systems; data centers; exergy; packetized energy; FractaVolta; SiC; GaN; 380 V DC

---

## 1. Introduction

The modern electrical grid is usually described as an energy infrastructure. Architecturally, it is also a synchronization infrastructure. Its central constraint is not merely that electricity must flow through conductors, but that large AC systems require phase, frequency, voltage, protection, and balancing discipline over an extended physical network.

The Energy Packet Network reverses this assumption. In an EPN, the basic unit is not a continuous current flowing through a shared conductor. It is a discrete unit of stored exergy: a battery, an electric vehicle, a containerized storage module, or another energy carrier capable of being charged, transported, addressed, discharged, exchanged, or converted into computation.

This shift makes the AC/DC question newly important. Alternating current was historically favored because it made long-distance wired distribution practical through transformers. But an EPN reduces dependence on long-distance wires. Once the wire becomes optional, the historical reason for AC weakens.

The issue is therefore not ideological. It is architectural:

> Where the system is wired, synchronized, legacy, and shared, AC remains useful.
> Where the system is packetized, stored, local, electronic, renewable, and computational, DC becomes the natural form.

This paper first reviews the historical context of the AC/DC settlement (§2), then applies the packet-switching analogy (§3), quantifies the efficiency case for DC (§4), presents a layered architectural analysis (§5), maps the EPN DC stack (§6), addresses protection and safety constraints (§7), discusses regulatory consequences (§8), and derives specific design doctrine for FractaVolta nodes (§9–10).

---

## 2. The Historical Settlement: Why AC Won

Direct current was the original practical form of electric distribution. Batteries are DC devices. Early lighting systems were DC. Edison's distribution network in lower Manhattan (1882) operated at 110 V DC [1]. The difficulty was voltage transformation: resistive losses in a conductor are proportional to I²R, and without the ability to step voltage up for transmission and down for consumption, DC systems were limited to roughly 1–2 km service radii before losses became prohibitive.

Alternating current solved this problem through the transformer. By stepping voltage up to tens of kilovolts for transmission and back down for final distribution, AC made centralized generation and long-distance wired distribution economically feasible. The U.S. Department of Energy summarizes the original weakness of DC plainly: DC was not easily converted to higher or lower voltages, whereas AC could be transformed efficiently for transmission and end use [2].

The victory of AC was therefore not a victory of alternating current as such. It was the victory of *voltage transformation* under nineteenth-century constraints — specifically, before solid-state power electronics existed.

That settlement created the modern grid:

- large synchronous generators;
- high-voltage AC transmission (typically 110–765 kV);
- synchronized frequency (50 or 60 Hz);
- regional or continental balancing;
- AC distribution (11–33 kV medium voltage, 230/400 V low voltage) to passive consumers;
- local rectification back to DC inside every electronic device.

For most of the twentieth century, this was rational. Loads were motors, incandescent lighting, resistance heating, and industrial equipment — all usable directly with AC. Generation was centralized and synchronous. Storage was negligible. Power electronics were primitive.

Those assumptions no longer hold.

---

## 3. The Packet-Switching Analogy

Information networks underwent a comparable architectural shift. The telephone network was circuit-switched: a dedicated physical path was established and held for the duration of a communication session, reserving bandwidth regardless of actual traffic. ARPANET (1969) demonstrated that messages could instead be broken into addressed packets, routed independently, and reassembled at the destination [3]. Packet switching became the architectural foundation of the internet.

*The Unconscious Grid* applies this distinction to energy [4]. It argues that the electrical grid remains structurally circuit-switched, while an EPN applies store-and-forward logic to energy: batteries become packets; vehicles, ferries, and logistics networks become routers; AI inference becomes an application-layer transduction of solar exergy into internet-routable value.

This is where DC becomes central. A packet-switched information network does not require a continuous physical circuit between sender and receiver. Likewise, an energy packet does not require a continuous electrical circuit between generation and consumption. The packet is charged, isolated, transported, and later discharged.

During all phases of storage and transport, the packet is necessarily DC in nature:

- electrochemical cells produce and store DC;
- state of charge (SoC) is a DC quantity;
- battery management systems (BMS) operate on DC cell voltages;
- PV string voltage is DC (600–1500 V DC in utility-scale installations, 30–60 V per module at Vmp);
- inverter output is only needed when the destination explicitly requires AC.

**The packet was always DC.** The AC layer was a wrapper for grid interoperability, not an intrinsic property of stored exergy.

---

## 4. The Quantitative Case for DC

The return of DC is driven by four converging facts, each reinforced by measurable performance data.

### 4.1 Generation is increasingly DC

Photovoltaic panels generate DC directly. A typical 60-cell silicon module outputs 30–40 V at maximum power point; utility-scale strings reach 600–1500 V DC. Large PV plants therefore already operate at high-voltage DC internally, inverting only at the point of grid injection.

Wind turbines commonly produce variable-frequency AC, which must be fully rectified and re-inverted before grid connection — functionally making modern wind turbines DC-intermediate devices inside [5].

Fuel cells produce DC. Batteries store DC. All of these technologies enter the system through power electronics, not synchronous rotating machines. Their natural interface is a DC bus, not an AC grid.

### 4.2 Storage is DC, and conversion losses compound

Batteries, supercapacitors, and electrochemical storage are DC devices. Round-trip efficiency for modern lithium iron phosphate (LFP) cells is 95–98% for the electrochemical cycle alone [6]. However, every AC↔DC conversion stage adds 2–5% loss:

| Conversion Stage | Typical Efficiency |
|---|---|
| PV MPPT DC/DC | 98–99.5% |
| DC/AC inverter (string) | 97–99% |
| MV transformer | 98–99.5% |
| LV distribution transformer | 97–99% |
| AC/DC rectifier (UPS or charger) | 94–97% |
| DC/DC battery interface | 97–99% |

In a conventional chain — PV → AC grid → UPS → battery → load — three to five conversion stages are traversed. Compounded, this adds up to 10–20% overhead compared to a direct DC path: PV → DC/DC → battery → DC bus → load.

For a FractaVolta node generating 10 kWh/day from Mediterranean irradiance (approximately 5 peak sun hours at ~2 kWh/m²/day in Corsica), recovering 10% through DC-native architecture yields roughly 1 kWh/day/node — enough to run a full GPU inference session or sustain 24 hours of LoRa telemetry and sensor acquisition.

### 4.3 Loads are increasingly DC

The load mix has transformed. The dominant loads of the twenty-first century energy system are:

- Computers and servers (internally 12 V DC, 5 V, 3.3 V, 1.x V);
- Telecom equipment (48 V DC bus — the global telecom standard since the 1960s);
- LED lighting (DC at the LED junction, with AC-DC conversion at the driver);
- Variable-speed motor drives (AC motor controlled via DC intermediate bus);
- EV chargers (AC to DC conversion for battery charging);
- USB-C powered devices (up to 240 W at 48 V DC per USB PD 3.1);
- AI inference nodes (GPU boards internally operating at 12 V, supplied via AC-DC PSU).

Lawrence Berkeley National Laboratory demonstrated the efficiency advantage of DC power delivery for data centers as early as 2008, comparing AC-based distribution with 380 V DC buses [7]. The Open Compute Project's 2026 LVDC white paper treats 380 V DC as the reference voltage for next-generation data center power distribution, addressing voltage selection, earthing, protection, and system components in detail [8].

Data centers constitute the clearest quantitative case. A conventional AC data center achieves a Power Usage Effectiveness (PUE) of 1.4–1.6, meaning 40–60% overhead beyond the IT load itself, largely attributable to UPS systems, transformers, and cooling sized for worst-case AC losses. DC-optimized architectures regularly achieve PUE of 1.1–1.3 [7].

### 4.4 Wide-bandgap semiconductors have dissolved the transformer argument

The nineteenth-century advantage of AC was the transformer: lossless voltage transformation with no moving parts, based on magnetic induction requiring alternating flux. The twenty-first-century equivalent is solid-state power conversion using wide-bandgap (WBG) semiconductors.

Silicon carbide (SiC) MOSFETs operate at switching frequencies of 100 kHz–1 MHz, compared to 20–100 kHz for conventional silicon IGBTs. This allows a 10× reduction in passive component size (inductors, capacitors) and supports converter efficiencies exceeding 98.5% at rated power [9]. Gallium nitride (GaN) devices push this further, enabling multi-megahertz switching with extremely low switching losses.

The consequence is that DC/DC voltage conversion — previously expensive, heavy, and lossy — is now efficient, compact, and affordable at power levels from milliwatts (IoT) to megawatts (grid interface). The IEC's DC Power Distribution Technology Trend Report (2024) explicitly treats this as a paradigm shift, enabling DC distribution from building level to grid edge [10].

**AC is no longer necessary for voltage flexibility. It is now a choice.**

---

## 5. Layered Answer: How Far Can DC Go?

The correct answer is not "all the way." It is layer-dependent. Each layer has a distinct cost-benefit profile.

### 5.1 Inside the packet: almost entirely DC

At the cell, module, rack, and container level, EPN packets should be DC-native.

A FractaVolta standard battery container should be designed with:

- **Cell level**: 3.2 V LFP nominal (3.65 V fully charged, 2.5 V discharge cutoff);
- **Module level**: 48 V nominal (16S LFP configuration) or 51.2 V (16S);
- **Rack/pack level**: 48 V or stepped to 400 V via series stacking or DC/DC;
- **Container DC bus**: 400–800 V DC for transport efficiency and inverter compatibility;
- **Packet interface**: IEC 62196-compliant DC connectors (CCS Combo 2) or proprietary high-current DC bus connectors with pre-charge and isolation monitoring.

The container should not internally pretend to be a miniature AC grid. Its native architecture:

```
[LFP cells] → [BMS] → [DC module bus 48V]
                              ↓
                    [DC/DC boost converter]
                              ↓
                    [Container DC bus 400V]
                              ↓
                    [Isolation monitor + DC MCB]
                              ↓
              [AC inverter — only if AC output required]
```

This mirrors internet architecture: packets carry their own structure internally and adapt only at interfaces.

### 5.2 Inside renewable-storage-compute nodes: mostly DC

A FractaVolta node combining solar generation, batteries, LoRaWAN telemetry, edge compute, sensors, cameras, and AI inference should use a DC backbone throughout.

**Reference FractaVolta node architecture:**

```
[PV array 1500V DC strings]
        ↓
[MPPT DC/DC converter → 48V or 400V DC bus]
        ↓
[LFP battery bank — direct DC coupling]
        ↓
[DC distribution bus 48V]
        ├─ [Edge compute / GPU inference node — 12V via DC/DC]
        ├─ [LoRaWAN gateway — 12V]
        ├─ [IP cameras — PoE 48V DC]
        ├─ [LED lighting — 24V DC]
        ├─ [Weather station, sensors — 3.3/5V via DC/DC]
        ├─ [EV/e-bike charging — 48V or 400V DC]
        └─ [AC inverter 230V 50Hz — legacy tools / outlets only]
```

AC appears at the boundary only — for tools, compliance with electrician codes, or inter-grid injection when applicable. This is the first major practical design conclusion for FractaVolta:

> **A FractaVolta EPN node should be DC-first, AC-compatible — not AC-first.**

### 5.3 Inside data centers: strongly DC

FractaVolta's highest-value application layer is sovereign AI inference. A solar-battery-compute node is not merely compatible with DC — it is structurally DC-native from generation through final load.

Standard voltage levels for data center DC adoption:

| Voltage | Application |
|---|---|
| 400 V DC (LVDC) | Server rack power (Open Compute, Vicor, Vertiv) |
| 48 V DC | Server boards (Open Rack v3, Google 48V), telecom |
| 12 V DC | Individual server boards (ATX standard) |
| 5 / 3.3 / 1.x V | On-board regulators |

The 48 V DC bus at rack level is the emerging consensus in hyperscaler design (Google, Meta, Microsoft) precisely because it reduces I²R losses in busbars (P = I²R; doubling voltage from 12 V to 48 V reduces current by 4×, losses by 16× for equal power).

### 5.4 Inside buildings: selectively DC

Buildings cannot immediately become fully DC because appliance ecosystems, electrician training, protection codes, and user expectations remain AC-based.

DC can expand progressively in defined bounded zones:

- **Telecom cabinets**: 48 V DC, already standard;
- **Server rooms**: 380 V or 400 V DC;
- **LED lighting circuits**: 24 V DC;
- **USB-C / PoE zones**: 48 V DC (USB PD 3.1 up to 240 W, IEEE 802.3bt PoE up to 90 W);
- **PV-battery rooms**: DC-native;
- **EV charging**: DC fast charge via CCS;
- **Microgrid-connected outbuildings**: DC-first node architecture.

The IET (2015) and NEMA (2018) have both documented the growing significance of LVDC distribution in buildings [11,12]. IEC TC8 SC8A is actively developing standards for LVDC building distribution.

A particularly significant convergence point is USB Power Delivery 3.1 (EPR, 2021), which operates at exactly 48 V DC — the SELV ceiling — and delivers up to 240 W per port. This is not coincidental: 48 V is the maximum touch-safe voltage under IEC 60479-1, allowing USB-C connectors to carry serious power without arc-flash enclosures or specialist protection. At 240 W, USB-C PD 3.1 covers nearly all laptops (45–140 W), monitors, Raspberry Pi and Jetson-class edge compute nodes, full LED lighting circuits, LoRaWAN gateways, and IP cameras. The cable is already in every user's pocket.

This makes the USB-C connector the **human-facing interface of the 48 V SELV bus**: touch-safe, power-negotiated via the PD protocol, and ubiquitous. A FractaVolta node exposing 48 V DC through USB-C PD 3.1 ports renders the legacy 230 V AC socket optional for a growing share of daily energy uses — with no electrician, no special training, and no shock risk. The 230 V outlet becomes a compatibility shim for motors, kitchen appliances, and legacy tools; the USB-C port becomes the native energy interface of the packetized DC world.

The practical rule for FractaVolta deployment:

> DC should enter buildings first where the load is already electronic, supervised, and bounded.

### 5.5 Local microgrids: DC where bounded, hybrid where public

DC microgrids are technically feasible for bounded systems: farms, campuses, ports, islands within islands, container villages, telecom sites, autonomous shelters, disaster-resilience nodes, AI inference nodes.

However, public distribution remains AC for institutional, not primarily technical, reasons: protection practices, metering infrastructure, electrician certification, regulatory frameworks, and appliance compatibility are all AC-centred.

The realistic near-term architecture for FractaVolta Mediterranean deployments is therefore hybrid:

- **DC core** (PV, storage, compute, sensing, local loads);
- **AC public interface** (grid interconnection point, compliance, export metering);
- **DC packet exchange** (inter-node energy transfer via logistics);
- **AC compatibility layer** (user outlets, legacy tools, code compliance).

### 5.6 Long-distance wired transmission: HVDC, not EPN

For large fixed transfers over justified corridors, HVDC is the existing DC answer. HVDC is efficient over long distances and useful for interconnecting asynchronous grids — the U.S. DOE identifies HVDC breakeven distance at approximately 800 km for overhead lines and 50–80 km for underground or submarine cables [13].

Modern VSC-HVDC (Voltage Source Converter) links operate at ±320 kV to ±525 kV, transmitting 1–3 GW per bipole. The proposed Mediterranean Interconnection (EuroAfrica, TuNur, ElMedlink) projects consistently target VSC-HVDC in the ±500 kV class.

But HVDC remains a **wire**.

It solves part of the AC problem without solving the circuit problem. It still requires corridors, environmental impact studies, capital in the range of €1–3 M/km, permitting timelines of 10–20 years, and physical continuity.

The EPN asks a more radical question:

> What if some energy does not need a wire at all?

In that sense, HVDC is not the endpoint of DC's return. It is the wired branch. The EPN is the wireless branch.

---

## 6. The FractaVolta EPN DC Stack

A DC-native EPN can be described as a five-layer stack, analogous to the OSI model.

### Layer 1 — Physical

- PV modules (1500 V DC strings, 600 W+ per module);
- LFP / sodium-ion battery cells and modules;
- EV and e-bike packs (400–800 V DC);
- Containerized storage (20-foot ISO frames, DC bus at 400–800 V);
- DC busbars and protection (DC-rated MCBs, fuses, contactors);
- Thermal management (passive + active cooling);
- Logistics: ferry, road, rail, drone-assisted last-mile.

### Layer 2 — Link

- Packet identification (UUID, serial number, QR/NFC/RFID);
- State-of-charge metadata (SoC, SoH, cell temperature, cycle count);
- Provenance (generation source, location, timestamp, carbon intensity);
- Voltage class and connector type (CCS2, CHAdeMO, proprietary DC bus);
- Safety certification (UN 38.3, IEC 62619, UL 9540);
- Custody transfer protocol (digital handshake at charge/discharge points).

### Layer 3 — Network

- Routing by price, destination, urgency, degradation cost, and exergy quality;
- Local storage markets (peer-to-peer energy settlement);
- Multi-modal routing (ferry, road, rail, last-mile);
- Stochastic repositioning based on weather forecasting and demand prediction;
- AI-assisted dispatch (Cogentia inference layer).

### Layer 4 — Transport

- Guaranteed delivery of usable exergy above minimum SoC threshold;
- Degradation accounting (capacity fade per cycle, calendar aging);
- Loss accounting (self-discharge during transit, thermal losses);
- Failure handling and redundancy (N+1 packet reserve pools).

### Layer 5 — Application

- DC-native AI inference (GPU clusters on 48 V or 400 V DC);
- EV / e-bike fast charging;
- Water pumping and desalination;
- Refrigeration (brushless DC compressors);
- Telecom and LoRaWAN gateway power;
- Emergency power and disaster resilience;
- Heat recovery from compute workloads.

In this stack, AC is not abolished. It is treated as an **adapter protocol** at Layer 1 boundaries — the equivalent of an Ethernet-to-WiFi bridge.

---

## 7. Safety and Protection: The Primary Engineering Constraint

The strongest technical argument against DC is not efficiency. It is **arc interruption**.

AC current crosses zero 100 or 120 times per second (at 50 or 60 Hz), which naturally extinguishes arcs during circuit breaking. DC arcs are sustained: the arc does not self-extinguish, and the breaker must force current to zero by mechanically lengthening and cooling the arc channel. At high voltages (>60 V DC) and high energies (>Wh-scale batteries), DC faults can be fast, violent, and difficult to clear.

Specific engineering requirements for DC systems:

- **Voltage segmentation**: keep touch-accessible DC below 60 V (IEC 60479-1 threshold for ventricular fibrillation risk); use 48 V DC for human-accessible zones, 400 V DC only in locked enclosures;
- **Touch-safe connectors**: IEC 62196 (CCS), ISO 15118 (V2G), or proprietary designs with recessed contacts, mechanical interlock, and pre-charge resistor;
- **Pre-charge circuits**: limit inrush current when connecting capacitive DC bus segments;
- **Isolation monitoring**: continuous Insulation Monitoring Devices (IMD) per IEC 61557-8 for IT-earthed DC systems;
- **DC-rated breakers and contactors**: DC MCBs derate significantly versus AC ratings (a breaker rated 40 A AC may be rated 10–20 A at 60 V DC); specify DC-rated devices explicitly;
- **Arc flash detection**: optical arc flash detectors (response time < 1 ms) for data center and container environments;
- **Fire containment**: thermal runaway suppression for LFP (CO₂ or HFC-125 suppression, passive fire-rated enclosures);
- **Trained maintenance**: DC arc flash PPE per NFPA 70E; electricians require specific DC hazard training.

These constraints define deployment boundaries:

> DC should expand first in **engineered, supervised, modular environments** — EPN packets, ISO containers, data centers, telecom sites, farms, autonomous microgrids — not in uncontrolled domestic improvisation.

This boundary is actually a FractaVolta advantage: the EPN packet model naturally produces supervised, certified, bounded environments.

---

## 8. Regulatory Consequences

An EPN battery packet is not a public electrical distribution circuit. It is a **movable storage asset**. This legal distinction is architecturally significant.

When electricity flows through a public wire, it enters the legal domain of:
- grid operation licenses;
- network access tariffs;
- TSO balancing obligations;
- distribution system operator interconnection codes;
- regulated metering and settlement.

When energy is stored in a battery and moved as a physical object, it enters the domain of:
- product safety (IEC 62619, UN 38.3 for lithium batteries);
- transport safety (ADR road, IMDG maritime, IATA air for Li-ion);
- fire safety (NFPA 855, EN 50604-1);
- battery certification and end-of-life recycling (EU Battery Regulation 2023/1542);
- metrology for energy settlement (MID-compliant kWh metering at custody transfer points).

This is not deregulation. It is a **change of regulatory category** — from grid asset to logistics asset — that allows EPN infrastructure to develop at the edge before utility regulation fully adapts.

For FractaVolta, the immediate strategic consequence is:

> Sovereign AI inference nodes powered by physically transported battery packets are **not subject to grid interconnection codes or distribution tariffs**. They operate under product safety and logistics law — a much lighter and faster-moving regulatory regime.

---

## 9. Design Doctrine for FractaVolta Engineers

For engineers building FractaVolta nodes and packets, the practical design doctrine:

### D1 — DC-native inside every packet

Battery modules, container systems, EV-based packets, and field batteries should remain DC internally. The AC inverter is always optional and always at the boundary.

**Preferred bus voltages:**
- Cell level: 3.2 V (LFP) or 2.7–3.65 V cell range;
- Module level: 48 V nominal (16S LFP);
- Container bus: 400–800 V DC;
- Field distribution: 48 V SELV (Safety Extra-Low Voltage) for human-accessible zones.

### D2 — DC-first inside every autonomous node

PV, storage, compute, LoRa, cameras, pumps, sensors, and AI inference should share a DC backbone. AC outlets are exported services, not internal truth.

**Node design checklist:**
- [ ] MPPT charge controller with DC/DC (not AC inverter) primary path;
- [ ] 48 V DC distribution bus as spine;
- [ ] All telecom on 48 V DC (IEEE 802.3bt PoE for cameras, LoRa);
- [ ] Compute on 12 V via DC/DC from 48 V bus;
- [ ] LED lighting on 24 V DC circuit;
- [ ] Isolation monitoring (IMD) on IT-earthed 48 V bus;
- [ ] USB-C PD 3.1 ports (48 V / 240 W max) as primary human-facing DC outlets;
- [ ] AC inverter as optional boundary module, disconnectable.

### D3 — Data centers are native DC loads

The sovereign inference layer strengthens the DC case. GPU servers, UPS systems, and batteries are all DC internally. The preferred architecture for a FractaVolta inference node:

```
[PV 1500V DC] → [MPPT] → [400V DC bus]
                                 ↓
                    [LFP storage — DC coupled]
                                 ↓
                    [48V server rack bus (Open Rack v3)]
                                 ↓
                         [GPU inference servers]
```

Target: eliminate UPS AC bypass and MV transformer for a fully islanded AI node. A 400 V DC bus interfaced directly to PV MPPT and LFP storage removes two conversion stages, targeting PUE < 1.15 in Corsican ambient conditions.

### D4 — HVDC is complementary, not central

HVDC is useful where fixed corridors are justified (island interconnection, bulk renewable export). EPN is useful where corridors are absent, saturated, contested, slow, or politically captured.

For Corsica specifically: the SARCO submarine interconnection operates at 225 kV AC with limited capacity and political sensitivity. The FractaVolta thesis is that AI inference nodes powered by physically transported solar packets bypass SARCO entirely — converting solar exergy to internet-routable computation tokens without needing the cable.

### D5 — The packet is the new transformer

In the nineteenth century, the transformer made AC scalable by enabling voltage transformation across distances. In the twenty-first century, the battery packet makes DC **mobile**: it transforms temporal and spatial availability of solar exergy without requiring continuous electrical connectivity.

The FractaVolta packet is the physical instantiation of this principle: a certified, addressed, routable unit of DC exergy, compatible with the logistics network rather than the grid.

---

## 10. Conclusion

The question "How far can we return to direct current?" is misleading if framed as a nostalgic contest between Edison and Tesla.

The better formulation is:

> Once energy is packetized, how much alternating current is still structurally necessary?

The answer is: much less than before — and the quantitative case is straightforward. Each avoidable AC/DC conversion stage costs 2–5%. A FractaVolta node avoiding three stages recovers 8–12 percentage points of generated exergy. At Mediterranean irradiance, that is 0.8–1.2 kWh per node per day — enough to run a complete AI inference session from stored solar energy that would otherwise be wasted in conversion overhead.

AC remains valuable for legacy grids, public distribution, motors, appliances, and interoperability. HVDC remains valuable for bulk wired corridors where permitting and capital are available. But the EPN layer is naturally DC-native because its sources, storage media, control electronics, computational loads, and packets are DC by construction.

The EPN does not require a universal DC revolution. It requires a more precise, layered architecture:

- **DC inside packets** — the electrochemical truth of stored exergy;
- **DC inside autonomous nodes** — eliminating conversion overhead from generation through compute;
- **DC inside compute-heavy infrastructures** — 48 V rack buses, GPU direct-DC supply;
- **Hybrid AC/DC at building and community boundaries** — code compliance, legacy appliances;
- **HVDC for justified fixed transmission** — bulk corridors, island interconnection;
- **Physical packet transport where wires are saturated, unavailable, or politically captured** — the FractaVolta differentiator.

The old grid needed AC because it was a continuous synchronized circuit.

The EPN needs DC because it is a **store-and-forward network of autonomous exergy packets**.

The persistence of AC where it is no longer structurally necessary is not a technical failure. It is a case of what the companion paper [6] calls *amathia* — the Aristotelian term for the ignorance of one's own ignorance: the inability to formulate the question, not the inability to answer it. Grid engineers possess every piece of knowledge required to conceive the energy packet. What is missing is not information but the synthetic intelligence that assembles the pieces across domain boundaries. The DC-native EPN is not a technical proposal addressed to engineers who have considered and rejected it. It is a demonstration addressed to the amathia that has prevented the question from forming.

That is the real return of direct current: not as the defeated current of Edison, but as the native current of packetized sovereignty — and the engineering foundation of FractaVolta's Mediterranean inference layer.

---

## References

[1] Hughes, T.P. *Networks of Power: Electrification in Western Society, 1880–1930*. Johns Hopkins University Press, 1983.

[2] U.S. Department of Energy. *The War of the Currents: AC vs. DC Power*. energy.gov, 2014.

[3] Leiner, B.M. et al. *A Brief History of the Internet*. ACM SIGCOMM Computer Communication Review, 39(5), 2009.

[4] Robert, J.H.N. *The Unconscious Grid: On Store-and-Forward as the Repressed Solution to Energy Sovereignty*. FractaVolta, 2024. https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md

[5] Yaramasu, V. and Wu, B. *Model Predictive Control of Wind Energy Conversion Systems*. Wiley-IEEE Press, 2017.

[6] Manthiram, A. *A Reflection on Lithium-Ion Battery Cathode Chemistry*. Nature Communications, 11, 1550, 2020.

[7] Ton, M. and Fortenbery, B. *DC Power for Improved Data Center Efficiency*. Lawrence Berkeley National Laboratory, LBNL-1247E, 2008.

[8] Open Compute Project. *DCF Power Distribution LVDC White Paper*. OCP, 2026.

[9] Millan, J. et al. *A Survey on Wide Bandgap Power Semiconductor Devices*. IEEE Transactions on Power Electronics, 29(5), 2143–2163, 2014.

[10] IEC. *DC Power Distribution: Technology Trend Report*. IEC TR 63282, Geneva, 2024.

[11] IET. *Low and Extra Low Voltage Direct Current Power Distribution in Buildings*. IET Technical Briefing, 2015.

[12] NEMA. *Direct Current in Buildings*. NEMA White Paper, 2018.

[13] U.S. Department of Energy. *Connecting the Country with HVDC*. DOE Grid Modernization Series, 2023.

[14] Nardelli, P.H.J. et al. *Energy Internet via Packetized Management: Enabling Technologies and Deployment Challenges*. IEEE Access, 7, 1–15, 2019.

[15] Gelenbe, E. *Energy Packet Networks: ICT-Based Energy Allocation and Storage*. Proceedings of the 2nd International Workshop on GreenCom, 2012.

[16] IEC 60479-1. *Effects of Current on Human Beings and Livestock*. IEC, 2016.

[17] IEC 62619. *Secondary Cells and Batteries Containing Alkaline or Other Non-Acid Electrolytes — Safety Requirements for Secondary Lithium Cells and Batteries, for Use in Industrial Applications*. IEC, 2022.

[18] European Parliament. *Regulation (EU) 2023/1542 Concerning Batteries and Waste Batteries*. OJ L 191, 2023.


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Concept Index — FractaVolta](research/concepts.md)
- [Corpus Status — FractaVolta](research/corpus-status.md)
- [Research Index — FractaVolta](research/index.md)

<!-- END_AUTO: backlinks -->
