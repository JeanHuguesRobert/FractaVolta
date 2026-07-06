---
title: "FractaLog — Fractal Append-Only Logs for Agents, Mandates, Custody, Inheritance and Delayed Transparency"
subtitle: "Distributed logs as memory, proof, custody and accountability substrate for FractaNet and COP"
description: "Source working paper defining FractaLog: a fractal append-only log architecture for agent-bound traces, mandate acts, ownership/custody transitions, inheritance, restricted access, delayed transparency and anti-capture auditability."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
x-address: "1 cours Paoli, F-20250 Corte, Corsica, France"
x-email: "jhr@baronsmariani.org"
canonical_path: "FractaVolta/research/fractalog.md"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractalog.md"
version: "0.1-draft"
status: "working-paper — source document, human validation required"
date: "2026-07-06"
last_modified_at: "2026-07-06"
last_stamped_at: "2026-07-06"
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
  - "barons-Mariani/research/traceabilite_des_actes.md"
  - "barons-Mariani/research/dao_imputabilite_dhitl.md"
tags:
  - fractalog
  - fractanet
  - append-only-log
  - distributed-logs
  - agent-logs
  - custody
  - ownership
  - inheritance
  - mandate
  - accountability
  - delayed-transparency
  - classified-traces
  - right-to-be-forgotten
  - cop
  - auditability
  - anti-capture
human_validation_required: true
validation_points:
  - "Validate FractaLog as the canonical name for the fractal log substrate."
  - "Validate the distinction between privacy erasure and mandate-memory non-erasure."
  - "Validate the delayed-transparency model for classified or restricted traces."
  - "Validate whether ownership semantics should remain outside FractaLog and be referenced through FractaNet ownership artifacts."
  - "Validate the event vocabulary before turning it into a COP conformance profile."
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
---

# FractaLog

## Fractal Append-Only Logs for Agents, Mandates, Custody, Inheritance and Delayed Transparency

**Jean Hugues Noël Robert, baron Mariani**  
Institut Mariani / C.O.R.S.I.C.A. / FractaVolta  
Working paper — 2026-07-06

---

## 0. Corpus navigation

FractaLog belongs to the Fractanet source layer.

It should be read after:

- [`FractaVolta/research/fractanet.md`](fractanet.md) — generalized control planes for heterogeneous packet networks;
- [`FractaVolta/research/traceable_governance.md`](traceable_governance.md) — fractal traceability and Merkle-root aggregation;
- [`FractaVolta/research/generalized_packet_networks.md`](generalized_packet_networks.md) — packet grammar across substrates;
- [`barons-Mariani/research/traceabilite_des_actes.md`](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/traceabilite_des_actes.md) — mandate, accountability and engaging acts;
- [`inseme/packages/cop-core/Invariants.md`](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Invariants.md) — COP non-negotiable invariants.

It should later be declined into:

- [`inseme/research/cop_fractalog_profile.md`](https://github.com/JeanHuguesRobert/inseme/blob/main/research/cop_fractalog_profile.md) — COP-side source profile;
- a future operational note in `inseme/packages/cop-core/` if the profile stabilizes.

---

## 1. Abstract

FractaLog is a proposed fractal log substrate for FractaNet and COP.

Its core claim is that distributed agentic infrastructure cannot treat logs as mere technical by-products. A log is not only a file, stream, queue, or observability artifact. In a mandate-bearing distributed system, a log is also memory, proof, custody, succession, accountability, and anti-capture infrastructure.

FractaLog defines a forest of local append-only logs, typically associated with agents, tasks, tools, mandates, or federations. Agents may spawn child agents. Child agents may have their own logs. Logs can be causally linked, sealed, transferred, inherited, audited, redacted, classified, declassified, or archived without rewriting the past.

The central rule is simple:

> A log may change phase, custodian, owner, visibility, or accessibility.  
> Its committed past must not be silently rewritten or made causally invisible.

This source document introduces the historical and technical background, the proposed FractaLog model, the distinction between ownership and custody, the lifecycle of agent-bound logs, the non-erasure of mandate traces, the model of restricted traces and delayed transparency, and the intended impact on COP.

---

## 2. Problem statement

Classical software logging is usually designed for debugging, operations, security monitoring, compliance, or post-incident forensics. These uses remain valid, but they are insufficient for FractaNet and COP.

In FractaNet, agents act under mandates, spawn sub-agents, route capacity, call tools, emit artifacts, delegate work, suspend continuations, and sometimes affect humans, institutions, property, public records, or shared infrastructure.

This raises questions that classical logs do not answer adequately:

1. Which agent is the subject of the log?
2. Which actor wrote each entry?
3. Under which mandate did the act occur?
4. Who owns the log?
5. Who merely keeps custody of it?
6. What happens when an agent dies, is suspended, or is replaced?
7. Who inherits the log, the duty to preserve it, or the right to access it?
8. Which parts may be redacted for privacy?
9. Which traces may be restricted for security?
10. When must a secret be reviewed, downgraded, or declassified?
11. How can higher levels audit lower levels without absorbing their private contents?
12. How can a system preserve accountability without becoming a surveillance system?

FractaLog addresses these questions by treating the log itself as a first-class governed object.

---

## 3. Historical background: logs before computers

Logs precede computing.

The ship logbook recorded navigation, wind, speed, position, incidents, decisions, and responsibility. Administrative registers recorded taxes, births, deaths, property, court acts, and public decisions. Merchants kept ledgers. Scientists kept laboratory notebooks. Monasteries, courts, parliaments, armies, hospitals and families all developed forms of durable records.

Across these traditions, a log is not merely memory. It is often:

- ordered memory;
- proof of sequence;
- protection against later denial;
- transmission device between operators;
- basis for accountability;
- institutional continuity mechanism.

The historical lesson is important: a log is a social technology before it is a computer technology.

FractaLog generalizes this old function for distributed agentic systems.

---

## 4. Computer science background

### 4.1 System logs

Syslog and later logging frameworks treat logs as streams of events emitted by processes, services, hosts and applications. They provide event messages, severity, timestamps, origins, structured data and transport conventions.

This is useful but not sufficient. System logs usually answer:

```text
what happened operationally?
```

FractaLog must also answer:

```text
who acted, under which mandate, with which custody, with which future accountability?
```

### 4.2 Observability logs, traces and metrics

Modern observability distinguishes logs, metrics and traces. Distributed tracing adds correlation identifiers, spans, parent-child relationships, and causal reconstruction of a request across services.

This is directly relevant: FractaLog needs correlation, causality, local ordering and cross-log references. But FractaLog is not only observability. It is also governance memory.

### 4.3 Event sourcing

Event sourcing treats state changes as immutable events. Current state is reconstructed by replaying the event log. Corrections are represented by new events rather than mutation of the past.

This aligns strongly with COP and FractaLog.

However, FractaLog adds questions usually outside event sourcing:

- log lifecycle;
- custody transfer;
- ownership projection;
- inheritance;
- restricted visibility;
- delayed transparency;
- mandate memory;
- proof without content disclosure.

### 4.4 Commit logs and streaming systems

Systems such as Kafka make the append-only commit log an infrastructure primitive. A distributed log may be partitioned, replicated, retained, consumed and replayed.

FractaLog borrows the append-only and replay intuition, but rejects the idea that the infrastructure log alone is enough. The log must carry governance semantics.

### 4.5 Version control systems

Git demonstrates another relevant form of log: commits are signed or hash-addressed changes, linked through parent references, forming a durable graph. The corpus already uses Git history as part of its own method: priority, review, objection, correction and provenance are visible in commits, issues and forks.

FractaLog applies the same pattern to agentic acts: the trace is not a secondary report; it is part of the deliverable.

---

## 5. Distributed systems background

### 5.1 No reliable global now

Distributed systems do not have a simple, universally trusted global present. Local clocks drift. Messages arrive late. Networks partition. A total order across all events is often costly, fragile, or conceptually false.

FractaLog should therefore avoid a single global log.

The correct structure is:

```text
many local logs
+ local total order
+ explicit causal references
+ optional cryptographic anchoring
+ higher-level root aggregation
```

### 5.2 Lamport clocks, vector clocks and causal order

Lamport clocks and vector clocks show how systems can reason about happened-before relationships without requiring absolute time. FractaLog should preserve this lesson: causal links matter more than wall-clock order.

### 5.3 Merkle logs and transparency systems

Certificate Transparency and related verifiable log systems show how append-only logs can be audited using Merkle trees, inclusion proofs, consistency proofs and signed tree heads.

FractaLog should use this pattern for integrity:

- local log entries are append-only;
- segments may be sealed;
- Merkle roots may be anchored upward;
- a federation may audit lower-level logs through roots and proofs without reading all content.

This matches the FractaVolta traceable governance pattern: higher levels should aggregate roots, not absorb all lower-level content.

### 5.4 Local-first and CRDT lessons

Local-first systems and CRDTs show that durable user-controlled state can be replicated, merged and preserved without a single cloud authority. FractaLog can use CRDT-like techniques for projections, indexes, labels, access-control views and derived metadata.

But the source log itself should remain append-only and causally explicit. Convergent projections are not a substitute for an accountable event history.

---

## 6. Core model

FractaLog is a forest, not a chain.

```text
FractaNet
└── root audit / federation logs
    ├── agent logs
    │   ├── child-agent logs
    │   ├── tool invocation logs
    │   └── task logs
    ├── custody logs
    ├── mandate logs
    └── restricted / classified trace logs
```

A log is a governed append-only sequence of entries with lifecycle metadata and causal links.

A minimal log object:

```json
{
  "schemaVersion": "fractalog.log.v0",
  "logId": "urn:fractalog:log:...",
  "rootLogId": "urn:fractalog:log:...",
  "parentLogId": "urn:fractalog:log:...",
  "subjectAgentId": "urn:fractanet:agent:...",
  "logKind": "agent|task|tool|audit|custody|mandate|restricted|federation",
  "lifecycleState": "active",
  "ownerRef": "urn:fractanet:ownership:...",
  "custodianRef": "urn:fractanet:agent-or-node:...",
  "visibilityPolicyRef": "urn:fractanet:policy:...",
  "retentionPolicyRef": "urn:fractanet:policy:...",
  "inheritancePolicyRef": "urn:fractanet:policy:...",
  "creationEventId": "urn:cop:event:...",
  "currentHeadHash": "sha256-...",
  "currentMerkleRoot": "sha256-...",
  "createdAt": "2026-07-06T00:00:00Z"
}
```

A minimal log entry:

```json
{
  "schemaVersion": "fractalog.entry.v0",
  "eventId": "urn:cop:event:...",
  "logId": "urn:fractalog:log:...",
  "logSeq": 1842,
  "topicId": "urn:cop:topic:...",
  "topicSeq": 91,
  "actorId": "urn:fractanet:agent:...",
  "subjectAgentId": "urn:fractanet:agent:...",
  "eventType": "agent.step.completed",
  "payloadRef": "urn:cop:artifact:...",
  "parentEventIds": ["urn:cop:event:..."],
  "wallTime": "2026-07-06T00:00:00Z",
  "observedAt": "2026-07-06T00:00:01Z",
  "previousEntryHash": "sha256-...",
  "entryHash": "sha256-...",
  "signature": "..."
}
```

---

## 7. Agents, child agents and log trees

A COP/FractaNet agent may spawn another agent. The child agent may act under a mandate derived from the parent agent, a human actor, an institution, or a policy.

A child agent should not disappear into the parent agent's opaque memory. It should have a log relation.

Typical events:

```text
agent.spawned
agent.mandated
agent.suspended
agent.resumed
agent.retired
agent.failed
agent.died
agent.replaced
agent.successor.appointed
fractalog.log.created
fractalog.log.bound_to_agent
fractalog.log.bound_to_parent_log
```

A child log should carry at least:

- parent agent reference;
- parent log reference;
- mandate reference;
- scope of delegated action;
- allowed tools;
- trace requirements;
- lifecycle policy;
- inheritance or successor policy.

The death, suspension or replacement of an agent does not delete the log. It only closes or transforms the agent's writing capacity.

---

## 8. Ownership, custody and inheritance

FractaLog must not confuse authorship, subject, ownership and custody.

| Role | Meaning |
|---|---|
| `actor` | Entity that produced the event. |
| `subjectAgent` | Agent primarily associated with the log. |
| `owner` | Entity holding a control, disposition or ownership relation defined outside FractaLog. |
| `custodian` | Entity physically or logically preserving the log. |
| `controller` | Entity defining access, retention or release policies. |
| `successor` | Entity appointed to continue or preserve a log after death, suspension or transfer. |
| `auditor` | Entity allowed to verify integrity or policy compliance. |
| `beneficiary` | Entity for whom the log is kept or whose interests the log protects. |

Ownership should probably remain a FractaNet-level concept. FractaLog should reference ownership artifacts, not define the whole theory of property.

Custody transfer example:

```json
{
  "schemaVersion": "fractalog.event.custody.v0",
  "eventType": "fractalog.custody.transferred",
  "logId": "urn:fractalog:log:...",
  "actorId": "urn:fractanet:agent-or-human:...",
  "previousCustodianRef": "urn:fractanet:agent-or-node:...",
  "newCustodianRef": "urn:fractanet:agent-or-node:...",
  "causeEventIds": [
    "urn:cop:event:agent.died",
    "urn:cop:event:succession.rule.applied"
  ],
  "mandateRef": "urn:fractanet:mandate:...",
  "humanAnchorRef": "urn:cop:artifact:human-decision:...",
  "effectiveAt": "2026-07-06T00:00:00Z",
  "signature": "..."
}
```

---

## 9. Lifecycle states

A log may move through phases:

```text
created
active
quiescent
sealed
retired
transferred
inherited
archived
tombstoned
redacted_view
restricted
classified
declassified
```

These states are projections from events. They are not mutable flags that silently override history.

Lifecycle events include:

```text
fractalog.log.created
fractalog.log.segment.opened
fractalog.log.segment.sealed
fractalog.log.root.anchored
fractalog.log.snapshot.created
fractalog.log.redacted_view.created
fractalog.log.access.granted
fractalog.log.access.revoked
fractalog.log.retention.policy.changed
fractalog.log.custody.transferred
fractalog.log.ownership.claimed
fractalog.log.ownership.contested
fractalog.log.ownership.resolved
fractalog.log.inheritance.rule.declared
fractalog.log.inherited
fractalog.log.archived
fractalog.log.tombstoned
```

---

## 10. Right to be forgotten vs mandate memory

FractaLog distinguishes privacy protection from erasure of mandate-bearing acts.

The right to be forgotten may be legitimate when it protects a private person from undue, disproportionate or permanent exposure. It should be implemented through data minimization, redacted views, access limitation, pseudonymization of collateral third parties, and separation between content and trace.

But this logic must not be extended without limit to acts performed under mandate.

A mandate-holder acts on behalf of others. Delegated capacity creates a duty of memory. An engaging act performed under mandate must remain traceable, attributable, contestable, correctable and, where necessary, sanctionable.

Principle:

```text
The right to be forgotten protects private persons from undue exposure.
It must not become a right for mandate-holders to erase the trace of acts performed on behalf of others.
```

Operational rule:

```text
Private data may be minimized.
Collateral personal data may be redacted.
Mandate traces must remain causally visible.
```

Therefore, FractaLog may support:

```text
fractalog.erasure.requested
fractalog.erasure.granted_private_data
fractalog.erasure.rejected_mandate_trace
fractalog.redaction.applied
fractalog.context.added
fractalog.correction.added
fractalog.public_interest_retention.asserted
fractalog.mandate_trace.sealed
```

A rejection of erasure must itself be reasoned and traced. Otherwise anti-erasure becomes arbitrary power.

---

## 11. Classified traces and delayed transparency

FractaLog also distinguishes transparency from immediate publicity.

Some information may legitimately be withheld temporarily: defence, safety, source protection, ongoing investigations, critical infrastructure vulnerabilities, personal safety, or other narrowly defined public-interest reasons.

But secrecy is an accessibility regime, not an existence regime.

Principle:

```text
Secrecy may defer access.
It must not destroy memory.
```

A classified or restricted trace must still have:

- an authority;
- a reason;
- a level;
- a perimeter;
- a classification date;
- a review date;
- a declassification date or event;
- a maximum duration or renewal rule;
- an audit path;
- a respondent;
- an event trail for each extension.

A classification without review becomes a capture surface. A permanent secret without periodic justification becomes institutional darkness.

Minimal classification event:

```json
{
  "schemaVersion": "fractalog.classification.v0",
  "eventType": "fractalog.classification.applied",
  "targetEventId": "urn:cop:event:...",
  "targetArtifactId": "urn:cop:artifact:...",
  "classificationLevel": "restricted|confidential|secret|very_secret",
  "classificationAuthority": "urn:fractanet:agent-or-human:...",
  "legalOrPolicyBasis": "national_security|privacy|ongoing_investigation|source_protection|critical_infrastructure",
  "reasonSummary": "Operational details would expose active protection mechanisms.",
  "classifiedFields": [
    "payload.operationalDetails",
    "payload.sourceIdentity"
  ],
  "publicEnvelopeAllowed": true,
  "existenceMayBeAcknowledged": true,
  "classifiedAt": "2026-07-06T00:00:00Z",
  "reviewDueAt": "2027-07-06T00:00:00Z",
  "declassifyAt": "2036-07-06T00:00:00Z",
  "maxClassificationUntil": "2051-07-06T00:00:00Z",
  "extensionRequires": {
    "humanDecision": true,
    "independentAudit": true,
    "reasonedAct": true
  },
  "appealOrAuditPath": "urn:fractalog:procedure:classification-review",
  "signature": "..."
}
```

Classification events may themselves be restricted, but they must exist.

---

## 12. Restricted trace levels

FractaLog should support several visibility layers:

| Level | Meaning | Public access |
|---|---|---|
| `open` | Public content. | Immediate. |
| `redacted` | Content partly masked. | Immediate, with omissions. |
| `restricted` | Access limited to authorized actors. | Delayed or conditional. |
| `sealed` | Existence and integrity may be attestable, content closed. | Delayed or summary release. |
| `opaque_but_escrowed` | Even existence may be temporarily protected, but under escrow and audit. | Exceptional and time-bounded. |

The last level should be exceptional. It may be justified only when acknowledging existence would itself endanger a person, operation or critical system.

Even then, non-existence must not be real. Only public confirmability is delayed.

---

## 13. Review deadlines and audit triggers

Secrecy must not self-extend by inertia.

COP/FractaLog should emit or derive review obligations:

```text
classification.applied
  -> schedule review task
  -> if no review event before reviewDueAt
  -> emit classification.review_overdue
  -> escalate to authorized auditor
```

Useful events:

```text
fractalog.classification.requested
fractalog.classification.applied
fractalog.classification.denied
fractalog.classification.downgraded
fractalog.classification.upgraded
fractalog.classification.review_scheduled
fractalog.classification.review_due
fractalog.classification.review_overdue
fractalog.classification.review_performed
fractalog.classification.extended
fractalog.classification.extension_denied
fractalog.classification.declassified
fractalog.classification.partially_declassified
fractalog.classification.redacted_release_created
fractalog.classification.audit_requested
fractalog.classification.audit_completed
fractalog.classification.abuse_suspected
fractalog.classification.abuse_confirmed
fractalog.classification.public_interest_override_requested
fractalog.classification.public_interest_override_granted
fractalog.classification.public_interest_override_denied
```

A prolongation is a new act. It must be reasoned and traced.

---

## 14. Destruction without darkness

FractaLog should not claim that no content can ever be destroyed. Real systems may have lawful retention limits, source-protection rules, safety procedures, or minimization duties.

The correct rule is narrower and stronger:

```text
Destroying content may sometimes be legitimate.
Destroying the trace of destruction is not.
```

A destruction event should preserve:

- who authorized destruction;
- under what rule;
- what class of content was destroyed;
- when;
- which proof remains;
- which audit path applies;
- whether a minimal hash, root, sealed reference or destruction certificate remains.

Events:

```text
fractalog.content.destruction_requested
fractalog.content.destruction_authorized
fractalog.content.destruction_performed
fractalog.content.destruction_denied
fractalog.content.destruction_audited
```

---

## 15. COP impact

FractaLog should become a COP profile, not a replacement for COP.

COP already has the right foundations:

- immutable Events and Artifacts;
- topic-local ordering;
- idempotent processing;
- durability through event logs and artifacts;
- stateless agents;
- coordination through Events and Artifacts;
- deterministic replay of traces;
- explicit schema versioning;
- transparency over convenience.

FractaLog adds profile-specific semantics:

- log lifecycle events;
- agent-bound logs;
- child-agent logs;
- custody transitions;
- ownership references;
- inheritance events;
- redacted views;
- restricted traces;
- classification/declassification events;
- review deadlines;
- non-erasure of mandate traces.

Suggested profile name:

```text
COP/FractaLog
```

Suggested implementation source document:

```text
inseme/research/cop_fractalog_profile.md
```

---

## 16. Invariants

### 16.1 Append-only commitment

A persisted FractaLog entry must not be silently modified or deleted. Corrections are new entries.

### 16.2 Local order, explicit causality

Each log has a strict local order. Cross-log causality must be explicit.

### 16.3 Ownership as projection

The owner of a log is not a mutable field of convenience. It is a projection from ownership, mandate, transfer, dispute and resolution events.

### 16.4 Custody distinct from ownership

The custodian may preserve the log without owning it. The owner may control disposition without physically storing it.

### 16.5 Death without disappearance

Agent death, suspension, replacement or retirement must not cause log disappearance. It triggers lifecycle and succession events.

### 16.6 Mandate memory

An engaging act performed under mandate must not be erased as if it had never existed.

### 16.7 Privacy without causal erasure

Privacy protection should minimize, redact or restrict content without destroying the minimal accountability chain.

### 16.8 Secret as delayed transparency

Classification restricts access. It does not abolish memory.

### 16.9 Prolongation as act

Secret extension, retention extension, destruction authorization and declassification are engaging acts and must be traced.

### 16.10 Audit without content capture

Higher levels should verify lower-level integrity through roots, proofs and attestations whenever possible, not by absorbing all private content.

---

## 17. Minimal accountability chain

For mandate-bearing acts, the minimum chain is:

```text
mandate -> act -> respondent -> justification -> contestation path -> correction/revocation/sanction path
```

Two companion formulas:

```text
A trace without a respondent is only an archive.
A respondent without a trace is only a fiction.
```

---

## 18. Open questions

1. Should every COP Topic have a corresponding FractaLog, or should FractaLog only apply above a threshold of significance?
2. Should a child agent always receive a distinct log, or may its acts be logged only inside the parent log for low-stakes tasks?
3. What is the minimal log lifecycle state machine?
4. How should FractaLog reference FractaNet ownership objects without defining ownership itself?
5. What is the threshold between private data erasure and mandate-trace preservation?
6. What is the maximum acceptable duration for restricted traces in civic systems?
7. What constitutes an abusive extension of secrecy?
8. How should Merkle-root anchoring work across federated logs with different confidentiality levels?
9. Which parts belong in COP/Core, which parts belong only in `COP/FractaLog`, and which parts remain application policy?
10. What conformance tests should prove that a FractaLog implementation does not permit silent causal erasure?

---

## 19. References and prior art anchors

This draft is a synthesis. The following references are anchors, not exhaustive bibliography:

- RFC 5424 — The Syslog Protocol: https://www.rfc-editor.org/rfc/rfc5424
- OpenTelemetry Logs Data Model: https://opentelemetry.io/docs/specs/otel/logs/data-model/
- Martin Fowler, Event Sourcing: https://martinfowler.com/eaaDev/EventSourcing.html
- Apache Kafka documentation / distributed commit log model: https://kafka.apache.org/documentation/
- Leslie Lamport, Time, Clocks, and the Ordering of Events in a Distributed System.
- W3C PROV Data Model: https://www.w3.org/TR/prov-dm/
- OpenLineage object model: https://openlineage.io/docs/spec/object-model/
- Certificate Transparency v2, RFC 9162: https://www.rfc-editor.org/rfc/rfc9162.html
- Trillian / verifiable data structures: https://transparency.dev/verifiable-data-structures/
- Local-first software principles: https://www.inkandswitch.com/local-first/
- GDPR Article 17, right to erasure and exceptions: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679
- French Conseil d'État, access to secret-defence archives after legal non-communication periods: https://www.conseil-etat.fr/actualites/l-acces-aux-archives-secret-defense-doit-etre-possible-sans-procedure-prealable-une-fois-expires-les-delais-legaux-de-non-communication
- U.S. Executive Order 13526, Classified National Security Information: https://www.archives.gov/isoo/policy-documents/cnsi-eo.html

---

## 20. Continuation

Next useful actions:

1. Validate the name `FractaLog`.
2. Validate the split between FractaLog theory and COP profile.
3. Add this document to the FractaVolta research index.
4. Add a backlink from `fractanet.md` once the concept is stable enough.
5. Consolidate the COP-specific profile in `inseme/research/cop_fractalog_profile.md`.
6. Later extract a shorter public article on: "Secrecy may defer access; it must not destroy memory."
