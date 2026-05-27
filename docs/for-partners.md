---
title: For partners
subtitle: Energy and compute as integrated sovereignty infrastructure, billed for avoided interruption and audited at every layer.
description: "FractaVolta travaille avec des partenaires publics et privés pour transformer du solaire local en capacité traçable et souveraine (énergie-paquet, inférence, civic tech). Modèle : intégration et opérations, pas de lock-in logiciel."
canonical_url: https://fractavolta.com/for-partners
last_stamped_at: 2026-05-15
---

## The commercial proposition

Thirty years of asking "how do autonomous agents coordinate without a capturable centre?" — in programming languages, sensor networks, energy infrastructure, and democratic institutions. We know how to answer it as a stack. We charge for the engineering, integration, and operations — not for the answer.

We do not sell electrons on a grid, carbon credits, generic consulting, or closed-source SaaS lock-in. We do not license the software (it's MIT). We sell the deployment, the integration, the operations, and the regulatory and engineering judgment that makes the stack run on a real site.

**En résumé :** Nous concevons, déployons et exploitons des infrastructures locales (énergie + compute + civic) en Corse et en Méditerranée, avec traçabilité complète et sans dépendance à un fournisseur logiciel.

---

## Ce que nous proposons concrètement

### Énergie locale (Energy substrate)

Nous aidons à transformer une installation solaire en source de capacité utile et traçable sur le territoire :

- Études de faisabilité spécifiques au site (dimensionnement, flux de paquets, cadre réglementaire).
- Conception de nœuds DC-natifs 48V SELV (sécurisés, sans électricien agréé dans beaucoup de cas).
- Ingénierie de containers batteries (2 MWh, certifiés transport maritime, traçables BLE).
- Intégration de réseaux gravitationnels (PGN) quand le site s’y prête (cas Corse).

### Compute souverain (si pertinent pour votre projet)

- Inférence locale solaire avec tarification CXU (énergie × efficacité × SLA) — prix auditable par inférence utile.
- Nœuds edge solaires avec continuité garantie via Inference Packet Networks quand les grands fournisseurs sont indisponibles ou trop chers.
- Pas de dépendance à un hyperscaler pour les fonctions critiques.

### Intégration complète (si souhaité)

- Assemblage de la pile complète : énergie + compute souverain + couche de cognition (cogentia.js) + outils citoyens (inseme).
- Configuration multi-instances pour communes ou sites (Kudocracy.Survey, Inseme Agora).
- Médiation IA Ophélia sur nœuds locaux, sans appel à des API externes.
- Traçabilité et audit complets de toutes les décisions — livrables standards du projet.

### Operations

- Operational training for site staff
- Deployment support
- Cogentia Commons editor role (if you want the corpus methodology applied to your domain)

---

## Notre logique de valeur : la continuité évitée

Nous ne vendons pas de l’énergie ou des tokens. Nous vendons la **garantie de ne pas être bloqué**.

- Énergie : éviter les coupures quand le câble SARCO est saturé ou le réseau tombe.
- Compute : garder de l’inférence locale quand les grands modèles deviennent indisponibles ou trop chers.
- Cognition : ne pas perdre le raisonnement quand un fournisseur change ses conditions.
- Civic : garder la main sur vos outils de délibération sans dépendre d’un éditeur SaaS.

C’est un modèle de service et d’intégration, pas de licence logicielle.

## What you also receive — the audit trail

Beyond the hardware and the running platform, every project ships with its own audit chain — produced live during the engagement, not assembled retroactively.

- **Decisions are typed**, via the `cogentia.continuation.v1` protocol implemented in `cogentia.js`. When a deployment decision required judgment (which battery topology for site X; which inverter for that grid-tie context; how to size the inference cluster), the question, the alternatives we considered, the chosen path, and the reasoning are all preserved as JSON in the project's `.cogentia/continuations/`. You can replay them.
- **Failed alternatives are not erased.** When we tried something and it didn't work, the failed branch is part of the record — with the reason. The next operator (us in two years, or a different firm if you change supplier) can read why we ruled options out.
- **Claims are anchored.** Every datasheet number, every architectural assertion, every cost estimate points at a canonical document under version control. If we change a number, the change is visible in the git history.
- **The AI we use is replaceable.** Any continuation we emit can be resumed by another agent — Claude today, ChatGPT tomorrow, a local model next year, a human operator at any point. No provider lock-in flows down to you through us.

This is not compliance theater layered on top of normal work. It is how the work is done. See the [methodology page](./methodology) for the formal account.

---

## Projets et opportunités en Corse

Nous avançons actuellement sur plusieurs chantiers et discussions en Corse :

- Mariani Village (Tavignano) — habitat DC-natif repositionnable.
- Valorisation de réseaux hydrauliques historiques (PGN).
- Nœuds d’inférence solaires locaux.

Pour les acteurs locaux (propriétaires, collectivités, installateurs), les pages pratiques sont ici :
- [Seconde Vie solaire](./fr/seconde-vie)
- [Marchés locaux](./fr/marches)
- [Installateurs et mainteneurs](./fr/installateurs)

Les documents techniques plus approfondis sont disponibles sur demande ou via la page [Pour déployer](./for-deployers).

---

## Avec qui nous travaillons

Nous privilégions les partenaires qui cherchent de la **véritable souveraineté locale** :

- Collectivités et autorités régionales
- Exploitations agricoles et coopératives
- Sites industriels ou touristiques avec besoins en autonomie énergétique et compute
- Institutions qui veulent des outils de délibération sans dépendance à un éditeur

Nous ne travaillons pas avec des structures qui recherchent du lock-in logiciel, des chaînes d’audit opaques, ou de l’IA comme outil d’extraction.

---

## Prochaines étapes

Si vous êtes une collectivité, un exploitant agricole, un installateur ou un acteur de l’énergie en Corse ou en Méditerranée et que vous voulez transformer du solaire local en capacité réelle et traçable, contactez-nous directement.

**Contact direct :**
- 📧 [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org)
- 🔗 [LinkedIn – FractaVolta](https://www.linkedin.com/company/fractavolta/)

Pour les opportunités concrètes en Corse (propriétaires, collectivités, installateurs), voir directement la section [En Corse](./fr/).

Pour les aspects techniques (unités DC-natives, coûts, cadre réglementaire), consultez la page [Pour les porteurs de projet](./for-deployers).

Nous répondons personnellement et dans les meilleurs délais.

*Véhicule commercial : Dilorta SAS (Corse). Gouvernance des connaissances : Cogentia Commons.*
