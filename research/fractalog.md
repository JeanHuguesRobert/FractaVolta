---
title: "FractaLog — Fractal Append-Only Logs for Agents, Mandates, Custody, Inheritance and Delayed Transparency"
subtitle: "Distributed logs as memory, proof, custody and accountability substrate for FractaNet and COP"
description: "Source working paper defining FractaLog: a fractal append-only log architecture for packet-local and other accountable source traces, mandate acts, custody, restricted access, delayed transparency and anti-capture auditability."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
x-address: "1 cours Paoli, F-20250 Corte, Corsica, France"
x-email: "jhr@baronsmariani.org"
canonical_path: "FractaVolta/research/fractalog.md"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractalog.md"
version: "0.2-draft"
status: "working-paper — source document, human validation required"
date: "2026-07-06"
last_modified_at: "2026-08-16"
last_stamped_at: "2026-08-16"
license: "CC BY-SA 4.0"
language: "en"
type: "source-document"
source_or_derived: "source-document"
repository: "FractaVolta"
related_repositories:
  - "JeanHuguesRobert/FractaVolta"
  - "JeanHuguesRobert/inseme"
  - "JeanHuguesRobert/barons-Mariani"
  - "JeanHuguesRobert/cogentia"
related_documents:
  - "FractaVolta/research/fractanet.md"
  - "FractaVolta/research/traceable_governance.md"
  - "FractaVolta/research/generalized_packet_networks.md"
  - "FractaVolta/research/capability_regimes.md"
  - "inseme/packages/cop-core/Invariants.md"
  - "inseme/packages/cop-core/Architecture.md"
  - "inseme/research/cop_fractalog_profile.md"
  - "inseme/packages/cop-kernel/docs/packet-strict-accounting-cascade.md"
  - "barons-Mariani/research/traceabilite_des_actes.md"
  - "barons-Mariani/research/dao_imputabilite_dhitl.md"
tags:
  - fractalog
  - fractanet
  - cognitive-packets
  - packet-local-trace
  - append-only-log
  - distributed-logs
  - custody
  - mandate
  - accountability
  - delayed-transparency
  - auditability
  - anti-capture
human_validation_required: true
validation_points:
  - "Validate FractaLog as the canonical name for the fractal log substrate."
  - "Validate packet-local source traces for packet-borne accountable acts."
  - "Validate the distinction between source facts and higher-level FractaLog projections."
  - "Validate the distinction between privacy erasure and mandate-memory non-erasure."
  - "Validate the delayed-transparency model for classified or restricted traces."
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
---

# FractaLog

## Fractal Append-Only Logs for Agents, Mandates, Custody, Inheritance and Delayed Transparency

**Jean Hugues Noël Robert, baron Mariani**  
Institut Mariani / C.O.R.S.I.C.A. / FractaVolta

---

## 0. Corpus navigation

FractaLog belongs to the Fractanet source layer. Its COP projection is specified in `inseme/research/cop_fractalog_profile.md`.

The present revision aligns FractaLog with a more general Corpus invariant already used by strict packet accounting:

> **Put source facts where the accountable act occurs; federate and consolidate by projection.**

For packet-borne acts this means that the Cognitive Packet is the preferred source carrier for the trace facts produced by its processing. A content-addressed object directly referenced by the packet is equivalent when inline storage is inappropriate. Higher-level FractaLog structures must not become competing source ledgers.

---

## 1. Abstract

FractaLog is a proposed fractal trace and log substrate for FractaNet and COP.

Its core claim is that distributed agentic infrastructure cannot treat logs as mere technical by-products. In a mandate-bearing distributed system, trace is memory, proof, custody, succession, accountability and anti-capture infrastructure.

The v0.2 model distinguishes **source traces** from **FractaLog projections**. When an accountable act occurs while processing a Cognitive Packet, the packet carries or directly references the authoritative trace facts for that act. FractaLog then projects, orders, seals, indexes, federates and audits those facts without duplicating their authority into a second ledger.

Not every accountable act is packet-borne. Human, legal, custody or infrastructure acts may originate in another legitimate append-only source. The general invariant is therefore source-local rather than packet-exclusive.

---

## 2. Problem statement

Classical logging asks what happened operationally. FractaLog must additionally answer who acted, under which mandate, using which capacity, with which evidence, custody and future accountability.

A previous formulation risked creating two authorities: the Cognitive Packet that actually travelled and accumulated evidence, and a separate FractaLog object into which the same facts were copied. This is unnecessary and creates divergence risk.

The corrected architecture is:

```text
accountable act
    ↓
source-local trace facts
    ↓
packet-local when packet-borne
    ↓
FractaLog projection / federation
    ↓
mission / twin / institution / network views
```

The projection may be durable and append-only. It may also carry projection-specific facts such as anchoring, access, custody and release events. But it must preserve provenance back to the source facts and must not silently become their competing authority.

---

## 3. Historical and technical background

Logs precede computing: ship logbooks, ledgers, scientific notebooks and administrative registers all combine memory, sequence and accountability. Computer systems later added syslog, event sourcing, commit logs, distributed tracing, Merkle transparency structures and local-first replication.

FractaLog retains the useful properties of these traditions while applying a source-local rule suited to Cognitive Packet Switching Networks.

Distributed systems provide three especially important lessons:

1. there is no cheap, universally trustworthy global order;
2. causal provenance matters more than pretending to have one global present;
3. higher levels can verify lower levels through references, roots, proofs and attestations without absorbing all source content.

---

## 4. Source facts and projections

### 4.1 General invariant

```text
SourceTruth lives where the accountable act occurs.
HigherLevelState is a projection over source facts.
```

A projection can be authoritative about its own projection acts — for example sealing a segment or changing a visibility regime — without becoming the authority for the underlying act it references.

### 4.2 Packet-borne acts

For an act performed while processing a Cognitive Packet:

```text
PacketBorneAct => SourceTrace in Packet | directly content-addressed by Packet
```

Typical packet-local facts include, when applicable:

```text
packet identity and lineage
mandate / authority references
handler / actor identity
input and output artifact references
capacity/provider used
spending / resource consumption
step and continuation facts
evidence and tool-call references
causal parent references
result / failure state
source trace hashes or signatures
```

This mirrors strict packet accounting: one physical provider call has one owning packet; consolidated spend is a projection. Trace should obey the same non-duplication principle.

### 4.3 Non-packet acts

FractaLog is not packet-exclusive. A human signature, legal act, custody transfer, physical observation or infrastructure event may have a legitimate source outside a Cognitive Packet.

The rule remains:

```text
Put the fact at its accountable source.
Reference it causally.
Project it upward only as needed.
```

### 4.4 Projection role

A FractaLog projection may provide:

- local or scoped ordering;
- causal navigation;
- indexes and query views;
- Merkle roots and integrity proofs;
- custody and lifecycle views;
- privacy/redaction projections;
- restricted-access and delayed-transparency views;
- federation roots;
- mission, agent, institution or network-level audit views.

A projection must preserve enough provenance to identify the source fact or its lawful destruction trace.

---

## 5. Fractal model

FractaLog is a forest of projections over distributed sources, not one universal chain.

```text
source packets / source acts
        ↓
local trace projections
        ↓
agent / task / mission projections
        ↓
institution / federation projections
        ↓
roots / proofs / attestations
```

Higher levels should aggregate references and proofs whenever possible rather than copy private lower-level content.

A minimal projected entry may look like:

```json
{
  "schemaVersion": "fractalog.projection.entry.v0",
  "projectionId": "urn:fractalog:projection:...",
  "projectionSeq": 1842,
  "sourceRef": "urn:cop:packet:...#trace/...",
  "sourceHash": "sha256-...",
  "actorId": "urn:fractanet:agent:...",
  "eventType": "agent.step.completed",
  "parentSourceRefs": ["urn:cop:packet:...#trace/..."],
  "visibility": "open",
  "previousProjectionHash": "sha256-...",
  "projectionEntryHash": "sha256-..."
}
```

The `sourceRef` is essential: the projection does not erase the distinction between the act and the view over the act.

---

## 6. Lifecycle, ownership, custody and succession

FractaLog must not confuse authorship, subject, ownership and custody.

| Role | Meaning |
|---|---|
| `actor` | Entity that produced the accountable act. |
| `subject` | Entity primarily concerned by a projection. |
| `owner` | Ownership/control relation defined outside FractaLog. |
| `custodian` | Entity preserving source or projection material. |
| `controller` | Entity defining access, retention or release policies. |
| `successor` | Entity appointed to preserve or continue obligations. |
| `auditor` | Entity allowed to verify integrity or policy compliance. |

Ownership is a projection from accountable acts; it must not be a mutable convenience field. Custody is distinct from ownership. Agent death, suspension or replacement must not make accountable history unreachable.

Lifecycle states such as `active`, `sealed`, `transferred`, `archived`, `restricted` or `released` are projections from acts and events, not silent mutations of history.

---

## 7. Privacy, erasure and mandate memory

Private data may be minimized. Collateral personal data may be redacted. Mandate-bearing acts must remain causally visible, although their content may legitimately be restricted.

```text
The right to be forgotten protects private persons from undue exposure.
It must not become a right for mandate-holders to erase the trace of acts performed on behalf of others.
```

Redaction is itself an accountable act. A redacted view is a projection; it does not silently rewrite the source history.

---

## 8. Restricted traces and delayed transparency

Secrecy is an accessibility regime, not an existence regime.

```text
Secrecy may defer access.
It must not destroy memory.
```

A restricted trace should retain or reference authority, reason, perimeter, restriction date, review date, release condition, maximum duration, audit path and respondent. Extensions are new accountable acts and must be traced.

Even where public acknowledgement of existence must temporarily be withheld, an accountable escrowed source or proof must exist.

---

## 9. Destruction without darkness

Real systems may lawfully destroy some content. The invariant is narrower than universal retention:

```text
Destroying content may sometimes be legitimate.
Destroying the trace of destruction is not.
```

The destruction act should preserve who authorized it, under what rule, what class of material was affected, when it occurred, and what proof or audit path remains.

---

## 10. COP impact

FractaLog is a COP profile, not a replacement for COP.

COP already provides packets, immutable Events and Artifacts, causal lineage, durable state, continuations, replay and explicit schemas. COP/FractaLog adds governed trace semantics while avoiding a second source ledger.

The preferred relationship is:

```text
Cognitive Packet
  ├── work state
  ├── lineage
  ├── mandate
  ├── spending
  ├── evidence
  └── source trace facts / direct source references
             ↓
       FractaLog projector
             ↓
  scoped append-only projections
             ↓
  federation roots / audit views
```

A Mission or other higher-level object should therefore reference a FractaLog **projection/view** when useful, not imply that the referenced log is the unique source container for all underlying packet acts.

---

## 11. Invariants

1. **Source locality** — source facts belong where the accountable act occurs.
2. **Packet locality for packet-borne acts** — packet-borne source traces live in or are directly content-addressed by the Cognitive Packet.
3. **No competing source ledger** — higher FractaLog views are projections/federations, not duplicate authorities.
4. **Append-only commitment** — persisted accountable history is not silently rewritten; corrections are new acts.
5. **Explicit causality** — cross-source relationships are explicit.
6. **Custody distinct from ownership** — preservation does not imply ownership.
7. **Death without disappearance** — succession does not erase history.
8. **Mandate memory** — engaging acts under mandate remain causally accountable.
9. **Privacy without causal erasure** — content can be minimized without fabricating non-occurrence.
10. **Secret as delayed transparency** — restricted access does not abolish accountable memory.
11. **Prolongation as act** — extension of secrecy, retention or destruction authority is traced.
12. **Audit without content capture** — higher levels prefer roots, proofs and attestations over wholesale content absorption.

---

## 12. Minimal accountability chain

For mandate-bearing acts:

```text
mandate -> act -> respondent -> justification -> contestation path -> correction/revocation/sanction path
```

Two companion formulas:

```text
A trace without a respondent is only an archive.
A respondent without a trace is only a fiction.
```

---

## 13. Verification and regression obligations

The packet-local correction creates a concrete regression obligation.

A conformance fixture should demonstrate:

```text
1. packet P records source trace fact T
2. projector derives FractaLog view F(T)
3. replay reconstructs the same visible view under the same policy
4. deliberate divergence in F(T) is detectable from sourceRef/sourceHash or proof
5. correction creates a new projection act; it does not mutate T
6. restricted/redacted projection preserves causal existence according to policy
```

The propagation is not fully verified until such a fixture or equivalent implementation evidence exists.

---

## 14. References and prior-art anchors

- RFC 5424 — The Syslog Protocol.
- OpenTelemetry Logs Data Model.
- Leslie Lamport, *Time, Clocks, and the Ordering of Events in a Distributed System*.
- W3C PROV Data Model.
- Certificate Transparency v2, RFC 9162.
- Event sourcing and append-only commit-log architectures.
- Local-first software and verifiable data structures.
- `inseme/packages/cop-kernel/docs/packet-strict-accounting-cascade.md` — Corpus precedent for packet-local source facts and consolidated projections.

---

## 15. Continuation

1. Keep `inseme/research/cop_fractalog_profile.md` aligned with this source-local model.
2. Remove any Mission-level wording that implies `fractalogRef` points to a competing source ledger.
3. Implement the regression fixture defined above.
4. Only then mark propagation `PR-2026-001` as `verified`.
