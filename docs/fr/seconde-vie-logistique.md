---
title: "FractaVolta Seconde Vie Logistique"
subtitle: "Transformer les actifs solaires existants en nœuds de mobilité, collecte, livraison et recharge"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
lang: fr
status: "draft — human validation required"
version: "0.1"
date: "2026-06-24"
license: "CC BY-SA 4.0"
canonical_path: "FractaVolta/docs/fr/seconde-vie-logistique.md"
source_or_derived: "produit décliné de haute fidélité"
related_documents:
  - "FractaVolta/docs/fr/seconde-vie.md"
  - "FractaVolta/research/fractavolta_seconde_vie_corse.md"
  - "FractaVolta/research/fractanet.md"
  - "FractaVolta/research/electricity_in_containers.md"
  - "FractaVolta/README.md"
  - "FractaVolta/AGENTS.md"
human_validation_required: true
---

# FractaVolta Seconde Vie Logistique

**FractaVolta Seconde Vie Logistique** est une extension de l’offre [FractaVolta Seconde Vie](./seconde-vie).

Elle s’adresse aux propriétaires d’installations photovoltaïques existantes ou arrivant en fin de contrat d’obligation d’achat, ainsi qu’aux communes, transporteurs, producteurs locaux, agriculteurs et acteurs économiques qui veulent transformer une production solaire sous-valorisée en services concrets : recharge, collecte, livraison, mobilité flexible, secours, froid, continuité logistique.

L’idée simple :

> Une installation solaire en seconde vie ne doit pas seulement produire des kWh. Elle peut devenir un nœud de capacité locale.

L’ajout logistique change la valeur du site : l’énergie n’est plus seulement vendue ou injectée. Elle peut être stockée, déplacée, utilisée pour des tournées, affectée à des usages prioritaires, et reliée à des personnes, des marchandises, des véhicules et des preuves.

---

## 1. Pourquoi cette offre

De nombreuses installations photovoltaïques construites en Corse ont été pensées autour d’un modèle simple :

```text
produire
→ injecter
→ vendre au tarif prévu par contrat
```

Lorsque le contrat arrive à son terme, ou lorsque le tarif devient peu attractif, l’actif peut entrer dans une zone grise :

- production encore réelle ;
- maintenance parfois incertaine ;
- revenu moins lisible ;
- dépendance au réseau ;
- absence d’usage local organisé ;
- risque de vieillissement silencieux ;
- valeur solaire captée trop loin du territoire.

FractaVolta Seconde Vie Logistique propose un autre chemin :

```text
installation solaire existante
→ audit technique et contractuel
→ maintenance organisée
→ stockage stationnaire ou mobile
→ recharge de véhicules électriques
→ collecte / livraison / mobilité flexible
→ traçabilité des flux
→ valeur locale vérifiable
```

Formule :

> La fin d’un contrat d’achat ne doit pas être la fin d’un actif solaire. Elle peut être le début de sa territorialisation.

---

## 2. Ce qui change avec la logistique

Sans logistique, la seconde vie solaire cherche surtout à mieux utiliser l’énergie sur place.

Avec la logistique, la demande devient mobile.

On peut déplacer :

- un véhicule vers un site solaire ;
- une batterie mobile vers un hub ;
- des marchandises vers un point de collecte ;
- une personne vers une destination utile ;
- un stock d’énergie vers un besoin réel ;
- une preuve vers le corpus de traçabilité.

La question n’est plus seulement :

> Que vaut ce kWh ?

Elle devient :

> Quelle capacité utile ce kWh permet-il de produire ici, maintenant, pour qui, avec quelle preuve et sous quel régime de priorité ?

---

## 3. Les trois flux

L’offre articule trois flux qui sont habituellement séparés.

### 3.1. Flux d’énergie

Le site solaire produit une énergie locale qui peut être :

- autoconsommée ;
- stockée ;
- injectée seulement quand c’est pertinent ;
- utilisée pour recharger des véhicules ;
- déplacée sous forme de batterie mobile ou containerisée ;
- réservée à des usages prioritaires.

### 3.2. Flux de marchandises

La flotte peut transporter :

- colis ;
- produits agricoles ;
- hydrolats, huiles essentielles, produits locaux ;
- pièces détachées ;
- courses ;
- matériel communal ;
- petits volumes professionnels ;
- retours, emballages, batteries ou déchets valorisables.

### 3.3. Flux de personnes

Lorsque le véhicule, le cadre réglementaire et les contrats le permettent, la même architecture peut transporter des personnes :

- habitants sans solution simple de mobilité ;
- étudiants ;
- seniors ;
- producteurs se rendant vers un marché ou un point de dépôt ;
- personnels ou partenaires identifiés ;
- passagers dans un service fermé, conventionné ou expérimental.

Point de doctrine :

> Une personne peut être routée, mais jamais réduite à un paquet.

Le COP peut traiter une demande de déplacement humain comme une intention de déplacement avec contraintes renforcées : confort, sécurité, information, consentement, horaires, détour maximal, dignité et responsabilité.

---

## 4. Véhicule pivot : utilitaire modulable

Le véhicule d’amorçage idéal n’est pas nécessairement le camion le plus gros.

Pour un premier démonstrateur, le meilleur candidat est un utilitaire électrique modulable capable de servir à la fois au transport de marchandises et au transport de passagers. Le Kia PV5 Crew / cabine allongée est un exemple intéressant si les caractéristiques annoncées sont confirmées pour le marché français, mais l’offre ne doit pas dépendre d’un modèle unique.

L’intérêt n’est pas seulement l’autonomie ou le volume. L’intérêt est la convertibilité.

```text
si passagers
  → sièges mobilisés

si marchandises
  → volume de chargement augmenté

si flux mixte
  → arbitrage dynamique par réservation et COP

si risque de trajet à vide
  → recherche de colis, personne ou détour utile
```

Formule :

> Le véhicule donne la flexibilité physique ; Fractanet donne l’intelligence de routage.

---

## 5. Architecture Fractanet

Chaque site solaire en seconde vie peut être qualifié comme un nœud Fractanet.

```yaml
site:
  type: hangar_pv | toiture | ombriere | petite_centrale | friche_reconfiguree
  puissance_kwc: ...
  fin_obligation_achat: ...
  etat_modules: ...
  etat_onduleurs: ...
  acces_vehicules: ...
  stockage_possible: oui/non
  recharge_possible: ac | dc | non
  usages_locaux:
    - recharge
    - froid
    - collecte
    - livraison
    - mobilite
    - secours
    - eau
    - calcul
  risques:
    - technique
    - contractuel
    - assurance
    - incendie
    - acces
    - transport_personnes
    - transport_marchandises
  priorites:
    - habitants
    - producteurs_locaux
    - services_essentiels
    - transporteurs_qualifies
```

Le COP arbitre ensuite :

```text
produire
ou stocker
ou recharger
ou router un véhicule
ou envoyer une batterie mobile
ou différer une demande
ou utiliser EDF en backup
ou rerouter vers un autre nœud
ou activer un régime dégradé
```

L’objectif n’est pas la maximisation brute de l’énergie. L’objectif est la maximisation de la capacité utile sous contraintes de coût, temps, risque, priorité, preuve et exposition à la capture.

---

## 6. Relation à EDF et au réseau

L’offre ne suppose pas une rupture brutale avec EDF.

Le modèle recommandé est hybride :

```text
solaire local en base
+ stockage stationnaire ou mobile
+ EDF comme backup ou appoint
+ générateur thermique seulement en dernier recours
+ COP pour arbitrer les régimes
```

Le réseau peut rester utile, mais il ne doit plus être le centre unique de décision.

Formule :

> EDF doit devenir une option routable, pas une dépendance structurante.

Cette logique permet d’optimiser le CAPEX : viser d’abord une forte part d’autoconsommation et de stockage utile, sans surdimensionner dès le départ pour atteindre une autonomie totale coûteuse et parfois inutile.

---

## 7. Offre modulaire

Le marketing peut être intégré ; les contrats doivent rester modulaires.

### 7.1. Seconde Vie Site

Qualification et remise en capacité d’un actif solaire existant.

Livrables possibles :

- audit technique ;
- audit contractuel ;
- état de maintenance ;
- analyse des accès ;
- usages locaux possibles ;
- risques principaux ;
- premières hypothèses de reconfiguration ;
- estimation des données manquantes.

### 7.2. Seconde Vie Stock

Ajout ou organisation d’un stockage local.

Livrables possibles :

- scénario batterie stationnaire ;
- scénario batterie mobile ;
- règles d’usage EDF / solaire / stockage ;
- contraintes de sécurité ;
- estimation CAPEX/OPEX ;
- stratégie de maintenance ;
- régimes normal, perturbé, dégradé et secours.

### 7.3. Seconde Vie Recharge

Création d’un point de recharge privé, professionnel, fermé, ouvert sous conditions ou conventionné.

Livrables possibles :

- qualification juridique du mode d’accès ;
- choix AC/DC ;
- puissance cible ;
- contraintes IRVE ;
- compatibilité avec véhicules cibles ;
- supervision ;
- facturation ou contrat de service ;
- règles de priorité.

### 7.4. Seconde Vie Passage

Service de mobilité et logistique flexible.

Livrables possibles :

- tournées personnes / marchandises ;
- application de réservation ;
- règles de détour maximal ;
- priorités territoriales ;
- contraintes passagers ;
- contraintes colis ;
- optimisation du remplissage ;
- suivi des kilomètres à vide ;
- preuve de service rendu.

### 7.5. Seconde Vie Hub

Agrégation de plusieurs sites autour d’un hub, par exemple à Corte.

Livrables possibles :

- cartographie multi-sites ;
- scénario hub ;
- containers batteries ;
- recharge rapide ;
- flotte utilitaire ;
- relation transporteurs ;
- capital patient ;
- gouvernance anti-capture ;
- tableaux de bord de valeur locale.

---

## 8. Marchés concernés

### 8.1. Propriétaires de hangars photovoltaïques

Ils disposent souvent d’un actif réel, mais ne veulent pas devenir énergéticiens, logisticiens ou opérateurs de recharge.

Promesse :

> Nous reprenons la complexité, vous gardez un revenu lisible, une sortie réversible et une meilleure territorialisation de votre actif.

### 8.2. Agriculteurs et producteurs locaux

Le site solaire peut devenir un point de recharge, collecte, froid, transformation légère ou départ de tournée.

Usages :

- collecte de produits ;
- livraison vers marché ou boutique ;
- recharge utilitaire ;
- froid agricole ;
- réserve électrique ;
- mutualisation avec d’autres producteurs.

### 8.3. Communes

Une commune peut accueillir ou soutenir un nœud de capacité.

Usages :

- mobilité locale ;
- desserte de villages ;
- transport solidaire encadré ;
- recharge communale ;
- secours ;
- continuité de services essentiels.

### 8.4. Transporteurs et artisans

Ils peuvent accéder à une énergie plus stable que le gazole, sans porter seuls tout le risque technique.

Usages :

- recharge contractuelle ;
- flotte louée ;
- tournées partagées ;
- accès à un hub ;
- appui à l’électrification progressive.

### 8.5. Investisseurs locaux et capital patient

L’épargne corse sous-employée peut financer des actifs réels si la confiance est reconstruite par la transparence, la traçabilité, la limitation des promesses et la gouvernance anti-capture.

Formule :

> Patient ne veut pas dire gratuit ; patient veut dire non extractif.

---

## 9. Intérêt territorial sans accès public automatique

Le bénéfice territorial ne suppose pas nécessairement une ouverture indifférenciée au public.

Un site peut être privé, contractuel, fermé, réservé à des partenaires, ou conventionné avec une collectivité, tout en servant des flux utiles aux habitants.

```text
habitants
← biens livrés / mobilité utile / services essentiels
← transporteurs, communes, producteurs ou opérateurs qualifiés
← site solaire en seconde vie
```

L’accès doit être qualifié site par site. Il ne faut pas confondre :

- intérêt territorial ;
- accès public ;
- service privé ;
- service conventionné ;
- infrastructure critique ;
- expérimentation.

---

## 10. Garde-fous

FractaVolta ne doit pas promettre :

- rendement garanti ;
- autorisation acquise ;
- absence de contrainte réglementaire ;
- autonomie totale ;
- sécurité sans contrôle professionnel ;
- transport de personnes sans cadre adapté ;
- transport de marchandises sans qualification adaptée ;
- recharge publique déguisée ;
- absence de risque batterie ;
- compatibilité automatique avec les aides ;
- rentabilité sans volume suffisant.

Toujours distinguer :

```text
idée
→ note de travail
→ audit
→ pré-étude
→ démonstrateur
→ prototype
→ pilote
→ service commercial
→ infrastructure critique
```

La page publique doit rester sobre. Les engagements précis doivent être renvoyés à un audit site par site.

---

## 11. Données minimales pour une préqualification

Pour un site solaire :

- localisation ;
- puissance installée ;
- année de mise en service ;
- date de fin d’obligation d’achat ;
- propriétaire des panneaux ;
- propriétaire du terrain ou bâtiment ;
- contrat existant ;
- factures ou données de production ;
- état de maintenance ;
- accès véhicules ;
- possibilité de stationnement ;
- distance aux usages locaux ;
- risques incendie connus ;
- présence ou non de consommation sur site ;
- intérêt pour stockage, recharge, froid, collecte ou mobilité.

Pour un besoin logistique :

- lieux de départ ;
- lieux d’arrivée ;
- fréquence ;
- horaires ;
- volume ;
- poids ;
- personnes concernées ;
- contraintes de confort ;
- contraintes de livraison ;
- acceptabilité du détour ;
- priorité territoriale ;
- tolérance au report.

---

## 12. Pilote recommandé : Boucle solaire Corte

Un pilote réaliste pourrait associer :

```text
1 site solaire en seconde vie
+ 1 stockage modeste
+ 1 utilitaire électrique modulable
+ 1 réservation simple
+ 1 boucle de collecte / livraison / passagers identifiés
+ 1 tableau de bord COP minimal
```

Indicateurs à suivre :

- kWh produits ;
- kWh autoconsommés ;
- kWh utilisés pour mobilité ;
- kWh EDF utilisés en backup ;
- kilomètres parcourus ;
- kilomètres à vide ;
- sièges occupés ;
- volume transporté ;
- tournées utiles ;
- gazole évité ;
- incidents ;
- retards ;
- satisfaction des propriétaires ;
- satisfaction des utilisateurs ;
- valeur locale créée ;
- part réinvestie localement.

La réussite du pilote ne doit pas être mesurée seulement par le coût du kWh. Elle doit être mesurée par la capacité utile produite.

---

## 13. Formulation publique

Version courte :

> FractaVolta Seconde Vie Logistique transforme les installations solaires existantes en nœuds de mobilité, collecte, livraison et recharge locale.

Version propriétaire :

> Votre installation solaire entre dans sa seconde vie. Nous étudions comment l’utiliser pour produire non seulement de l’électricité, mais de la capacité utile : recharge, collecte, livraison, froid, secours ou mobilité flexible.

Version territoriale :

> Au lieu de laisser le soleil corse produire une rente dégradée ou captée, nous le connectons aux flux réels du territoire : habitants, producteurs, villages, véhicules, marchandises et services essentiels.

Version Fractanet :

> Le kWh devient un paquet de capacité : produit, stocké, routé, consommé, audité.

---

## 14. Appel à action

Vous possédez ou exploitez :

- un hangar photovoltaïque ;
- une toiture solaire ;
- une ombrière ;
- une petite centrale ;
- un bâtiment agricole ;
- un site pouvant accueillir recharge, stockage ou collecte ;
- une flotte ou un besoin de transport local.

Préparez les premières informations : puissance, date de mise en service, contrat, date de fin, localisation, accès, maintenance, usages locaux possibles.

Contact : [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org)

---

## 15. Rapport minimal de rédaction

- Target document: `FractaVolta/docs/fr/seconde-vie-logistique.md`
- Files produced or changed: `seconde-vie-logistique.md` draft only
- Source or derived product: produit décliné de haute fidélité à partir de documents sources FractaVolta
- Critiques integrated: nécessité de distinguer offre publique, hypothèse technique, transport de personnes, transport de marchandises, statut IRVE, EDF backup, intérêt territorial sans accès public automatique et capital patient
- Critiques rejected or deferred: chiffrages CAPEX/OPEX détaillés, promesses d’aides, comparatifs réglementaires exhaustifs, modèles de contrat
- Known risks: qualification juridique du transport mixte, assurance batteries, sécurité IRVE, requalification en service public ou borne ouverte au public, volume réel de demande
- Human validation needed: yes
- Next useful action: créer une issue ou une branche d’intégration, puis relire juridiquement les sections transport, IRVE et aides
