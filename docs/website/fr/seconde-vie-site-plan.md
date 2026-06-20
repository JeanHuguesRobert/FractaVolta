---
title: "Plan site — FractaVolta Seconde Vie"
subtitle: "Entrées françaises/corses à intégrer au site public"
status: "website integration draft"
version: "0.1"
date: "2026-06-20"
language: "fr"
source_document: "../../../research/fractavolta_seconde_vie_corse.md"
human_validation_required: true
---

# Plan site — FractaVolta Seconde Vie

## Objectif

Ajouter au site public de FractaVolta une entrée française/corse pour les actifs solaires, ruraux et agricoles à reconfigurer.

Le site doit rester sobre : il ne doit pas promettre une rentabilité, une autorisation ou une maturité technique déjà acquise.

## Menu recommandé

```text
Accueil
Déconnexion
Seconde Vie
Vignes IA
Coopérative IA
Pour les communes
Pour les propriétaires
Méthode anti-capture
Démonstrateurs
Contact
```

## Page d’accueil — bloc à ajouter

Titre :

> FractaVolta Seconde Vie

Texte court :

> Vous avez une centrale solaire ancienne, un hangar, une friche ou un ancien vignoble ? FractaVolta audite le site et construit une trajectoire de seconde vie : énergie locale, batteries, courant continu, usages critiques, recharge, inférences éventuelles et gouvernance anti-capture.

Appel à action :

> Demander une préqualification de site

## Page Seconde Vie

Source de contenu : `docs/offers/fractavolta-seconde-vie.md`.

Sections :

1. Le problème ;
2. Les quatre cas d’usage ;
3. Ce que nous auditons ;
4. Batteries fixes et mobiles ;
5. Inférences IA ou non ;
6. Recharge véhicules et poids lourds ;
7. Gouvernance anti-capture ;
8. Première étape : audit.

## Page Vignes IA

Source de contenu : `docs/offers/vignes-ia-de-montagne.md`.

Sections :

1. Pourquoi les anciens vignobles de montagne ;
2. Pourquoi des panneaux verticaux bifaciaux ;
3. Pourquoi le courant continu ;
4. Que produit un hectare ;
5. Qu’est-ce qu’un viticulteur IA ;
6. Qu’est-ce qu’une coopérative IA ;
7. Pourquoi les poids lourds électriques ;
8. Comment participer ;
9. Communes pilotes recherchées.

## Page Audit

Source de contenu : `docs/offers/audit-seconde-vie.md`.

Formulaire minimal :

```text
Type de site :
- centrale solaire ancienne
- hangar
- toiture agricole
- friche viticole
- ancien vignoble
- terrain de montagne
- station-service
- autre

Objectif :
- réduire dépendance réseau
- valoriser surplus
- batteries
- recharge véhicules
- recharge poids lourds
- inférences IA
- projet communal
- participation habitants
```

## Ton public

À dire :

> On ne vend pas des panneaux. On construit une trajectoire de capacité.

À éviter :

- rendement garanti ;
- autorisation acquise ;
- autonomie totale immédiate ;
- placement sûr ;
- IA autonome de décision ;
- slogans anti-institutionnels sans stabilisateur.

## Première intégration technique

Tâche pour agent de coding :

1. identifier le framework du site ;
2. créer ou relier les routes françaises ;
3. intégrer les trois pages : Seconde Vie, Vignes IA, Audit ;
4. ajouter un bloc d’accueil ;
5. ajouter un formulaire ou un lien de contact ;
6. vérifier build, lint et liens internes ;
7. conserver les pages Markdown comme source éditoriale.

Human validation required: yes.
