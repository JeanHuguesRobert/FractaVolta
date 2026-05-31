---
title: Rossignol Node
subtitle: Un nœud pastoral minimal pour tester l’énergie-paquet sur le terrain.
description: "Rossignol Node : prototype minimal en Corse (abreuvoir automatisé + météo) démontrant la chaîne complète source locale → stockage → usage utile → mesure → traçabilité."
canonical_url: https://fractavolta.com/fr/rossignol-node
last_stamped_at: 2026-05-20
date: "2026-05-20"
status: "draft — auto-filled (frontmatter cleanup)"
---

# Rossignol Node

**Rossignol Node** est un prototype minimal : un abreuvoir automatisé pour Rossignol, colocalisé avec une station météo et alimenté par une petite chaîne énergétique mesurable.

Ce prototype n’a pas pour but de démontrer une puissance industrielle.

Il démontre une structure :

```text
source locale
  -> stockage local
  -> usage utile
  -> contexte mesuré
  -> action automatisée
  -> journalisation
  -> paquet d’énergie
```

## Pourquoi un abreuvoir ?

Parce qu’un abreuvoir est un service local très concret : il doit fournir de l’eau, de manière fiable, dans un contexte météo réel, avec une énergie disponible localement.

C’est une bonne preuve fractale de FractaVolta : petite échelle, mais même logique que pour un hangar, une ombrière ou une commune.

## Chaîne minimale

```text
panneau solaire
  -> contrôleur de charge
  -> batterie locale
  -> capteurs d’eau
  -> pompe ou électrovanne
  -> station météo
  -> microcontrôleur
  -> journal local
```

## Données utiles

- production solaire ;
- état de la batterie ;
- consommation de la pompe ou vanne ;
- niveau d’eau ;
- température ;
- pluie ;
- vent ;
- événements d’ouverture / fermeture ;
- défauts ou alertes.

## Paquets produits

Le nœud peut produire plusieurs types de paquets :

- paquet d’énergie ;
- événement de consommation ;
- paquet de contexte météo ;
- paquet d’action ;
- alerte.

Exemple simplifié :

```json
{
  "type": "energy_packet",
  "source": "PV-ROSSIGNOL-01",
  "amount_wh": 12.4,
  "stored_in": "BATTERY-ROSSIGNOL-01",
  "used_by": "WATER-PUMP-01",
  "purpose": "abreuvoir refill"
}
```

## Rôle dans FractaVolta

Rossignol Node est un premier nœud local réel.

Il permet de tester :

- la mesure ;
- la journalisation ;
- la logique de paquets ;
- l’orchestration ;
- les alertes ;
- la relation entre énergie, météo, service rendu et action.

## Formule

**Ce qui fonctionne pour un abreuvoir peut s’agrandir vers une exploitation, une commune, puis un réseau de paquets d’énergie.**
