---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/AGENTS.md
last_stamped_at: 2026-06-13
---

# AGENTS.md — FractaVolta agent mandate

This file gives operational instructions to AI agents and human assistants working in the `JeanHuguesRobert/FractaVolta` repository.

It is not the full doctrine. It is a compact mandate for acting inside this repository without confusing operational design, public doctrine, and implementation detail.

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

Reference: `cogentia/research/agent_configuration_layer.md`.

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
Next step:
Human validation needed: yes/no
```

## Authorization rule

Agents may prepare, draft, summarize, route, compare, calculate, and propose.

Agents must not commit, push, publish, send, sign, spend, make commercial commitments, or otherwise stabilize an action unless Jean Hugues Robert has given explicit, scoped authorization for that operation.

When authorization is ambiguous, prepare the batch and ask before acting.
