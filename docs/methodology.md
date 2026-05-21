---
title: Methodology
subtitle: How we work — every decision auditable, every objection first-class, every AI agent replaceable. Not compliance theater; the way the platform fundamentally operates.
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/methodology.md
last_stamped_at: 2026-05-15
---

FractaVolta is an engineering firm and a stack operator. We design, build, and run infrastructure across four layers — energy, compute, cognition, civic. The methodology described on this page is not separate from the engineering. It is how the engineering is done.

Three concrete commitments shape every project:

1. **Every claim is anchored.** When we say "the LFP container delivers 1.9 MWh of useful work" or "the inference packet executes in under 30 seconds on a 50W node," there is a canonical document with a stable URL where that claim lives. We don't sell brochures of unsupported numbers.
2. **Every objection becomes a first-class contribution.** If you disagree with a claim — file an issue. We will either convert it into a falsifiable claim, mark it as a feeling-of-certainty (with attribution), or request the specifics that would settle it. Disagreement is part of the record, not noise to be erased.
3. **Every AI agent is replaceable.** When we use Claude, ChatGPT, a local model, or a human reviewer for any decision in the deployment, the work is captured as a typed [continuation](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md). A different agent — or a different human — can pick up the same work from the same point, without modifying our tooling. No vendor can lock us in. No vendor can lock you in.

These three commitments are operationalized through a small set of named instruments.

## Cogentia Commons

[**Cogentia Commons**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md) is the methodology for distributed knowledge production across the corpus. It is GitHub-anchored — every research-grade document carries a `canonical_url` in its front-matter pointing at its authoritative location on github.com. The corpus is its own evidence: forks, objections, and revisions are all visible in the git history.

## cogentia.js

[**`cogentia.js`**](https://github.com/JeanHuguesRobert/cogentia/blob/main/scripts/cogentia.js) is the operational CLI. Zero-dependency Node.js. Multi-repository registry. Commands are organised by concern:

**Sync & inspection.**

- `drift` — fetch and report ahead/behind/diverged vs upstream across all repos; `--pull` fast-forwards behind repos; `--strict` exits non-zero on drift.
- `lint` — single-table corpus health report: unreferenced, frontmatter issues, drift, in one pass.
- `scan` — flag markdown files not referenced in `research/index.md` (rule 4: every claim must be anchored).
- `check` — validate internal and external links across the corpus.

**Derived views (one command refreshes all).**

- `refresh` — runs `corpus-status`, `backlinks`, `trails`, and `documents` in canonical order.
- `documents` — consolidated cross-corpus catalogue with reverse-chronological activity and chronological authorship; bulk-pass commits filtered out.
- `corpus-status` — per-repository status page; structural sections auto-regenerated, curated sections preserved.
- `backlinks` / `trails` — auto-inject "Mentioned in" lists and Previous/Next playlist navigation; cross-repo links use absolute GitHub URLs so they render on the web.

**Frontmatter governance.**

- `frontmatter check [repo]` — diagnose docs missing Level 2 fields, using deprecated names, or carrying a `status:` value outside the controlled vocabulary.
- `frontmatter promote <file>` — add a Level 2 skeleton (title, author, affiliation, date, license, status).
- `frontmatter promote --batch` — bulk-inject the three invariants (author, affiliation, license) across substantive docs; leaves judgment fields for human edit.
- `frontmatter schema` — canonical schema reference.

**Personal scheduler (fractal).**

- `todo` — list, add, done, defer, drop. Each `.cogentia/SCHEDULE.md` is sovereign at its scope; `--global` aggregates across the workspace.
- `next [--pick]` — apply scheduler policy (priority → overdue → FIFO) and surface the next item; `--pick` marks it Active and audits.

**Authoring.**

- `stamp` — insert `canonical_url` + `last_stamped_at` into a document's front-matter, anchored to its GitHub commit URL.
- `continuation` — emit / inspect / resume / fail / abort / queue typed continuation requests. See below.
- `concepts` — typed concept registry: init, list, check (orphan validation), graph, ref, schema.

Every state-changing call appends one JSONL line to `.cogentia/audit.jsonl`. The audit log is a first-class deliverable, not a compliance afterthought.

## The continuation protocol

`cogentia.continuation.v1`, defined in the paper [Agent-Resumable CLI](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md) and implemented in `cogentia.js` as of v0.5.0, is the typed protocol for suspended judgment.

When the CLI reaches a point where deterministic computation is insufficient, it does not call an AI API. It emits a continuation: a JSON object carrying the context, the alternatives, the expected result schema, and the resumption metadata. The surrounding system — a human reviewer, an AI agent, a script, a CI pipeline — supplies a structured `step_result`. The tool validates the response and resumes.

The soundness test is binding:

> Can the current AI agent be replaced by another agent or by a human, without modifying `cogentia.js`?
> If yes, the protocol is sound. If no, it is contaminated.

Every resumption produces a [Heraclitean follow-up](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md#heraclitean-followup) — a dormant successor that keeps the chain non-terminal. History never 100% ends; the only constant is change.

## Cognitive Packets

[**Cognitive Packets**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md) (v0.3) generalise the continuation protocol beyond the CLI. A cognitive packet is composed of two layers:

- an **envelope** carrying kind-agnostic metadata (protocol header, provenance, context reference, transmission mode, routing, traces) that any agent — human or machine — can read without interpreting the inner work;
- a **payload** carrying kind-specific cognitive content (continuation, objection, hypothesis, decision, failure, or routing), validated by an agent that understands the declared kind.

A routing agent (workflow engine, human dispatcher, queue manager) can validate, queue, archive, or acknowledge a packet by reading the envelope alone. Only an agent capable of handling the declared kind needs to interpret the payload. New kinds may be added without modifying the envelope.

The `cogentia.continuation.v1` object **is** the canonical payload of a packet whose `packet_kind = continuation` — no semantic change to the CLI primitive, only a clearer transport story when the work needs to leave the CLI runtime (copied into a GitHub issue, attached to a document, pasted into a different AI conversation, resumed by a different agent).

## The Second Method

The methodological foundation of the entire corpus is the [Discours de la seconde méthode](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md). Five rules:

- **Rule 0 — Encode the boundary in the architecture.** AI agents may participate in epistemic production (drafting, summarizing, mediating). Political governance — binding decisions — belongs to living humans alone.
- **Rule 1 — Publish the process, not only the result.** The audit log, the continuation log, the git history are part of the deliverable.
- **Rule 2 — Make every objection a first-class contribution.** Falsifiable claims, marked feelings-of-certainty, requests for specifics — all are typed, all are recorded.
- **Rule 3 — Structure for machine readability from the start.** Stable identifiers, schemas, canonical URLs, append-only audit logs.
- **Rule 4 — Let the corpus be its own evidence.** The repositories demonstrate the method on themselves.

## What this means in practice

**If you are a partner.** You don't have to take our word for what we delivered. The audit trail of the deployment is part of what you receive. If we ever can't be found, the next operator can pick up exactly where we left off — every decision recorded, every alternative considered, every objection filed.

**If you are a deployer.** Your installation produces its own typed audit trail. You can run `cogentia.js scan` against your site's documentation to verify it matches the canonical specification. Drift becomes visible.

**If you are a researcher.** The corpus is open. Fork it. Contest a claim by filing an issue — it will be converted into a falsifiable form, marked as unfalsifiable with attribution, or escalated for more context. Your objection becomes part of the public record. Methods: see the [for-researchers page](./for-researchers).

**If you are a citizen using a deployed Inseme instance.** The AI mediator Ophélia is bound by the same protocol. Her contributions are typed events; her reasoning is replayable; she is replaceable. The deliberation belongs to the assembly — not to a vendor, not to her.

## How to engage

- File issues at any of the corpus repositories listed in the [ecosystem](#) footer. They are read.
- Install `cogentia.js` locally — it's MIT-licensed, zero-dependency Node.js. The [README](https://github.com/JeanHuguesRobert/cogentia#readme) is the entry point.
- Read the [Cogentia Commons Working Paper](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md) for the methodology's formal specification.
- Read [Agent-Resumable CLI](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md) for the continuation protocol's design rationale.

The methodology is offered. It is not imposed. Operations that want compliance theater, opaque audit chains, or vendor-locked cognition will not find FractaVolta a useful partner.
