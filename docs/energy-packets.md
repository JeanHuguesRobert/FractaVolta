---
title: Energy packets
subtitle: From electricity as flow to energy as traceable, routable, local capacity.
description: "FractaVolta transforme l’énergie solaire locale en paquets d’énergie mesurés, stockés, routés et tracés. Du flux continu vers des unités de capacité utiles, auditables et souveraines."
canonical_url: https://fractavolta.com/energy-packets
last_stamped_at: 2026-05-20
date: "2026-05-20"
status: "draft — auto-filled (frontmatter cleanup)"
---

## The shift

FractaVolta is a transition toward **energy packets**.

The dominant electrical model treats energy as a continuous, homogeneous flow:

```text
production -> grid -> consumption -> abstract billing
```

FractaVolta treats energy as a sequence of accountable units:

```text
source -> measurement -> storage -> routing -> use -> trace
```

An energy packet is not a labelled electron. It is a measured and attributable unit of useful energy, with a known source, path, custody history, destination, losses, and uncertainty.

## Pourquoi c’est important (et concret en Corse)

La valeur du solaire local est souvent diluée ou captée par le réseau. En transformant l’énergie en paquets traçables, on peut la stocker, l’orienter et l’utiliser localement (eau, froid, recharge, compute, services critiques).

**Applications concrètes en Corse** (vitrine terrain) :
- [Seconde Vie solaire](./fr/seconde-vie)
- [Marchés locaux](./fr/marches)
- [Pour les agriculteurs et propriétaires](./fr/agriculteurs)
- [Pour les communes et collectivités](./fr/collectivites)
- [Partenaires installateurs](./fr/installateurs)

Ces pages sont écrites pour les acteurs locaux (propriétaires, collectivités, installateurs).

Local solar value is often captured or diluted:

```text
local sun -> local surface -> remote value capture -> weak local benefit
```

FractaVolta reverses that logic:

```text
local sun -> local production -> local storage -> local priority uses -> auditable benefit
```

The grid remains useful, but it is no longer the invisible default substrate. It becomes one peer, one backup path, or one arbitrage layer among others.

## Principes concrets

1. **Priorité locale.** Le territoire qui reçoit le soleil doit en tirer un bénéfice visible et mesurable.
2. **Stocker avant d’exporter aveuglément.** L’excédent doit d’abord chercher un usage utile local (stockage, eau, froid, recharge, compute).
3. **Le réseau comme secours.** Le réseau public reste utile, mais il n’est plus l’évacuateur par défaut de tout surplus.
4. **Interfaces sûres.** Le 48V DC est conçu comme une interface modulaire et sûre pour l’humain.
5. **Traçabilité.** Chaque paquet d’énergie porte son origine, son trajet, sa destination et son usage. Rien n’est invisible.
6. **Reversibility.** Owners and territories should not be trapped by opaque or excessive exit costs.
7. **Open cognition.** Cogentia, the open-source cognitive layer of FractaVolta, applies the same packet logic to reasoning, continuations, and invention workflows.

## Generic chain

```text
local energy source
  -> sensing and provenance
  -> efficient conversion
  -> local storage
  -> routing decision
  -> safe packet interface
  -> useful local load
  -> signed consumption record
```

For solar:

```text
PV panels
  -> PV packetizer / MPPT / provenance gateway
  -> battery or mobile storage
  -> 48 V safe interface when appropriate
  -> local load / compute / EV / cold storage / water
  -> energy provenance record
```

For inference:

```text
solar packet
  -> battery custody
  -> compute energy meter
  -> inference job
  -> provenance certificate
```

## Markets

Energy packets are not limited to one asset class. They apply wherever local production risks becoming an indistinct captured flow:

- agricultural hangars reaching the end of historical contracts;
- professional rooftops;
- parking canopies;
- existing solar fields;
- public buildings;
- degraded land, quarries, and landfills;
- critical infrastructure;
- collective self-consumption systems;
- mobile batteries and EVs;
- edge compute and sovereign inference nodes.

## FractaVolta in one sentence

**FractaVolta turns local energy into local capacity: measured, stored, routed, used, and traced.**
