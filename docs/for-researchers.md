---
title: For researchers
subtitle: Papers, methodology, contestation as first-class contribution. The corpus is its own evidence — fork it, challenge it, build on it.
canonical_url: https://fractavolta.com/for-researchers
last_stamped_at: 2026-05-26
date: "2026-05-15"
status: "working-paper — auto-filled (frontmatter cleanup)"
---

Cette page s’adresse aux chercheurs et aux partenaires techniques qui souhaitent entrer dans la profondeur du travail. Si vous cherchez plutôt des opportunités concrètes, allez directement dans la section [En Corse](./fr/).

Pour un résumé plus opérationnel de la méthode et des outils concrets, voir la page [Méthode](./methodology).

Pour les opportunités et les chantiers concrets en Corse, voir directement la section [En Corse](./fr/).

## The corpus

The work spans six repositories, each producing research-grade documents that cross-reference each other:

- **[MareNostrum](https://github.com/JeanHuguesRobert/marenostrum)** — strategic framework, CXU specification, DHITL (Democratic Humans in the Loop), Mediterranean solar commons, circuit-to-packet transition theory
- **[FractaVolta](https://github.com/JeanHuguesRobert/FractaVolta)** — physical infrastructure layer: EPN, PGN, DC-native nodes, IPN, Mariani Village
- **[Cogentia](https://github.com/JeanHuguesRobert/cogentia)** — cognitive infrastructure tooling: cogentia.js, Cogentia Commons methodology, Pipeline method, continuation protocol
- **[inseme](https://github.com/JeanHuguesRobert/inseme)** — platform and COP runtime: Cognitive Orchestration Protocol, briques, applications
- **[barons-Mariani](https://github.com/JeanHuguesRobert/barons-Mariani)** — political/institutional framework: Plan 2038, *Discours de la seconde méthode*, *Projet #1755*
- **[Inox](https://github.com/JeanHuguesRobert/Inox)** — language and runtime substrate: concatenative stack VM with strict control/data plane separation, designed for nodes of the future *Fractanet*

Each repository carries a [`research/index.md`](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md) (this is FractaVolta's) and a [`research/corpus-status.md`](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/corpus-status.md). Together they constitute the navigable map.

---

## Foundational papers by layer

**Energy substrate**
- [The Unconscious Grid](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md) — store-and-forward as the repressed solution to energy sovereignty; §8 extends the diagnosis to cognition, sociability, money, and territory, making this the entry point to the wider packetization corpus ([FR](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/LE_RESEAU_INCONSCIENT.md))
- [Generalized Packet Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md) (v0.3) — the cross-domain framework: heterogeneous packets, resource occupancy, congestion elasticity, packet decay, cache hierarchies, backbone/last-mile decomposition, mesh resilience. EPN, PGN, IPN and Thermal Packets are instances of this.
- [DC-Native Energy Packet Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md) — 48V SELV node architecture
- [Packetized Gravity Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/PGN.md) — hydraulic exergy
- [Thermal Packet Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/thermal_packet_networks.md) (v0.2) — multi-scale store-and-forward architecture for low-exergy heat and cold distribution
- [Packet Paper Template](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_paper_template.md) (v0.2) — methodological template for declining the Generalized Packet Networks framework into substrate-specific papers
- [The Packet Transition: A Lateral Reading](https://github.com/JeanHuguesRobert/marenostrum/blob/main/packet_transition.md) — phronèsis, amathia, transition taxonomy
- [The Packet as Evolutionary Attractor](https://github.com/JeanHuguesRobert/marenostrum/blob/main/packet_attractor.md) — complexity-theoretic framing

**Compute substrate**
- [CXU Specification](https://github.com/JeanHuguesRobert/marenostrum/blob/main/CXU_SPEC.md) — Compute eXergy Unit pricing primitive
- [Inference Packet Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/inference_packet_network.md) (v2.0, 2026-05) — packet logic applied to inference continuity

**Cognition layer**
- [Agent-Resumable CLI](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md) — externalized judgment, continuations, provider-neutral resumption
- [Cognitive Packets](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md) (v0.3) — envelope-and-payload format generalising the continuation pattern beyond the CLI; six packet kinds (continuation, objection, hypothesis, decision, failure, routing)
- [Cognitive Packet Switching](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_switching.md) (published source v1.0) — a protocol layer for routable ideas, continuations and agent orchestration: extends the envelope/payload model into a switching/routing layer. The same conceptual shift that took information networks from circuit-switched to packet-switched, applied to cognition.
- [COP Reactive Cognitive Extension](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/REACTIVE_COGNITIVE_EXTENSION.md) (v0.1, operational note) — protocol surface for packet attractors, CogQueries and pressure strategies, derived from the [source document](https://github.com/JeanHuguesRobert/inseme/blob/main/research/reactive_cognitive_cop_extension.md); native implementation delegated to [Inox](https://github.com/JeanHuguesRobert/Inox/blob/master/research/reactive_sets_inox_cop_implementation.md).
- [COP Implementation Profiles](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/ImplementationProfiles.md) — documentation convention for concrete COP implementations; the kernel reference profile lives in [`packages/cop-kernel/PROFILE.md`](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-kernel/PROFILE.md).
- [Pipeline](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md) (method note v0.4) — *pipeline on the surface, packet network in depth.* The corpus's operational method note; self-applicative; operational counterpart of the *Discours de la seconde méthode*.
- [Derived Products](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md) (v0.2) — source ↔ derived split: the substantive content belongs to a versioned source corpus; academic papers, blogposts, parliamentary notes, public dashboards are all derived forms of equal status. *Do not popularize from the academic paper; derive from the corpus.*
- [cogentia.js — Tutorial and Near-Specification](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia_js_tutorial.md) (auto-generated, v0.1, targets `cogentia.js v0.10.0`) — core ideas, storage model, 14 workflows, command reference. Sufficient detail to seed a faithful re-implementation in another language, persistence layer, or rendering format.

**Language and runtime substrate**
- [Inox — Programming Language Specification](https://github.com/JeanHuguesRobert/Inox/blob/master/research/inox-spec.md) — concatenative stack VM with strict control/data plane separation; runtime substrate for the future *Fractanet*; TS reference implementation today, heading for WASM, C/C++, and bare-metal ESP32
- [Reactive Sets in Inox — Native Implementation Path](https://github.com/JeanHuguesRobert/Inox/blob/master/research/reactive_sets_inox_cop_implementation.md) (v0.1) — implementation path from Toubkal-style dataflow toward the COP Reactive Cognitive Extension; positions Inox as the native runtime for the reactive cognitive layer
- [The COP Manifesto](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Manifesto.md) — TCP/IP for intelligences
- [COP Architecture](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Architecture.md) — full protocol specification
- [Cogentia Commons Working Paper](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md) — methodology for distributed knowledge production

**Civic layer**
- [DHITL — Democratic Humans in the Loop](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md) — the axiom: AI may participate in epistemic production; living persons alone govern
- [Democratic AI Safety](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/democratic_ai_safety.md) (v0.5) — the political layer of AI Safety: a model controllable by its deployer may still accelerate AI-augmented legal persons against the demos. Companion to DHITL.
- [Discours de la seconde méthode](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md) — methodology rules (publish process, objections as first-class, machine-readable structure, corpus as evidence)
- [La méthode des terrains féconds](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/methode_terrains_feconds.md) (v0.4) — pre-deliberative protocol: depolarize conflicts of ideas by reconfiguring the oppositions before the argumentative confrontation
- [Traçabilité des actes](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/traceabilite_des_actes.md) (v0.15.1) — governance doctrine of engaging acts: trace, imputation, justification, correction, revocation; an AI may assist deliberation but must not absorb imputability
- [Test du critère Rossignol](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/test_critere_rossignol.md) (v0.1, working note) — doctrinal criterion for procedural stabilizers: a dispositif is valid iff it can produce a *Rossignol* (a point of attestation exposable outside its own frame). Applied to four candidate dispositifs (Cogentia, symmetric traceability, FractaVolta, Kudocracy) and to [Inox itself](https://github.com/JeanHuguesRobert/Inox/blob/master/research/test_critere_rossignol_inox.md)

---

## The methodology

The corpus follows the **second method**:

1. **Publish the process, not only the result.** Continuations make the process inspectable — where the system asked, what alternatives existed, who answered, how it resumed.
2. **Every objection is a first-class contribution.** Falsifiable claims, marked-unfalsifiable feelings of certainty, requests for specifics — all are typed, all are recorded, none are erased.
3. **Structure for machine readability from the start.** Stable identifiers, schemas, canonical URLs, append-only audit logs.
4. **Let the corpus be its own evidence.** The repositories demonstrate the method on themselves: cogentia.js scans for unanchored claims; continuations process those decisions; the audit trail is part of the proof.
5. **Encode the boundary in the architecture (Rule 0).** Epistemic participation vs political governance: AI agents may supply judgment, but binding decisions require signed human accountability.

The **operational counterpart** of the second method is the [Pipeline](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md): *pipeline on the surface, packet network in depth.* Intuitions become cognitive packets; packets become versioned source documents; source documents derive into audience-specific products (papers, blogposts, parliamentary notes, public dashboards); public feedback reintegrates into the corpus. The method note is itself a self-describing artefact of the method it describes — Rule 4 applied to method-production. The companion paper [Derived Products](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md) formalises the source ↔ derived split.

---

## The continuation protocol

`cogentia.continuation.v1` is the operational realization of `cop/continuation` (COP's foundational continuation primitive). It is a typed, validated, provider-neutral resumption point for CLI tools.

The soundness test is binding:

> Can Claude be replaced by a human, or by another agent, without modifying `cogentia.js`?
> If yes, the protocol is sound. If no, the protocol is contaminated.

The protocol is implemented in [`scripts/cogentia.js`](https://github.com/JeanHuguesRobert/cogentia/blob/main/scripts/cogentia.js) as of v0.5.0. Subcommands: `continuation emit`, `inspect`, `resume`, `fail`, `abort`, `queue`, `schema`. See the [paper](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md) for the full design.

Heraclitean follow-up: every resume that closes a continuation (success or abort) emits a dormant successor. History never 100% ends; the only constant is change.

---

## How to contribute

The corpus is open source under CC BY-SA 4.0 (research) and MIT (code). Three ways to engage:

**As a contestant**
- File an objection on any paper as a GitHub issue or pull request.
- Per Rule 2, your objection becomes part of the record. We will either convert it to a falsifiable claim, mark it as a feeling-of-certainty (with attribution), or request the specifics that would make it testable.
- A continuation will be emitted for the conversion. You can watch the audit trail in `.cogentia/continuations/`.

**As a contributor**
- Fork any repository.
- Add to the research index following the canonical patterns (front-matter with `canonical_url`, the `.cogentiaignore` for operational artifacts).
- Run `cogentia.js scan` to verify your additions are anchored.
- Open a PR.

**As an extender**
- Write a new brique for inseme (see [BRIQUE_SPEC](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-host/BRIQUE_SPEC.md)).
- Write a new continuation profile on top of `cop/continuation`.
- Replicate the EPN / PGN / IPN architecture on a different territory.

---

## Toolchain

- **`cogentia.js`** — the Cogentia Commons CLI. Multi-repo scan, link validation, canonical URL stamping, continuation protocol. Installation: clone the [cogentia repo](https://github.com/JeanHuguesRobert/cogentia), run `node scripts/cogentia.js help`.
- **inseme + COP** — the deployable platform. Installation: clone the [inseme repo](https://github.com/JeanHuguesRobert/inseme), see the README for the Turbo monorepo setup.
- **`.cogentia.json`** — per-corpus registry of repositories (created by `cogentia.js add`).
- **`.cogentiaignore`** — per-repo ignore patterns for operational artifacts that shouldn't be flagged as unanchored claims.

---

## Contact & prochaines étapes

📧 [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org)  
🔗 [LinkedIn – FractaVolta](https://www.linkedin.com/company/fractavolta/)

Pour les opportunités et les chantiers concrets en Corse, voir directement la section [En Corse](./fr/).

*All papers: CC BY-SA 4.0. All software: MIT.*
