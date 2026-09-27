---
title: Simulateur FractaVolta
subtitle: Explorer les conditions économiques et logistiques d'une chaîne de buffers énergétiques mobiles.
lang: fr
description: "Simulateur exploratoire FractaVolta : producteurs Seconde Vie, collecte légère, conteneurs mobiles, transport lourd et stations de recharge."
canonical_url: https://fractavolta.com/fr/simulateur
date: "2026-09-26"
status: "prototype exploratoire"
---

# Simulateur FractaVolta

Le simulateur permet d'explorer une hypothèse simple : au lieu d'imposer à tous les producteurs de rejoindre un hub fixe, **déplacer les gros buffers vers les zones où l'énergie apparaît**.

Le modèle compare notamment un hub fixe, des conteneurs ou buffers mobiles pré-positionnés près des producteurs, la collecte locale par utilitaires électriques, le transport lourd massifié vers les stations de recharge, différents prix payés aux producteurs et différents coûts logistiques.

## Lancer le simulateur

[**Ouvrir le simulateur interactif**](https://fracta.fractavolta.com/simulateur/)

L'application interactive est servie depuis l'infrastructure FractaVolta. La page que vous lisez reste la référence éditoriale et documentaire.

## Pourquoi ce modèle en Corse ?

En Corse, le prix des carburants dépend à la fois des marchés énergétiques mondiaux et de contraintes structurelles propres à l'île.

L'Autorité de la concurrence relève depuis plusieurs années plusieurs facteurs durables : forte dépendance des ménages à l'automobile, approvisionnement des carburants uniquement par voie maritime, acheminement routier rendu plus coûteux par le relief, forte saisonnalité de la demande liée au tourisme, capacités de stockage limitées et marché de la distribution particulièrement concentré.

Ces caractéristiques rendent le coût de la mobilité automobile particulièrement sensible à l'organisation locale de l'approvisionnement et de la distribution. L'Autorité de la concurrence a d'ailleurs de nouveau souligné en 2025 la forte concentration du secteur et l'absence, en Corse, de la pression concurrentielle exercée sur le continent par les grandes et moyennes surfaces.

L'électricité ouvre une autre chaîne de valeur : une partie de l'énergie nécessaire à la mobilité peut être produite localement, stockée, déplacée puis livrée aux véhicules.

Cela ne signifie pas que l'électricité est automatiquement moins chère. Elle exige elle aussi des investissements, du stockage, du transport, des bornes et une organisation économique viable.

Le simulateur permet donc de poser ensemble deux questions :

1. **À quel prix peut-on livrer durablement un kWh électrique au client final ?**
2. **À ce prix, combien un automobiliste économise-t-il sur son énergie en passant du thermique à l'électrique ?**

Le calcul de gain usager se limite volontairement, à ce stade, à la dépense d'énergie. Il ne compare pas encore le prix d'achat, le financement, l'entretien, l'assurance ou la valeur de revente des véhicules.

Sources institutionnelles :
- [Autorité de la concurrence — avis 20-A-11 du 17 novembre 2020](https://www.autoritedelaconcurrence.fr/fr/avis/relatif-au-niveau-de-concentration-des-marches-en-corse-et-son-impact-sur-la-concurrence)
- [Autorité de la concurrence — carburants en Corse, décision annoncée le 17 novembre 2025](https://www.autoritedelaconcurrence.fr/fr/communiques-de-presse/carburants-en-corse-lautorite-de-la-concurrence-inflige-une-sanction-de-1875)

## Ce que l'on peut modifier

Le prototype permet notamment de faire varier la taille des paquets énergétiques, l'énergie transportée par rotation légère, la capacité d'un conteneur, le rendement de la chaîne, le prix payé aux producteurs, les coûts des véhicules, le coût des cycles de batterie, les coûts de station et un **niveau prospectif d'autonomie de conduite**.

## Gain usager : thermique → électrique

Le simulateur estime aussi le gain budgétaire lié au passage d'un véhicule thermique à un véhicule électrique, en se limitant au **coût de l'énergie pour rouler**.

Trois profils de kilométrage servent de repères :

- petit rouleur ;
- rouleur moyen ;
- gros rouleur.

Le kilométrage mensuel de chaque profil reste modifiable. Le visiteur peut également modifier le prix du carburant liquide, la consommation du véhicule thermique, la consommation du véhicule électrique et le prix final du kWh.

Le résultat est affiché en économie mensuelle et annuelle. Cette comparaison ne constitue pas un calcul de coût total de possession : achat du véhicule, financement, entretien, assurance, pneumatiques, fiscalité et valeur de revente restent hors modèle pour l'instant.

## Prix client final et marge par kWh

Le simulateur permet de faire varier le **prix client final TTC par kWh**, c'est-à-dire l'équivalent du prix « à la pompe » pour une recharge électrique.

À partir de ce prix, le modèle calcule la recette hors taxe, puis la compare au coût modélisé par kWh effectivement livré au client final. Il affiche ainsi :

- la **marge contributive par kWh livré** ;
- la marge journalière correspondant au volume livré ;
- le **prix d'équilibre TTC**, c'est-à-dire le prix client auquel cette marge contributive devient nulle.

Cette mesure permet d'étudier directement la sensibilité économique du modèle au prix payé par l'usager final.

Elle ne doit cependant pas être confondue avec une rentabilité comptable complète : le prototype ne représente pas encore exhaustivement les CAPEX, le financement, les assurances, toutes les taxes spécifiques, ni le taux réel d'utilisation des véhicules, buffers et bornes.

## Deux catégories de tracteurs

Le simulateur distingue désormais deux catégories génériques :

- **tracteur léger** : véhicule de collecte locale capable de tracter une remorque ou un petit paquet énergétique ;
- **tracteur lourd** : véhicule destiné au déplacement des gros buffers et conteneurs entre zones de production et lieux de consommation.

Le Kia PV5 peut rester un exemple concret de tracteur léger, mais il n'est plus une hypothèse structurante du modèle.

Pour chaque catégorie, la **capacité de tractage en kilogrammes** est un paramètre distinct de la **quantité d'énergie transportée en kWh**. Le simulateur ne transforme pas automatiquement l'un en l'autre : cette conversion exige de connaître la masse réelle des cellules, de leur enveloppe, de la remorque et des équipements.

## Et si les véhicules deviennent autonomes ?

Une part importante du coût de la collecte locale vient aujourd'hui du temps de conduite. Le simulateur permet donc d'explorer un scénario futur dans lequel les tracteurs légers de collecte et les tracteurs lourds deviennent progressivement capables de circuler sans conducteur humain à bord.

Le paramètre **Autonomie de conduite** va de 0 à 100 %. Il réduit uniquement le coût de conduite dans le modèle. Il ne suppose pas que le chargement, le déchargement, la maintenance ou la supervision de la chaîne énergétique sont eux-mêmes automatisés.

Cette distinction est importante : le simulateur ne prédit pas une date d'arrivée de véhicules autonomes généralisés. Il permet seulement de mesurer ce que leur disponibilité changerait à l'économie du réseau.

L'hypothèse à tester est la suivante : **plus le transport devient autonome, moins la multiplication de petits trajets est pénalisante**, et plus des paquets énergétiques fins et distribués peuvent devenir intéressants. À terme, les véhicules pourraient ainsi fonctionner comme des agents physiques de Fractanet, chargés de déplacer des paquets entre producteurs, buffers et lieux de consommation.

## Ce que les résultats signifient

Les résultats servent à identifier des **zones de plausibilité** et des paramètres dominants. Ils ne constituent ni une promesse de rentabilité, ni une offre commerciale, ni une validation réglementaire, ni une spécification d'ingénierie, ni une preuve qu'un site réel est exploitable.

Les premières simulations utilisent encore des coordonnées synthétiques. L'étape suivante consiste à remplacer progressivement ces points par des sites corses réellement qualifiés : actifs [Seconde Vie](./seconde-vie), emplacements admissibles de buffers et stations de recharge.

## Hypothèse centrale

Le coût dominant peut être la collecte capillaire, pas le transport lourd.

Déplacer un conteneur de plusieurs MWh sur quelques dizaines de kilomètres peut coûter moins cher que d'imposer des kilomètres supplémentaires à de nombreux petits véhicules transportant chacun une fraction de cette énergie.

Le simulateur sert précisément à tester cette intuition au lieu de la supposer vraie.

## Liens

- [FractaVolta Seconde Vie](./seconde-vie)
- [Marchés locaux](./marches)
- [Energy packets](../energy-packets)
- [Corpus FractaVolta sur GitHub](https://github.com/JeanHuguesRobert/FractaVolta)
