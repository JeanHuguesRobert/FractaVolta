---
layout: default
title: Agent John — confidentialité et conditions
subtitle: Conversations dans le navigateur, corpus public uniquement, sans compte.
lang: fr
alternate_url: /legal/agent-john
description: "Notice de confidentialité et conditions pour la conversation publique Agent John sur fractavolta.com. Association C.O.R.S.I.C.A., opérateur FractaVolta, jumeau Cogentia, open source."
canonical_url: https://fractavolta.com/fr/legal/agent-john
date: "2026-08-22"
status: "active — public agent surface"
---

Vous allez parler à **un agent**, pas à une personne. Son nom est **John**. C'est une face **publique, en lecture seule**, d'un [jumeau numérique Cogentia](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia-digital-twin.md), proposée dans l'offre **FractaVolta**, avec un logiciel développé **en open source** par l'association **C.O.R.S.I.C.A.**

Cette page est la notice de [Agent John](/fr/john). Ce n'est **pas** la politique des services C.O.R.S.I.C.A. avec compte, comme [Olé Olé](https://oleole.acorsica.org).

## Responsables

- **Éditeur / responsable de traitement (v1) :** association **C.O.R.S.I.C.A.**, Corte, Corse. Contact : [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org).
- **Opérateur de l'hôte d'inférence :** FractaVolta, VPS **fracta** (endpoint public du Guide).
- **Logiciel :** open source (MIT pour le code ; documentation souvent CC BY-SA). Sources : [Cogentia](https://github.com/JeanHuguesRobert/cogentia), [FractaVolta](https://github.com/JeanHuguesRobert/FractaVolta).

Si l'association désigne plus tard un DPO ou un responsable distinct, la mise à jour paraîtra ici avec une nouvelle version de consentement.

## Ce que l'agent fait — et ne fait pas

John sur ce site répond à partir du **corpus public**, par la même route gouvernée que le [Guide public](/fr/guide) (`POST https://cogentia.fractavolta.com/guide/chat`). Il cite ses sources quand il le peut. Il peut se tromper. Il n'ouvre **pas** de compte, ne prend **pas** mandat de votre part, ne déploie pas, ne publie pas, ne dépense pas de budget, et ne parle pas avec l'autorité privée du propriétaire.

La frontière personnelle / propriétaire de John est ailleurs ([jhn.baronsmariani.org](https://jhn.baronsmariani.org)). Cette page est le sous-ensemble **public FractaVolta**.

## Données traitées

| Données | Où | Pourquoi | Base (RGPD) |
|---|---|---|---|
| Votre question, langue, chemin de page | Envoyées à l'endpoint Guide sur fracta | Produire une réponse | Consentement (case obligatoire) |
| Fil de conversation optionnel | **Votre navigateur uniquement** (`localStorage`) | Relire, exporter ou effacer | Consentement (case optionnelle) |
| Métadonnées techniques de requête | Journaux Guide/hôte déjà en place sur fracta | Exploiter et sécuriser l'endpoint public | Intérêt légitime d'un service public, minimisé |

Pas de profil utilisateur, pas de cookies publicitaires, pas de vente de données. La mémoire optionnelle ne quitte votre appareil que si vous posez une suite : les dix derniers tours partent tels quels, les plus anciens sous forme d'un compact extractif (pas un second appel au modèle).

## Conservation

- Fil navigateur : jusqu'à suppression, environ sept jours d'inactivité, ou retrait du consentement mémoire.
- Serveur : pas de boîte de conversation supplémentaire pour cette page. Les journaux web/serveur de fracta suivent la rétention déjà en place.

## Vos droits

Depuis ce navigateur : **exporter** le fil (JSON) et **l'effacer**. Refuser le traitement : l'agent n'envoie rien. Retirer le consentement : commandes sur [Agent John](/fr/john) ou données du site fractavolta.com.

Pour un accès ou un effacement concernant des **journaux serveur**, écrivez à [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org). Nous ne prétendrons pas que les journaux n'existent pas.

## Transferts

L'inférence tourne sur le VPS fracta (Oracle Cloud, HTTPS public). La page statique est servie par GitHub Pages. Cette interface n'ajoute pas de sous-traitant.

## Conditions d'utilisation

Service fourni **en l'état**, pour s'orienter dans le corpus public. Droit français. Pas d'usage d'urgence, médical, juridique ou de décision contraignante. N'envoyez pas de données sensibles ni de secrets.

## Notices voisines

- [Guide public](/fr/guide) — même moteur, cadrage outil corpus.
- [Olé Olé](https://oleole.acorsica.org) — autre service public C.O.R.S.I.C.A. (carte de présence ; données et stockage différents).
- [Offre jumeaux numériques (brouillon)](/offers/accountable-digital-twins).
