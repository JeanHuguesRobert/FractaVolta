---
title: FractaVolta
layout: home
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/index.md
last_stamped_at: 2026-05-26
---

## Transition toward energy packets

FractaVolta turns local energy into local capacity: **measured, stored, routed, used, and traced**.

The dominant electrical model treats energy as a continuous, homogeneous flow:

```text
production -> grid -> consumption -> abstract billing
```

FractaVolta treats energy as a sequence of accountable packets:

```text
source -> measurement -> storage -> routing -> use -> trace
```

A charged battery is an energy packet. A mobile battery or EV can carry a packet. A local solar installation can become a packet source. A compute node can turn those packets into attributable inference.

The grid remains useful, but it is no longer the invisible default substrate. It becomes one peer, one backup path, or one arbitrage layer among others.

## Local deployment in Corsica

**Le soleil doit bénéficier d’abord à ceux qu’il arrose.**

For local Corsican deployment, the entry point is in French: hangars, rooftops, parking canopies, existing solar fields, public buildings, storage, reversibility, and practical pilot sites.

- [FractaVolta en Corse](./fr/)
- [FractaVolta Seconde Vie](./fr/seconde-vie)
- [Marchés locaux](./fr/marches)
- [Partenaires installateurs](./fr/installateurs)
- [Rossignol Node](./fr/rossignol-node)

## Research architecture

The deeper architecture remains open and research-oriented.

In 1964, Paul Baran introduced packet-switching. By 2000, it had replaced circuit-switched networks. The electrical grid has not fully made that conceptual shift. Neither has cognitive infrastructure.

FractaVolta applies packet-switching to energy. The same logic applies one layer up: a reasoning step is a cognitive packet. A judgment, suspended and serialized as a typed continuation, is a unit of cognitive work that survives across agents, providers, and process boundaries.

And one layer up again: a vote, a delegation, a deliberation is a civic packet — atomic, traceable, revocable, federated.

> photons -> energy packets -> inference packets -> cognitive packets -> civic packets

## What we do

**Energy substrate.** Feasibility studies and system design for Energy Packet Network deployments: PV, batteries, mobile storage, DC-native nodes, safe 48 V interfaces where appropriate, local-first routing, and provenance-aware operations.

**Compute substrate.** Sovereign AI inference infrastructure powered by local or Mediterranean solar. CXU-priced compute on solar-backed nodes. Inference Packet Networks (IPN) for bounded continuity when hyperscale degrades.

**Cognition layer.** Cogentia is the open-source cognitive layer of FractaVolta: cognitive packets, continuations, `cogentia.js`, provider-neutral orchestration and auditable knowledge production.

**Civic layer.** Inseme platform deployment and operations. Multi-instance Kudocracy.Survey installation. Ophélia AI mediator integration on sovereign inference backends.

## Why it matters

Solar energy is no longer scarce. Compute is no longer scarce. What is scarce:

- **reliability** — when you need it, not when conditions align;
- **timing** — arbitrage between generation, demand, storage, and decision;
- **quality of service** — guaranteed uptime for compute, deliberation, and routing;
- **auditability** — proof that the system did what it claims, at every layer;
- **sovereignty** — the right to inspect, modify, and outlive every layer you depend on.

The highest-value use of local solar is not always exporting electrons. It can be storing, routing, and using energy locally as accountable capacity: water, cold, mobility, critical services, compute, inference, and civic continuity.

## How we work

Every deployment should produce its own typed audit trail. Every claim should be anchored at a stable URL. Every AI agent we use should be replaceable without modifying the toolchain. Every objection becomes a first-class contribution to the record, not noise to be erased.

This is governed by the [Cogentia Commons methodology](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md), the operational [Pipeline](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md) method (*pipeline on the surface, packet network in depth*) with its source ↔ derived split formalised in [Derived Products](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md), implemented operationally through the [`cogentia.js` CLI](https://github.com/JeanHuguesRobert/cogentia) and the [`cogentia.continuation.v1` protocol](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md). For the working details, see [methodology](./methodology).

## Status

Early-stage. Architecture documented across energy, compute, cognition, and civic layers. New local deployment pages added for Corsica. Prototype work in progress through Rossignol Node. See [Energy packets](./energy-packets) and [FractaVolta en Corse](./fr/) for the current positioning.
