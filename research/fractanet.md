---
title: "Fractanet — Generalized Control Planes for Heterogeneous Packet Networks"
subtitle: "Verbs, packets, COP/Inox, RAIX, exergy and anti-capture infrastructure"
description: "Working draft refactoring Fractanet as the infrastructural instance of Generalized Packet Networks: a programmable, distributed, anti-capture network of capability verbs governing heterogeneous data planes through COP/Inox, RAIX redundancy and exergy-oriented routing."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
x-address: "1 cours Paoli, F-20250 Corte, Corsica, France"
x-email: "jhr@baronsmariani.org"
x-website: "https://fractavolta.com"
canonical_path: "FractaVolta/research/fractanet.md"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md"
version: "0.3.2-draft"
status: "working-paper — redactor revised draft under human validation"
date: "2026-06-10"
last_modified_at: "2026-06-14"
last_stamped_at: "2026-06-14"
license: "CC BY-SA 4.0"
language: "en"
type: "source-document"
source_or_derived: "source-document"
repository: "FractaVolta"
related_repositories:
  - "JeanHuguesRobert/FractaVolta"
  - "JeanHuguesRobert/cogentia"
  - "JeanHuguesRobert/Inox"
  - "JeanHuguesRobert/inseme"
  - "JeanHuguesRobert/marenostrum"
related_documents:
  - "FractaVolta/research/generalized_packet_networks.md"
  - "FractaVolta/research/inference_packet_network.md"
  - "FractaVolta/research/thermal_packet_networks.md"
  - "FractaVolta/research/packet_paper_template.md"
  - "FractaVolta/research/index.md"
  - "Inox/research/inox-spec.md"
  - "cogentia/research/pipeline.md"
  - "cogentia/prompts/redactor.md"
  - "cogentia/prompts/reviewer.md"
  - "cogentia/prompts/cognitive_packet.md"
  - "cogentia/research/cognitive_packets.md"
  - "cogentia/research/cognitive_packet_switching.md"
  - "cogentia/research/cogentia_continuation_packet_routing.md"
  - "inseme/packages/cop-core/Invariants.md"
  - "inseme/packages/cop-core/ImplementationProfiles.md"
  - "inseme/research/reactive_cognitive_cop_extension.md"
  - "marenostrum/safe_compute_exergy.md"
  - "marenostrum/compute-exergy-omitted-variable.md"
  - "marenostrum/CXU_SPEC.md"
related_document_urls:
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/inference_packet_network.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/thermal_packet_networks.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_paper_template.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md"
  - "https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/redactor.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/reviewer.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/cognitive_packet.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_switching.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia_continuation_packet_routing.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Invariants.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/ImplementationProfiles.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/research/reactive_cognitive_cop_extension.md"
  - "https://github.com/JeanHuguesRobert/marenostrum/blob/main/safe_compute_exergy.md"
  - "https://github.com/JeanHuguesRobert/marenostrum/blob/main/compute-exergy-omitted-variable.md"
  - "https://github.com/JeanHuguesRobert/marenostrum/blob/main/CXU_SPEC.md"
tags:
  - fractanet
  - generalized-packet-networks
  - control-plane
  - data-plane
  - heterogeneous-packets
  - cop
  - inox
  - raix
  - exergy
  - anti-capture
  - programmable-gateway
  - capability-verbs
  - continuation
  - streaming
  - backtracking
  - second-method
x-keywords:
  - Fractanet
  - Generalized Packet Networks
  - COP
  - Inox
  - RAIX
  - exergy
  - generalized control plane
  - heterogeneous data planes
  - envelope payload distinction
  - capability verbs
  - programmable gateway
  - programmable routing
  - programmable cache
  - script registry
  - continuations
  - streaming execution
  - backtracking
  - energy-based routing
  - exergy-based routing
  - no single point of failure
  - no single point of capture
human_validation_required: true
review_status: "Grok constructive review completed 2026-06-13; high-signal points selectively integrated in v0.3; corpus anchors added in v0.3.1"
revision_note: "v0.3 integrates selected reviewer objections: envelope comparison, exergy toy model, registry anti-capture, minimal verb schema, JavaScript/Inox boundary, and one cross-scale fractal example. v0.3.1 adds corpus anchors for open questions. Review remains advisory; human author arbitrates."
validation_points:
  - "Confirm whether this v0.2 should replace the current FractaVolta/research/fractanet.md or be reviewed first as a separate draft."
  - "Validate the public definition of Fractanet as the infrastructural instance of Generalized Packet Networks."
  - "Validate the naming and scope of RAIX."
  - "Validate the claim that JavaScript should remain an adoption profile while COP/Inox carries complex Fractanet execution."
  - "Validate whether exergy-based routing should be framed as a true model family or as an energy-inspired cost function at this stage."
  - "Validate all institutional references before public publication."
---

## 0. Corpus navigation

This draft uses clickable corpus anchors for easier review and continuation.

### Primary source anchors

| Role | Corpus document |
|---|---|
| General packet grammar | [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md) |
| Inference packet sibling paper | [FractaVolta/research/inference_packet_network.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/inference_packet_network.md) |
| Thermal packet sibling paper | [FractaVolta/research/thermal_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/thermal_packet_networks.md) |
| Packet-paper discipline | [FractaVolta/research/packet_paper_template.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_paper_template.md) |
| FractaVolta research index | [FractaVolta/research/index.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md) |
| Inox specification | [Inox/research/inox-spec.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md) |
| Cogentia pipeline | [cogentia/research/pipeline.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md) |
| Redactor prompt | [cogentia/prompts/redactor.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/redactor.md) |
| Reviewer prompt | [cogentia/prompts/reviewer.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/reviewer.md) |
| COP invariants | [inseme/packages/cop-core/Invariants.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Invariants.md) |
| COP implementation profiles | [inseme/packages/cop-core/ImplementationProfiles.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/ImplementationProfiles.md) |
| Compute exergy | [marenostrum/safe_compute_exergy.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/safe_compute_exergy.md) |
| CXU specification | [marenostrum/CXU_SPEC.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/CXU_SPEC.md) |


# Fractanet

## Generalized Control Planes for Heterogeneous Packet Networks

**Jean Hugues Noël Robert, baron Mariani**  
Institut Mariani / C.O.R.S.I.C.A. / FractaVolta  
1 cours Paoli, F-20250 Corte, Corsica, France  

*Working paper — v0.3 draft — June 2026*  
*License: CC BY-SA 4.0*  
*Repository: `JeanHuguesRobert/FractaVolta` — target path: [research/fractanet.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md)*

---

## Abstract

**Fractanet** is the infrastructural instance of **Generalized Packet Networks**: a programmable, distributed, anti-capture network of capability verbs governing heterogeneous data planes.

Where the Internet routes packets of bits, Fractanet aims to route, supervise, compose, cache, suspend, resume, and optimize packets of useful capacity: data packets, energy packets, thermal packets, inference packets, cognitive packets, logistics packets, water packets, mandates, permissions, responsibilities, continuations, and other bounded units of operational usefulness.

Its core architectural thesis is that the classical distinction between **control plane** and **data plane** can be generalized beyond digital networks. The control plane carries envelopes: identity, origin, destination, rights, policy, priority, TTL, freshness, signatures, routing constraints, traceability, and supervision events. The data planes carry heterogeneous payloads: bits, energy, water, heat, goods, compute, inference, cognition, delegation, or institutional authority.

Fractanet is not a single platform, protocol, cloud, or product. It is a fractal architecture of capacity: the same invariants recur at several scales — inside the Inox virtual machine, inside a programmable gateway, across a mesh of gateways, across energy and compute infrastructures, and across human/AI cognitive workflows.

Its execution substrate is **Inox**, especially in its minimal concatenative form and its richer dialects. Its supervision layer is **COP**. Its redundancy model is **RAIX**, a generalization of RAID where `X` may be data, energy, cache, compute, model, route, policy, trace, jurisdiction, agent, or institution. Its optimization criterion is not raw energy minimization but **exergy**: useful capacity produced per unit of cost, latency, risk, noise, capture exposure, and irreversible loss.

The resulting promise is:

> **No single point of failure. No single point of capture.**

---

## Reading guide — key architectural commitments

This document is long because it is a source document, not a short public article. The following commitments are the load-bearing ones:

1. **GPN vs. Fractanet** — Generalized Packet Networks provide the theoretical grammar; Fractanet is one infrastructural implementation of that grammar.
2. **Envelope vs. payload** — the control plane governs envelopes; heterogeneous data planes carry payloads.
3. **Verbs vs. endpoints** — clients call stable verbs; the gateway dispatches to the appropriate implementation.
4. **COP/Inox core** — Inox executes capability-bound compositions; COP supervises long, streamable, resumable, or human-sensitive acts.
5. **RAIX anti-capture** — redundancy must apply not only to data planes but also to registries, policies, traces, and other control surfaces.
6. **Exergy first** — routing should maximize useful capacity under hard constraints, not merely minimize raw energy or cost.
7. **Human arbitration** — dense Inox and agent-readable traces are acceptable only if the act remains explainable to humans.

---

## Keywords

Fractanet; Generalized Packet Networks; control plane; data plane; envelope; payload; COP; Inox; RAIX; exergy; packet switching; programmable gateway; capability verbs; distributed routing; programmable cache; script registry; continuations; streaming; backtracking; energy-based models; anti-capture; signal/noise; cognitive packets; Seconde méthode.

---

## 1. Purpose and status

This document refactors the initial Fractanet working paper into a broader source document. It should be read as a **corpus source draft**, not as a finished specification, product announcement, or public manifesto.

Its purpose is to stabilize the current formulation of Fractanet after several conceptual convergences:

1. **Generalized Packet Networks** provide the theoretical grammar.
2. **Fractanet** provides the infrastructural instance.
3. **Inox** provides a micro-architecture and execution substrate.
4. **COP** provides the supervision and orchestration plane.
5. **RAIX** provides generalized redundancy.
6. **Exergy** provides the criterion of useful capacity.
7. **Anti-capture** provides the political and architectural finality.

The document is deliberately written as a source document: its thesis, distinctions, boundaries, failure modes, and non-claims should be reconstructible from the text alone.

### 1.1 Methodological stance

This draft follows the corpus redactor/reviewer discipline: source before derived product, signal/noise classification, explicit non-claims, failure modes, open questions, and human validation. The external review of v0.2 is treated as advisory, not sovereign: it is used to increase testability and reduce ambiguity, while final naming, scope, and publication decisions remain human decisions.

---

## 2. Core thesis

Fractanet can be defined as follows:

> **Fractanet is the programmable infrastructural instance of Generalized Packet Networks: a distributed, anti-capture, exergy-oriented network of capability verbs governing heterogeneous data planes through COP/Inox, RAIX redundancy, and traceable control-plane supervision.**

A shorter operational formulation:

> **Internet routes packets of bits. Fractanet routes packets of capacity.**

A still shorter architectural test:

> **No single point of failure. No single point of capture.**

These formulas are not slogans substituting for design. They are compression devices for the architecture developed below.

### 2.1 MVP constraint

The first implementation should not attempt to cover all substrates. The MVP should be a programmable API gateway that demonstrates the invariants at small scale:

- capability verbs rather than fixed endpoints;
- a minimal script/verb registry;
- Inox Core execution for the serious path;
- a limited JavaScript adoption profile for short bounded scripts;
- explicit capabilities and quotas;
- programmable cache with TTL/freshness policy;
- COP event tracing;
- simple dispatch with fallback;
- one small exergy-inspired scoring function applied only after hard constraints.

The broader multi-substrate claim should be tested through this limited digital/API case before being generalized further.

---

## 3. From packet switching to generalized packet networks

The historical reference is packet switching. ARPANET and the Internet showed that communication could become more resilient when continuous circuits were replaced by discrete, addressed, routable packets.

Generalized Packet Networks extend that intuition across substrates. A packet is not merely a sequence of bits. In the broader framework, a packet is a bounded unit of operational usefulness that can occupy constrained resources, be routed, delayed, transformed, cached, replicated, degraded, prioritized, audited, or delivered.

Examples include:

- a data packet;
- an energy packet;
- a thermal packet;
- a containerized battery;
- a parcel;
- a water allocation;
- an inference request;
- an AI-generated answer;
- a cognitive packet;
- a continuation;
- a vote;
- a mandate;
- a permission;
- a responsibility.

The common claim is not physical identity. Heat, votes, water, bits, and AI prompts do not obey the same physical laws. The claim is operational recurrence: similar questions appear when a bounded useful unit circulates through a constrained network.

The relevant questions are:

- What is the packet?
- What makes it bounded?
- What makes it addressable?
- What resource does it occupy?
- How long can it wait?
- What degrades with time?
- What gives it priority?
- Who or what routes it?
- What validates it?
- What is delivered?
- What is lost?
- What remains traceable?

Fractanet is the infrastructural answer to this generalized packet grammar.

---

## 4. GPN and Fractanet

The distinction between **Generalized Packet Networks** and **Fractanet** must remain stable.

| Concept | Status | Function |
|---|---|---|
| **Generalized Packet Networks** | theoretical framework | Provides the cross-domain grammar of packets, resource occupancy, routing, decay, cache, congestion, and delivery. |
| **Fractanet** | infrastructural instance | Implements that grammar as a programmable, distributed, supervised network of capability verbs and heterogeneous data planes. |

GPN may be studied as theory without deploying Fractanet. Fractanet may be built incrementally without requiring every participant to adopt the full theoretical apparatus.

The separation protects both sides:

- GPN remains analytically useful even if a particular Fractanet implementation fails.
- Fractanet remains operationally buildable even if some theoretical claims require revision.

---

## 5. Control plane and data planes, generalized

In classical networking, one distinguishes:

- the **control plane**, which decides how packets should move;
- the **data plane**, which actually forwards packets.

Fractanet generalizes this distinction.

### 5.1 The generalized control plane

The control plane carries the envelope of operation:

- origin;
- destination;
- identity;
- authorization;
- capability;
- priority;
- TTL;
- freshness;
- routing constraints;
- cost constraints;
- exergy criteria;
- signatures;
- version;
- namespace;
- trace;
- supervision events;
- policies;
- revocation rules;
- disclosure level;
- custody chain.

It answers:

> Under which rights, routes, constraints, and responsibilities may this packet move or act?

### 5.2 Heterogeneous data planes

The data plane carries or activates payloads. In Fractanet, there is not one data plane but many possible data planes:

| Data plane | Payload example |
|---|---|
| Data | bits, documents, events, rows, streams |
| Energy | useful energy, battery packets, charging slots |
| Thermal | hot water, cold storage, thermal inertia |
| Water | volume, allocation, reserve, delivery right |
| Goods | parcel, tool, material, food, spare part |
| Inference | prompt, model call, answer, fallback computation |
| Cognition | cognitive packet, hypothesis, objection, continuation |
| Governance | vote, mandate, delegation, permission, responsibility |

The control plane may route, prioritize, validate, or audit a packet without unnecessarily opening or capturing the payload.

This is central to anti-capture. A system that must inspect every payload to route every packet is structurally exposed to capture, surveillance, and platform lock-in.

---

## 6. Envelope and payload

The operational form of the control/data distinction is:

```text
packet = envelope + payload
```

The **envelope** is what the network needs in order to route, authorize, trace, prioritize, cache, suspend, resume, revoke, or supervise the packet.

The **payload** is the useful content, resource, or capacity transported, transformed, executed, delegated, or delivered.

This distinction must be preserved across substrates.

### 6.1 Example: data packet

- Envelope: source, destination, TTL, protocol, route, signature.
- Payload: bytes.

### 6.2 Example: energy packet

- Envelope: source, destination, time window, storage constraints, priority, exergy value, proof of origin.
- Payload: useful energy or claim on useful energy.

### 6.3 Example: cognitive packet

- Envelope: topic, author, version, disclosure level, continuation state, review status, relevance, intended repository.
- Payload: hypothesis, objection, draft, proof fragment, transformation map, continuation.

### 6.4 Example: mandate packet

- Envelope: delegator, delegate, scope, duration, revocability, legitimacy condition, trace.
- Payload: authority to act within a bounded domain.

The same invariant recurs:

> **The envelope governs movement and accountability. The payload carries useful capacity.**

### 6.5 Comparative envelope sketch

The shared grammar must remain modest. It does not mean that all substrates share the same physics or legitimacy rules. It means that a minimal envelope can often expose enough control information for routing, authorization, supervision, and traceability.

| Packet type | Minimal envelope fields | Payload | Specific degradation / risk | Validation question |
|---|---|---|---|---|
| **Data packet** | origin, destination, TTL, protocol, signature, confidentiality level | bytes, document, event | staleness, leakage, corruption | Is the data authentic, authorized, and still fresh? |
| **Energy packet** | source, destination, time window, storage interface, exergy value, proof of origin | useful energy or claim on useful energy | conversion loss, storage loss, grid congestion | Is useful energy deliverable at the required place and time? |
| **Water packet** | source, destination, volume, quality, time window, usage right, priority | water volume or allocation right | evaporation, contamination, scarcity conflict | Is the allocation legitimate, available, and fit for use? |
| **Goods packet** | origin, destination, custody chain, handling constraints, deadline, proof of receipt | material item, component, parcel | loss, damage, delay, custody dispute | Is custody traceable and delivery verifiable? |
| **Inference packet** | model policy, input disclosure level, cost budget, latency target, trace requirement | inference request or result | hallucination, privacy leak, model drift | Is the inference authorized, explainable, and useful enough? |
| **Mandate packet** | delegator, delegate, scope, duration, revocation rule, legitimacy condition, trace | bounded authority to act | abuse, expiration, contested legitimacy | Is the action inside the mandate and still revocable? |

This table is not a final schema. It is a test: if a substrate cannot expose a bounded envelope of this kind, it should not be forced into the packet model.

---

## 7. Verbs instead of endpoints

A conventional API exposes endpoints:

```text
GET /customers/{id}
GET /orders?customer_id={id}
```

Fractanet abstracts over endpoints by exposing **verbs**.

A verb is a named operational capability:

```text
customer.summary
energy.dispatch
inference.fallback
continuation.resume
mandate.delegate
packet.trace
```

The client calls a verb. The Fractanet control plane dispatches that verb to an implementation.

The implementation may be:

- a source API endpoint;
- a synthetic endpoint;
- a cached result;
- an Inox script;
- a COP task;
- a continuation;
- a streaming job;
- a fallback route;
- a physical operation;
- a human validation step.

The verb is stable. The endpoint is an implementation detail.

This matters because stable verbs allow systems to evolve without forcing every client to track every infrastructure change.

---

## 8. Dispatch as generalized method selection

The analogy with object-oriented dispatch is useful.

In object-oriented languages, a method call names an operation while the runtime chooses the concrete implementation according to the receiver type or dispatch table.

In Fractanet, a verb call names an operation while the gateway or mesh selects the concrete implementation according to context.

Dispatch may depend on:

- namespace;
- tenant;
- client type;
- region;
- version;
- capability;
- cost;
- latency;
- cache state;
- data residency;
- endpoint availability;
- freshness requirement;
- exergy criterion;
- supervision requirement;
- continuation affinity;
- human approval requirement.

Example:

```text
customer.summary(input)
```

may resolve to:

- a public endpoint for a public client;
- a tenant-specific synthetic endpoint;
- a mobile-optimized version;
- a cache-aware degraded version;
- an EU-only route;
- a supervised continuation if the operation is long;
- a human-approved operation if the payload implies responsibility.

Thus:

> **The verb is the stable vocabulary. Dispatch chooses the admissible implementation.**

---

## 9. Programmable gateway

The first concrete implementation layer is a programmable gateway.

Modern JSON APIs often require multiple round trips. A client asks for a user, then for orders, then for tickets, then for permissions, then for recent activity. The latency cost is large even when each endpoint is individually fast.

A Fractanet gateway should support bounded API-side scripting:

```text
client → verb / script → gateway → local API calls → aggregate result
```

The script should be:

- sandboxed;
- quota-limited;
- capability-bound;
- traceable;
- versioned when registered;
- cache-aware;
- optionally streamable;
- optionally resumable;
- supervised when long, costly, mutating, or critical.

At the simplest level, this is a batch endpoint. At the Fractanet level, it is the local execution point of a distributed control plane.

---

## 10. Script registry and synthetic endpoints

A script sent once is useful. A script registered, versioned, named, and governed becomes infrastructure.

Fractanet therefore needs a **registry** of scripts and verbs.

A registered script can become a synthetic endpoint:

```text
/x/public/customer-summary/v1
/x/client/mobile/customer-summary/v2
/x/private/acme/customer-summary/v3
```

The registry should track:

- verb name;
- namespace;
- version;
- status;
- runtime;
- source script;
- input schema;
- output schema;
- capabilities;
- cache policy;
- routing policy;
- quotas;
- trace policy;
- owner;
- review status;
- deprecation status;
- continuation compatibility.

The registry is not merely a deployment tool. It is a corpus of executable capabilities.

### 10.1 Minimal verb record

A minimal registry entry should be machine-readable and reviewable by humans. For a first MVP, a verb record could be no more than:

```yaml
verb: customer.summary
version: 0.1.0
namespace: /client/mobile
status: draft
runtime: inox-core
entrypoint: verbs/customer_summary.inox
input_schema: schemas/customer_summary.input.json
output_schema: schemas/customer_summary.output.json
capabilities:
  read:
    - /customers/{id}
    - /orders?customer_id={id}
  write: []
cache:
  ttl_seconds: 300
  scope: tenant
routing:
  preferred_region: eu
  fallback: stale-cache-if-authorized
quotas:
  max_runtime_ms: 500
  max_api_calls: 25
trace:
  cop_required: true
  include_candidate_routes: true
owner: FractaVolta
review_status: human-validation-required
```

The schema is intentionally conservative. It should be sufficient to test the model without pretending to solve all registry governance questions.

### 10.2 Registry as capture surface

The registry is itself a potential point of capture. Whoever controls naming, signing, capability grants, namespace allocation, or deprecation can influence the whole dispatch layer. Therefore RAIX must apply to the registry and not only to the data planes.

Minimal anti-capture requirements for the registry:

- append-only or versioned history;
- signed verb records;
- mirrorable registry state;
- explicit namespace authority;
- auditable capability grants;
- reproducible script hashes;
- visible deprecation and override rules;
- at least one independent trace of registry changes.

A centralized registry may be acceptable for an MVP. It is not acceptable as the mature Fractanet pattern unless it can be mirrored, audited, forked, and reconciled.

---

## 11. Namespaces and public/private capability surfaces

Fractanet must distinguish capability surfaces.

Possible namespaces:

```text
/public/...
/partner/{partner}/...
/client/{client_type}/...
/tenant/{tenant}/...
/private/{organization}/...
/local/{node}/...
/experimental/...
```

The same verb may have several visible forms depending on the caller.

A public verb should not accidentally expose a private tenant implementation. A local verb should not silently become global. A partner-specific route should not become the default path for unknown clients.

Namespace is therefore not decoration. It is part of the security model.

---

## 12. Inox as micro-architecture

Inox is not only one possible language for scripts. It is the micro-architectural model of Fractanet.

The reason is structural.

Inox is a concatenative stack-based language and virtual machine with a strict separation between control and data planes. It has at least two fundamental stacks:

- a **control stack**, corresponding broadly to what is often called the call stack;
- a **data stack**, carrying values, payloads, and active data.

This is not an incidental implementation detail. It mirrors the Fractanet architecture at a lower scale.

| Scale | Control plane | Data plane |
|---|---|---|
| Inox VM | control stack, verbs, execution state | data stack, named values, active data |
| Gateway | dispatch, routing, policy, cache policy, registry | endpoints, payloads, scripts, streams, continuations |
| Fractanet | COP, envelopes, capabilities, traces | data, energy, water, goods, inference, cognition, mandates |

Thus:

> **Inox implements at VM scale what Fractanet generalizes at network scale.**

This is the meaning of “fracta” in Fractanet: invariants recur across scales.

---

## 13. Inox Core and dialects

Inox should not be understood only as a maximal expressive language.

It can exist in strata:

1. **Inox Core** — a minimal Forth-like concatenative runtime, small enough to embed close to endpoints, devices, gateways, and edge nodes.
2. **Inox dialects** — domain-specific forms for API composition, cache, routing, COP supervision, continuations, packet handling, and governance constraints.
3. **Full Inox** — the highly expressive language suitable for complex compositions and AI-agent manipulation.

This stratification reconciles two needs:

- very small runtimes close to physical or API endpoints;
- very expressive representations for agents, authors, and advanced control logic.

A Fractanet node does not need the whole language everywhere. It needs the smallest runtime capable of executing the local capacity safely.

Formula:

> **Full Inox for thinking and generation. Inox Core for execution everywhere.**

---

## 14. JavaScript as adoption profile, not authority model

JavaScript may be useful at the beginning.

It is familiar, JSON-native, and easy for API developers to understand. A sandboxed JavaScript profile can support simple bounded scripts:

- short API aggregation;
- simple transformations;
- cache-aware reads;
- explicit-state resumable jobs;
- synthetic endpoint prototypes.

But JavaScript should not become the authority model of Fractanet.

Beyond a certain level of complexity, Fractanet requires:

- continuations;
- streaming supervision;
- backtracking;
- capability-first execution;
- strict control/data separation;
- small runtimes;
- inspectable dialects;
- COP integration;
- exergy-aware routing;
- traceable dispatch.

At that level, the core should be COP/Inox.

Formula:

> **JavaScript can introduce the model. COP/Inox must carry the model.**

---

## 15. COP as supervision plane

COP — Cognitive Orchestration Protocol — provides the supervision plane of Fractanet.

A programmable network that supports long executions, continuations, streaming, cache, routing, and backtracking cannot remain a black box.

It must expose events such as:

```text
verb.called
capability.checked
candidate.enumerated
route.rejected
route.selected
cache.hit
cache.miss
checkpoint.created
continuation.paused
continuation.resumed
stream.chunk.emitted
branch.started
branch.failed
branch.backtracked
human.approval.requested
human.approval.granted
execution.cancelled
artifact.produced
```

COP does not replace the runtime. It supervises the act.

It should allow authorized actors to:

- observe;
- inspect;
- pause;
- resume;
- cancel;
- approve;
- deny;
- retry;
- fork;
- checkpoint;
- explain;
- audit.

Formula:

> **Inox executes. COP supervises. Agents explain. Humans arbitrate.**

---

## 16. Long requests, continuations, and streaming

Fractanet must distinguish short execution from long execution.

### 16.1 Short execution

A short execution returns within a normal request/response window.

Example:

```text
call verb → aggregate three endpoints → return result
```

### 16.2 Asynchronous job

A long operation may become a job:

```text
submitted → running → completed / failed / cancelled
```

The client retrieves the result later.

### 16.3 Continuation

A deeper model captures execution state and resumes later.

A continuation must preserve:

- local state;
- logical stack;
- script version;
- runtime version;
- consumed quotas;
- capabilities;
- trace;
- cache references;
- checkpoint identity;
- pending decisions.

This is natural in Inox if the language and runtime are designed for persistable execution states. In JavaScript, full continuation capture is harder and should initially be replaced by explicit state-based resumable jobs.

### 16.4 Streaming

Some executions should emit progressive output:

```text
started
progress
partial_result
warning
checkpoint
requires_approval
completed
```

Streaming turns a request into an observable process. That is precisely why COP is needed.

---

## 17. Programmable cache

A Fractanet gateway should not only call APIs locally. It should know when not to call them.

The cache must be programmable, but not uncontrolled.

A script or verb may use:

- TTL;
- freshness policies;
- ETag-like revalidation;
- stale-while-revalidate;
- quota-aware caching;
- cost-aware caching;
- exergy-aware caching;
- tenant-scoped cache;
- script-local memoization;
- regional cache;
- edge cache.

The cache is a capability, not a free storage area.

It should be:

- scoped;
- quota-limited;
- TTL-bounded;
- traceable;
- purgeable;
- non-shared by default across tenants;
- governed by policy.

Cache decisions should appear in the trace.

A cache hit is not “nothing happened”. It is a technical act that chose not to spend capacity.

---

## 18. Backtracking and exploratory routing

Fractanet should not be limited to sequential execution, nor even to sequential execution with parallel calls.

Because Inox can support continuation-like mechanisms, it can also support Prolog-like backtracking.

This matters for routing.

When a verb is called, there may be several admissible strategies:

- direct endpoint;
- synthetic endpoint;
- fresh cache;
- stale cache;
- regional gateway;
- tenant-specific route;
- fallback model;
- continuation;
- human-supervised branch;
- degraded answer.

A simple router selects one. A Fractanet router may explore several.

The execution can be seen as:

```text
generate candidates
apply hard constraints
rank by exergy
try best route
if failure, backtrack
try next admissible route
trace every branch
return result or explanation
```

Backtracking is not an excuse for opacity. Every branch should be supervised.

Formula:

> **Inox enables exploration. COP prevents exploration from becoming a black box.**

---

## 19. Exergy-oriented routing

Fractanet may use strategies inspired by energy-based models, but its core metric should be exergy.

Energy alone is not enough. The corpus uses **exergy** as the central concept: useful energy, or more generally useful capacity capable of producing work, action, cognition, or resilience.

In routing, the question is not merely:

> Which route consumes the least energy?

but:

> Which admissible route produces the most useful capacity with the least global cost, latency, risk, noise, degradation, and capture exposure?

A route may be evaluated by a generalized score:

```text
useful capacity produced
-------------------------------------------------------------
energy + latency + monetary cost + risk + noise + staleness + quota + capture exposure
```

Or, in an energy-inspired formulation, one may minimize a generalized energy function that includes penalties and bonuses:

```text
E(route) =
  latency penalty
+ monetary cost penalty
+ physical energy penalty
+ quota penalty
+ staleness penalty
+ risk penalty
+ capture exposure penalty
+ complexity penalty
- useful exergy bonus
- signal bonus
- sovereignty bonus
```

But the order of decision is critical:

1. Hard constraints first.
2. Capabilities first.
3. Policies first.
4. Then exergy optimization.

A route forbidden by capability, law, sovereignty, privacy, or explicit policy must not become admissible merely because it has low cost.

Formula:

> **Capabilities bound the search space. Exergy ranks the admissible routes. Inox explores them. COP explains the decision.**

### 19.1 Toy scoring example

The following numbers are deliberately simple. They are not a formal model; they show the decision order.

A client calls:

```text
customer.summary(customer_id=123)
```

Candidate routes:

| Route | Hard constraints | Useful capacity | Cost bundle | Exergy score | Decision |
|---|---:|---:|---:|---:|---|
| A — direct source APIs | allowed | 90 | 60 | 1.50 | admissible |
| B — regional synthetic endpoint | allowed | 85 | 35 | 2.43 | selected |
| C — stale cache | allowed only if freshness > 5 min | 60 | 10 | 6.00 | rejected if freshness rule fails |
| D — non-EU gateway | violates data-residency policy | 95 | 20 | n/a | rejected before scoring |

The apparent best score may be route C, but if the freshness rule fails it is not admissible. Route D may look efficient, but it violates a hard constraint. The selected route is therefore B, not because it is globally cheapest, but because it produces the best useful capacity among admissible routes.

In a COP trace, this should not appear as a mysterious “AI routing choice”. It should appear as:

```text
constraints.applied
candidate.rejected(route=D, reason=data_residency)
candidate.rejected(route=C, reason=freshness_policy)
energy_score.estimated(route=A, score=1.50)
energy_score.estimated(route=B, score=2.43)
route.selected(route=B)
```

At this stage, exergy routing should therefore be framed as an **exergy-inspired scoring function under constraints**, not yet as a fully specified model family.

---

## 20. RAIX: generalized redundancy

RAID made storage more resilient by using redundant arrays of independent disks.

Fractanet generalizes the pattern as **RAIX**:

> **Redundant Array of Independent X**

where `X` may be:

- disks;
- nodes;
- gateways;
- caches;
- energy sources;
- batteries;
- water reserves;
- models;
- agents;
- scripts;
- routes;
- policies;
- traces;
- jurisdictions;
- communities;
- institutions.

RAIX is not redundancy for its own sake.

It is redundancy as anti-capture and anti-fragility.

A minimal RAIX taxonomy should distinguish:

| RAIX type | What is redundant | Failure/capture resisted | Typical cost |
|---|---|---|---|
| **RAIX-data** | data copies, mirrors, archives | data loss, deletion, hostage platforms | storage, consistency |
| **RAIX-compute** | runtimes, gateways, workers | cloud outage, compute monopoly | orchestration, scheduling |
| **RAIX-cache** | local/regional caches | latency, upstream outage, quota pressure | freshness management |
| **RAIX-route** | alternative paths and dispatch targets | network failure, endpoint capture | routing complexity |
| **RAIX-policy** | policy mirrors and review authorities | opaque governance, unilateral rule change | reconciliation |
| **RAIX-trace** | independent trace custody | audit capture, evidence loss | privacy and sealing |
| **RAIX-institution** | multiple legitimate carriers of authority | political or administrative chokepoints | coordination |

The minimum correctness condition is not “many copies”. It is:

> **At least one independent admissible path must remain available when any single ordinary failure or capture surface is removed.**

This condition must itself be tested against exergy: a redundant path that costs more capacity than it preserves is only redundancy theater.

A centralized system may be efficient under ideal conditions but fragile under stress. A monopolized system may be convenient but capturable. Fractanet treats excessive centralization as both a technical and political risk.

Formula:

> **A non-redundant capacity is fragile. A centralized capacity is capturable.**

However, RAIX must remain exergetic. Redundancy that produces more noise, cost, and complexity than useful capacity is not Fractanet; it is waste.

---

## 21. No single point of failure, no single point of capture

Classical resilience often focuses on avoiding a **single point of failure**.

Fractanet adds the symmetrical requirement:

> **No single point of capture.**

A system can be technically redundant and politically capturable. It can have many servers but one proprietary registry, one cloud account, one identity provider, one opaque model, one payment rail, one administrative chokepoint, or one platform controlling visibility.

Fractanet should therefore avoid capture points in:

- compute;
- storage;
- routing;
- identity;
- cache;
- policy;
- registry;
- model selection;
- trace custody;
- energy supply;
- water control;
- institutional authority;
- publication channels.

Anti-capture is not an afterthought. It is an architectural invariant.

---

## 22. Distributed gateways close to target endpoints

Because Fractanet begins as a gateway, the gateway should not be imagined as a single central proxy.

It can be deployed close to target endpoints:

```text
client
  → global routing layer
    → regional gateway
      → local API / cache / energy node / inference node / COP node
```

This enables:

- lower latency;
- better cache locality;
- reduced cross-region traffic;
- data residency control;
- failover;
- multi-instance redundancy;
- local execution near physical substrates;
- programmable routing;
- continuation affinity;
- edge supervision.

The gateway becomes a distributed capability plane.

It does not merely forward requests. It decides where and how bounded scripts, verbs, caches, continuations, streams, and physical packet operations should execute.

---

## 23. Signal/noise for humans and agents

Fractanet must increase the signal/noise ratio for two populations:

1. humans;
2. AI agents.

They do not need the same representation.

For agents, signal is:

- structure;
- types;
- capabilities;
- versions;
- traces;
- policies;
- schemas;
- dependencies;
- constraints;
- continuations.

For humans, signal is:

- intention;
- effect;
- responsibility;
- risk;
- explanation;
- justification;
- decision point;
- possibility of control.

Inox can be extremely concise and expressive. That may reduce readability for humans but increase manipulability for agents. This is acceptable only if the act remains humanly intelligible through COP traces, generated explanations, metadata, tests, and reviewable policies.

Formula:

> **The code may be optimized for agents. The act must remain intelligible to humans.**

---

## 24. Fractal invariants

The “fracta” in Fractanet refers to multi-scale invariants.

The same forms recur across levels:

| Invariant | Inox scale | Gateway scale | Fractanet scale |
|---|---|---|---|
| Control/data separation | control stack / data stack | dispatch / payloads | envelopes / heterogeneous data planes |
| Verbs | concatenative words | synthetic endpoints | capability verbs |
| Packetization | stack values | requests, jobs, streams | data, energy, water, goods, cognition, mandates |
| Continuation | captured execution state | resumable jobs | long-lived workflows and cognitive packets |
| Backtracking | branch/retry | route exploration | adaptive multi-substrate dispatch |
| Cache | local memoization | programmable cache | RAIX of storage and useful capacity |
| Trace | execution state | logs/events | COP supervision |
| Exergy | useful computation | useful response | useful territorial/cognitive capacity |

Fractanet is fractal not because it uses a decorative metaphor, but because its invariants are intended to survive changes of scale and substrate.

---

## 25. Relationship to existing work

Fractanet does not invent each of its components from nothing. It synthesizes several lineages:

- packet switching and ARPANET;
- RAID and generalized redundancy;
- active networks;
- software-defined networking;
- cyber-physical systems;
- energy packet networks;
- packetized energy management;
- cognitive packet networks;
- information-centric and named-data networking;
- delay-tolerant networking;
- combinatorial optimization;
- energy-based models;
- exergy theory;
- capability-based security;
- workflow orchestration;
- actor systems;
- continuation-based computation;
- versioned knowledge corpora.

The distinctive claim is not that no prior work touches any part of the architecture. The claim is that Fractanet composes these lines into a single anti-capture, exergy-oriented, multi-substrate, COP/Inox-supervised architecture.

---

## 26. Minimal Fractanet node

A minimal Fractanet node should probably include:

1. a small execution runtime, ideally Inox Core;
2. a capability model;
3. a local registry of verbs or scripts;
4. a local cache with explicit policy;
5. a COP-compatible event interface;
6. a routing table or dispatch policy;
7. a trace log;
8. a way to advertise capabilities;
9. a way to receive, execute, pause, resume, or reject packets;
10. a way to verify versions and signatures.

A larger node may add:

- AI-agent explanation;
- energy-aware routing;
- exergy-aware scheduling;
- physical packet interfaces;
- streaming supervision;
- distributed continuation storage;
- human approval workflows;
- federation.

---

## 27. Failure modes

The concept is powerful. Therefore its failure modes must be explicit.

### 27.1 Metaphorical overreach

The packet abstraction may be stretched too far. Not every flow should be packetized. Not every relation is a packet. Not every analogy is operational.

Boundary rule:

> A unit qualifies as a packet only when its operational identity is bounded, addressable, storable or delayable, and independently routable or governable.

Positive examples: a signed inference request, a battery charging slot, a mandate limited in scope and duration.

Negative examples: a permanent social relation, an unbounded cultural influence, a continuous physical flow with no addressable unit and no independent governance boundary.

Related open question: #9, physical data-plane envelope compatibility.

### 27.2 Control-plane capture

Even if data planes are distributed, the control plane may be captured by:

- a proprietary registry;
- a central identity provider;
- a model vendor;
- a cloud account;
- a dominant policy engine;
- a legal chokepoint;
- an opaque routing algorithm.

Fractanet must therefore apply RAIX to control planes as well as data planes. Related open questions: #1, #2, #7.

### 27.3 Opaque optimization

Energy-based or AI-assisted routing can become opaque. COP must make candidate routes, rejected routes, constraints, scores, and overrides inspectable. Related open questions: #5 and #6.

### 27.4 Redundancy noise

Redundancy can become waste. RAIX is valid only when it increases useful capacity, resilience, sovereignty, or signal more than it increases cost, noise, or complexity. Related open question: #7.

### 27.5 Human displacement

AI agents may read dense Inox better than humans. This does not authorize removing human validation from decisions involving doctrine, law, identity, governance, irreversible data choices, or public commitments. Related open question: #8.

### 27.6 Security through complexity

A system of scripts, gateways, registries, caches, continuations, and routes can hide vulnerabilities. Minimal runtimes, explicit capabilities, sandboxing, testable policies, and traceable execution are required.

---

## 28. Non-claims

This document does not claim that all substrates are physically equivalent.

It does not claim that all systems should be packetized.

It does not claim that Fractanet is already implemented as a complete working network.

It does not claim that JavaScript is unsuitable for all uses. It claims only that JavaScript should not carry the complex core of Fractanet when continuations, backtracking, supervision, routing, cache, and exergy become central.

It does not claim that AI-based routing should decide outside capability constraints.

It does not claim that anti-capture is automatically achieved by distribution. Distribution can still be captured if control surfaces are centralized.

It does not claim that exergy is a complete ethical or political criterion. Exergy measures useful capacity; the question of what should count as useful remains governed by doctrine, legitimacy, and human arbitration.

---

## 29. Open questions

1. What is the minimal formal definition of a Fractanet verb?
2. Should the verb registry be part of FractaVolta, Cogentia, Inox, or a dedicated Fractanet repository?
3. What is the minimal Inox Core needed for edge execution?
4. Which COP events are mandatory for a Fractanet node?
5. How should exergy scores be represented without producing opaque technocratic optimization?
6. What are the hard constraints that must always precede exergy ranking?
7. What is the relation between RAIX and existing fault-tolerance taxonomies?
8. How should human approval be represented in the control plane?
9. Can physical data planes — energy, water, goods — share enough envelope structure to justify a common registry?
10. What is the first MVP: programmable API gateway, COP-supervised continuation router, or Inox Core Fractanet node?

### 29.1 Corpus anchors for open questions

The following anchors are not answers. They are the first corpus locations to consult before turning an open question into a new document, MVP issue, or derived product.

| Open question | First corpus anchors | Expected contribution | Current status |
|---|---|---|---|
| Q1 — Minimal Fractanet verb | [FractaVolta/research/fractanet.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md); [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md); [Inox/research/inox-spec.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md) | Formalize a verb as a capability-bound operation over generalized packets, executable or dispatchable through Inox/COP. | Needs a dedicated minimal schema. |
| Q2 — Registry placement and governance | [FractaVolta/research/index.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md); [cogentia/research/pipeline.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md); [cogentia/research/concepts.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md); [cogentia/scripts/cogentia.js](https://github.com/JeanHuguesRobert/cogentia/blob/main/scripts/cogentia.js) | Reuse the existing corpus-indexing discipline before inventing a new registry. | Needs decision: FractaVolta first, then possibly dedicated Fractanet registry. |
| Q3 — Minimal Inox Core | [Inox/research/inox-spec.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md); [Inox/research/inox-docs-index.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-docs-index.md); [Inox/research/inox-tutorial-basic.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-tutorial-basic.md) | Identify the smallest concatenative runtime required for verbs, stacks, capabilities, continuations and dispatch. | Needs extraction into an Inox-side note. |
| Q4 — Mandatory COP events | [inseme/packages/cop-core/Invariants.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Invariants.md); [inseme/packages/cop-core/ImplementationProfiles.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/ImplementationProfiles.md); [inseme/research/reactive_cognitive_cop_extension.md](https://github.com/JeanHuguesRobert/inseme/blob/main/research/reactive_cognitive_cop_extension.md) | Define the mandatory event vocabulary for observation, pause, resume, approval, rejection, branch exploration and trace sealing. | Needs mapping from COP invariants to Fractanet node profile. |
| Q5 — Exergy scoring without opacity | [marenostrum/safe_compute_exergy.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/safe_compute_exergy.md); [marenostrum/compute-exergy-omitted-variable.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/compute-exergy-omitted-variable.md); [marenostrum/CXU_SPEC.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/CXU_SPEC.md); [FractaVolta/research/fractanet.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md) | Keep exergy as useful capacity, not technocratic black-box optimization. | For now: cost/scoring function under hard constraints, not full model family. |
| Q6 — Hard constraints before optimization | [inseme/packages/cop-core/Invariants.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Invariants.md); [cogentia/prompts/redactor.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/redactor.md); [FractaVolta/docs/methodology.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/methodology.md) | Separate non-negotiable constraints from soft ranking criteria. | Needs invariant list: capability, legality, privacy, consent, sovereignty, safety. |
| Q7 — RAIX and fault-tolerance | [FractaVolta/research/fractanet.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md); [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md); [FractaVolta/research/packet_paper_template.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_paper_template.md) | Extend redundancy from storage to data, compute, policy, trace, route, institution and substrate. | RAIX remains a thesis needing taxonomy and metrics. |
| Q8 — Human approval in control plane | [cogentia/research/pipeline.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md); [cogentia/prompts/redactor.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/redactor.md); [cogentia/prompts/reviewer.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/reviewer.md); [inseme/packages/cop-core/Invariants.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Invariants.md) | Preserve human arbitration while allowing agent-readable and runtime-readable control events. | Needs lifecycle: request, grant, deny, revoke, trace, appeal. |
| Q9 — Physical data-plane compatibility | [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md); [FractaVolta/research/inference_packet_network.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/inference_packet_network.md); [FractaVolta/research/thermal_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/thermal_packet_networks.md); [FractaVolta/research/packet_paper_template.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_paper_template.md); [FractaVolta/dc_native_epn.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md) | Test whether energy, thermal, inference and possibly water/goods packets share enough envelope structure. | Needs comparative packet papers, not only Fractanet. |
| Q10 — First MVP | [FractaVolta/research/fractanet.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md); [FractaVolta/research/bonne_marque_mvp.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/bonne_marque_mvp.md); [cogentia/research/cogentia_continuation_packet_routing.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia_continuation_packet_routing.md); [Inox/research/inox-spec.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md) | Start with a programmable API gateway rather than the full multi-substrate network. | Recommended MVP: Fractanet API gateway with Inox Core, COP trace, cache, dispatch and simple exergy scoring. |

---

## 30. First MVP direction

The most realistic MVP is not the full multi-substrate Fractanet.

The first MVP should be a programmable API gateway that demonstrates the core invariants at small scale:

- verbs instead of endpoints;
- script registry;
- Inox-first execution;
- limited JavaScript adoption profile;
- programmable cache;
- traceable dispatch;
- COP event stream;
- optional long-running job;
- explicit capabilities;
- small RAIX-style redundancy between two gateways or routes;
- simple exergy-inspired routing score.

This MVP would not prove the whole theory. It would instantiate the invariants.

A successful MVP should answer:

> Can a verb be called, dispatched, executed near target endpoints, cached, traced, supervised, and explained without creating a new point of capture?

---

## 31. Claim manifest

| Claim | Status | Validation level |
|---|---|---|
| Fractanet is the infrastructural instance of GPN | corpus thesis | human validation required |
| Control/data separation can be generalized beyond bits | strong conceptual claim | supported by GPN framework; requires further examples |
| Inox is the micro-architecture of Fractanet | corpus architectural claim | supported by Inox control/data stack design; requires technical formalization |
| COP is the supervision plane | corpus architectural claim | supported by COP event/task/continuation model; requires implementation mapping |
| RAIX generalizes RAID to arbitrary X | conceptual extension | promising but needs formal definition |
| Exergy is the correct routing criterion | doctrinal/technical claim | strong within corpus; needs operational metrics |
| JavaScript should remain an adoption profile | design recommendation | pragmatic; subject to implementation feedback |
| No single point of capture is as important as no single point of failure | core doctrine | stable; requires architectural checklist |
| Fractanet increases signal/noise for humans and AI agents | design goal | requires evaluation criteria |

---

## 32. Continuation

The next useful actions are:

1. submit this draft to review under [cogentia/prompts/reviewer.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/reviewer.md);
2. integrate only high-signal objections;
3. produce a diagram of the architecture;
4. define a minimal Fractanet verb schema;
5. define the MVP programmable gateway;
6. update [FractaVolta/research/index.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md) only after human validation;
7. extract cognitive packets into `cogentia` if the draft stabilizes.

---

## Minimal completion report

- **Target document:** [FractaVolta/research/fractanet.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md)
- **Files produced or changed:** conversational draft prepared as `fractanet.md`; no GitHub repository write performed.
- **Source or derived product:** source document draft.
- **Critiques integrated:** none yet from Grok/reviewer; this is the redactor draft to be reviewed.
- **Critiques rejected or deferred:** frontmatter-specific document not found; used observed corpus frontmatter conventions and [cogentia/prompts/redactor.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/redactor.md) requirements.
- **Known risks:** over-integration of too many concepts; possible need to split into a shorter working paper plus appendices; RAIX and exergy metrics require formalization.
- **Human validation needed:** naming, public claims, RAIX scope, JavaScript positioning, exergy-routing formulation, repository update decision.
- **Next useful action:** review this file with [cogentia/prompts/reviewer.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/reviewer.md), then integrate only high-signal corrections.
