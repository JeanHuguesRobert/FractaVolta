---
title: For researchers
subtitle: Papers, methodology, contestation as first-class contribution. The corpus is its own evidence — fork it, challenge it, build on it.
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/for-researchers.md
last_stamped_at: 2026-05-15
---

## The corpus

The work spans five repositories, each producing research-grade documents that cross-reference each other:

- **[MareNostrum](https://github.com/JeanHuguesRobert/marenostrum)** — strategic framework, CXU specification, DHITL (Democratic Humans in the Loop), Mediterranean solar commons, circuit-to-packet transition theory
- **[FractaVolta](https://github.com/JeanHuguesRobert/FractaVolta)** — physical infrastructure layer: EPN, PGN, DC-native nodes, IPN, Mariani Village
- **[Cogentia](https://github.com/JeanHuguesRobert/cogentia)** — cognitive infrastructure tooling: cogentia.js, Cogentia Commons methodology, continuation protocol
- **[inseme](https://github.com/JeanHuguesRobert/inseme)** — platform and COP runtime: Cognitive Orchestration Protocol, briques, applications
- **[barons-Mariani](https://github.com/JeanHuguesRobert/barons-Mariani)** — political/institutional framework: Plan 2038, *Discours de la seconde méthode*

Each repository carries a [`research/index.md`](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md) (this is FractaVolta's) and a [`research/corpus-status.md`](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/corpus-status.md). Together they constitute the navigable map.

---

## Foundational papers by layer

**Energy substrate**
- [The Unconscious Grid](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md) — store-and-forward as the repressed solution to energy sovereignty
- [DC-Native Energy Packet Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md) — 48V SELV node architecture
- [Packetized Gravity Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/PGN.md) — hydraulic exergy
- [The Packet Transition: A Lateral Reading](https://github.com/JeanHuguesRobert/marenostrum/blob/main/packet_transition.md) — phronèsis, amathia, transition taxonomy
- [The Packet as Evolutionary Attractor](https://github.com/JeanHuguesRobert/marenostrum/blob/main/packet_attractor.md) — complexity-theoretic framing

**Compute substrate**
- [CXU Specification](https://github.com/JeanHuguesRobert/marenostrum/blob/main/CXU_SPEC.md) — Compute eXergy Unit pricing primitive
- [Inference Packet Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/inference_packet_network.md) (v2.0, 2026-05) — packet logic applied to inference continuity

**Cognition layer**
- [Agent-Resumable CLI](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md) — externalized judgment, continuations, provider-neutral resumption
- [The COP Manifesto](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Manifesto.md) — TCP/IP for intelligences
- [COP Architecture](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Architecture.md) — full protocol specification
- [Cogentia Commons Working Paper](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md) — methodology for distributed knowledge production

**Civic layer**
- [DHITL — Democratic Humans in the Loop](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md) — the axiom: AI may participate in epistemic production; living persons alone govern
- [Discours de la seconde méthode](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md) — methodology rules (publish process, objections as first-class, machine-readable structure, corpus as evidence)

---

## The methodology

The corpus follows the **second method**:

1. **Publish the process, not only the result.** Continuations make the process inspectable — where the system asked, what alternatives existed, who answered, how it resumed.
2. **Every objection is a first-class contribution.** Falsifiable claims, marked-unfalsifiable feelings of certainty, requests for specifics — all are typed, all are recorded, none are erased.
3. **Structure for machine readability from the start.** Stable identifiers, schemas, canonical URLs, append-only audit logs.
4. **Let the corpus be its own evidence.** The repositories demonstrate the method on themselves: cogentia.js scans for unanchored claims; continuations process those decisions; the audit trail is part of the proof.
5. **Encode the boundary in the architecture (Rule 0).** Epistemic participation vs political governance: AI agents may supply judgment, but binding decisions require signed human accountability.

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

## Contact

📧 jhr@baronsmariani.org
🌐 [FractaVolta on GitHub](https://github.com/JeanHuguesRobert/FractaVolta) · [research index](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md)

*All papers: CC BY-SA 4.0. All software: MIT.*
