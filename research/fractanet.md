---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-06-01
title: "Fractanet"
date: "2026-05-31"
status: "working-paper — auto-filled (frontmatter cleanup)"
---

# Fractanet

**The Decentralized Cognitive Mesh**

**Jean Hugues Noël Robert, baron Mariani**  
FractaVolta — Corte, Corsica

*Working paper — May 2026*  
*License: CC BY-SA 4.0*

---

## Abstract

**Fractanet** is the name given to the emerging decentralized cognitive infrastructure that arises when several independent lines of work are combined:

- Packet-based architectures for survivability and distribution (ARPANET lineage, generalized through Energy Packet Networks and Inference Packet Networks).
- Cognitive Orchestration (COP) as the protocol and runtime for structured, traceable, long-running multi-agent reasoning, including its recent evolution with hierarchical sub-buses and federation primitives.
- Inox as the portable, efficient execution substrate designed to run from cloud down to bare-metal edge devices with strict control/data plane separation.

Fractanet is **not** a single product or network. It is an **architectural pattern**: a way to organize computation, memory, energy, and agency so that useful cognitive work can continue even when large parts of the conventional stack are unavailable, captured, or compromised.

Its core promise is **bounded cognitive continuity without a capturable center**.

---

## 1. Generalized Packet Networks vs. Fractanet

This document uses a deliberate distinction introduced in *Generalized Packet Networks*:

- **Generalized Packet Networks (GPN)** designates the *theoretical cross-domain framework* — a vocabulary and research programme for applying packet thinking across heterogeneous substrates (information, energy, heat, inference, logistics, governance, etc.).
- **Fractanet** designates the *concrete infrastructural instance* being developed in this corpus: the actual repositories, tools (`cogentia.js`), pilot deployments, governance experiments, and running systems that instantiate GPN principles.

The two are not interchangeable. GPN can be studied as theory without committing to Fractanet as infrastructure. Fractanet can be built and operated without requiring every participant to adopt the full theoretical framework.

This separation is maintained throughout the corpus.

---

## 1. The Packetization Thesis

A recurring structural transition appears across many complex systems as they mature:

> Continuous flows → Discrete, addressed, routable packets

This pattern has been observed or engineered in:

- **Information networks** — ARPANET / Internet (packet switching)
- **Storage** — RAID (redundant arrays of independent disks)
- **Energy** — Energy Packet Networks (EPN)
- **Inference / Cognition** — Inference Packet Networks (IPN)

Each layer applies the same idea: break a valuable but fragile continuous resource into discrete, versioned, signed, movable units that can be stored, routed, redundantly executed, and audited.

Fractanet completes this stack at the **cognitive layer**.

---

## 3. COP as the Cognitive Orchestration Layer

While the packet layers below provide the substrate for moving and redundantly executing units of work, they do not by themselves provide structure, causality, or long-term reasoning across agents and time.

**COP (Cognitive Orchestration Protocol)** supplies the missing coordination protocol:

- **Topics** as long-lived scopes of activity
- **Tasks and Steps** as structured units of work
- **Events** as the immutable source of truth (the "packets" at the cognitive level)
- **Artifacts** as durable outputs
- **Continuations** as first-class portable suspended reasoning (the key mechanism for long-running, resumable, cross-system cognition)
- **Bus + Scheduler + JobScheduler** as the decentralized routing and supervision mechanisms

The 2026 kernel evolution has added critical Fractanet capabilities:

- Native **sub-buses** (`bus.forTopic(topicId)`, `bus.sub(namespace)`) for hierarchical, per-topic scoping.
- **Federation primitives** (`federate()`, `declareInterest()`, `propagateInterest()`) enabling multiple COP instances to form a resilient mesh.
- Deeper integration of Task/Step/Continuation lifecycle with the scoped bus.

COP is therefore positioned as the **coordination and agency layer** of Fractanet — the place where cognitive work is structured, suspended, resumed, supervised, and routed across the underlying packet substrates.

---

## 4. Inox as the Execution Substrate

Inox is the language and runtime designed to implement the lower levels of this architecture efficiently and portably:

- Concatenative stack VM with strict **control plane / data plane separation**
- Actor model with named values and reactive sets
- Designed to descend gracefully from comfortable hosts (Node, Deno, browsers) down to bare metal (ESP32, etc.)

In a mature Fractanet, Inox nodes become the physical "X" in RAIX — redundant, independent execution units that can host COP agents, run inference packets, and participate in the mesh with the same semantics as larger nodes.

See also the Inox specification and research in the Inox repository.

---

## 5. Fractanet as Synthesis

Fractanet is the name for the system that emerges when these layers are composed intentionally:

| Layer                    | Packet Primitive             | Primary Function                        | Key Technology                  |
|--------------------------|------------------------------|-----------------------------------------|---------------------------------|
| Information              | IP packets                   | Survivable communication                | ARPANET / Internet              |
| Storage                  | Blocks                       | Survivable data                         | RAID                            |
| Energy                   | Exergy packets               | Survivable energy supply                | EPN                             |
| Inference                | Inference packets            | Survivable cognition (degraded mode)    | IPN                             |
| **Coordination**         | **Events + Continuations**   | **Survivable reasoning & agency**       | **COP + Fractanet Bus** (sub-buses + federation) |
| **Execution**            | **Instructions + State**     | **Portable agent runtime**              | **Inox**                        |

The result is a system in which:

- Cognitive work can be suspended (Continuation), packaged, moved, or resumed on any available redundant node in the mesh.
- Failure, delay, partition, or capture of any single "X" produces observable events rather than silent catastrophe.
- No single operator, jurisdiction, energy source, or hardware vendor can become a single point of failure or control.

See also:
- `research/generalized_packet_networks.md` for the overarching GPN framework
- `research/inference_packet_network.md` for the inference layer
- The COP kernel (especially the bus and federation work in the `inseme` repository)

---

## 5. Design Principles

Fractanet inherits and extends several strong principles:

- **Everything is an Event** (or can be projected from one).
- **Discretization as resilience** — continuous dependence is fragility.
- **Control / Data plane separation** at every layer (visible in Inox, in COPBus design, in packet networks).
- **RAIX generalization** — redundancy is applied not just to disks or nodes, but to the full stack of resources required for cognition.
- **Actor-oriented coordination** — agents (human or machine) interact only through well-defined messages/events on the Bus.
- **Observable supervision** — resumption, retry, backoff, and obsolescence are first-class and auditable.

---

## 6. Relationship to Existing Work

- **Inference Packet Networks** (`research/inference_packet_network.md`) describe the payload layer.
- **COP** (in the `inseme` repository) provides the orchestration protocol and the evolving bus + federation implementation.
- **Inox** provides the execution environment.
- **Energy Packet Networks** and related work provide the physical substrate layer.
- The broader corpus (MareNostrum, barons-Mariani, Cogentia, etc.) supplies the philosophical, political, and methodological framing.

Fractanet is the name for the integrated vision.

---

## 7. Current Status (May 2026)

As of this writing:

- The core COP kernel (including Task/Step/Continuation helpers and the generalized bus with sub-buses and federation primitives) is being actively hardened in the `inseme` repository.
- The primary validation environment is the COP Continuation Bac-à-Sable (`inseme/sandbox/cop-continuation-bac-a-sable`), which now includes a dedicated `federation-demo` scenario.
- Multiple packet-layer papers (Inference, Energy, Thermal, Generalized) exist as working papers.
- Inox continues development as the long-term execution substrate.
- Pilot physical deployments (Mariani Village, agrivoltaic, datacenter experiments) are being used to ground the concepts.

## 8. Open Questions & Next Steps

- How should topic-scoped sub-buses interact with cross-node federation in practice?
- What is the minimal viable "Fractanet Node" (especially on Inox)?
- How do we handle custody transfer, provenance, and economic signaling across the mesh?
- What governance and incentive models are compatible with the architectural invariants?

These questions are being explored through continued kernel and bac-à-sable work in `inseme`, through the packet papers in this repository, and through physical/governance experiments across the corpus.

---

**Fractanet is not a network you join.**  
**It is an architectural posture you adopt** — one that treats discretization, distribution, redundancy, and observable coordination as the foundation for sovereign, long-term cognitive capability.

> Sovereignty is not measured only by peak performance under ideal conditions.  
> It is measured by the ability to continue producing useful reasoning when conditions fail.

---

*Comments, objections, and contributions are welcome via the usual channels of the corpus.*