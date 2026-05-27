---
title: For citizens
subtitle: Free, open-source, neutral digital infrastructure for citizen participation, augmented deliberation, and democratic transparency. Built around Corte, Corsica — usable anywhere.
description: "Inseme et Kudocracy : outils open source (MIT) de démocratie liquide, consultation citoyenne et délibération augmentée. Multi-instances, souverains, sans vendor lock-in. Origine : Corte, Corse."
canonical_url: https://fractavolta.com/for-citizens
last_stamped_at: 2026-05-15
---

## Une couche civique souveraine

**inseme** est la plateforme open source (MIT) que FractaVolta peut déployer sur ses infrastructures locales. Elle est née du mouvement citoyen **#PERTITELLU** à Corte et a pour but de donner aux communautés des outils de délibération et de consultation libres, neutres et sans dépendance à un éditeur.

inseme propose :

- Des outils **libres** (licence MIT)
- Une plateforme **neutre** (aucun soutien à un parti ou candidat)
- Une architecture **multi-instances** (chaque commune ou communauté peut avoir la sienne)
- Un système **modulaire** (briques) que l’on peut assembler et faire évoluer
- Une conception **souveraine** (compatible avec des modèles locaux et du matériel FractaVolta)

---

## The applications

### 🗳️ Inseme Agora

The direct and liquid democracy tool. Designed for physical or remote assemblies. Instant voting. Digital gestures. AI-mediated by Ophélia (without imposing).

- Submit proposals
- Vote on motions
- Delegate your voice to a trusted person on a specific topic (liquid democracy / **Kudocracy**)
- Participate from a physical assembly hall or remotely
- Audit the full record afterwards — every gesture is an event, every event is replayable

### 📊 Kudocracy.Survey

The consultation and engagement platform. Multi-instance — every commune, university, or association runs its own.

- Citizen consultations
- Collaborative wiki
- Citizen gazette
- Social café (informal exchange)
- Deployed per-commune (Corte, Bastia, Università di Corsica, etc.)

### 🤖 Ophélia — the AI mediator

Ophélia is the platform's AI. She:

- Answers questions
- Helps formulate ideas clearly
- Guides users through processes
- Facilitates consensus during debates

She does **not**:

- Decide for anyone
- Impose a position
- Run on a vendor's servers if your instance prefers local inference (she can run on solar-backed sovereign edge nodes — the FractaVolta stack closes here)

### ☕ Cyrnea

Social and gamified experience for community spaces (bars, cafés). Citizen gazette integration. Local AI assistant. Lightweight PWA for clients of the establishment.

### 🌿 Atlas of Biodiversity

GIS layer for biodiversity observation and citizen science.

- Interactive mapping with IGN integration
- Submit and validate wildlife observations
- Real-time filtering by species, date, location
- GBIF/INPN data integration
- Open data — GeoJSON API for external integrations
- Specialized layers for biodiversity, with citizen contribution tools

---

## Why this matters for citizens

Software for democratic participation has historically been built on three weak foundations:

1. **Vendor-locked SaaS** — the platform owner can change terms, pull the plug, or hand over data on demand. Your deliberation is rented, not owned.
2. **Opaque AI mediation** — when an AI summarizes a consultation, you cannot inspect how. The reasoning is hidden inside a service contract.
3. **Centralised hosting** — when the central server goes down or gets compromised, every community using the platform goes down too.

inseme inverts all three:

1. **You own your instance.** MIT license, your hardware, your Supabase, your domain.
2. **The AI is auditable.** Ophélia's reasoning is captured as typed events; her contributions are part of the public record; she is replaceable by any other compliant AI or by a human moderator without modifying the platform. Technically: she is bound by the same [continuation protocol](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md) FractaVolta uses across the rest of the stack. See the [methodology page](./methodology) for the formal account of what that means and how to verify it.
3. **Federation, not centralisation.** Every commune runs its own. Topics can be shared across instances when participants want to; otherwise they stay local.

---

## How to use it

**As a citizen using an existing instance:**
- Visit the instance for your commune or community (e.g. `agora.<your-commune>.fr` or similar — your local operator can tell you).
- Participate in consultations, votes, deliberations.
- Read the audit trail — every decision is replayable.

**As a community looking to deploy:**
- Clone the [inseme repository](https://github.com/JeanHuguesRobert/inseme)
- See the multi-instance documentation: [MULTI_INSTANCE](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-host/docs/MULTI_INSTANCE.md)
- For full-stack (DC-native edge node, sovereign inference, off-grid capable): see the [for-deployers page](./for-deployers).

**As a developer:**
- Briques are how you extend inseme — see [BRIQUE_SPEC](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-host/BRIQUE_SPEC.md).
- Built on COP (Cognitive Orchestration Protocol). The [Manifesto](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Manifesto.md) is the entry point.

---

## Ethics, neutrality, legal framework

inseme is **neutral** and **independent**. It does not finance, promote, or support any political party, electoral campaign, candidate, or list. It provides digital tools usable by any citizen, collective, or institution wishing to strengthen local democracy.

The ethical principles, the governance of Ophélia, and the legal constraints (data protection, democratic processes, usage in social spaces like bars) are tracked in the inseme technical roadmap. See [ROADMAP-TECH.md](https://github.com/JeanHuguesRobert/inseme/blob/main/ROADMAP-TECH.md) (sections P2: Ophélia's ethics & governance; P3: applicative governance via Kudocracy).

Per **Rule 0** of the corpus methodology: AI agents may participate in *epistemic* production (drafting, summarizing, mediating). *Political* governance — binding decisions, votes that count — belongs to living humans alone. The architecture enforces this distinction.

---

## Ecosystem & support

- **C.O.R.S.I.C.A. association** — supports the project's institutional anchor
- **[LePP.fr community](https://lepp.fr)**
- **#PERTITELLU** — the citizen movement of origin
- **Cogentia Commons methodology** — knowledge production governance ([cogentia repo](https://github.com/JeanHuguesRobert/cogentia))

---

## Contact

Pour déployer ces outils en Corse ou sur infrastructure locale :

📧 [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org)  
🔗 [LinkedIn – FractaVolta](https://www.linkedin.com/company/fractavolta/)

🐙 [inseme sur GitHub](https://github.com/JeanHuguesRobert/inseme)

Pour les projets terrain en Corse, voir directement la section [En Corse](./fr/).

**#PERTITELLU | CORTI CAPITALE**
