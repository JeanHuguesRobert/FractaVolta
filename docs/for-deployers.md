---
title: For deployers
subtitle: Concrete materials for deploying Mariani Village or comparable DC-native, local-first infrastructure.
lang: en
description: "Deployment guidance for Mariani Village and comparable FractaVolta sites: DC-native units, 48 V SELV architecture, local energy packets, optional edge inference, audit trails, and operational continuity."
canonical_url: https://fractavolta.com/for-deployers
last_stamped_at: 2026-06-02
date: "2026-06-02"
status: "active — English deployment entry point"
---

## Deployment scope

This page is for partners, builders, site owners, and technical teams preparing a concrete FractaVolta deployment.

The reference case is **Mariani Village**: a repositionable, DC-native habitat or site unit based on ISO 20-foot containers, local solar, LFP storage, safe low-voltage distribution, and optional edge compute.

The same deployment logic can also apply to:

- agricultural sites;
- isolated or seasonal facilities;
- cooperative housing;
- campuses;
- public buildings;
- industrial or tourism sites;
- pilot territories seeking energy, compute, and civic continuity.

For Corsica-based owners, farmers, municipalities, installers, and local partners, the French operational entry point is [FractaVolta en Corse](./fr/).

## Mariani Village in brief

Mariani Village units are designed around:

- ISO 20-foot containers or comparable modular structures;
- DC-native 48 V SELV distribution where appropriate;
- local photovoltaic production;
- LFP battery storage;
- optional portable battery packets;
- optional edge inference node;
- local-first operation with the grid treated as backup, peer, or arbitrage path.

The goal is not off-grid ideology. The goal is **reversible local capacity**: a unit that can operate, move, be audited, and be extended without becoming dependent on an opaque infrastructure provider.

Full technical reference: [mariani_village.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/mariani_village.md).

## What a unit contains

| Component | Spec |
|---|---|
| Container | ISO 20-foot or comparable modular structure |
| PV array | Roof-mounted or nearby photovoltaic source, sized to seasonal load |
| Storage | LFP battery bank, 48 V SELV bus where appropriate |
| Distribution | DC-first; USB-C PD 3.1 as a human-facing interface when suitable |
| AC capability | Adapter layer or portable battery packet, not the primary substrate |
| Compute | Optional edge inference node when the stack closes locally |
| Connectivity | Mesh-capable, low-power radio plus opportunistic WAN where relevant |
| Traceability | Metered energy flows, operational logs, and versioned deployment records |

The 48 V SELV bus is the spine when it is appropriate. AC becomes an adapter protocol at the boundary, not the default substrate. USB-C PD 3.1 — operating at up to 48 V DC and up to 240 W — can serve as a safe, negotiated, widely understood user interface.

See the layered analysis in [dc_native_epn.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/dc_native_epn.md).

## Regulatory navigation

Deployment is not only hardware. It also requires regulatory judgment.

Typical topics include:

- **SELV electrical frameworks** — keeping the low-voltage layer safe and legally coherent;
- **grid interaction** — explicit backup, injection, non-injection, or arbitrage scenarios;
- **IMDG maritime framework** — when LFP packets or battery containers cross ferry routes;
- **GDPR / RGPD** — when sensing, BLE tracking, occupancy, or biodiversity observation layers are installed;
- **local zoning** — container deployment, host-site agreements, seasonal repositioning, and land-use constraints;
- **insurance and operational responsibility** — making the operator boundary explicit.

The principle is not loophole exploitation. It is architectural discipline: keep each layer within its proper technical, legal, and operational boundary.

## Optional full-stack layer

A deployment can remain strictly energy-oriented. It can also host the full FractaVolta stack when useful.

Optional extensions include:

- local or solar-backed edge inference;
- Inseme Agora;
- Kudocracy.Survey;
- Ophélia AI mediation;
- biodiversity observation layer;
- site-specific Cogentia Commons corpus;
- typed audit trail for deployment decisions.

The full-stack option adds autonomy and traceability for residents, operators, institutions, or local communities. It is not mandatory for the energy unit to make sense.

## Deployment as a traced corpus

A working deployment should not leave behind only folders of PDFs. It should produce a small, inspectable operational corpus.

A site repository can contain:

- `research/index.md` listing canonical documents for the site: bill of materials, site plan, regulatory dossiers, BLE asset registry;
- `.cogentia.json` registering the corpus;
- `.cogentia/audit.jsonl` accumulating one JSONL line per state-changing operation;
- `.cogentia/continuations/` storing typed continuation records for decisions requiring judgment.

With this pattern, commissioning steps, adjustments, objections, rejected alternatives, and operator decisions remain inspectable. If another firm extends the site later, it receives a working corpus, not an opaque archive.

This is optional. A Mariani Village can run as housing or infrastructure alone. But when the corpus practice is adopted, the deployment becomes contestable, auditable, and survivable across operator changes.

## Technical references

Core documents:

1. [mariani_village.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/mariani_village.md) — reference housing and modular deployment pattern.
2. [dc_native_epn.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/dc_native_epn.md) — DC-native Energy Packet Network architecture.
3. [UNCONSCIOUS_GRID.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/UNCONSCIOUS_GRID.md) — foundational energy packet paper.
4. [Energy packets](./energy-packets) — public site introduction.
5. [Methodology](./methodology) — Cogentia Commons and continuation-based operational method.

## Cost envelope

The current reference estimate for the electrical layer of one Mariani Village unit is approximately **€2,740–€4,080**, depending on photovoltaic and battery sizing.

The total per-unit cost including container, fit-out, installation, tracking, regulatory work, and site integration varies by deployment.

The full-stack option — edge inference, civic platform, audit corpus, and integration work — is quoted per project because the useful depth varies.

## How to engage

FractaVolta can assist with:

- site survey and feasibility;
- DC-native node design and bill of materials;
- photovoltaic and storage sizing;
- regulatory navigation;
- deployment supervision;
- operational training;
- integration with cognitive and civic layers when useful;
- ongoing operations when appropriate.

Dilorta SAS is the commercial vehicle where relevant for Corsica-based housing deployment. For other deployment patterns — academic, industrial, agricultural, cooperative, or institutional — engagement is direct with FractaVolta.

Contact:

- [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org)
- [FractaVolta on GitHub](https://github.com/JeanHuguesRobert/FractaVolta)
- [LinkedIn — FractaVolta](https://www.linkedin.com/company/fractavolta/)
