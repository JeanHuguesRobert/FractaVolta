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
  - "Confirm whether this v0.3.2 should remain the canonical working draft."
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

The historical reference is packet switching. ARPANET showed that communication could be made more resilient by avoiding a single centralized switching authority and by routing discrete packets through a distributed network.

Fractanet extends this intuition, but not by metaphor alone. The extension follows the grammar developed in **Generalized Packet Networks**: what matters is not that every substrate is identical to digital data, but that many operational domains can be analyzed through bounded, addressable, governable units that circulate, wait, degrade, occupy resources, require routing, and may be transformed or consumed.

Thus the candidate packet types are not only data packets. They may include:

- energy packets;
- thermal packets;
- water packets;
- goods or logistics packets;
- inference packets;
- cognitive packets;
- continuation packets;
- governance packets;
- mandates, permissions, duties, responsibilities.

This list is not a license to call everything a packet. It is a hypothesis: if a unit is bounded, addressable, delayable or storable, independently governable, and operationally measurable, then it may be packetized. If not, it should not be forced into the framework.

---

## 4. GPN and Fractanet

The distinction between **Generalized Packet Networks** and **Fractanet** should remain explicit.

| Layer | Role | Status |
|---|---|---|
| Generalized Packet Networks | Theoretical grammar of packetization across substrates | Conceptual framework |
| Fractanet | Programmable infrastructural implementation of that grammar | Working architectural proposal |
| Inox | Execution substrate and micro-architecture | Language/runtime project |
| COP | Supervision and control protocol | Control/supervision protocol |
| RAIX | Redundancy principle across arbitrary X | Concept to formalize |
| Exergy | Useful-capacity criterion | Cross-domain evaluation principle |

Fractanet therefore should not claim to replace all domain-specific networks. It proposes a shared control-plane grammar and programmable infrastructure through which heterogeneous packet networks can interoperate, be supervised, and be optimized for useful capacity.

---

## 5. Generalized control plane and heterogeneous data planes

The classical distinction is:

- **control plane** — the part of a network that decides how packets are routed;
- **data plane** — the part that forwards the packets themselves.

Fractanet generalizes this distinction beyond bits.

The **control plane** carries the envelope:

- origin;
- destination;
- identity;
- rights;
- capabilities;
- priority;
- TTL;
- freshness;
- decay policy;
- signatures;
- trace requirements;
- routing constraints;
- supervision events;
- human approval requirements;
- exergy/scoring metadata.

The **data planes** carry payloads:

- bits;
- energy;
- heat;
- water;
- goods;
- compute;
- inference;
- cognition;
- delegation;
- institutional authority.

The same control plane must not pretend that all payloads are identical. Its role is not to erase substrate differences. Its role is to expose the common operational questions: who may route, where, under what constraints, with what trace, what freshness, what risk, what reversibility, and what useful capacity.

---

## 6. Packet = envelope + payload

The generic form is:

```text
packet = envelope + payload
```

The envelope is for governance, routing, tracing, and supervision. The payload is what is actually transported, delivered, transformed, consumed, activated, or revoked.

The control plane should be able to route and supervise the envelope without unnecessarily capturing the payload. This is essential for:

- privacy;
- sovereignty;
- anti-capture;
- security;
- reduction of exposure;
- multi-substrate interoperability.

### 6.1 Comparative envelope sketch

The following table is not a finished schema. It is a test of the claim that heterogeneous packet types can share enough envelope structure to be governed by a common control plane while preserving substrate-specific fields.

| Packet type | Payload | Shared envelope fields | Substrate-specific fields |
|---|---|---|---|
| Data packet | file, message, event, API response | origin, destination, rights, TTL, signature, trace, freshness | encoding, size, checksum, confidentiality level |
| Energy packet | useful energy allocation, battery slot, charging right | origin, destination, priority, rights, validity window, trace | kWh, power limit, voltage/current profile, storage losses, safety constraints |
| Water packet | volume allocation, delivery, reserve access | origin, destination, rights, priority, validity window, trace | volume, potability, pressure, local scarcity, legal usage category |
| Goods packet | physical item, spare part, food, material | origin, destination, custody, priority, trace | weight, volume, perishability, chain of custody, transport mode |
| Inference packet | prompt, model call, result, continuation | origin, destination, rights, TTL, trace, cost limit | model, token budget, confidentiality, latency tolerance, context window |
| Mandate packet | delegation, permission, responsibility | origin, destination, identity, rights, revocation, trace | duration, scope of authority, human approval, legal/institutional validity |

The table shows partial compatibility, not identity. A shared envelope does not imply a shared physics. It implies a shared control grammar.

---

## 7. Verbs instead of endpoints

A conventional API client calls endpoints:

```text
GET /users/123/orders
POST /tasks
```

A Fractanet client calls **verbs**:

```text
customer.summary
route.energy.packet
deliver.cognitive.packet
approve.mandate
resume.continuation
```

A verb is a named operational capacity. Its implementation may vary according to:

- namespace;
- tenant;
- client type;
- capability set;
- region;
- data residency;
- runtime;
- cache state;
- supervision requirement;
- cost;
- latency;
- exergy;
- fallback policy;
- availability of gateways or endpoints.

Therefore:

> **The verb is the stable vocabulary. The endpoint is only one possible implementation.**

---

## 8. Dispatch

Calling a verb does not necessarily bind the caller to a fixed endpoint.

The Fractanet gateway resolves:

```text
verb + namespace + capabilities + policy + context -> implementation
```

This resembles dispatch tables in object-oriented languages. A method call names an operation; the runtime selects the concrete implementation. Likewise, a Fractanet call names a verb; the gateway selects the appropriate route, script, cache, endpoint, continuation, or fallback.

A possible dispatch sequence:

```text
call customer.summary
  -> resolve namespace
  -> check capabilities
  -> reject forbidden routes
  -> inspect cache and freshness
  -> estimate exergy score of admissible routes
  -> select implementation
  -> execute through Inox/COP
  -> return result, stream, or continuation
```

The dispatch decision must be traceable. It is itself an act.

---

## 9. Registry of verbs and scripts

Fractanet requires a registry of verbs, scripts, versions, policies, and namespaces.

The registry should track:

- verb name;
- namespace;
- version;
- owner;
- status;
- input schema;
- output schema;
- capabilities required;
- APIs or data planes touched;
- runtime profile;
- cache policy;
- trace policy;
- human validation requirement;
- deprecation policy;
- review status.

A registered script may become a synthetic endpoint, but the more stable abstraction is the verb.

### 9.1 Minimal verb record

A minimal verb record could begin as follows:

```yaml
verb: customer.summary
version: 0.1.0
namespace: public.demo
status: draft
runtime: inox-core
input_schema:
  customer_id: string
output_schema:
  customer_id: string
  summary: object
capabilities_required:
  api.read:
    - /customers/{customer_id}
    - /orders?customer_id={customer_id}
  cache.write:
    max_ttl_seconds: 300
routing:
  default_policy: exergy_after_constraints
  fallback: stale_cache_if_allowed
trace:
  cop_events_required:
    - verb.called
    - capabilities.checked
    - route.selected
    - result.returned
human_approval:
  required: false
capture_surface:
  registry_raix_required: true
```

This is intentionally small. It is not yet the Fractanet schema. It is a first test object.

---

## 10. Namespaces and local/private endpoints

Namespaces are not cosmetic. They are control surfaces.

Fractanet should distinguish, at minimum:

- public verbs;
- tenant-private verbs;
- client-type verbs;
- partner verbs;
- local gateway verbs;
- experimental verbs;
- deprecated verbs.

Example:

```text
public.customer.summary@v1
client.mobile.customer.summary@v2
tenant.acme.customer.summary@v3
local.gateway.eu-west.energy.buffer@v1
experimental.cognitive.packet.route@v0
```

Namespaces must be governed. Otherwise the registry itself becomes a capture surface.

---

## 11. Registry as capture surface

A distributed network can still be captured through its registry.

If a single actor controls:

- namespace allocation;
- script signing;
- capability grants;
- version promotion;
- deprecation;
- routing policies;
- trace custody;
- model selection;
- identity binding;

then Fractanet has not removed capture. It has relocated it.

Therefore the registry layer must itself satisfy RAIX principles:

- mirrored registries;
- transparent diffs;
- signed records;
- independent review paths;
- local override under explicit policy;
- auditable namespace governance;
- exit and fork rights;
- traceable promotion/deprecation;
- no single registry authority for critical verbs.

This is one of the central design constraints of Fractanet.

---

## 12. Inox as micro-architecture

Inox is not merely an implementation language. It is the micro-architecture of Fractanet.

Its relevant properties are:

- concatenative logic;
- verb composition;
- explicit control/data separation;
- minimal core close to Forth;
- expressive dialects;
- potential for continuations;
- suitability for backtracking;
- compact representation readable by agents;
- capacity-oriented execution.

At the VM level, Inox already separates at least:

- a control stack;
- a data stack.

This mirrors the Fractanet distinction:

| Scale | Control plane | Data plane |
|---|---|---|
| Inox VM | control stack, verbs, continuation state | data stack, values, payload fragments |
| Programmable gateway | dispatch, policies, registry, COP events | API results, cache values, streams |
| Fractanet network | envelopes, rights, supervision, routing | heterogeneous packet payloads |
| GPN substrate | governance of packets | data, energy, water, goods, inference, mandates |

Thus Inox is to Fractanet what a cell is to an organism: the same organizational invariant appears at a smaller scale.

---

## 13. Inox Core, dialects, and Full Inox

Inox should not be understood as one monolithic runtime.

A useful stratification is:

| Layer | Role |
|---|---|
| Inox Core | minimal concatenative runtime, Forth-like, small enough for distributed gateways |
| Inox API dialect | verbs, endpoint composition, schemas, cache, dispatch |
| Inox COP dialect | supervision events, pause/resume, approval, traces |
| Inox routing dialect | route exploration, fallback, exergy scoring, backtracking |
| Full Inox | expressive language for complex authoring, agents, transformations |

This solves a tension. Fractanet needs a runtime small enough to run near endpoints, but also expressive enough to define sophisticated verbs and be manipulated by agents.

Formula:

> **Full Inox for thinking and generation. Inox Core for execution everywhere.**

---

## 14. JavaScript as adoption profile

JavaScript should be available at first, but only as an adoption profile.

It is useful for:

- short scripts;
- JSON transformations;
- simple API aggregation;
- low-risk synthetic endpoints;
- developer onboarding.

It should not carry the deep Fractanet model:

- full continuations;
- backtracking;
- complex routing;
- streaming supervision;
- exergy-oriented route exploration;
- long-lived computation;
- critical capability governance.

JavaScript can be sandboxed, especially through engines such as QuickJS or V8 isolates, but it does not naturally express the control/data separation and continuation logic that Fractanet needs.

Recommended boundary:

| Profile | Use |
|---|---|
| `javascript-sandbox@1` | bounded adoption scripts, no full continuation, explicit state only |
| `inox-core@1` | serious execution path, capability verbs, registry, compact runtime |
| `inox-full@1` | complex composition, continuations, backtracking, agent-assisted generation |
| `cop-inox@1` | supervised, streamable, resumable, human-sensitive acts |

Thus:

> **JavaScript may onboard. COP/Inox must govern.**

---

## 15. COP as supervision plane

COP is the supervision plane of Fractanet.

It should describe and trace:

- verb calls;
- capability checks;
- route selection;
- cache hits and misses;
- branch exploration;
- backtracking;
- continuation capture;
- pause/resume;
- human approval;
- fallback;
- failure;
- explanation;
- revocation.

Example COP events:

```text
verb.called
capabilities.checked
route.candidate.enumerated
route.rejected
route.selected
cache.hit
cache.miss
branch.started
branch.backtracked
continuation.paused
continuation.resumed
human.approval.requested
human.approval.granted
human.approval.denied
result.returned
```

COP is not the runtime. It is the control and supervision protocol that makes runtime acts inspectable.

### 15.1 Human approval lifecycle

For sensitive verbs, human approval should itself be a first-class control-plane object:

```text
approval.requested
  -> approval.displayed
  -> approval.granted | approval.denied | approval.expired
  -> approval.bound_to_trace
  -> approval.revoked? if policy allows
```

The approval envelope should include:

- requested action;
- requesting actor;
- affected payload class;
- time window;
- risk level;
- reversibility;
- required explanation;
- trace identifier;
- revocation policy.

This prevents human approval from becoming a vague checkbox.

---

## 16. Long-running executions, streaming, and continuations

Fractanet should support at least three execution modes:

| Mode | Description |
|---|---|
| sync | short request/response execution |
| async job | long execution with later retrieval |
| streaming | progressive results, trace, checkpoints, warnings |
| continuation | suspendable/restartable execution context |

Long-running execution requires persistent state.

A continuation should preserve, at minimum:

- script version;
- runtime version;
- input;
- local execution state;
- logical stack or continuation point;
- capabilities;
- quotas consumed;
- cache references;
- trace state;
- pending approvals;
- route candidates or branch state.

Inox is well suited to this because its execution model can be designed around serializable control/data structures. JavaScript should initially be limited to explicit state-based resumable jobs.

---

## 17. Programmable cache

The cache should not be an opaque optimization. It should be a programmable, scoped, traceable capability.

A script or verb may use:

- TTL;
- freshness policy;
- stale-while-revalidate;
- quota-aware caching;
- cost-aware caching;
- exergy-aware caching;
- tenant-scoped cache;
- gateway-local cache;
- regional cache;
- script-local memoization.

Cache operations should produce trace events:

```text
cache.lookup
cache.hit
cache.miss
cache.set
cache.revalidate
cache.stale_used
cache.invalidated
```

The cache must not become a hidden data store. Its scope, TTL, sharing policy, and invalidation logic are part of the envelope.

---

## 18. Backtracking and exploratory routing

Fractanet should not be limited to sequential execution or simple parallelism.

With continuations and a concatenative model, Inox can support Prolog-like backtracking:

```text
try best route
  if forbidden -> backtrack
  if unavailable -> backtrack
  if too costly -> backtrack
  if stale unacceptable -> backtrack
  try fallback route
```

This makes dispatch exploratory rather than merely table-driven.

A route is not just selected. It may be searched for under constraints.

Backtracking is useful for:

- fallback;
- route optimization;
- constraint satisfaction;
- distributed gateway selection;
- cache vs. recomputation decisions;
- model selection;
- continuation placement;
- human approval alternatives.

But it must be supervised. Each branch should be visible through COP.

Formula:

> **Inox explores. COP explains.**

---

## 19. Exergy-oriented routing

Fractanet should not optimize for raw energy alone.

The relevant concept is **exergy**: useful energy, or more generally useful capacity produced relative to cost, loss, risk, and noise.

In routing terms:

> **Capabilities and policies define the admissible space. Exergy ranks the admissible routes.**

Hard constraints come first:

- no capability, no route;
- wrong jurisdiction, no route;
- forbidden payload exposure, no route;
- required human approval missing, no route;
- tenant-private verb called by public client, no route.

Only then may the system compare routes using an exergy-inspired score.

A possible score:

```text
score(route) = useful_capacity / (energy + latency + monetary_cost + risk + noise + staleness + quota + capture_exposure)
```

Or equivalently, an energy-based style objective:

```text
E(route) = penalties - useful_capacity_bonus
```

At this stage, it is safer to describe this as an **exergy-inspired scoring function under hard constraints**, not yet as a complete model family.

### 19.1 Toy exergy scoring example

Assume three admissible routes remain after hard constraints:

| Route | Useful capacity | Energy | Latency | Risk | Capture exposure | Score sketch |
|---|---:|---:|---:|---:|---:|---:|
| A direct endpoint | 90 | 20 | 10 | 5 | 8 | 90 / 43 = 2.09 |
| B regional cache | 75 | 5 | 3 | 4 | 4 | 75 / 16 = 4.68 |
| C recomposition | 95 | 35 | 25 | 8 | 12 | 95 / 80 = 1.18 |

A pure quality maximizer might choose C. A pure latency optimizer might choose B. An exergy-oriented router chooses B if freshness is acceptable, because it produces the most useful capacity per combined cost and exposure.

This is only a toy example. It illustrates the ordering principle, not a final metric.

---

## 20. RAIX — Redundant Array of Independent X

RAIX generalizes RAID.

Where RAID originally concerns redundant arrays of independent disks, RAIX concerns redundant arrays of independent X, where X may be:

- nodes;
- gateways;
- routes;
- APIs;
- caches;
- storage;
- energy sources;
- models;
- agents;
- registries;
- policies;
- traces;
- jurisdictions;
- institutions;
- communities.

RAIX is justified only if redundancy increases useful capacity, resilience, sovereignty, or anti-capture more than it increases cost, noise, and complexity.

### 20.1 Minimal RAIX taxonomy

| X | Redundancy question | Capture risk reduced |
|---|---|---|
| Data | Are there independent copies or derivable reconstructions? | storage monopoly, data loss |
| Gateway | Can another gateway execute or supervise the verb? | infrastructure choke point |
| Route | Can traffic or execution be rerouted? | network or provider lock-in |
| Cache | Can stale/fresh alternatives preserve service? | endpoint dependency |
| Registry | Can verbs and policies survive registry capture? | namespace/capability monopoly |
| Trace | Can audit evidence survive local deletion or tampering? | accountability capture |
| Model | Can another model or agent evaluate the act? | AI vendor capture |
| Energy | Can another source provide useful capacity? | energy dependency |
| Institution | Can authority be checked or forked? | political capture |

RAIX remains underdefined at this stage. It needs its own taxonomy and metrics. But it already acts as a design test:

> **Where is the single point of failure? Where is the single point of capture?**

---

## 21. Anti-capture

Fractanet's finality is anti-capture as much as resilience.

A system may be technically redundant and politically capturable. A system may be politically plural but technically fragile. Fractanet should avoid both.

Capture surfaces include:

- cloud provider;
- API provider;
- model provider;
- identity provider;
- registry;
- namespace;
- cache;
- routing policy;
- trace custody;
- energy source;
- institutional authority;
- publication platform;
- governance process.

The architectural test is:

> **No single point of failure. No single point of capture.**

This requires not only technical redundancy, but also traceability, exit rights, forkability, and explicit control-plane governance.

---

## 22. Fractanet as distributed gateway mesh

Fractanet can begin as a programmable gateway, but it should not remain a centralized gateway.

Because it is a gateway architecture, instances can be placed near target endpoints:

- near APIs;
- near compute clusters;
- near energy controllers;
- near caches;
- near institutions;
- near communities;
- near users.

A Fractanet mesh should support:

- multi-instance deployment;
- load balancing;
- routing policy;
- redundancy;
- local cache;
- regional routing;
- continuation placement;
- trace replication;
- fallback;
- local autonomy under policy.

This is why RAIX and anti-capture must apply to control surfaces, not only payload paths.

---

## 23. Signal/noise for humans and agents

Fractanet aims to increase the signal/noise ratio for two populations:

- humans;
- AI agents.

For agents, signal means:

- structure;
- types;
- verbs;
- capabilities;
- schemas;
- traces;
- policies;
- versions;
- constraints.

For humans, signal means:

- intention;
- responsibility;
- risk;
- effect;
- reversibility;
- explanation;
- approval;
- appeal;
- memory.

Inox can be ultra-concise and agent-readable. COP must make the act human-intelligible.

Formula:

> **The code may be optimized for agents. The act must remain intelligible to humans.**

---

## 24. Fractal invariants

The "fracta" in Fractanet refers to multi-scale invariants.

The same structures recur:

| Invariant | Inox scale | Gateway scale | Network scale | Institutional scale |
|---|---|---|---|---|
| Control/data | control stack / data stack | registry / payload | envelope / data plane | mandate / act |
| Verb | word / operation | API verb | routed capacity | institutional action |
| Packet | value / stack item | API result / cache entry | data, energy, inference | mandate, responsibility |
| Continuation | captured execution | resumable job | long-lived route/workflow | deferred decision |
| Trace | execution state | COP events | audit stream | accountability record |
| Redundancy | alternative branch | fallback gateway | RAIX mesh | plural authority |
| Exergy | useful operation | efficient route | useful capacity | legitimate effect |

### 24.1 Cross-scale example: continuation

A continuation appears at several scales:

1. **Inox VM:** execution state can be suspended and resumed.
2. **Gateway:** a long-running verb becomes a resumable job.
3. **COP:** pause/resume events make the suspended act inspectable.
4. **Cognitive packet:** a reasoning process is packaged for later continuation.
5. **Institutional process:** a pending mandate or approval remains valid only under explicit conditions.

The invariant is not a metaphor. It is the repeated structure: preserve enough state to resume an act under controlled conditions.

---

## 25. Generalized packet boundary rule

The packet metaphor must be constrained.

A candidate packet should satisfy most of the following:

- bounded;
- identifiable;
- addressable;
- storable, delayable, or bufferable;
- independently routable or governable;
- measurable or auditable;
- transformable, consumable, executable, validable, or revocable;
- capable of carrying an envelope distinct from its payload.

Positive examples:

- an API request;
- a cached result;
- a battery charging slot;
- an inference request;
- a signed delegation;
- a task continuation.

Negative or borderline examples:

- continuous rainfall before measurement;
- an ongoing friendship;
- a vague political aspiration;
- diffuse cultural influence;
- unbounded institutional legitimacy;
- sensor noise before sampling.

This rule protects the framework from conceptual inflation.

---

## 26. Minimal Fractanet node

A minimal Fractanet node should support:

- receiving a verb call;
- resolving the verb in a registry;
- checking capabilities;
- selecting a route or implementation;
- executing a bounded Inox script or compatible profile;
- using a scoped cache;
- emitting COP trace events;
- returning a result, stream, or continuation;
- rejecting unauthorized or unbounded execution;
- exposing enough explanation for human review.

The first MVP should not attempt to implement physical packets. It should prove the digital/API control-plane invariant first.

---

## 27. Failure modes

### 27.1 Packet metaphor over-extension

If everything becomes a packet, the framework loses precision.

Mitigation: apply the boundary rule in section 25.

### 27.2 Control-plane capture

A distributed data plane can still be captured by a centralized registry, identity provider, model provider, or routing authority.

Mitigation: apply RAIX to control surfaces, not only data paths.

### 27.3 Opaque exergy optimization

A scoring function may become an opaque technocratic authority.

Mitigation: hard constraints first, inspectable candidate routes, COP explanation, human override where relevant.

### 27.4 Redundancy noise

Redundancy can become waste, complexity, and maintenance burden.

Mitigation: require exergetic accounting for RAIX.

### 27.5 Human displacement by agent-readable code

Dense Inox may become legible to agents but opaque to humans.

Mitigation: every critical act must have a human-readable COP explanation and review path.

### 27.6 Registry as chokepoint

The registry may become the new central point of capture.

Mitigation: registry RAIX, signed records, mirrored registries, transparent diffs, local override under explicit policy.

---

## 28. Non-claims

This document does not claim that:

- every flow should become a packet;
- all substrates are equivalent;
- Fractanet is already implemented;
- RAIX is already formally defined;
- exergy routing is already a complete model family;
- JavaScript can safely carry complex continuations;
- physical packet networks can be governed with no domain-specific law or engineering;
- anti-capture can be solved by architecture alone;
- COP/Inox eliminates the need for human validation.

The document claims only that a shared architectural grammar is emerging and that a limited programmable gateway MVP can test it.

---

## 29. Open questions

1. What is the minimal canonical schema for a Fractanet verb?
2. How should registry governance avoid capture?
3. What is the smallest viable Inox Core runtime?
4. Which COP events are mandatory for a minimal node?
5. How should exergy scoring be formalized without opacity?
6. How can RAIX be measured rather than merely named?
7. Which data-plane substrates should be tested first after the API gateway MVP?
8. How should human approval, revocation, and appeal be represented in the control plane?
9. How much of the generalized envelope can be shared across data, energy, water, goods, inference, and mandates?
10. What is the minimum demo that proves the fractal invariant without overbuilding?

### 29.1 Corpus anchors for open questions

The following anchors should be consulted before turning each open question into a new specification or article.

| Open question | Corpus anchors |
|---|---|
| Minimal verb schema | [Inox/research/inox-spec.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md); [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md); [cogentia/research/cognitive_packets.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md) |
| Registry governance and capture | [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md); [FractaVolta/research/index.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md); [cogentia/research/pipeline.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md) |
| Inox Core minimal runtime | [Inox/research/inox-spec.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md) |
| Mandatory COP events | [inseme/packages/cop-core/Invariants.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Invariants.md); [inseme/packages/cop-core/ImplementationProfiles.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/ImplementationProfiles.md); [inseme/research/reactive_cognitive_cop_extension.md](https://github.com/JeanHuguesRobert/inseme/blob/main/research/reactive_cognitive_cop_extension.md) |
| Exergy scoring | [marenostrum/safe_compute_exergy.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/safe_compute_exergy.md); [marenostrum/compute-exergy-omitted-variable.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/compute-exergy-omitted-variable.md); [marenostrum/CXU_SPEC.md](https://github.com/JeanHuguesRobert/marenostrum/blob/main/CXU_SPEC.md) |
| RAIX measurement | [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md); [FractaVolta/research/packet_paper_template.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_paper_template.md) |
| Physical data planes | [FractaVolta/research/thermal_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/thermal_packet_networks.md); [FractaVolta/research/inference_packet_network.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/inference_packet_network.md); [FractaVolta/research/generalized_packet_networks.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md) |
| Cognitive packets and continuations | [cogentia/prompts/cognitive_packet.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/cognitive_packet.md); [cogentia/research/cognitive_packets.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md); [cogentia/research/cognitive_packet_switching.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_switching.md); [cogentia/research/cogentia_continuation_packet_routing.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia_continuation_packet_routing.md) |
| MVP gateway | [FractaVolta/research/packet_paper_template.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_paper_template.md); [Inox/research/inox-spec.md](https://github.com/JeanHuguesRobert/Inox/blob/main/research/inox-spec.md); [inseme/packages/cop-core/ImplementationProfiles.md](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/ImplementationProfiles.md) |

---

## 30. First MVP direction

The first MVP should be digital and narrow.

A good candidate:

> **A Fractanet programmable API gateway exposing capability verbs over existing JSON APIs, executed by Inox Core, supervised by COP, with a small registry, scoped cache, simple fallback, and exergy-inspired routing after hard constraints.**

The MVP should demonstrate:

- one verb registry;
- two or three source APIs;
- one synthetic verb;
- one cache policy;
- one fallback branch;
- one continuation or resumable job;
- one COP trace stream;
- one JavaScript adoption script;
- one Inox core script;
- one exergy score example;
- one registry anti-capture mechanism, even if only by mirrored signed records.

Success criterion:

> A reviewer should be able to inspect the trace and understand why the gateway selected one route rather than another.

---

## 31. Claim manifest

| Claim | Status |
|---|---|
| Fractanet is the infrastructural instance of GPN | provisional but central |
| Fractanet generalizes control/data plane beyond bits | central claim |
| Inox is the micro-architecture of Fractanet | strong internal claim |
| COP is the supervision plane | strong internal claim |
| JavaScript is adoption-only | recommendation |
| RAIX prevents both failure and capture | promising but underformalized |
| Exergy is the correct optimization concept | central but requires metrics |
| Physical packet compatibility is plausible | to be demonstrated |
| Anti-capture requires control-plane redundancy | strong claim |
| MVP should begin as programmable API gateway | recommended next step |

---

## 32. Continuation

Useful next documents:

1. `fractanet_mvp_gateway_spec.md`
2. `raix_taxonomy.md`
3. `exergy_routing_note.md`
4. `fractanet_minimal_verb_schema.md`
5. `fractanet_registry_anti_capture.md`
6. `fractanet_cop_event_profile.md`
7. `fractanet_envelope_payload_examples.md`

Recommended next action:

1. validate whether this v0.3.2 remains the canonical working draft;
2. update `FractaVolta/research/index.md`;
3. produce a narrow MVP gateway specification;
4. extract a shorter technical note on envelope/payload/verbs;
5. ask a second reviewer to test whether the scope is now clearer;
6. avoid public manifesto-style publication until RAIX, exergy, and registry governance are better scoped;
7. extract cognitive packets into `cogentia` if the draft stabilizes.

---

## Minimal completion report

- **Target document:** [FractaVolta/research/fractanet.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md).
- **Files produced or changed:** `FractaVolta/research/fractanet.md` updated in GitHub as v0.3.2-draft.
- **Source or derived product:** source document draft.
- **Critiques integrated:** high-signal points from Grok/reviewer selectively integrated: envelope comparison, minimal verb record, registry capture surface, JavaScript/COP-Inox boundary, exergy toy example, RAIX taxonomy, corpus anchors for open questions, clickable references.
- **Critiques rejected or deferred:** full RAIX formalization, full exergy model, registry governance, physical packet compatibility, and MVP specification deferred to dedicated follow-up documents.
- **Known risks:** over-integration of concepts; registry capture; opaque optimization; redundancy noise; physical data-plane compatibility still to be demonstrated.
- **Human validation needed:** public definition, RAIX scope, JavaScript positioning, exergy-routing formulation, MVP boundary, institutional references.
- **Next useful action:** update `FractaVolta/research/index.md`, then produce either the MVP gateway spec or a short derived technical note.
