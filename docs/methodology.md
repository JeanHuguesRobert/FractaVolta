---
title: Methodology
subtitle: How we work — every decision auditable, every objection first-class, every AI agent replaceable. Not compliance theater; the way the platform fundamentally operates.
canonical_url: https://fractavolta.com/methodology
last_stamped_at: 2026-05-26
---

FractaVolta conçoit, déploie et exploite des infrastructures locales en Corse et en Méditerranée. La méthode n’est pas une surcouche administrative : elle fait partie intégrante de la façon dont nous livrons les projets à nos partenaires.

Trois engagements concrets structurent chaque projet chez FractaVolta :

1. **Chaque affirmation est traçable.** Si nous avançons un résultat technique ou économique, il existe un document stable et versionné qui le justifie.

2. **Chaque objection compte.** Si vous n’êtes pas d’accord avec une hypothèse ou un choix, elle devient partie du dossier. Nous ne l’effaçons pas.

3. **Aucun outil IA n’est indispensable.** Tout ce qui est produit avec une IA peut être repris par une autre (ou par un humain) sans tout refaire.

La section ci-dessous présente les outils et concepts opérationnels en détail. Elle s’adresse principalement aux partenaires techniques et aux chercheurs qui souhaitent cette profondeur.

Si vous êtes un acteur de terrain ou un partenaire commercial, vous pouvez passer directement à la section [En Corse](./fr/), qui présente les applications concrètes.

## Cogentia Commons

[**Cogentia Commons**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md) est la méthode de gouvernance des connaissances à travers le corpus. Chaque document important porte une `canonical_url` stable. Le corpus est sa propre preuve : les forks, objections et évolutions restent visibles dans l’historique git.

## cogentia.js

[**`cogentia.js`**](https://github.com/JeanHuguesRobert/cogentia/blob/main/scripts/cogentia.js) est l’outil opérationnel (CLI Node.js sans dépendance). Il permet de piloter la gouvernance du corpus sur plusieurs dépôts.

Les principales familles de commandes :

- **Synchronisation et inspection** (`drift`, `lint`, `scan`, `check`)
- **Vues dérivées** (`refresh`, `documents`, `corpus-status`, `backlinks`, `trails`)
- **Gouvernance du frontmatter** (`frontmatter check`, `frontmatter promote`)

Ces outils rendent la traçabilité et la maintenance du corpus concrètes et automatisables.
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

## The Pipeline — packet-switching applied to method

FractaVolta's TL;DR is *packet-switching to energy, COP to cognition, liquid democracy to deliberation*. The same insight applies recursively to the cognitive infrastructure layer's own working method.

The [**Pipeline**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md) (method note v0.4, 2026-05-25) is the corpus's operational method, captured in one phrase:

> **Pipeline on the surface, packet network in depth.**

Intuitions become cognitive packets, packets become versioned source documents, source documents derive into audience-specific products (papers, blogposts, parliamentary notes, public dashboards), public feedback reintegrates into the corpus. Not a linear circuit — a packet-switched cognitive network.

The companion paper [**Derived Products**](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md) (v0.2) formalises the *source ↔ derived* split it implies: the substantive content belongs to a versioned source corpus; academic papers, public essays, social posts, video scripts, parliamentary notes are derived forms adapted to specific audiences/platforms/personas. Operating rule:

> *Do not popularize from the academic paper; derive from the corpus.*

This is the cognition-layer instance of the same packet/circuit diagnostic that drives the energy and civic layers. It is also the operational counterpart of the [Discours de la seconde méthode](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md). The method survives being applied to itself: `pipeline.md` is *a self-describing artefact of the method it describes*.

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

La méthode est proposée, pas imposée. Les structures qui cherchent du théâtre de conformité, des audits opaques ou de la cognition verrouillée par un fournisseur ne trouveront pas FractaVolta un partenaire adapté.

**Travaux en Corse** : la plupart de nos déploiements et pilotes concrets se font actuellement en Corse (seconde vie solaire, habitat DC-natif, nœuds locaux).

Pour les acteurs de terrain (agriculteurs, collectivités, installateurs), les pages les plus directement utiles sont :
- [Seconde Vie solaire](./fr/seconde-vie)
- [Marchés locaux](./fr/marches)
- [Partenaires installateurs](./fr/installateurs)

Ces pages sont écrites dans un registre plus opérationnel et ancré sur le territoire. Si vous êtes sur le terrain, commencez par là plutôt que par cette page.

---

**Vous souhaitez travailler avec nous ?**  
Contact : [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org) • [LinkedIn](https://www.linkedin.com/company/fractavolta/)
