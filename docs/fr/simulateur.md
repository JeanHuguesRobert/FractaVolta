---
title: Simulateur FractaVolta
subtitle: Explorer les conditions économiques et logistiques d'une chaîne de buffers énergétiques mobiles en Corse.
lang: fr
description: "Simulateur exploratoire FractaVolta : topologie insulaire corse, corridors T20/T10/T50, registre officiel EDF-SEI, dimensionnement de flotte et valorisation de la flexibilité réseau."
canonical_url: https://fractavolta.com/fr/simulateur
date: "2026-09-28"
status: "prototype exploratoire territorial"
---

# Simulateur FractaVolta

Le simulateur permet d'explorer une hypothèse logistique et physique fondamentale : au lieu d'imposer à tous les producteurs de rejoindre un hub fixe ou de subir les limites d'injection du réseau électrique, **déplacer les gros buffers de stockage vers les zones où l'énergie apparaît**, puis acheminer cette énergie massifiée le long des corridors routiers vers les lieux de consommation urbains.

Le modèle compare notamment un hub central fixe (Corte), des conteneurs tampons mobiles (3 MWh) pré-positionnés le long des axes structurants, la collecte capillaire par tracteurs légers, le transport lourd massifié vers les stations de recharge rapides, différents prix payés aux producteurs, l'autonomie de conduite et la **valorisation de la flexibilité réseau**.

---

## Lancer le simulateur en ligne

👉 [**Ouvrir le simulateur interactif**](https://fracta.fractavolta.com/simulateur/)

L'application interactive est déployée en production sur l'infrastructure FractaVolta (`fracta2`, Streamlit, Plotly, OpenStreetMap). La page que vous lisez constitue la référence éditoriale, méthodologique et documentaire.

---

## 1. Topologie insulaire réelle : Corridors et Hubs urbains

Le simulateur intègre une **cartographie OpenStreetMap native** (strictement libre de tout jeton propriétaire, fidèle à la doctrine Anti-Capture) représentative de la géographie de la Corse :

* **Les 3 hubs urbains et pôles de consommation majeurs** :
  * **Bastia** (Grand Bastia / Marana-Golo)
  * **Corte** (Centre Corse, carrefour nodal insulaire)
  * **Ajaccio** (Pays Ajaccien / Mezzavia)
  * *(auquel s'ajoute **Porto-Vecchio** pour mailler l'extrême sud)*
* **Les 3 corridors de transport routier structurants** :
  * **T20 (Axe central)** : Ajaccio ➔ Mezzavia ➔ Bocognano ➔ Col de Vizzavona ➔ Vivario ➔ Venaco ➔ Corte ➔ Ponte-Leccia ➔ Casamozza ➔ Bastia.
  * **T10 (Plaine Orientale)** : Casamozza ➔ Folelli ➔ Moriani ➔ Aléria ➔ Ghisonaccia ➔ Solenzara ➔ Sainte-Lucie ➔ Porto-Vecchio.
  * **T50 (Transversale Tavignano)** : Corte ➔ Erbajolo ➔ Cateraggio / Aléria.
* **4 positions de buffers mobiles régionaux (conteneurs 3 MWh)** :
  * Casamozza (Grand Bastia / jonction T20-T10)
  * Mezzavia (Pays Ajaccien)
  * Corte (Centre Corse)
  * Cateraggio / Aléria (Plaine Orientale)

Les distances sont calculées en coordonnées géodésiques réelles corrigées du facteur de sinuosité du relief corse (1,30x), reflétant le kilométrage routier réel (ex. 65 km entre Corte et Bastia, 72 km entre Corte et Ajaccio).

---

## 2. Le Registre officiel des producteurs solaires (ODRÉ / EDF-SEI)

Le simulateur intègre les données officielles consolidées du **Registre national des installations de production d'électricité** (ODRÉ / EDF-SEI au 31 décembre 2023) pour la Corse :

* **742 installations solaires en service**, totalisant **233,1 MWc** de puissance installée (154,6 MWc en grandes centrales HTA au sol et 78,4 MWc en toitures et hangars agricoles BT).
* **Le mur contractuel de la Seconde Vie** : en Corse, les parcs solaires bénéficient historiquement d'un contrat d'Obligation d'Achat (OA) de 20 ans avec EDF. À l'issue des 20 ans, ces installations perdent leur tarif d'achat garanti :
  * **Échéance ≤ 2030 (Imminent)** : **24,1 MWc** (61 sites prioritaires, dont Piève, Casalta, Corte, etc.) ;
  * **Échéance 2031–2035 (Court terme)** : **99,9 MWc** (145 sites, dont 33 grandes centrales HTA) ;
  * **Potentiel Seconde Vie d'ici 2035** : **124,1 MWc**, soit **53,2 % de l'ensemble du parc solaire corse** qui sortira des contrats garantis dans les dix prochaines années.

Dans l'onglet dédié du simulateur, un explorateur interactif permet de filtrer ces 742 installations par commune, niveau de tension (`HTA` vs `BT`), horizon de fin d'OA et bassin territorial, avec export CSV complet.

---

## 3. Simulation à l'échelle macro & Dimensionnement de flotte

Grâce au pont direct entre le registre et le moteur de modélisation, le simulateur ne se limite plus aux 12 sites pilotes témoins du MVP (4,5 MWh/j) : l'utilisateur peut choisir de **simuler tout le parc Seconde Vie imminent (24 MWc, ~89 MWh/j)**, l'horizon 2035 (124 MWc), ou une sélection filtrée sur-mesure.

Le simulateur calcule automatiquement :
* **Le nombre de conteneurs 3 MWh requis** : ex. 2 conteneurs pour le MVP témoin, **30 conteneurs** pour absorber la production journalière des 61 sites de la vague 2030 ;
* **La flotte de tracteurs lourds** : rotations de semi-remorques conteneurs le long des corridors T20/T10/T50 vers les bornes urbaines ;
* **La flotte de tracteurs légers** : rotations capillaires en paquets de 150 kWh depuis les petites toitures agricoles vers les buffers régionaux ;
* **La distinction physique HTA / BT** : les grandes centrales au sol (> 1 MW) hébergent directement les conteneurs 3 MWh sur site (0 km tracteur léger), alors que les toitures diffuses bénéficient de la collecte capillaire ;
* **Les émissions de CO₂ fossile évitées** : tonnes de CO₂ évitées chaque année par rapport au carburant diesel ou au mix thermique insulaire (~0,70 kg CO₂ / kWh décarboné).

---

## 4. Pourquoi EDF-SEI devrait rémunérer cette flexibilité ?

En Corse (Zone Non Interconnectée - ZNI), le système électrique souffre d'une asymétrie quotidienne structurelle :

### A. L'écrêtement solaire à midi (Énergie fatale)
Aux heures de pointe d'ensoleillement (11h–15h), la production photovoltaïque dépasse la capacité d'absorption instantanée du réseau insulaire. Pour préserver la stabilité de fréquence, le code de l'énergie et la PPE fixent un plafond de pénétration instantanée des EnR intermittentes (35 %). Faute de stockage, EDF-SEI doit **brider ou déconnecter les centrales solaires**. Cette énergie propre est **purement perdue**.

### B. La pointe du soir aux hydrocarbures (Centrales de Lucciana et du Vazzio)
Entre 18h et 22h, la demande d'électricité explose (recharges de véhicules, vie quotidienne) alors que le soleil est couché. EDF-SEI doit compenser en démarrant les moteurs thermiques de **Lucciana** (Bastia) et du **Vazzio** (Ajaccio), brûlant du fioul lourd et du fioul léger importés par bateau.
Le coût marginal de combustible fossile de ces centrales atteint **0,18 € à 0,35 €/kWh**, un surcoût lourdement compensé par la solidarité nationale via les Charges de Service Public de l'Énergie (CSPE).

### C. Le report de charge opéré par FractaVolta
En capturant l'énergie fatale de midi dans ses conteneurs mobiles (3 MWh) pour la restituer le soir aux bornes urbaines, FractaVolta :
1. **Évite l'écrêtement solaire** : réinjection d'énergie décarbonée à coût marginal quasi nul ;
2. **Évite des millions de litres de fioul importé** : à l'échelle des 61 sites de 2030, FractaVolta évite à EDF-SEI de brûler plus de **2,9 millions de litres de fioul par an** (~5,3 M€/an d'économies de combustible fossile) ;
3. **Justifie une prime de flexibilité** : si l'opérateur de réseau rémunère ce service d'effacement et de réserve à hauteur de **0,04 €/kWh**, cela ne représente qu'une petite fraction de l'économie de fioul réalisée par EDF (0,18 €/kWh évités), tout en consolidant durablement la rentabilité du réseau mobile (+1,1 M€/an de recettes pour la flotte).

Le simulateur permet de tester directement l'impact de ce taux d'écrêtement évité (0 à 50 %), du coût du fioul économisé et du montant de la prime de flexibilité.

---

## 5. Gain usager : passer du thermique à l'électrique

Le modèle compare la dépense en carburant d'un véhicule thermique à celle d'un véhicule électrique alimenté aux bornes FractaVolta, selon trois profils modifiables :
* **Petit rouleur** (500 km/mois)
* **Rouleur moyen** (1 000 km/mois)
* **Gros rouleur** (2 000 km/mois)

Le calcul s'affiche en économie mensuelle et annuelle, isolant le gain strictement lié à l'énergie pour rouler (hors coût d'acquisition ou assurance).

---

## 6. Tracteurs génériques et conduite autonome

* **Classes génériques** : le simulateur distingue la contrainte physique de tractage en kilogrammes (ex. 1 500 kg pour un tracteur léger, 30 000 kg pour un tracteur lourd) de la charge utile en kWh.
* **Autonomie de conduite (0 à 100 %)** : ce paramètre prospectif réduit le coût de la main-d'œuvre de conduite (la manutention restant humaine). Il illustre une propriété clé de FractaVolta : **plus le transport devient autonome, plus la multiplication de petits paquets énergétiques distribués devient économiquement compétitive**.

---

## Liens et ressources

* [Simulateur en direct](https://fracta.fractavolta.com/simulateur/)
* [FractaVolta Seconde Vie](./seconde-vie)
* [Seconde Vie Logistique](./seconde-vie-logistique)
* [Marchés locaux](./marches)
* [Code source et modèles sur GitHub](https://github.com/JeanHuguesRobert/FractaVolta)
