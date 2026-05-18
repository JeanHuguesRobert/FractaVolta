---
title: "Guaranteed Inference"
subtitle: "A Resilient, Routable and Traceable Fallback Layer for Critical AI Workloads"
description: "FractaVolta as an ARPANET-like architecture for critical AI inference: guaranteed capacity, inference switching, provenance, CXU and territorial resilience."
layout: default
nav_order: 1
version: "0.3-market"
last_modified_at: "2026-05-18"
author: "Jean Hugues Noël Robert"
affiliation: "FractaVolta — Institut Mariani / C.O.R.S.I.C.A."
license: "CC BY-SA 4.0 (text), MIT (code and schemas)"
repository: "github.com/JeanHuguesRobert/FractaVolta"
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/garanteed_inference.md
last_stamped_at: 2026-05-18
---

# Guaranteed Inference

## A Resilient, Routable and Traceable Fallback Layer for Critical AI Workloads

**Jean Hugues Noël Robert**  
**FractaVolta — Applied research toward territorially grounded, verifiable and resilient AI infrastructure**

Version: `0.3-market`  
Date: 18 May 2026  
Status: Draft for critical review

---

## Executive Summary

Organizations are beginning to depend on AI inference as an operational layer.

Today, most inference is bought as a commodity: API calls, tokens, throughput, latency, subscription plans. Hyperscalers are excellent at this normal-condition market. They optimize for scale, utilization, price, latency and global availability.

But critical systems require something different.

They require **assured inference capacity**: the ability to produce a necessary inference when normal optimized infrastructure is unavailable, degraded, politically constrained, economically repriced, energy-constrained or operationally opaque.

This working paper proposes **Guaranteed Inference** as a new infrastructure category.

FractaVolta does not aim to compete with hyperscalers on raw scale or normal-condition efficiency. It aims to complement them with a resilient fallback layer for critical inference workloads.

The strategic analogy is ARPANET.

ARPANET did not merely optimize telecommunications. It changed the architecture of communication by introducing resilient, distributed, routable packets instead of relying only on centralized circuits.

FractaVolta proposes the equivalent direction for AI inference:

> AI inference requests should become routable units, not blind API calls.

This requires an **Inference Switching Layer** able to route workloads across hyperscalers, sovereign clouds, local nodes, edge devices, smaller fallback models, cached responses, delayed batch execution or human-in-the-loop escalation.

The customer does not buy a cheaper model.  
The customer buys assurance that a critical inference can still be produced.

Within this broader offer:

- **Inference Provenance** records the physical, energetic, computational and governance conditions under which an inference was produced.
- **CXU — Compute eXergy Unit** is an experimental accounting unit linking useful energy, compute, resilience, locality and auditability.
- **Territorial Inference Nodes** convert local energy, storage and compute into resilient inference capacity.
- **FractaVolta** positions itself as an impact startup for territories and critical operators seeking operational resilience, digital sovereignty and auditable infrastructure.

Core positioning:

> **Hyperscale for efficiency. FractaVolta for guaranteed critical inference.**

---

## 1. The Problem: AI Inference Becomes a Critical Dependency

AI inference is no longer an occasional experiment.

It is becoming embedded into:

- scientific workflows;
- administrative services;
- public decision support;
- health and social systems;
- logistics;
- infrastructure monitoring;
- energy management;
- emergency response;
- industrial operations;
- legal and compliance workflows;
- knowledge management;
- agentic automation.

Training remains concentrated and episodic. Inference becomes continuous and demand-driven.

This changes the risk profile.

An organization that integrates AI deeply into its workflows eventually faces a simple operational question:

> What happens when the inference layer fails?

Failure can take several forms:

- API outage;
- degraded latency;
- provider rate limits;
- sudden price increase;
- geopolitical restriction;
- data jurisdiction issue;
- energy constraint;
- network partition;
- model withdrawal;
- vendor lock-in;
- regulatory non-compliance;
- unavailable audit trail;
- loss of trust in the output chain.

In normal conditions, hyperscale providers are efficient and convenient. But critical infrastructure cannot rely only on normal conditions.

The relevant question becomes:

> Who guarantees inference capacity when optimized infrastructure is insufficient?

---

## 2. Why Hyperscale Alone Is Not Enough

Hyperscalers are not the enemy. They are the normal-condition backbone of AI inference.

They are good because they optimize:

- massive utilization;
- low marginal cost;
- high throughput;
- global deployment;
- model availability;
- developer experience;
- economies of scale.

But this optimization hides the real cost of resilience.

The price of an API call is not the price of guaranteed capacity under stress.

The analogy is simple:

> Nobody buys a backup generator because it is cheaper than the grid.  
> They buy it because the grid can fail.

The same logic applies to AI inference.

Nobody will buy FractaVolta because it is cheaper than hyperscale inference in normal conditions.

They will buy it because critical AI workflows should not depend entirely on opaque, remote, optimized infrastructure.

The market currently sells optimized inference endpoints.

FractaVolta proposes to develop:

> **routable, resilient, traceable inference capacity.**

---

## 3. What FractaVolta Sells

FractaVolta does not sell cheaper inference.

FractaVolta sells **guaranteed critical inference capacity**.

This means:

1. **A routing layer for AI inference**  
   Inference requests are routed according to operational policy, not blindly sent to one endpoint.

2. **Reserved fallback capacity**  
   Critical workloads have defined fallback paths when primary providers fail or become unsuitable.

3. **Territorial inference nodes**  
   Local or regional nodes provide physically grounded inference capacity.

4. **Provenance records**  
   Each critical inference can leave a trace of where, how, with what energy, under what route and under what proof level it was produced.

5. **Energy and resilience auditability**  
   The physical capacity behind inference is measured, estimated, matched, contracted or physically coupled depending on the proof level.

6. **Degraded-mode operation**  
   When the best model or provider is unavailable, the system can route toward a smaller model, cached answer, local model, delayed response or human-in-the-loop process.

7. **Integration with existing hyperscaler workflows**  
   FractaVolta complements hyperscale infrastructure. It does not require customers to abandon it.

The product category can be summarized as:

> **Guaranteed Inference Infrastructure**

or:

> **Resilient AI Inference Capacity**

---

## 4. Target Buyers

The primary target is not the general AI market.

The target buyer is an actor for whom inference failure has a real cost and who has the power to act: budget, mandate, infrastructure, regulatory authority or operational responsibility.

### 4.1 Critical infrastructure operators

Examples:

- energy operators;
- telecom operators;
- transport infrastructure;
- ports and airports;
- water systems;
- emergency and civil protection networks.

Their concern:

> AI is entering operational systems. We cannot let it become an unplanned single point of failure.

### 4.2 Public territorial authorities

Examples:

- regions;
- islands;
- mountain territories;
- energy syndicates;
- public digital agencies;
- local resilience agencies.

Their concern:

> The territory becomes dependent on infrastructures it does not control.

Relevant concept:

> **autonomy of capacity**

### 4.3 Research infrastructure

Examples:

- laboratories;
- universities;
- scientific computing centers;
- observatories;
- field research stations.

Their concern:

> Scientific inference must be traceable, reproducible and operationally available.

### 4.4 Regulated industries

Examples:

- banking;
- insurance;
- health;
- legal services;
- aviation;
- maritime;
- industrial safety.

Their concern:

> We need auditability, continuity and fallback for AI-supported decisions.

### 4.5 Energy and data center actors

Examples:

- regional data centers;
- edge compute operators;
- renewable producers;
- battery operators;
- microgrid operators;
- industrial sites with energy and land.

Their concern:

> How do we transform local energy capacity into higher-value digital services?

---

## 5. The ARPANET Analogy

The FractaVolta thesis is best understood through the ARPANET analogy.

Legacy telecommunications relied on circuit-like assumptions: centralized infrastructure, reserved paths, fragile dependencies.

ARPANET reframed communication as packet-based, distributed and resilient.

For AI today, the dominant pattern is still endpoint-centric:

```text
client → provider API → model output
```

This is simple, efficient and productive.

But it is weak for critical use.

A resilient inference network would treat inference requests as routable units, with constraints attached to them:

- required capability;
- acceptable latency;
- confidentiality level;
- jurisdiction requirement;
- energy provenance requirement;
- resilience level;
- audit requirement;
- cost ceiling;
- degraded-mode tolerance;
- human-in-the-loop requirement.

The system can then decide how to route the request:

```text
critical inference request
    → normal hyperscaler endpoint
    → sovereign cloud fallback
    → regional inference node
    → local edge model
    → smaller degraded-mode model
    → cached/RAG-supported answer
    → delayed batch inference
    → human escalation
```

This is not only technical routing.

It is operational governance.

---

## 6. Inference Switching Layer

FractaVolta proposes an **Inference Switching Layer**.

Its role is to route inference demand across heterogeneous compute and energy resources according to policies.

### 6.1 Basic functions

The layer should support:

- provider abstraction;
- route selection;
- fallback execution;
- degraded-mode policy;
- capacity reservation;
- provenance generation;
- audit logging;
- cost and energy estimation;
- jurisdiction constraints;
- human-in-the-loop escalation.

### 6.2 Policy examples

Example 1 — Normal non-critical workload:

```text
Use cheapest provider meeting latency and quality constraints.
No local fallback required.
Proof Level 0 sufficient.
```

Example 2 — Sensitive public administration workload:

```text
Use sovereign or territorial route if available.
Fallback to approved provider.
Metadata-only provenance required.
Proof Level 2 minimum.
```

Example 3 — Emergency response workload:

```text
Use fastest available route.
If network degraded, use local edge model.
If confidence below threshold, escalate to human.
Proof Level 3 or 4 preferred.
```

Example 4 — Scientific record:

```text
Record model, route, energy zone, timestamp, token/task metrics and provenance hash.
Proof Level 2 minimum.
Proof Level 4 for critical reproducibility studies.
```

### 6.3 Architectural principle

The system should not assume one perfect provider.

It should assume:

- heterogeneity;
- partial failure;
- uncertain costs;
- variable energy;
- jurisdictional constraints;
- different levels of model capability;
- the need for traces.

This is the ARPANET lesson applied to inference.

---

## 7. Inference Provenance

**Inference Provenance** is the proof layer of Guaranteed Inference.

It is not the product by itself. It is what makes the operational guarantee auditable.

A provenance record answers:

1. What inference was produced?
2. By which model or model class?
3. Through which route?
4. On which compute infrastructure?
5. At what time?
6. In which location or energy zone?
7. With what measured or estimated energy consumption?
8. With what carbon intensity?
9. With what water intensity, where relevant?
10. With what energy source or allocation proof?
11. With what storage or routing context?
12. Under what quality-of-service condition?
13. Under what governance and audit regime?

### 7.1 Provenance layers

A robust provenance model should include:

| Layer | Description |
|---|---|
| Energy production | Source or contractual allocation of energy |
| Storage | Battery, reservoir, mobile storage or other buffer |
| Routing | Grid, microgrid, off-grid, mobile energy path |
| Compute execution | Hardware, utilization, power, cooling, latency |
| Model and workload | Model class, task type, tokens where relevant |
| Governance | signatures, audit, proof level, retention policy |

### 7.2 Privacy principle

A provenance record should not store private prompt content by default.

The default mode should be:

> metadata-only provenance

The system should prove the conditions of inference without exposing confidential content unless explicitly required and legally justified.

---

## 8. Proof Levels

Different customers require different levels of proof.

| Level | Name | Description | Typical use | Verifiability |
|---|---|---|---|---|
| 0 | Estimate | Public or provider estimates only | Awareness | Low |
| 1 | Measured execution | Local telemetry for compute energy | Internal reporting | Medium |
| 2 | Energy-zone matched | Time and location matched with grid data | Carbon-aware routing | Good |
| 3 | Contractual provenance | Linked to contracts, certificates or storage allocation | Regulated reporting | Strong |
| 4 | Physical-territorial | Physically coupled local energy, storage and compute | Sovereign or territorial resilience | Very strong |
| 5 | Audited sovereign | Full chain independently audited, including governance | Critical public-interest use | Maximum |

This table is deliberately incremental.

It avoids overclaiming.

On a shared grid, individual electrons cannot be traced. But inference can still be measured, matched, contractually allocated or physically coupled depending on the proof level.

FractaVolta's long-term target zone is Level 4 and Level 5.

Its MVP can start at Level 0, 1 or 2.

---

## 9. CXU — Compute eXergy Unit

### 9.1 Why exergy?

Energy tells how much energy is involved.

Exergy tells how much useful physical capacity is available to perform work.

AI inference is not only an energy consumer. It is a transformation chain:

```text
photons → electrons → stored energy → compute → inference → decision/action
```

For FractaVolta, the strategic framing is:

> From photons to inferences.

The point is not to export raw kilowatt-hours.  
The point is to transform local energy into high-value, traceable digital capacity.

### 9.2 Preliminary definition

**CXU — Compute eXergy Unit** is a proposed experimental unit for expressing the useful physical capacity mobilized to produce AI inference.

It is not a cryptocurrency.  
It is not a speculative token.  
It is not a finished standard.  
It is not a replacement for carbon accounting.

It is a research direction for connecting:

- useful energy;
- hardware efficiency;
- system efficiency;
- storage and routing losses;
- carbon intensity;
- water intensity where relevant;
- quality of service;
- resilience;
- locality;
- governance confidence;
- auditability.

### 9.3 Candidate expression

A first simplified expression could be:

```text
CXU ≈ E_useful × η_hw × η_sys × η_sla × C_governance
```

Where:

- `E_useful` represents useful energy mobilized for the inference;
- `η_hw` represents hardware efficiency;
- `η_sys` includes cooling, storage, routing and operational overhead;
- `η_sla` represents availability and resilience quality;
- `C_governance` represents confidence in the trace and governance process.

This must remain experimental until tested against real workloads.

---

## 10. Territorial Inference Nodes

A **Territorial Inference Node** is a local or regional node combining:

- renewable or contracted low-carbon energy;
- storage;
- compute;
- telemetry;
- routing integration;
- provenance logging;
- optional local AI models;
- operational governance.

It can begin small.

Examples:

- municipal building;
- containerized node;
- mountain site;
- island site;
- research station;
- public safety facility;
- energy cooperative site;
- heritage or environmental monitoring site.

The node does not need to beat hyperscalers in normal conditions.

Its function is to provide:

- fallback;
- locality;
- auditability;
- resilience;
- proof;
- learning;
- territorial capacity building.

---

## 11. Corsica as Pilot Territory

Corsica is a relevant pilot territory because it combines:

- strong solar potential;
- island constraints;
- grid limitations;
- seasonal peaks;
- mountain geography;
- water and energy tensions;
- public-service fragility;
- political demand for autonomy;
- symbolic Mediterranean position.

The goal is not isolation.

The goal is to demonstrate a model for territories that cannot or should not depend entirely on remote hyperscale infrastructures.

Relevant territories include:

- islands;
- mountains;
- rural regions;
- constrained grids;
- border territories;
- strategic public-service territories;
- territories seeking digital and energy sovereignty.

Strategic claim:

> Corsica should not merely consume imported digital services or export raw energy.  
> It can transform its sun, water, relief and storage capacity into guaranteed inference capacity.

---

## 12. MVP Proposal

A credible MVP should be small, measurable and publishable.

### 12.1 MVP name

**FractaVolta Guaranteed Inference MVP**

### 12.2 Components

1. Cloud inference endpoint.
2. Local fallback inference endpoint.
3. Routing policy engine.
4. Energy/carbon estimation module.
5. Optional hardware telemetry module.
6. Electricity-zone data connector.
7. Provenance JSON record.
8. Append-only hash-chained log.
9. Experimental CXU score.
10. Markdown session report.

### 12.3 Per-inference output

```text
Inference ID: ...
Timestamp: ...
Task type: ...
Primary route: ...
Fallback route: ...
Model class: ...
Energy zone: ...
Estimated energy: ... Wh
Estimated carbon: ... gCO2e
Proof level: 0 / 1 / 2
CXU experimental score: ...
Record hash: ...
```

### 12.4 What the MVP proves

The MVP proves three things:

1. An inference request can be routed, not merely sent.
2. A critical fallback can be defined and executed.
3. Each inference can produce a trace.

That is enough for a first applied research milestone.

---

## 13. Business Model Options

### 13.1 Open-core protocol

The routing and provenance schema can be open source.

Commercial value comes from:

- deployment;
- managed API;
- integration;
- certification;
- physical node design;
- audit tooling;
- territorial reporting;
- operational support.

This is compatible with a Red Hat-like model:

> open protocol, paid expertise.

### 13.2 API subscription

A hosted API can provide:

- route selection;
- fallback logic;
- provenance generation;
- audit trail storage;
- reporting;
- integration with customer AI workflows.

Customers pay for:

- volume;
- retention;
- capacity reservation;
- fallback options;
- compliance exports;
- support levels.

### 13.3 Territorial deployment services

For territories and infrastructure operators, FractaVolta can provide:

- feasibility studies;
- node architecture;
- energy-compute coupling;
- telemetry setup;
- governance framework;
- open-source implementation;
- training;
- monitoring.

### 13.4 Verified inference capacity

The strategic endpoint is to sell:

> inference with guaranteed fallback and provenance.

This is not commodity inference.

It is capacity assurance.

---

## 14. Relationship to Existing Markets

### 14.1 AI carbon observability

These platforms measure cost, energy and carbon per request, model, provider or token.

They validate the market need.

FractaVolta differs by focusing on guaranteed capacity, fallback, provenance and territorial infrastructure.

### 14.2 Cloud carbon dashboards

Hyperscalers provide useful customer-facing carbon data.

But the data remains provider-controlled.

FractaVolta aims for portable, independent and auditable records.

### 14.3 GreenOps and FinOps

GreenOps and FinOps optimize cloud operations.

FractaVolta complements them with:

- resilience;
- fallback;
- provenance;
- territorial capacity.

### 14.4 Energy certificate systems

Some systems certify renewable energy or tokenize energy claims.

FractaVolta should avoid speculative framing.

The relevant object is not a speculative energy token.

The relevant object is a traceable inference event and the capacity behind it.

---

## 15. Strategic Principles

### 15.1 Do not pretend to beat hyperscalers in normal conditions

Hyperscalers are optimized for normal operation.

FractaVolta's value is the complementary layer:

- fallback;
- resilience;
- provenance;
- locality;
- autonomy of capacity.

### 15.2 Do not start with blockchain

Start with logs, hashes, provenance, audit and infrastructure.

Blockchain-like mechanisms may become useful later.

They are not the starting point.

### 15.3 Do not overclaim traceability

On a shared grid, individual electrons cannot be traced.

Claims must be framed honestly:

- estimated;
- measured;
- matched;
- contractually allocated;
- physically coupled;
- independently audited.

### 15.4 Keep CXU experimental

CXU should be presented as a research hypothesis until validated by real workloads.

### 15.5 Start small

A small node with honest telemetry is more credible than a large theoretical architecture.

### 15.6 Keep humans in governance

AI agents can help read, criticize, synthesize and operate.

Binding governance remains human.

This links FractaVolta to the broader DHITL principle:

> Democratic Humans In The Loop.

---

## 16. First Implementation Tasks

1. Create `guaranteed_inference.md`.
2. Create `/schemas/inference_provenance.schema.json`.
3. Implement a minimal inference router.
4. Support two routes: cloud primary and local fallback.
5. Generate one provenance JSON record per inference.
6. Add hash chaining.
7. Add grid carbon data connector.
8. Add optional hardware telemetry.
9. Generate Markdown session reports.
10. Define CXU v0.1.
11. Define Inference Switching Layer v0.1.
12. Publish uncertainty and known limits.

---

## 17. Minimal Provenance Schema

```json
{
  "schema_version": "0.3",
  "inference_id": "uuid",
  "timestamp_utc": "ISO-8601",
  "operator": "FractaVolta or partner",
  "use_case": "public-interest / research / commercial / internal",
  "model": {
    "provider": "string",
    "model_id": "string",
    "model_class": "text / multimodal / embedding / agentic",
    "disclosure_level": "public / partial / confidential"
  },
  "routing": {
    "primary_route": "string",
    "fallback_route": "string",
    "routing_policy": "string",
    "degraded_mode_allowed": true,
    "human_in_the_loop_required": false
  },
  "execution": {
    "site_id": "string",
    "region": "string",
    "energy_zone": "string",
    "hardware_class": "string",
    "measured_energy_wh": null,
    "estimated_energy_wh": null,
    "cooling_overhead_factor": null
  },
  "energy": {
    "source_claim": "grid / solar / hybrid / contractual / physical-coupled",
    "carbon_intensity_gco2e_kwh": null,
    "water_intensity_ml_kwh": null,
    "storage_used": false,
    "storage_context": null,
    "matching_method": "none / hourly / contractual / physical"
  },
  "provenance": {
    "proof_level": 0,
    "data_sources": [],
    "audit_status": "none / internal / third-party",
    "record_hash": "string",
    "previous_hash": "string"
  },
  "cxu": {
    "cxu_version": "0.1",
    "cxu_estimate": null,
    "uncertainty": null
  }
}
```

---

## 18. Link to the Second Method

This market-oriented document deliberately keeps the Second Method in the background.

However, FractaVolta belongs to a broader corpus in which:

- agents may participate in knowledge production;
- objections are first-class objects;
- forks and issues are welcomed;
- git history is part of the proof;
- governance remains human;
- infrastructure claims must produce traces.

A companion document should be created:

```text
guaranteed_inference_second_method.md
```

Its role:

- document the epistemic process;
- preserve objections;
- connect to `DHITL.md`;
- connect to Cogentia;
- describe how AI agents contribute without governing;
- make the corpus itself auditable.

The present document answers:

> What is the operational and commercial proposition?

The companion document answers:

> How is the proposition produced, criticized, improved and governed?

---

## 19. Key Phrases

- Hyperscale for efficiency. FractaVolta for guaranteed critical inference.
- FractaVolta does not sell cheaper inference. It sells assured critical inference capacity.
- The market sells optimized inference endpoints. FractaVolta develops routable, resilient inference capacity.
- AI inference requests should become routable units, not blind API calls.
- The customer does not buy a model. The customer buys assurance that a critical inference can still be produced.
- Inference provenance is not the product. It is the proof layer of guaranteed inference.
- Carbon measures footprint. Exergy measures useful capacity. Provenance measures trust.
- Nobody buys a backup generator because it is cheaper than the grid. They buy it because the grid can fail.
- The future of AI infrastructure is not only larger data centers. It is also resilient, distributed, auditable inference capacity.
- From photons to inferences.

---

## 20. Conclusion

AI inference is becoming operational infrastructure.

The first market response is optimization: cheaper tokens, faster APIs, better models, better utilization.

The second response is observability: cost, energy, carbon, water, telemetry.

These are necessary.

They are not sufficient for critical uses.

Critical AI requires guaranteed inference capacity: routable, resilient, traceable and governable.

FractaVolta's thesis is that territories can become producers of such capacity by coupling local energy, storage, compute, routing and provenance.

This is not anti-hyperscale.

It is post-naive hyperscale.

Normal conditions require efficiency.

Critical conditions require resilience.

FractaVolta's space is the layer between the two:

> an ARPANET-like infrastructure for critical AI inference.
