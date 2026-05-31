---
title: For deployers
subtitle: Concrete materials for getting a Mariani Village (or comparable DC-native deployment) off the ground.
description: "Mariani Village : unités containers DC-natives 48V SELV, hors CONSUEL, repositionnables. Conçues pour la Corse et les territoires méditerranéens. Documentation technique pour installateurs et porteurs de projet."
canonical_url: https://fractavolta.com/for-deployers
last_stamped_at: 2026-05-15
date: "2026-05-15"
status: "draft — auto-filled (frontmatter cleanup)"
---

## Mariani Village en bref

Unités containers ISO 20 pieds en **DC-natif 48V SELV** (<14 m²), repositionnables, sans raccordement réseau obligatoire, sans électricien agréé, sans CONSUEL.

Coût électrique total par unité : 2 740 – 4 080 €.  
Commercialisé via **Dilorta SAS** (Corse).

Idéal pour sites isolés, saisonniers ou en autonomie en Corse et Méditerranée.

Lire le document technique complet : [mariani_village.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/mariani_village.md).

---

## What a unit contains

| Component | Spec |
|---|---|
| Container | ISO 20-foot, structural; SELV-certified electrical fit-out |
| PV array | Roof-mounted, sized to seasonal load |
| Storage | LFP battery bank, 48V SELV bus |
| Distribution | DC-first; USB-C PD 3.1 (240W) as the human interface |
| AC capability | Portable 700 Wh battery packet, BLE-tracked, borrowed from a shared charging station |
| Compute | Edge inference node when the stack closes (Ophélia + Agora on-site) |
| Connectivity | Mesh-capable, low-power radio + opportunistic WAN |

The 48V SELV bus is the spine. AC is an adapter protocol at the boundary, not the substrate. USB-C PD 3.1 — operating at exactly 48V DC, up to 240W — is touch-safe, power-negotiated, and already in every user's pocket.

See the full layered analysis in [dc_native_epn.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md).

---

## Regulatory navigation

The reason the unit avoids the licensed-electrician / CONSUEL path is precisely because it stays below the SELV threshold. This is engineering, not loophole exploitation: a 48V DC bus with current-limited outlets is genuinely touch-safe and falls under different regulatory frameworks than a 230V AC installation.

What we navigate for you:

- **SELV electrical codes** (NF C 15-100 part 7-701 and related) — keeping the installation below the licensed-installation threshold while meeting safety standards
- **IMDG maritime framework** for the LFP container packets traversing ferry routes
- **RGPD/GDPR** for any installed sensing (BLE tracking, occupancy, the Atlas of Biodiversity layer if you choose to deploy it)
- **Local zoning** — ISO container deployment, host-site agreements, seasonal repositioning permits

---

## Option "pile complète" (facultative)

Le Mariani Village est conçu pour pouvoir accueillir toute la pile de souveraineté si vous le souhaitez :

- Outils de délibération locale (Inseme Agora + Kudocracy)
- Médiation IA Ophélia fonctionnant 100 % sur site (pas d’appel API externe)
- Couche observation biodiversité (Atlas of Biodiversity)

Vous pouvez très bien déployer les unités en mode "habitat seul". L’option full-stack apporte simplement un niveau supplémentaire d’autonomie et de traçabilité pour les résidents ou la collectivité.

---

## Pour aller plus loin (documents techniques)

Ces documents sont destinés aux porteurs de projet et aux équipes techniques :

1. Référence habitat : [mariani_village.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/mariani_village.md)
2. Architecture DC-native : [dc_native_epn.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md)
3. Fondement de l’énergie-paquet : [UNCONSCIOUS_GRID.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md)

Pour les aspects pratiques et les opportunités en Corse, voir directement la section [En Corse](./fr/).

N’hésitez pas à nous contacter directement : [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org) ou via [LinkedIn](https://www.linkedin.com/company/fractavolta/).

## Votre déploiement comme corpus tracé

A working Mariani Village is also a small Cogentia Commons corpus. The site folder (whether on your own GitHub organization or a private Git host) carries:

- A `research/index.md` listing the canonical documents for the site (BOM, site plan, regulatory dossiers, BLE asset registry).
- A `.cogentia.json` registering the corpus.
- A `.cogentia/audit.jsonl` accumulating one JSONL line per state-changing operation — every commissioning step, every adjustment, every objection filed by residents or by the operator.
- A `.cogentia/continuations/` directory of typed continuation records for any decision that required judgment.

You can run `node cogentia.js scan` against this corpus to verify that every research-grade document is anchored. You can run `cogentia.js check` to validate cross-references. If you contract a different firm to extend the site in two years, they get a working corpus, not a folder of PDFs.

This is optional. A Mariani Village runs perfectly well as housing alone. But when you take the corpus practice seriously, the deployment becomes contestable, auditable, and survivable across operator changes.

---

## Cost envelope

Per-unit electrical: €2,740–4,080 (depending on PV/battery sizing). Per-unit total including container, fit-out, and tracking infrastructure varies by site.

The full-stack option (edge inference + civic platform) adds an edge compute node and software integration — quoted per project, since the integration depth varies.

---

## How to engage

We help you with:

- Site survey and feasibility
- DC-native node design and bill of materials
- Deployment supervision and operational training
- Integration with the cognitive and civic layers if you want the full stack
- Ongoing operations (optional)

Dilorta SAS is the commercial vehicle for the housing deployment specifically. For other deployment patterns (academic, industrial, cooperative), engagement is direct with FractaVolta.

---

## Contact

📧 jhr@baronsmariani.org
🌐 [FractaVolta on GitHub](https://github.com/JeanHuguesRobert/FractaVolta)
