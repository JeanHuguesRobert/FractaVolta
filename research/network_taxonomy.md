---
title: "From Quantum to Vote"
subtitle: "A Taxonomy of Networks by Packetizability"
description: "Which networks can be packetized, tested by the substitution test rather than assumed by analogy; and why the discrete regime holds at both ends of the scale while the continuous appears only in the middle."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
email: "jhr@baronsmariani.org"
repository: "https://github.com/JeanHuguesRobert/FractaVolta"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/network_taxonomy.md"
version: "0.1"
status: "working note"
date: "2026-07-22"
last_modified_at: "2026-07-22"
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "research-note"
visibility: "public"
lifecycle_state: "working"
tags: [fractanet, packetization, cpsn, xpsn, potentics]
related:
  - "research/when_cognition_became_traffic.md"
  - "research/UNCONSCIOUS_GRID.md"
---

# From Quantum to Vote

## A Taxonomy of Networks by Packetizability

## 1. Why a taxonomy, and against what test

The claim that everything is a network, and therefore that everything can be packetized, is soft analogy. It costs nothing and predicts nothing. The corpus proposes a harder claim, and it carries a test.

> A network is packetized to the degree that its unit of traffic can carry identity, mandate, state and a return address, and survive the replacement of the node currently handling it.

That is the substitution test of *When Cognition Became Traffic*, applied outside cognition. Some networks pass it natively; some pass it partially; some fail it, and the failures are the instructive cases — they say something about the substrate rather than about our imagination. What follows is ordered by decreasing packetizability, from the literal to the contested.

## 2. The scale is discrete at both ends

Before the taxonomy, its frame.

At the bottom of the scale, packetization is not an architectural choice but a physical law. Planck's discovery of 1900 was not a particle but a granularity: action comes in quanta, never continuously. *Quantum* is *quantus* — a bounded how-much that does not divide further. At that scale the dedicated circuit does not merely perform badly, as X.25 did; it does not exist. There are only quanta that travel.

At the top of the scale sits another indivisible: one human, one vote. The quantum of sovereignty. A vote resists subdivision for the same structural reason an electron does — nobody holds 1.7 electrons, nobody holds 1.7 votes. The refusal of Section 9 of *When Cognition Became Traffic* to let compute ownership buy political weight is, in this light, a refusal to let power become continuous again: divisible, cumulative, purchasable by the fraction.

Between those two ends, the continuous appears — macroscopic fluids, grid current, uninterrupted conversation, diffuse influence. But it is an artifact of intermediate scale. Zoom in far enough, or out far enough, and the grain returns.

> The continuous is a mid-scale approximation. The discrete is the regime at both extremes.

Packetizing a network is therefore not the imposition of a foreign structure. It is the restoration of a granularity that intermediate scale had concealed. The datagram did not invent the grain of information; it recovered it.

## 3. Physical substrates — literal packetization

Where FractaNet already operates, and where the packet is a physical object.

| Substrate | The packet | Status |
|---|---|---|
| Data | datagram | the founding case (Baran, 1964) |
| Matter | letter, parcel, container | the oldest packetized substrate of all — the mandate long predates us: bill of lading, customs declaration |
| Energy | charged battery | *The Unconscious Grid*; Gelenbe's EPN at the theoretical layer |
| Water | routable volume | gravity storage, drought reserve, incident resilience |
| Compute / inference | job, model request | already routed in practice |
| Cognition | cognitive packet (CPsN) | *When Cognition Became Traffic* |

Water deserves a note, because it breaks a symmetry. Water is fungible: its packet carries no individual identity, only a use mandate (potable, irrigation, fire reserve) and a provenance. Packetizing water serves governance rather than routing — which already shows that the mandate, not the identity, is the load-bearing field.

## 4. Infrastructure — partial packetization, high information content

| Network | The packet | Where it holds, where it breaks |
|---|---|---|
| Mobility | the passenger; the ticket is mandate + destination + return | ride-hailing packetized the trip; carpooling breaks on non-fungibility — unlike water, a human does not mix |
| Voice telephony | the voice packet | done in 1999; the primal scene of this corpus |
| Supply chains | the container, with mandate central | traceability, origin certificate, cold chain; a broken link is a packet returning with its failure as payload |
| Electrical grids | the energy packet | the frontier between continuous flow and packet is precisely the corpus's originating question |

## 5. Human and social networks — contested packetization

Here the substitution test bites hardest, and the failures are more eloquent than the successes.

**Social platforms.** The post appears packetized — identity, timestamp, thread. But the platform captures it: no return address outside itself, no exportable mandate. This is the X.25 of the social. A strongly packetized social network would be a protocol, not a product — one where the message survives the replacement of its instance. Packetization becomes here a political programme, not a technical observation.

**Influence networks.** The circulating unit is the argument, or the credit of reputation. Partially packetizable: a lobbying act leaves a trace, and a transparency register is a mandate plus a provenance. The corpus already holds an instrument — Kudos, the civic recognition currency, is an attempt to packetize influence by making it traceable and imputable. The limiting case is the botnet: intelligence without mandate. A strongly packetized influence network is one where every act carries mandate, trace, imputability and revocation — the anti-capture grammar applied to soft power.

**Trust networks.** The PGP web of trust already packetized trust: a signature is a transitive packet. The trust gradient of informational gravity is its heir.

**Professional networks.** Where the contact does not survive a change of channel, the network is unpacketized. The corpus has a documented instance: a first message lost between channels for want of a traceable return address.

## 6. Abstract and structural networks — where the analogy must prove itself

**Biological neural networks.** The action potential is discrete, all-or-nothing: nature packetized the nerve signal before we did. But the unit carries neither mandate nor return address — it fails the substitution test. Instructive: a network packetized *at transport* and not *at cognition* — the exact mirror of CPN. Biological cognition is not in the spike.

**Citation and knowledge networks.** The citation is a near-perfect packet: identity (DOI), provenance, return address (the source). A corpus published in the open is a packetized knowledge network. Nanopublications have already built the brick.

**Semantic networks.** The RDF triple is the unit; packetized when each assertion carries its provenance.

**Financial networks.** The transaction is the packet; a distributed ledger is literally a packet network with immutable trace and verifiable return.

## 7. The finding

The taxonomy yields one asymmetry worth stating on its own.

> On physical substrates, packetization improves efficiency. On human substrates, it redistributes power.

Making a unit portable, traced and revocable is precisely what removes from platforms their power of capture. The political thesis of *When Cognition Became Traffic* — machines process, humans vote — and the mandate–trace–imputability–revocation grammar are therefore not an appendix to the network project. They are what packetization becomes when the substrate is us.

## 8. Non-claims

This note does **not** claim: that everything is a network; that every network should be packetized; that packetization is preferable where a stable circuit is simpler or safer; that the quantum-to-vote scale is a physical continuum rather than an ordering of substrates; that biological cognition is or is not packet-like beyond the narrow point made in Section 6; or that any taxonomy of this kind is exhaustive. It proposes a test and applies it, and the entries where the test fails are as much the content as the entries where it passes.

## Continuation

1. Whether the substitution test is the right discriminator for non-cognitive substrates, or whether each substrate needs its own.
2. Whether the mid-scale-continuity thesis of Section 2 survives contact with a physicist.
3. Nanopublications as a possible precursor of the cognitive packet applied to knowledge — to be examined.
4. Mobility as the clean case study of non-fungibility, against water as the clean case of fungibility.
5. A bullshit score, with the exact passages responsible for every point above zero.
