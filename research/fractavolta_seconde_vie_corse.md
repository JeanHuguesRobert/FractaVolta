---
title: "FractaVolta Seconde Vie — Corse"
subtitle: "Débrancher, reconfigurer, replanter et transformer les actifs solaires ou ruraux en capacités locales"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
status: "source working draft — human validation required"
version: "0.1"
date: "2026-06-20"
language: "fr"
license: "CC BY-SA 4.0"
canonical_path: "FractaVolta/research/fractavolta_seconde_vie_corse.md"
source_or_derived: "source document"
human_validation_required: true
related_documents:
  - "FractaVolta/AGENTS.md"
  - "FractaVolta/README.md"
  - "FractaVolta/research/fractanet.md"
  - "FractaVolta/research/capability_regimes.md"
  - "FractaVolta/DC_NATIVE_EPN.md"
  - "FractaVolta/electricity_in_containers.md"
  - "marenostrum/research/pacte_anti_capture_solaire_inferentielle.md"
  - "marenostrum/research/mare_nostrum_coalition_anti_capture.md"
---

# FractaVolta Seconde Vie — Corse

## Débrancher, reconfigurer, replanter et transformer les actifs solaires ou ruraux en capacités locales

## 0. Statut

Ce document est une **source de travail** pour l’offre française et corse de FractaVolta.

Il ne constitue pas une offre commerciale stabilisée, ni une promesse de rendement, ni une affirmation de faisabilité réglementaire pour un site donné. Il pose une architecture d’offre à tester, décliner et relire humainement.

La règle de base est celle du dépôt : distinguer doctrine, architecture, hypothèse commerciale, calcul d’ingénierie, produit décliné et claim public.

---

## 1. Thèse

**FractaVolta Seconde Vie** propose de donner une seconde vie aux actifs énergétiques, bâtis ou agricoles sous-utilisés en Corse.

Il ne s’agit pas de vendre des panneaux supplémentaires.

Il s’agit de transformer des dépendances en capacités :

```text
ancien actif solaire, hangar ou friche
→ audit
→ reconfiguration DC-native
→ stockage fixe ou mobile
→ inférence IA éventuelle
→ recharge locale, notamment logistique
→ gouvernance anti-capture
→ valeur conservée dans le territoire
```

Formule courte :

> On ne remplace pas une centrale. On reconvertit une dépendance en capacité.

---

## 2. Relation avec FractaVolta Déconnexion

FractaVolta Déconnexion part de l’usager : foyer, bâtiment, pièce, atelier, lieu pilote.

FractaVolta Seconde Vie part de l’actif : centrale ancienne, hangar, toiture, terrain, friche, ancien vignoble.

Les deux offres partagent la même grammaire :

```text
audit
→ réduction des dépendances
→ courant continu
→ stockage
→ usages critiques
→ trajectoire progressive
→ maintenance locale
→ documentation
```

Déconnexion répond à la question :

> De quoi dépend réellement un usager ?

Seconde Vie répond à la question :

> Que peut encore devenir capable de faire un actif déjà là, ou un terrain abandonné ?

---

## 3. Les quatre cas d’usage

### 3.1. Seconde Vie Centrale

Cible : ancienne centrale photovoltaïque au sol, centrale arrivant en fin de contrat, site sous-valorisé ou trop dépendant de la vente brute au réseau.

Objectif :

```text
vente basse du kWh
→ autoconsommation locale
→ batteries
→ recharge
→ compute / inférence éventuelle
→ réserve de crise
```

La question n’est pas seulement : « combien vaut le kWh vendu ? »

La question devient :

> Quelle valeur locale peut-on produire en évitant de vendre le soleil au plus bas de la chaîne de valeur ?

### 3.2. Seconde Vie Hangar

Cible : hangars agricoles, artisanaux, logistiques, ateliers, bâtiments de stockage, toitures solaires existantes ou équipables.

Objectif : transformer un toit ou un bâtiment en micro-nœud énergétique :

- froid agricole ;
- atelier autonome ;
- recharge utilitaires ;
- stockage local ;
- petit nœud d’inférence ;
- base de maintenance ;
- réserve électrique de proximité.

Formule :

> Le hangar n’est plus seulement un toit. Il devient une batterie productive.

### 3.3. Seconde Vie ReVigne

Cible : anciennes centrales au sol susceptibles d’être reconfigurées, partiellement démontées ou reconverties vers une fonction agricole réelle.

Objectif : sortir du solaire pur lorsque c’est possible, afin de recréer une production agricole compatible avec l’énergie.

Points à vérifier site par site :

- état des sols ;
- espacement ;
- accès mécanisé ;
- orientation ;
- ombrage ;
- statut juridique ;
- contraintes incendie ;
- faisabilité agronomique ;
- coût de reconfiguration.

Formule :

> Là où une centrale a remplacé un sol, FractaVolta cherche à rendre le sol à nouveau productif.

### 3.4. Vignes IA de montagne

Cible : anciens vignobles en friche, terrains pentus, zones rurales abandonnées, communes de montagne.

Objectif : replanter des vignes capables :

```text
vigne
+ panneaux verticaux bifaciaux
+ courant continu
+ batteries stationnaires
+ agents IA
+ batteries mobiles
+ recharge rapide DC, prioritairement poids lourds électriques
+ coopérative IA
```

La vigne produit deux récoltes :

- une récolte biologique : raisin, vin, paysage, entretien rural ;
- une récolte photonique : électricité DC, inférences, recharge, réserve de crise.

Formule :

> Le viticulteur IA apporte son raisin à la cave et ses électrons à la coopérative IA.

---

## 4. Le révélateur et le stabilisateur

Le cas EDF joue le rôle de révélateur : il rend visible la dépendance au réseau, au raccordement, au rachat, aux files d’attente, aux arbitrages centralisés et aux architectures où le solaire corse peut être traité comme une contrainte plutôt que comme une richesse.

Le stabilisateur n’est pas seulement critique. Il est productif :

```text
capture révélée
→ ancienne friche replantée
→ vigne capable
→ électricité DC
→ inférence IA
→ recharge logistique
→ financement habitant
→ valeur gardée localement
```

Formule politique :

> EDF révèle la capture. La vigne capable stabilise la sortie.

---

## 5. Architecture DC-native

L’offre Seconde Vie doit privilégier une chaîne courte en courant continu lorsque le site le permet :

```text
PV DC
→ batterie DC
→ bus DC
→ serveurs / GPU / CPU
→ batteries mobiles DC
→ recharge rapide DC
→ batteries de véhicules électriques
```

La logique n’est pas idéologique. Elle est physique : photovoltaïque, batteries, électronique, serveurs et recharge rapide fonctionnent nativement en courant continu ou passent nécessairement par du continu.

Objectif : réduire les conversions inutiles, les pertes, la complexité, les pannes et la dépendance à l’architecture AC héritée.

---

## 6. Coopérative IA

La coopérative IA est l’équivalent énergétique et cognitif d’une cave coopérative.

Elle agrège :

- kWh excédentaires ;
- batteries fixes et mobiles ;
- capacités d’inférence ;
- stations de recharge ;
- contrats de disponibilité ;
- données de traçabilité ;
- contributions habitants ;
- réserves de crise.

Elle rémunère les apporteurs et garde une part décisive de la valeur dans le territoire.

Elle ne vend pas seulement du kWh. Elle vend de la capacité : recharge, continuité, intelligence locale, sécurité d’approvisionnement, logistique, données auditées.

---

## 7. Priorité corse : poids lourds électriques et logistique insulaire

Dans la version corse, la recharge rapide doit viser en priorité les flux logistiques : utilitaires, transporteurs, poids lourds électriques, véhicules communaux, artisans, secours et flottes locales.

Corte est un nœud naturel d’expérimentation :

```text
centre de la Corse
+ carrefour intérieur
+ ville universitaire
+ proximité de communes de montagne
+ rôle logistique potentiel
+ symbole politique
```

Formule :

> Le soleil des vignes peut recharger les camions qui font vivre l’île.

---

## 8. Financement habitant et capital patient

Le financement local est une couche anti-capture, non un gadget de communication.

Il peut réduire :

- la dépendance bancaire ;
- la nécessité de céder le contrôle à un opérateur extérieur ;
- la défiance locale ;
- la rupture entre producteurs, habitants et communes.

Séquence prudente :

```text
1. financer la preuve : audit, juridique, mesures, pré-études
2. financer le pilote : 1 site démonstrateur
3. financer la coopérative : batteries, station, supervision
4. financer le déploiement : dette bancaire négociée en position plus forte
```

Aucune participation habitante ne doit être présentée comme placement sûr. Tout véhicule doit être documenté, plafonné, risqué, auditable et relu juridiquement.

---

## 9. Offre FractaVolta Seconde Vie

### 9.1. Audit Seconde Vie Express

Objectif : qualifier rapidement un site.

Entrées : photos, localisation, factures, contrat d’achat, puissance installée, type de terrain, accès, usages locaux possibles.

Sortie : note courte : potentiel, risques, prochaine étape.

### 9.2. Audit Seconde Vie Complet

Objectif : produire une première trajectoire réaliste.

Livrables :

- état technique ;
- production estimée ;
- contraintes ;
- scénarios EDF / hors EDF / hybride ;
- batteries ;
- usages locaux ;
- recharge ;
- inférence éventuelle ;
- CAPEX/OPEX estimatifs ;
- risques réglementaires ;
- clauses anti-capture.

### 9.3. Étude Vigne IA

Objectif : établir si un terrain de montagne ou ancien vignoble peut redevenir productif en vigne agrivoltaïque DC-native.

Livrables :

- hypothèse viticole ;
- hypothèse énergétique ;
- orientation panneaux ;
- scénario batterie ;
- scénario inférence ;
- scénario surplus / recharge ;
- acceptabilité paysagère ;
- modèle coopératif.

### 9.4. Étude Coopérative IA

Objectif : agréger plusieurs sites autour d’un hub de recharge, de batteries mobiles et d’inférence.

Livrables :

- périmètre multi-sites ;
- flux d’énergie ;
- logistique batteries ;
- station(s) cible(s) ;
- rémunération des apporteurs ;
- gouvernance ;
- financement habitant ;
- risques.

---

## 10. Garde-fous

Ne pas promettre :

- rendement garanti ;
- autorisation acquise ;
- raccordement inutile dans tous les cas ;
- autonomie totale ;
- IA souveraine sans gouvernance ;
- neutralité réglementaire ;
- absence de risque technique ;
- sécurité sans contrôle professionnel.

Toujours distinguer :

```text
démonstrateur
prototype
pilote
service commercial
infrastructure critique
```

---

## 11. Première déclinaison web

Le site français/corse de FractaVolta devrait afficher trois entrées :

1. **Déconnexion** — réduire la dépendance EDF des usagers et bâtiments.
2. **Seconde Vie** — reconvertir centrales anciennes, hangars, friches et actifs solaires.
3. **Vignes IA** — replanter les friches de montagne en vignes capables.

Appel à action :

> Vous avez une centrale ancienne, un hangar, une friche ou un ancien vignoble ? Demandez une préqualification Seconde Vie.

---

## 12. Prochaine étape

Créer les produits déclinés :

- page offre `docs/offers/fractavolta-seconde-vie.md` ;
- page offre `docs/offers/vignes-ia-de-montagne.md` ;
- page offre `docs/offers/audit-seconde-vie.md` ;
- page web française à intégrer par l’agent de coding ;
- formulaire de préqualification ;
- issue technique d’intégration au site.

Human validation required: yes.
