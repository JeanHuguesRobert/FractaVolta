---
title: "Concept Index — FractaVolta"
description: "Typed concept registry for humans and AI agents; structure only, not semantic authority."
layout: default
nav_order: 3
last_modified_at: 2026-05-16
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/concepts.md
last_stamped_at: 2026-06-01
license: CC BY-SA 4.0
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
date: 2026-05-16
creator: Jean Hugues Noël Robert, baron Mariani
document_role: "index"
document_kind: "concept-index"
visibility: "public"
lifecycle_state: "active"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "concept-index"
classification_confidence: "strong"
---

# Concept Index — FractaVolta

This file maps concepts used across the corpus.

`cogentia.js` maintains structure, links, scopes, status and graphs. It does not infer semantic truth.

## Status scale

- **Seed** — intuition not yet stabilized.
- **Working** — recurring and usable, but still evolving.
- **Defined** — explicit definition exists.
- **Operational** — connected to implementation, protocol, code, governance or legal use.
- **Canonical** — should be treated as a reference concept unless revised.

---

## Cogentia

**Type:** abstract concept / agentivity class
**Scope:** Global
**Status:** Working

**Short definition:**
Cogentia designates the actual situated agentivity of an entity — physical person, legal person, or AI agent — combining memory, mandate, capabilities, procedures, acts and traces.

**Parent concepts:**
- Traceable agency

**Child concepts:**
- Cogentigram
- Operational memory

**Reference documents:**
- `research/concepts.md`

**Used in:**
- digital twin work
- AI agent governance

---

## Cogentigram

**Type:** representation / map
**Scope:** Global
**Status:** Working

**Short definition:**
A cogentigram is a structured, partial, auditable and revisable representation of a Cogentia.

**Parent concepts:**
- Cogentia

**Related concepts:**
- Map vs territory
- Operational memory
- Traceable agency

---

## IPN (Inference Packet Network)

**Type:** network architecture
**Scope:** Global
**Status:** Defined

**Short definition:**
A network methodology for routing intelligence securely and efficiently across a distributed topology.

**Reference documents:**
- [`research/inference_packet_network.md`](inference_packet_network.md)

---

## EPN (Energy Packet Network)

**Type:** network architecture
**Scope:** Global
**Status:** Defined

**Short definition:**
DC-native topology addressing power routing in containerized and localized contexts.

**Reference documents:**
- [`dc_native_epn.md`](dc_native_epn.md)

---

## PGN (Power Generation Node)

**Type:** infrastructure component
**Scope:** Global
**Status:** Working

**Short definition:**
Decentralized nodes for local power generation, underpinning the IPN and EPN topologies.

**Reference documents:**
- [`PGN.md`](PGN.md)

---

## Packet Attractors (Fractanet routing)

**Type:** system dynamics
**Scope:** Global
**Status:** Working

**Short definition:**
Declarative demand primitive: a Fractanet node attracts governed packets it is **capable and
legitimate** to handle — the distributed-blackboard mechanism for capability routing (not fixed URLs).

**Reference documents:**
- [`packet_attractor_fractanet.md`](https://github.com/JeanHuguesRobert/inseme/blob/main/research/packet_attractor_fractanet.md) (canonical COP-side source)
- [Reactive Cognitive COP Extension](https://github.com/JeanHuguesRobert/inseme/blob/main/research/reactive_cognitive_cop_extension.md)

## Packet as evolutionary attractor

**Type:** complexity science
**Scope:** Global
**Status:** Working

**Short definition:**
Hypothesis that mature complex networks independently converge from circuit-switched flow toward
discrete store-and-forward packet structures.

**Reference documents:**
- [`packet_attractor.md`](packet_attractor.md)

---

## The Unconscious Grid

**Type:** abstract concept
**Scope:** Global
**Status:** Working

**Short definition:**
The array of network behaviors and implicit flows running silently beneath the conscious operations of the nodes.

**Reference documents:**
- [`UNCONSCIOUS_GRID.md`](UNCONSCIOUS_GRID.md)

---

## Mariani Village

**Type:** project
**Scope:** Global
**Status:** Working

**Short definition:**
The localized demonstrator and real-world grounding implementing these topologies in Corsica.

**Reference documents:**
- [`mariani_village.md`](mariani_village.md)

---

## Value-Shaped Solar

**Type:** energy strategy
**Scope:** project-specific
**Status:** Working

**Short definition:**
A specific energy utilization strategy adapting computational consumption organically to the generation curve of localized solar arrays.

**Reference documents:**
- [`value_shaped_solar_and_containerized_compute.md`](value_shaped_solar_and_containerized_compute.md)

---

## Containerized Compute (Tera)

**Type:** infrastructure format
**Scope:** repository-specific
**Status:** Defined

**Short definition:**
The physical, scalable form factor for deploying the inference nodes in tandem with localized power infrastructures (EPN).

**Reference documents:**
- [`tera.md`](tera.md)
- [`electricity_in_containers.md`](electricity_in_containers.md)

---

## Traceable Governance

**Type:** administrative protocol
**Scope:** repository-specific
**Status:** Working

**Short definition:**
The administrative protocol tying physical node ownership and IPN packet routing directly to cryptographic and auditable trails.

**Reference documents:**
- [`traceable_governance.md`](traceable_governance.md)
<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Research Index — FractaVolta](index.md)
<!-- END_AUTO: backlinks -->
