---
title: Simulateur FractaVolta
subtitle: Explorer les conditions économiques, logistiques et territoriales d'une chaîne de buffers énergétiques mobiles en Corse.
lang: fr
description: "Simulateur exploratoire FractaVolta : topologie insulaire corse, corridors T20/T10/T50, registre officiel EDF-SEI, dimensionnement de flotte, écrêtement et valorisation de la flexibilité réseau face aux centrales thermiques de Lucciana et du Vazzio."
canonical_url: https://fractavolta.com/fr/simulateur
date: "2026-09-28"
status: "prototype exploratoire territorial en ligne"
---

# Simulateur FractaVolta

Le simulateur permet d'explorer une hypothèse logistique, physique et économique fondamentale : au lieu d'imposer à tous les producteurs de rejoindre un hub central fixe ou de subir les contraintes d'injection du réseau électrique, **déplacer des buffers de stockage mobiles (3 MWh) vers les zones où l'énergie apparaît**, puis acheminer cette énergie massifiée le long des corridors routiers vers les hubs urbains de consommation et de recharge rapide.

Le modèle confronte en temps réel un scénario traditionnel centralisé à hub fixe (Corte) et un réseau agile de **conteneurs tampons mobiles pré-positionnés** le long des corridors structurants, en quantifiant :
* le dimensionnement de la flotte (conteneurs 3 MWh, navettes lourdes, collectes légères capillaires) ;
* le coût complet de revient au kWh livré et la marge contributive ;
* l'énergie solaire fatale sauvée de l'écrêtement méridien ;
* le combustible fossile évité aux centrales thermiques d'EDF-SEI (Lucciana et Vazzio) ;
* la prime de flexibilité réseau légitimée par ce service d'amortisseur insulaire ;
* le gain financier direct pour l'usager passant du thermique à l'électrique.

---

## Accès direct au simulateur et navigation

* 🚀 [**Lancer le simulateur interactif en ligne**](https://fracta.fractavolta.com/simulateur/)
* ☀️ [**Accueil de l'offre FractaVolta Seconde Vie**](./seconde-vie)
* 🚜 [**Espace Agriculteurs & Propriétaires de hangars**](./agriculteurs)
* 🏛️ [**Espace Communes & Collectivités corses**](./collectivites)
* 🔌 [**Espace Installateurs & Mainteneurs**](./installateurs)

> **Note d'exploitation :** L'application interactive est hébergée sur l'infrastructure de production FractaVolta (`fracta2`, Python 3.12, Streamlit 1.64, Plotly, cartographie OpenStreetMap native). Cette page constitue la documentation de référence, méthodologique et éditoriale.

---

## 1. Topologie insulaire réelle : Hubs urbains et Corridors de transport

Le simulateur intègre une **cartographie OpenStreetMap native** (strictement libre de tout jeton propriétaire, en application stricte de la doctrine *Anti-Capture*) modélisant la géographie réelle du réseau routier et énergétique corse :

* **Les 4 pôles urbains de consommation et stations de recharge rapide** :
  * **Bastia** (Grand Bastia / plaine de la Marana-Golo)
  * **Corte** (Centre Corse, carrefour nodal insulaire)
  * **Ajaccio** (Pays Ajaccien / Mezzavia)
  * **Porto-Vecchio** (Extrême Sud)
* **Les 3 corridors routiers structurants modélisés** :
  * **T20 (Axe central Nord–Sud)** : Ajaccio ➔ Mezzavia ➔ Bocognano ➔ Col de Vizzavona ➔ Vivario ➔ Venaco ➔ Corte ➔ Ponte-Leccia ➔ Casamozza ➔ Bastia.
  * **T10 (Axe littoral Plaine Orientale)** : Casamozza ➔ Folelli ➔ Moriani ➔ Aléria ➔ Ghisonaccia ➔ Solenzara ➔ Sainte-Lucie ➔ Porto-Vecchio.
  * **T50 (Axe transversal Tavignano)** : Corte ➔ Erbajolo ➔ Cateraggio / Aléria.
* **Les 4 positions stratégiques de buffers mobiles régionaux (conteneurs 3 MWh)** :
  * **Casamozza** (Nœud logistique Grand Bastia / bifurcation T20–T10)
  * **Mezzavia** (Nœud logistique Pays Ajaccien)
  * **Corte** (Plateforme logistique centrale)
  * **Cateraggio / Aléria** (Plateforme Plaine Orientale)

Les distances sont calculées en coordonnées géodésiques réelles corrigées par un coefficient de sinuosité topographique de **1,30x**, restituant fidèlement les contraintes routières insulaires (ex. 65 km routiers réels entre Corte et Bastia, 72 km entre Corte et Ajaccio).

---

## 2. Le Registre officiel des producteurs solaires (ODRÉ / EDF-SEI)

Le simulateur s'appuie directement sur les données officielles consolidées du **Registre national des installations de production d'électricité** (ODRÉ / EDF-SEI, millésime 2023) pour la Corse :

| Indicateur du parc solaire corse | Volume | Puissance cumulée |
| :--- | :---: | :---: |
| **Ensemble du parc raccordé** | **742 installations** | **233,1 MWc** |
| Grandes centrales au sol (Tension HTA > 1 MW) | 34 parcs | 154,6 MWc (66,3 %) |
| Toitures, hangars et ombrières (Tension BT) | 708 sites | 78,4 MWc (33,7 %) |

### Le mur contractuel de la Seconde Vie

En Corse, les parcs solaires bénéficient historiquement d'un contrat d'**Obligation d'Achat (OA)** d'une durée de 20 ans avec EDF. À l'échéance de ce contrat, les installations entrent en **Seconde Vie** : elles perdent leur tarif d'achat garanti et s'exposent au risque d'écrêtement massif sans indemnisation.

Le registre met en évidence le calendrier précis de sortie des contrats :

* **Vague 1 — Horizon ≤ 2030 (Sortie imminente)** : **61 installations** totalisant **24,1 MWc** (dont les parcs de Piève, Casalta, Corte, etc.) produisant environ **89 MWh/jour** ;
* **Vague 2 — Horizon 2031–2035 (Court terme)** : **145 installations** totalisant **99,9 MWc** (dont 33 parcs HTA au sol) ;
* **Potentiel Seconde Vie cumulé à 2035** : **206 installations** totalisant **124,1 MWc**, soit **53,2 % de l'ensemble de la capacité photovoltaïque de la Corse** qui sortira des mécanismes de soutien d'ici dix ans.

### L'explorateur interactif et l'injection directe

Dans l'onglet **Registre Seconde Vie EDF**, l'utilisateur dispose d'un outil de filtrage multicritères (par commune, niveau de tension `HTA` vs `BT`, horizon de fin d'OA, bassin de vie ou recherche textuelle).  
Une commande dédiée **« 🚀 Simuler cette sélection »** injecte instantanément l'échantillon filtré dans le moteur de simulation : le tableau de bord redimensionne alors la flotte et recalcule l'économie du périmètre en une fraction de seconde.

---

## 3. Guide de l'application : Les 5 onglets interactifs

L'interface du simulateur est articulée autour de 5 espaces de travail spécialisés :

### 1. Onglet « Carte de Corse »
Affiche la carte interactive OpenStreetMap avec les corridors T20/T10/T50, les hubs urbains, les buffers mobiles 3 MWh, les flux logistiques (légers et lourds) et la localisation précise de chaque centrale solaire simulée. Un sélecteur permet de basculer entre les producteurs du scénario actif, les 34 grandes centrales HTA ou l'intégralité des 742 sites insulaires.

### 2. Onglet « Registre Seconde Vie EDF »
Tableau de bord exhaustif du registre ODRÉ. Affiche la puissance totale, les indicateurs d'échéances 2030 et 2035, les filtres de recherche et permet l'export complet au format CSV (`registre_producteurs_edf_corse.csv`).

### 3. Onglet « Économie & Flexibilité »
Confronte les coûts de revient et marges entre hub fixe et buffers mobiles :
* **Tableau de synthèse financière** : coût complet, marge d'arbitrage brute, prime de flexibilité et marge bonifiée ;
* **Décomposition des coûts** : part respective de l'achat d'énergie, de la collecte légère, du transport lourd massifié et du cycle des batteries ;
* **Profil horaire journalier (Courbe 24h)** : visualisant l'absorption de l'écrêtement méridien (11h–15h) et la décharge aux bornes de recharge rapide lors de la pointe du soir (18h–23h).

### 4. Onglet « Sensibilité »
Quatre graphiques d'analyse paramétrique :
1. *Sensibilité au prix d'achat producteur* (de 0,05 à 0,20 €/kWh) ;
2. *Gain usager selon le kilométrage mensuel* (de 250 à 3 000 km/mois) ;
3. *Sensibilité au prix client final TTC à la borne* ;
4. *Sensibilité à la conduite autonome des véhicules* (de 0 % à 100 %).

### 5. Onglet « Données & Export »
Affiche les caractéristiques individuelles des producteurs modélisés (coordonnées, puissance, production journalière, tension) et propose le téléchargement des résultats complets de simulation en CSV (`fractavolta_simulation.csv`).

---

## 4. Dimensionnement de flotte : Massification HTA et Capillarité BT

Contrairement aux approches théoriques uniformes, FractaVolta distingue physiquement deux modes de collecte selon le raccordement électrique :

1. **Massification directe pour les parcs HTA (> 1 MW)** :  
   Ces parcs au sol disposent de la puissance et de l'espace requis pour charger directement des conteneurs de **3 MWh** (caisses mobiles normalisées). **Aucun kilomètre de tracteur léger** n'est nécessaire : les conteneurs sont chargés sur site puis transportés par semi-remorques routiers jusqu'aux stations urbaines.
2. **Collecte capillaire pour les toitures et hangars BT (< 250 kW)** :  
   Pour les toitures agricoles diffuses, des tracteurs légers effectuent des rotations en paquets d'énergie mobiles (150 kWh) vers le conteneur tampon 3 MWh le plus proche sur le corridor routier.

### Résultats de dimensionnement macroscopique

Pour la première vague de Seconde Vie (échéance ≤ 2030, soit 61 sites et 24,1 MWc produisant ~89 MWh/j) :
* **Stockage requis** : **30 conteneurs de 3 MWh** répartis sur les 4 nœuds corridors ;
* **Flotte lourde** : **12 à 15 tracteurs semi-remorques** assurant les navettes régulières sur la T20, la T10 et la T50 ;
* **Flotte légère** : **18 tracteurs légers** pour la collecte des toitures BT ;
* **Kilométrage évité** : le scénario à buffers mobiles réduit de **plus de 70 %** les kilomètres parcourus par rapport à un hub centralisé à Corte.

---

## 5. Pourquoi EDF-SEI devrait rémunérer cette flexibilité ?

En Corse (Zone Non Interconnectée — ZNI), le système électrique fait face à une double anomalie structurelle quotidienne :

```text
11h - 15h : Pic solaire méridien ────────> Plafond EnR 35% dépassé ───> Écrêtement (Énergie fatale perdue)
                                                                           │
                                                                           ▼ Absorbée par conteneurs FractaVolta
                                                                           │
18h - 23h : Pointe de consommation soir ──> Moteurs thermiques au fioul ──> Restitution aux bornes urbaines
                                            (Lucciana / Vazzio)            (Fioul évité, CO2 fossile évité)
```

### A. L'écrêtement solaire méridien (Énergie fatale)
Aux heures d'ensoleillement maximal (11h–15h), l'injection photovoltaïque cumulée aux autres énergies renouvelables franchit le plafond de pénétration instantanée fixé à **35 %** par le code de l'énergie (art. L. 141-5) pour préserver la stabilité de fréquence du réseau insulaire. Faute de stockage suffisant, EDF-SEI est contraint de **brider ou déconnecter les installations solaires**. Sans système mobile d'absorption, cette électricité décarbonée est **purement perdue**.

### B. La pointe du soir aux hydrocarbures importés (Lucciana et Vazzio)
Entre 18h et 23h, la demande d'électricité s'envole (recharge des véhicules, éclairage, cuisson, climatisation/chauffage) alors que la production solaire est nulle. Pour équilibrer le réseau, EDF-SEI doit faire tourner à plein régime les moteurs thermiques de ses deux centrales principales :
* la centrale de **Lucciana** (Bastia), fonctionnant au fioul lourd ;
* la centrale du **Vazzio** (Ajaccio), fonctionnant au fioul léger/gazole.

Le coût marginal du combustible fossile brûlé dans ces centrales se situe entre **0,18 € et 0,35 €/kWh**, un surcoût considérable financé par la solidarité nationale via les Charges de Service Public de l'Énergie (CSPE).

### C. La création de valeur par FractaVolta
En absorbant l'énergie fatale de midi dans ses caisses mobiles de 3 MWh pour la restituer le soir lors de la pointe de recharge urbaine, FractaVolta réalise un quadruple arbitrage :
1. **Énergie fatale sauvée** : jusqu'à **17,8 MWh/jour** d'énergie solaire préservée pour la seule vague 2030 (à 20 % d'écrêtement) ;
2. **Carburant thermique évité** : plus de **2,9 millions de litres de fioul par an** non brûlés à Lucciana et au Vazzio ;
3. **Économie directe pour EDF et la collectivité** : environ **5,3 millions d'euros par an** d'économies brutes de combustible fossile ;
4. **Légitimité de la prime de flexibilité** : si le régulateur ou EDF-SEI accorde à FractaVolta une rémunération de flexibilité de **0,04 €/kWh**, celle-ci génère **+1,1 M€/an** de recettes additionnelles pour l'opérateur mobile, tout en laissant à EDF-SEI **plus de 4,2 M€/an d'économies nettes de carburant**.

---

## 6. Gain financier pour l'usager : Thermique vs Électrique

Le simulateur calcule en temps réel l'économie réalisée par un automobiliste insulaire passant d'un véhicule thermique à un véhicule électrique rechargé sur le réseau FractaVolta :

* **Hypothèses par défaut** : carburant thermique à 2,00 €/L (conso 6,5 L/100 km = 13,00 €/100 km) vs électricité à 0,55 €/kWh TTC (conso 17 kWh/100 km = 9,35 €/100 km).
* **Économie nette** : **3,65 € économisés tous les 100 km**.

| Profil usager | Kilométrage mensuel | Économie par mois | Économie annuelle |
| :--- | :---: | :---: | :---: |
| **Petit rouleur** | 500 km/mois | **~18 €/mois** | **~219 €/an** |
| **Rouleur moyen** | 1 000 km/mois | **~37 €/mois** | **~438 €/an** |
| **Gros rouleur** | 2 000 km/mois | **~73 €/mois** | **~876 €/an** |

Ce calcul isole l'économie purement énergétique liée aux déplacements, sans spéculer sur la décote du véhicule ou les coûts d'assurance.

---

## 7. Automatisation et conduite autonome prospective

Le modèle intègre un curseur d'**autonomie de conduite des véhicules (0 % à 100 %)**.  
Ce paramètre prospectif réduit proportionnellement le coût de la main-d'œuvre de conduite (les opérations physiques de manutention et d'attelage restant manuelles).

Cette analyse met en lumière une loi économique essentielle de FractaVolta :  
> **Plus la conduite s'automatise, plus la logistique modulaire et distribuée surclasse les infrastructures fixes centralisées.**  
> Alors qu'un hub fixe est pénalisé par des flux convergents massifs et des nœuds d'engorgement, un essaim de petits tracteurs autonomes en rotations régulières abaisse le coût de revient au kWh de plus de 30 %.

---

## Liens transversaux et ressources utiles

* 🚀 [**Accéder au simulateur en direct**](https://fracta.fractavolta.com/simulateur/)
* ☀️ [**L'offre FractaVolta Seconde Vie (Présentation générale)**](./seconde-vie)
* 🚜 [**Espace Agriculteurs : valoriser hangars et toitures après 20 ans**](./agriculteurs)
* 🏛️ [**Espace Collectivités : résilience et mobilité propre sur le territoire**](./collectivites)
* 🔌 [**Espace Installateurs & Mainteneurs : bâtir la chaîne d'intervention**](./installateurs)
* 🚚 [**Détail de la logistique Seconde Vie**](./seconde-vie-logistique)
* 📊 [**Marchés prioritaires en Corse**](./marches)
* 💻 [**Dépôt GitHub du simulateur (Code source, modèles et tests)**](https://github.com/JeanHuguesRobert/FractaVolta)
