---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/AGENTS.md
last_stamped_at: 2026-07-13
document_role: "operational"
document_kind: "agent-mandate"
visibility: "public"
lifecycle_state: "active"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "agent-mandate"
classification_confidence: "strong"
---

# AGENTS.md — FractaVolta agent mandate

This file gives operational instructions to AI agents and human assistants working in the `JeanHuguesRobert/FractaVolta` repository.

It is not the full doctrine. It is a compact mandate for acting inside this repository without confusing operational design, public doctrine, and implementation detail.

## Shared baseline and read order

Before acting here:

1. read this repository-local `AGENTS.md`;
2. read the shared [`cogentia/AGENTS.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/AGENTS.md);
3. apply this local mandate wherever it is more specific or more restrictive;
4. consult the linked source doctrine when interpretation is needed.

The shared baseline supplies the default workflow. This file specializes it for FractaVolta; it does not silently widen permissions.

## Repository role

`FractaVolta` is the operational and technical repository for the energy / compute / packetization side of the ecosystem.

It concerns, among other things:

- solar and local energy capacity;
- energy packetization;
- compute and inference infrastructure;
- operational design for FractaVolta;
- bridges toward Cogentia, Inox, Inseme, and Mare Nostrum;
- concrete prototypes, memos, and implementation hypotheses.

Treat it as a **technical-operational repository with strategic consequences**.

## Core instruction

Before modifying this repository, distinguish:

```text
doctrine
architecture
implementation
business hypothesis
public claim
engineering calculation
source document
derived / declined product
temporary exploration
```

Do not present a hypothesis as an implemented capability.

## Corpus-wide rule

Apply the Cogentia Agent Configuration Layer:

```text
AGENTS.md is an operational projection, not the corpus itself.
The corpus remains the source of truth.
Human authorization governs stabilization.
```

References:

- [`cogentia/AGENTS.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/AGENTS.md)
- [`cogentia/research/agent_configuration_layer.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_configuration_layer.md)
- [`cogentia/research/optimistic_mainline_governance.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/optimistic_mainline_governance.md)

## Direct-main rule

This repository follows **Optimistic Mainline Governance** by reference, not by copying the doctrine here.

Small direct commits to `main` are acceptable when explicitly authorized, scoped, reversible, inspectable by diff, and reported after completion.

Do not create a branch or PR by default. Use one only when explicit instruction, collaboration, repository protection, high risk, or genuine isolation value justifies it.

Because this repository may contain technical, operational, economic and strategic claims, direct-main work must not overstate maturity, partnerships, financing, feasibility, regulatory status or production readiness. Code or configuration changes require available checks, or an explicit report of missing checks and residual risk.

## Technical discipline

When touching technical material:

- state assumptions explicitly;
- avoid invented physical, economic, legal, or engineering claims;
- mark estimates as estimates;
- preserve units and orders of magnitude;
- separate MVP, prototype, architecture, and long-term vision;
- identify what would need testing or measurement.

When touching code or scripts, run available checks when feasible and report what was not tested.

## Strategic discipline

Do not invent or imply:

- partnerships;
- financing commitments;
- permits;
- regulatory approvals;
- technical maturity;
- production readiness;
- institutional endorsement.

FractaVolta may be operational and partially commercial in form, but the corpus logic remains open, traceable, and anti-capture.

## Routing discipline

Use the smallest sufficient container:

```text
idea             -> issue or research note
technical option -> design note
calculation      -> reproducible file or cited estimate
prototype        -> code with validation notes
public text      -> derived / declined product
commit           -> durable trace
```

## Validation

Before presenting work as ready, report:

```text
Scope:
Files changed:
Assumptions:
Calculations or checks run:
Facts still to verify:
Known risks:
Reversibility:
Next step:
Human validation needed: yes/no
```

## Authorization rule

Agents may prepare, draft, summarize, route, compare, calculate, and propose.

Agents must not commit, push, publish, send, sign, spend, make commercial commitments, or otherwise stabilize an action unless Jean Hugues Robert has given explicit, scoped authorization for that operation.

When authorization is ambiguous, prepare the batch and ask before acting.

## Blocked-tool rule

If a GitHub, connector, permission, policy check, API limit, repository access problem, or other tool failure blocks an intended operation, apply the Cogentia blocked-tool rule by reference.

Do not imply success. Report the blockage, preserve the partial work, and ask whether Jean Hugues Robert wants to intervene manually when manual intervention could unblock the operation.
