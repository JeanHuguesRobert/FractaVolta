---
title: Energy packets
subtitle: From electricity as flow to energy as traceable, routable, local capacity.
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/energy-packets.md
last_stamped_at: 2026-05-20
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

## Why this matters

Local solar value is often captured or diluted:

```text
local sun -> local surface -> remote value capture -> weak local benefit
```

FractaVolta reverses that logic:

```text
local sun -> local production -> local storage -> local priority uses -> auditable benefit
```

The grid remains useful, but it is no longer the invisible default substrate. It becomes one peer, one backup path, or one arbitrage layer among others.

## Core principles

1. **Local-first value.** The territory receiving the sun should receive a visible share of its value.
2. **Storage before blind export.** Surplus should first seek useful local storage or local work.
3. **Grid as backup when useful.** The public grid remains valuable, but not as the automatic sink of every surplus.
4. **Safe interfaces.** 48 V DC is treated as a human-facing modular interface, not as a universal internal voltage constraint.
5. **Traceability.** Each packet should carry evidence: origin, amount, custody, destination, use, and uncertainty.
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
