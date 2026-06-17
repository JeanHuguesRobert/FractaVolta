---
title: Methodology
subtitle: How we work — every decision auditable, every objection first-class, every AI agent replaceable. Not compliance theater; the way the platform fundamentally operates.
lang: en
canonical_url: https://fractavolta.com/methodology
last_stamped_at: 2026-06-17
date: "2026-06-17"
status: "active — English methodology entry point"
---

FractaVolta designs, deploys, and operates local infrastructure across energy, compute, cognition, and civic continuity. The method is not an administrative layer added afterwards. It is part of how projects are delivered.

Three operational commitments structure each serious engagement:

1. **Every claim is traceable.** If we make a technical, economic, or architectural claim, it should be anchored in a stable, versioned document.
2. **Every objection counts.** Disagreement is not treated as noise. It becomes part of the record.
3. **No AI tool is indispensable.** Anything produced with AI assistance must be resumable by another AI agent or by a human without rebuilding the process.

This page presents the operational method and its tooling. For the research map, see [For researchers](./for-researchers). For concrete deployments, see [For deployers](./for-deployers). For local Corsica-based field projects, the French operational entry point is [FractaVolta en Corse](./fr/).

## Cogentia Commons

[**Cogentia Commons**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md) is the knowledge governance method used across the corpus.

Every important document should have a stable `canonical_url`. The corpus is its own evidence: forks, objections, revisions, and changes remain visible in git history.

## cogentia.js

[**`cogentia.js`**](https://github.com/JeanHuguesRobert/cogentia/blob/main/scripts/cogentia.js) is the operational CLI used to maintain the corpus across repositories.

Core command families include:

- **Corpus planning and verification** — `corpus plan`, `corpus apply`, `corpus verify`, `corpus privacy`.
- **Document navigation** — `docs summary`, `docs query`, `docs search`, `docs gaps`, `docs inspect`, `docs trails`.
- **Concept governance** — `concepts list`, `concepts check`.
- **Continuations and issue packets** — `continuation list`, `continuation inspect`, `continuation resolve`, `issues list`, `issues packet`.
- **Git and consolidation checks** — `git verify`, `git classify`, `consolidate`.

The current v2 surface is deliberately conservative: deterministic commands refresh generated views, while judgment-bearing work is externalized as continuations or GitHub issue packets. No issue command closes, labels, or comments on GitHub.

## The continuation protocol

`cogentia.continuation.v1`, defined in [Agent-Resumable CLI](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md), is the typed protocol for suspended judgment.

When deterministic computation is insufficient, the tool does not need to call a specific AI API. It emits a continuation: a JSON object carrying context, alternatives, expected result schema, and resumption metadata. A human reviewer, AI agent, script, or CI pipeline supplies a structured `step_result`. The tool validates the response and resumes.

The soundness test is binding:

> Can the current AI agent be replaced by another agent or by a human without modifying `cogentia.js`?
> If yes, the protocol is sound. If no, it is contaminated.

Every resumption produces a [Heraclitean follow-up](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md#heraclitean-followup): a dormant successor that keeps the chain non-terminal.

## Cognitive packets

[**Cognitive Packets**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md) generalise the continuation protocol beyond the CLI.

A cognitive packet has two layers:

- an **envelope** carrying kind-agnostic metadata: protocol header, provenance, context reference, transmission mode, routing, traces;
- a **payload** carrying kind-specific cognitive content: continuation, objection, hypothesis, decision, failure, or routing.

A routing agent can validate, queue, archive, or acknowledge a packet by reading the envelope alone. Only an agent capable of handling the declared kind needs to interpret the payload.

The `cogentia.continuation.v1` object is the canonical payload of a packet whose `packet_kind = continuation`.

## The Pipeline — packet switching applied to method

FractaVolta's TL;DR is: *packet switching to energy, COP to cognition, liquid democracy to deliberation*.

The same insight applies recursively to the cognitive infrastructure layer's own working method.

The [**Pipeline**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md) is the corpus's operational method, captured in one phrase:

> **Pipeline on the surface, packet network in depth.**

Intuitions become cognitive packets. Packets become versioned source documents. Source documents derive into audience-specific products: papers, blogposts, parliamentary notes, public dashboards. Public feedback reintegrates into the corpus.

This is not a linear circuit. It is a packet-switched cognitive network.

The companion paper [**Derived Products**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md) formalises the source ↔ derived split: substantive content belongs to a versioned source corpus; academic papers, public essays, social posts, video scripts, and institutional notes are derived forms adapted to specific audiences, platforms, and personas.

Operating rule:

> Do not popularize from the academic paper; derive from the corpus.

## The Second Method

The methodological foundation of the entire corpus is the [Discours de la seconde méthode](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md).

Five rules:

- **Rule 0 — Encode the boundary in the architecture.** AI agents may participate in epistemic production. Political governance — binding decisions — belongs to living humans alone.
- **Rule 1 — Publish the process, not only the result.** The audit log, continuation log, and git history are part of the deliverable.
- **Rule 2 — Make every objection a first-class contribution.** Falsifiable claims, marked feelings of certainty, and requests for specifics are all typed and recorded.
- **Rule 3 — Structure for machine readability from the start.** Stable identifiers, schemas, canonical URLs, and append-only audit logs.
- **Rule 4 — Let the corpus be its own evidence.** The repositories demonstrate the method on themselves.

## What this means in practice

**If you are a partner.** You do not have to take our word for what we delivered. The audit trail of the deployment is part of what you receive. If we ever cannot be found, the next operator can pick up where we left off.

**If you are a deployer.** Your installation produces its own typed audit trail. You can run corpus checks against site documentation. Drift becomes visible.

**If you are a researcher.** The corpus is open. Fork it. Contest a claim by filing an issue. Your objection becomes part of the public record. See [For researchers](./for-researchers).

**If you are a citizen using a deployed Inseme instance.** The AI mediator Ophélia is bound by the same distinction: her contributions are typed events; the deliberation belongs to the assembly, not to a vendor or to the mediator.

## How to engage

- File issues in the relevant corpus repository.
- Install `cogentia.js`; it is MIT-licensed and designed for local inspection.
- Read the [Cogentia Commons Working Paper](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md) for the formal methodology.
- Read [Agent-Resumable CLI](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md) for the continuation protocol.
- For local Corsica-based field pages, start from [FractaVolta en Corse](./fr/).

The method is proposed, not imposed. Structures seeking compliance theatre, opaque audits, or cognition locked into a single vendor will not find FractaVolta a suitable partner.

Contact: [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org) · [LinkedIn — FractaVolta](https://www.linkedin.com/company/fractavolta/)
