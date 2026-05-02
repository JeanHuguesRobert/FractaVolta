# FractaTera

**Fractal Terrestrial Awareness Network**

*Jean Hugues Noël Robert — Institut Mariani / C.O.R.S.I.C.A. — Corte, Corsica*  
*jhr@baronsmariani.org — github.com/JeanHuguesRobert/FractaVolta*

> Living document. Priority established by commit timestamp.  
> Challenge via issues. Fork to explore alternatives.

---

## Start Here: A Road in Corsica

A vehicle moves through the maquis at night. Somewhere ahead, a boar or a horse has crossed the road. No camera covers this stretch. No sensor is embedded in the asphalt. The animal carries no GPS. The driver has no warning.

This is not a hypothetical. It is the default condition on most of Corsica's rural network — and on most rural roads everywhere. The standard infrastructure response is: more cameras, more sensors, more centralized monitoring. This response is expensive, fragile, and arrives a decade too late for the vehicle that hit the animal tonight.

FractaTera proposes the opposite: a distributed perception system that uses the devices already present in the environment — vehicles, smartphones, low-cost radio tags — and extracts useful inference from their interactions, without requiring any individual device to be precise.

The core insight:

> **Motion transforms noise into structure.**

A stationary receiver sees a static noise floor. A moving vehicle passing near a tagged animal sees the signal rise and fall — a characteristic signature that, combined with GPS velocity and heading, yields a probabilistic proximity estimate. No single observation is reliable. A thousand such observations, aggregated across a network of moving vehicles, produce a real-time risk map of the territory.

This is FractaTera: distributed probabilistic awareness from existing devices, continuously revised, never exact, always useful.

---

## The Name

*Fractal* — the same structure at every scale. A single vehicle, a local cluster of vehicles, a territorial network: each applies the same sensing and inference logic, rescaled by density.

*Terra* — the earth, the land. FractaTera is grounded in physical territory: roads, landscapes, the actual movement of animals and vehicles and energy units through a specific place.

---

## Core Principle: Motion Structures Noise

Traditional sensing asks: *what is the exact position of object X?* This requires precise, synchronized, infrastructure-heavy measurement.

FractaTera asks instead: *is object X probably near location Y, within the next few minutes, with sufficient confidence to trigger a warning?* This requires only:

- a signal that varies with proximity (radio, optical, acoustic)
- a receiver whose own position and velocity are known
- enough receivers passing through the territory over time

The mathematics of this are well understood in radar theory and mobile sensing literature. What FractaTera contributes is the architectural principle: **consumer-grade devices deployed at territorial scale, with no dedicated infrastructure, can collectively produce useful probabilistic awareness** — provided the inference layer is designed for uncertainty rather than precision.

Uncertainty is not a degraded form of precision. It is the native representation of a distributed, asynchronous observation system. A probability field of animal presence, continuously updated as new vehicles pass, is strictly more honest than a point estimate that pretends to precision it does not have.

---

## Architecture

FractaTera is layered. Each layer has a defined responsibility and a defined interface to the layers above and below.

### Physical layer

Everything that moves or emits: vehicles, animals with beacon tags, mobile energy containers, smartphones, embedded low-cost radios. The physical layer is not designed or deployed by FractaTera — it is the territory as it already exists. FractaTera observes it.

### Perception layer

Signal capture: radio intensity variation (BLE, LoRa-class), GPS trajectory streams, temporal drift patterns, opportunistic proximity inference. The perception layer does not interpret signals — it records them with timestamps and position anchors, and passes them upward.

### Communication layer

Hybrid and opportunistic: cellular when available (backbone), device-to-device radio exchange when not, delayed synchronization when connectivity resumes. The design assumption is **intermittent connectivity** as the norm, not the exception. A system that requires continuous network access is fragile in exactly the environments FractaTera targets.

### Inference layer

The core computation: noisy signals → probabilistic fields, partial observations → trajectory estimates, sparse measurements → continuous risk models. The inference layer runs at the edge — on the vehicle's phone — and aggregates locally before contributing to the territorial model. Full centralization is neither required nor desirable: the territorial model is a consensus of distributed inferences, not a query against a central database.

### Application layer

Domain-specific instantiations built on the territorial probability field. Two are described below; the architecture supports others.

---

## Fractal Operating Model

The same logic applies at every scale, with density as the scaling parameter:

| Scale | Node count | Inference quality | Primary function |
|-------|-----------|-----------------|-----------------|
| Device | 1 | Single observation | Local warning |
| Local cluster | 10–100 | Situational awareness | Route-level risk map |
| Territory | 100–10,000 | Probabilistic field | Regional coordination |
| Network | 10,000+ | Aggregated learning | Pattern detection, optimization |

A single vehicle with a beacon receiver provides local warning. Ten vehicles on the same road provide situational awareness. A thousand vehicles across a territory produce a live risk map. The system improves continuously with density — no minimum threshold is required to be useful, and no maximum density degrades it.

---

## VIGILIA: Animal-Vehicle Collision Avoidance

VIGILIA is the first operational instantiation of FractaTera, designed for the specific conditions of Corsican rural roads.

**The problem.** Corsica has approximately 40,000 semi-wild animals (horses, cattle, pigs, boars) with customary rights of way on public roads. Collisions cause deaths, serious injuries, and significant economic loss annually. Conventional solutions — fencing, reflectors, warning signs — address a linear infrastructure problem with linear infrastructure responses. They do not scale to a territory where animals move freely and roads are everywhere.

**The approach.** Animals are equipped with low-cost, long-life beacon tags (BLE or LoRa-class, solar-charged where feasible). Vehicles carry a smartphone application that listens passively for beacon signals while driving. Each detection is processed locally: signal strength variation over the vehicle's trajectory yields a proximity estimate. When the estimate crosses a risk threshold, the driver receives a warning — not "an animal is at GPS coordinate X" but "an animal is probably within 200 meters ahead, confidence 80%."

**Why this works where cameras do not.** A camera covers a fixed point. An animal-vehicle encounter can happen anywhere on thousands of kilometers of road. VIGILIA's coverage scales with the number of participating vehicles — which is already large and growing without any infrastructure investment. Every new vehicle improves coverage for every other vehicle.

**The trace dimension.** Every detection event is a signed trace: vehicle identifier (pseudonymized), timestamp, signal characteristics, GPS position, derived risk estimate. These traces feed the territorial model and, aggregated over time, reveal patterns: habitual crossing zones, seasonal migration corridors, high-risk time windows. The trace record is also the evidence base for governance decisions — where to invest in fencing, which roads to target for speed reduction, how to allocate public funds.

This is where FractaTera connects to `traceable_governance.md`: the territorial awareness map is not just a safety tool. It is a governed, auditable record of the territory's physical behavior, produced by distributed observation, verifiable at every scale.

---

## Mobile Resource Tracking

The second application class: tracking mobile assets whose position matters but whose exact location need not be known at all times.

Target assets: swappable electric vehicle batteries, mobile energy storage containers, logistics units in transit, the 1m³ self-storage coffres of the kind deployed for student and tourist markets.

**The method.** Each asset carries a beacon. As vehicles and fixed infrastructure nodes pass nearby, they log detections. Over time, the aggregated detection record produces a probabilistic trajectory — not a live GPS track, but a useful model of where the asset probably is and where it has been.

**Why this matters economically.** A battery container whose location is known within 500 meters and 30 minutes is recoverable. One whose location is unknown is lost. The difference between a functional mobile energy network and an expensive experiment in battery abandonment is exactly this: probabilistic tracking at low infrastructure cost.

**The CXU connection.** Mobile energy units that are tracked generate a provenance record — their location history is part of the energy trace that feeds into CXU certification. A battery that moved from a solar farm in Corsica to a compute cluster, with a continuous detection record along the way, contributes to the η_traceability score of the inferences that battery powered. See `safe_compute_exergy.md`.

---

## Resilience by Design

FractaTera assumes that individual components fail, connectivity drops, and devices are replaced. Robustness is not a property of any individual node — it emerges from the density and diversity of the network.

Specific properties:

- **No single point of failure.** The territorial model degrades gracefully as nodes drop out; it does not collapse.
- **Density monotonicity.** Adding nodes never degrades performance. Coverage and inference quality improve monotonically with participation.
- **Connectivity tolerance.** Useful local inference runs with no network at all. Territorial aggregation requires only intermittent synchronization.
- **Heterogeneity tolerance.** Beacon tags from different manufacturers, phones of different generations, vehicles of different types — all contribute to the same inference layer without requiring standardization at the hardware level.

---

## Ethical Constraints

FractaTera is designed to be non-coercive and non-destructive.

Animal beacon tags are designed for welfare: lightweight, solar-charged, no behavioral modification. The system warns drivers; it does not constrain animals.

Vehicle participants are pseudonymized at the perception layer. Individual trajectories are not stored centrally. The territorial model is an aggregate — it reveals where animals tend to cross roads, not where a specific vehicle was at a specific time.

The principle: **replace constraint with awareness**. A system that makes risk visible reduces the need for enforcement, fencing, or elimination.

---

## Open Problems

**Beacon adoption.** VIGILIA works at territorial scale only if enough animals are tagged. Initial deployment requires coordination with pastoral communities and landowners. The governance of this coordination is not specified here.

**Pseudonymization and re-identification.** Vehicle trajectories, even pseudonymized, can potentially be re-identified from distinctive patterns. The privacy guarantees of the perception layer require formal analysis.

**Inference calibration.** The relationship between signal variation and proximity depends on terrain, vegetation, weather, and hardware. Calibration requires field data from Corsican environments specifically.

**Beacon durability.** Semi-wild animals in Corsican maquis subject beacons to conditions that laboratory testing does not replicate. Field durability data is needed.

**Governance of the territorial model.** Who owns the aggregate map? Who can query it? Who can challenge an inference? These questions are addressed by the framework in `traceable_governance.md` but require instantiation for the specific context of territorial safety data.

---

## Status

| Component | Status |
|-----------|--------|
| Core sensing model | Formalized conceptually |
| VIGILIA — animal collision avoidance | Designed, not yet deployed |
| Mobile resource tracking | Designed, not yet deployed |
| Beacon hardware specification | Pending |
| Inference calibration (Corsica) | Pending field data |
| Governance integration | Framework in `traceable_governance.md` |
| CXU provenance link | Specified in `safe_compute_exergy.md` |

---

*License: CC BY-SA 4.0 — Priority established by first commit timestamp.*
