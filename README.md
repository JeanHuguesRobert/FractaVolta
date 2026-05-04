# FractaVolta

**Physical inference, fractal governance, and the value of provenance**

> From photons to inferences

*Jean Hugues Noël Robert, baron Mariani — Institut Mariani / C.O.R.S.I.C.A.*

*1 cours Paoli, F-20250 Corte, Corsica*  

*jhr@baronsmariani.org — github.com/JeanHuguesRobert — fractavolta.com*

> This repository is a living design space, not a finished product.  
> Priority of ideas is established by commit timestamp.  
> Challenge anything via issues. Fork to explore alternatives.

---

## What FractaVolta Is

FractaVolta is an **open-core impact startup** developing distributed infrastructure for physical sensing, certified inference, and fractal governance of energy and mobility systems.

The business model is territorial and deliberate:

> What is built pro bono in Corsica becomes a paid service elsewhere.  
> Revenue generated outside Corsica funds the open infrastructure built inside it.

Corsica is the proof-of-concept territory — island grid isolation, low infrastructure density, mixed mobility environments, strong sovereignty aspirations. Its constraints are extreme by design, which makes it the ideal stress test for any distributed energy-sensing architecture. What works in Corsica works anywhere.

FractaVolta is the commercial and deployment arm of the [MareNostrum](https://github.com/JeanHuguesRobert/marenostrum) framework. It constitutes **Layer 1 (Physical/Energy)** of the [DHITL architecture](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md) for distributed AI governance.

**Shareholders:** Jean Hugues Noël Robert (80%), C.O.R.S.I.C.A. association loi 1901 (20%).  
The 20% stake ensures that net revenues flow structurally — not voluntarily — toward the Corsican public mission.

---

## The Problem

Physical reality is not directly measured. It is inferred — from photons, radio signals, thermal gradients, motion patterns, partial observations. Every sensor is imperfect. Every network is intermittent. Every measurement carries uncertainty.

Standard infrastructure responds to this by demanding more sensors, more bandwidth, more centralization. FractaVolta goes the other way:

> Physical systems do not need to be fully measured to be understood.  
> They can be governed from weak signals, distributed observation, and verified provenance.

The word "governed" is deliberate. The gap between sensing and action is not only technical — it is political. Who certifies a measurement? Who arbitrates a conflict between two sensors? Who decides when inference is good enough to act on? These are governance questions, and they need governance answers.

FractaVolta addresses the full chain: from photon to inference, from inference to certified value, from certified value to democratic accountability.

---

## The Name

*Fractal* — the same structure repeating at every scale. A node, a cluster, an island federation, a Mediterranean network: each governed by the same mechanism, rescaled but not redesigned.

*Volta* — turn, cycle (Italian/Corsican). Also: Alessandro Volta, whose work on electrical potential gave us the unit of electromotive force. Both readings apply. FractaVolta is about recursive governance cycles applied to the flow of energy and information.

---

## Three Layers

FractaVolta is structured as three interdependent layers, each documented in a dedicated file.

### Physical layer — distributed sensing and inference

The world emits signals constantly: electromagnetic, thermal, kinetic. Consumer devices — smartphones, vehicles, embedded radios — can act as distributed sensors, capturing signal variation, temporal drift, and motion-induced distortion.

The key insight is that **motion transforms noise into structure**. A stationary sensor sees a static noise floor. A moving sensor sees the geometry of the field it traverses. Distributed moving sensors, aggregated probabilistically, reconstruct reality without requiring any individual sensor to be precise.

Applications: collision avoidance, territorial risk mapping, mobility coordination, distributed energy tracking, logistics visibility. The inference target is not a perfect model of reality — it is a *usable* model, good enough to act on, continuously revised as new signals arrive.

See `tera.md` for the FractaTera reference architecture.

### Governance layer — fractal traceability

Distributed inference raises an immediate governance problem: how do you trust a measurement you did not make? How do you audit a decision whose inputs are distributed across hundreds of nodes you do not control?

The answer proposed here is to replace secrecy-based security with **traceability-based trust**. Every action is recorded in an append-only log. Logs are aggregated up the scale tower using Merkle trees: a higher level can verify the integrity of a lower level without reading its content. Privacy and accountability coexist because traceability applies to *actions*, not to data content.

The governance structure is fractal: the same audit interface at every level, from individual node to Mediterranean network. A citizen who understands governance at the cluster level understands it at the regional level by substitution. Governance literacy does not increase with scale — this is the democratic dividend of fractality.

See `traceable_governance.md` for the formal model.

### Economic layer — the value of provenance

A certified inference is worth more than an uncertified one. This is not a marketing claim; it is a structural property.

An inference whose entire energy provenance chain is cryptographically attested — from solar photon to output token — is a qualitatively distinct product. The attestation chain is the premium. Without it, "green AI" is a label. With it, it is a proof.

The Compute eXergy Unit (CXU) formalizes this: usable compute denominated in verified energy, hardware efficiency, SLA compliance, and provenance completeness. A CXU with complete provenance commands a Sovereign-tier premium. A CXU with no provenance chain approaches zero certified value by definition — not by penalty.

The Mediterranean deployment context (Corsica, Sardinia, Sicily, North Africa) makes this concrete: solar surplus converted to Sovereign-tier certified inference, held on the island as a high-value asset rather than exported as undifferentiated electricity through congested interconnections.

See `safe_compute_exergy.md` for the full CXU specification.

---

## How the Layers Connect

```
Physical layer           Governance layer          Economic layer
──────────────────       ─────────────────────     ──────────────────────
Solar panel meters  →    τ_solar signed        →   provenance link added
Compute node runs   →    τ_compute signed       →   provenance link added
Inference produced  →    τ_inference signed     →   CXU issued at tier T
                         Merkle root published
                         Regulator verifies L2
                         without reading L0
```

The physical layer produces measurements. The governance layer certifies their provenance chain. The economic layer converts certified provenance into market value. Each layer is independently useful; together they close the loop from photon to democratic accountability.

---

## Position in the MareNostrum / DHITL Ecosystem

FractaVolta is the physical substrate of a broader infrastructure sovereignty architecture.

| Layer | Repository | Function |
|---|---|---|
| **L1 — Physical** | **FractaVolta** (this repo) | Photon-to-inference pipeline, distributed sensing, CXU production |
| **L2 — Economic** | [MareNostrum](https://github.com/JeanHuguesRobert/marenostrum) | Sovereign energy fund, CXU markets, universal dividend |
| **L3 — Political** | [MareNostrum / DHITL](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md) | Democratic governance, 1p1v, anti-capture provisions |
| **L4 — Cognitive** | [Cogentia Commons](https://github.com/JeanHuguesRobert/cogentia) | Epistemic infrastructure, collective reasoning |
| **L5 — Technical** | [DHITL](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md) | Open core, traceable decisions, AI safety |

The FractaVolta photon-to-inference pipeline feeds the CXU definition formalized in DHITL:

> **Xc = E × η_hw × η_sys × η_sla × η_gov**

where E (available energy) originates from the sensing layer FractaVolta defines, and η_gov incorporates the democratic governance conditions MareNostrum establishes.

---

## Business Model

| Offering | Client profile | Pricing logic |
|---|---|---|
| Distributed sensing deployment | Municipalities, regional energy authorities | Project-based |
| Probabilistic inference engine (SaaS) | Utilities, mobility operators | Per-node subscription |
| Sovereign infrastructure design | Island territories, remote regions | Consulting + IP license |
| Training and transfer | Public institutions, cooperatives | Day-rate + materials |

Revenue destinations: operational costs of the open Corsican deployment, Institut Mariani R&D, MareNostrum sovereign energy fund (Plan 2038).

---

## Design Principles

**Inference under uncertainty, not measurement under control.** The system is designed for environments where perfect sensing is impossible: rural territories, intermittent connectivity, heterogeneous hardware. Graceful degradation is a first-class requirement.

**Traceability as architecture, not compliance.** Audit logs are not a regulatory afterthought. They are the primary security mechanism, replacing secrecy with accountability.

**Fractal governance.** The same mechanism at every scale. No opaque layer reserved for higher levels. Subsidiarity enforced as a protocol constraint, not a political aspiration.

**Continuous attestation.** Provenance is produced in real time, not reconstructed after the fact. Gaps in the attestation flow are themselves recorded — by the cluster observing the absence of node output.

**Democratic closure.** Technical measurements are inputs to governance, not substitutes for it. The system accepts that democratic decisions may diverge from physical optima. Legitimacy is the guarantee; optimality is not.

**Possibilism.** This repository explores what is potentially possible. A falsified hypothesis is a result. An open problem is an invitation. The goal is to extend the frontier, not to defend a position.

---

## Status

| Component | Status |
|---|---|
| Physical inference model | Conceptual — `tera.md` |
| Fractal governance model | Formalized — `traceable_governance.md` |
| CXU / SCE specification | Formalized — `safe_compute_exergy.md` |
| Reference inference v1 | Pending — `reference_inference_v1.md` |
| Exergy Lock Protocol | Outlined — formalization pending |
| Mediterranean deployment | Design phase — [MareNostrum](https://github.com/JeanHuguesRobert/marenostrum) |

---

## Engage

Open an issue to challenge a claim, propose a counter-example, or identify a gap.  
Fork to implement an alternative model and link back.  
PR to add a case study, a formal element, or a reference.  
Cite a commit hash for priority on a specific idea.

The review process is public, attributed, append-only.  
It is, in that sense, an instance of what it describes.

---

*License: CC BY 4.0 — Attribution required: Jean Hugues Noël Robert — FractaVolta (2026)*  
*Priority established by first commit timestamp.*
