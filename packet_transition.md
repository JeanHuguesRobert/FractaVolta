---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/packet_transition.md
last_stamped_at: 2026-05-15
---
# The Packet Transition: A Lateral Reading of Circuit Networks

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A. / FractaVolta

1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org | fractavolta.com

---

## Abstract

Every network begins as a circuit: a continuous, synchronized flow between fixed endpoints, optimized for throughput under the assumption that demand is constant and infrastructure is shared. The circuit model is rational under its founding constraints. It becomes irrational when those constraints dissolve — and yet it persists, not because it is technically superior, but because it is *unquestioned*.

This paper identifies the circuit-to-packet transition as a universal pattern in network evolution. Store-and-forward packet switching, first formalized for information networks in the 1960s and demonstrated operationally by ARPANET in 1969, has since propagated to monetary networks (Bitcoin, 2009) and is now emerging in energy networks (Energy Packet Networks, FractaVolta, 2024) and minimal habitat networks (Mariani Village, 2025). The pattern is not a metaphor. It is a structural recurrence with identifiable preconditions, predictable resistance mechanisms, and a characteristic cognitive barrier — the *unthought* — that is distinct from technical, economic, and regulatory resistance.

A taxonomy of candidate networks is proposed, classifying them by transition stage and by the type of barrier that currently prevents or delays the packet transition. The analysis suggests that the most powerful intervention against the dominant barrier — the unthought — is not a paper or a conference, but a physical demonstration that makes the packet *conceivable* to actors whose training, tools, norms, and performance metrics are built entirely around the circuit.

**Keywords:** packet switching; store-and-forward; lateral thinking; network theory; circuit networks; Energy Packet Network; FractaVolta; Mariani Village; epistemological barrier; paradigm; unthought; complexity; network evolution

---

## 1. A Debt to the Greeks

The concepts central to this paper are not new. They are 2,400 years old.

What we call *synthetic intelligence* — the capacity to recognize a structural pattern across unrelated domains and let that recognition generate new objects, protocols, and institutions — Aristotle called **phronèsis**: practical wisdom that transcends any single domain, that sees what a situation calls for and acts accordingly. Not *episteme*, the theoretical knowledge of how things work. Not *techne*, the technical mastery of how things are made. Something rarer: the capacity to move between the two, across domains, generatively.

What we call *the unthought* — the impossibility of formulating a question from inside a paradigm that has no place for it — Aristotle called **amathia**: not simple ignorance, which lacks information, but the ignorance of one's own ignorance, which lacks the very question. The actor in the grip of amathia possesses all the pieces and cannot assemble them, because the assembling thought has no foothold in their conceptual world.

What we call *the pattern* — the structural recurrence that, once seen in one domain, becomes a reading instrument for all others — Aristotle called **nous**: the capacity for direct intellectual intuition that precedes and exceeds systematic reasoning. The flash of recognition that says *this is the same as that*, before the argument that proves it.

We did not know these names when we formulated the concepts in this paper. We arrived at them independently, by observing the structure of the circuit-to-packet transition across multiple domains. We learned the Greek names afterward — and were not surprised to find them. Certain structures of human thought are real enough to be rediscovered in every epoch. The fact that they were named in Athens in the fourth century BC does not make them historical curiosities. It makes them load-bearing.

This acknowledgement is not decorative. It is a posture of humility that the subject requires. We are not inventing new concepts. We are recognizing old structures in new materials — which is, precisely, what phronèsis does, and what amathia prevents.

It seems fitting that this work originates in Corsica — a Mediterranean island whose history, language, and intellectual tradition are inseparable from the Greek and Roman worlds that first named these things. The Unconscious Grid, the Energy Packet Network, Mariani Village, and the Charte du Soleil Méditerranéen are contemporary objects. The thinking that generates them is older than electricity.

---

## 2. The Circuit as Default

Every network that has ever been built began as a circuit.

A circuit is a continuous, synchronized connection between a source and a destination. It assumes:

- that the source produces continuously;
- that the destination consumes continuously;
- that the path between them is permanent, shared, and maintained;
- that synchronization — of frequency, phase, voltage, bandwidth, or flow rate — is the fundamental technical discipline.

The circuit model is not irrational. Under its founding constraints, it is optimal. The electrical grid is a circuit because synchronous generators and passive loads made continuous flow the natural form of energy delivery. The telephone network was a circuit because voice requires real-time continuity. Water networks are circuits because gravity and pressure make continuous flow the path of least resistance.

The circuit persists, however, long after its founding constraints dissolve. It persists not because it remains optimal, but because it has become *invisible* — so deeply embedded in the infrastructure, the regulation, the training, the tools, and the mental models of practitioners that the alternative cannot be formulated from the inside.

This paper is about that alternative, and about why it is so hard to think.

---

## 3. The Packet as Pattern

The alternative to the circuit is the packet.

A packet is a discrete, addressed, self-contained unit of whatever the network carries — information, energy, money, shelter, water, care — that can be stored, routed independently, and delivered asynchronously. The packet model assumes:

- that production and consumption need not be simultaneous;
- that storage is possible and economically viable;
- that each unit can be individually addressed and tracked;
- that routing can be opportunistic, distributed, and adaptive.

The packet model was first formalized for information networks by Paul Baran at RAND Corporation in 1964 [1] and demonstrated operationally by ARPANET in 1969 [2]. Its defining insight was simple and radical:

> *A message does not need a dedicated circuit. It can be broken into pieces, each piece addressed independently, routed through whatever path is available, and reassembled at the destination.*

This insight, once seen, could not be unseen. It propagated — first through computer networking, then through telecommunications, then into monetary systems, and is now propagating into energy and habitat.

The propagation is not accidental. It follows a structural logic.

---

## 4. The Invariant Structure of the Packet Transition

Every circuit-to-packet transition, across every domain, follows the same five-step structural sequence:

### Step 1 — Discretization

The continuous flow is broken into discrete units. The unit must be:
- self-contained (it carries its own content and metadata);
- addressable (it has a unique identity);
- storable (it can wait without degrading unacceptably).

*Information*: the bit stream is broken into packets of fixed or variable size, each with a header.
*Money*: the continuous credit relationship is broken into discrete signed transactions.
*Energy*: the AC waveform is replaced by discrete battery modules with state-of-charge metadata.
*Habitat*: the fixed building is replaced by a transportable container unit with a standard connection interface.

### Step 2 — Storage

The packet waits between production and consumption. Storage is the enabling technology of every packet transition:

*Information*: RAM, disk, buffer.
*Money*: the wallet, the ledger, the vault.
*Energy*: the electrochemical cell, the battery pack, the LFP container.
*Habitat*: the ISO container on a site, awaiting occupancy.

Without affordable, reliable storage, the packet cannot exist. The history of packet transitions is therefore also the history of storage cost curves.

### Step 3 — Addressing

Each packet acquires a unique identity that allows it to be tracked, routed, and accounted for:

*Information*: IP address, packet sequence number.
*Money*: cryptographic public key, transaction hash.
*Energy*: container UUID, state-of-charge metadata, provenance certificate.
*Habitat*: container serial number, occupancy profile, site history.

### Step 4 — Routing

Packets are forwarded along available paths rather than along dedicated circuits. Routing becomes a distributed, adaptive, algorithmic problem:

*Information*: BGP, OSPF, dynamic routing tables.
*Money*: mempool, fee market, lightning network channels.
*Energy*: price signals, demand forecasts, ferry schedules, road logistics.
*Habitat*: seasonal demand, site availability, occupancy calendar.

### Step 5 — Delivery and Acknowledgement

The packet arrives, discharges its content, and confirms delivery:

*Information*: TCP ACK, HTTP 200.
*Money*: block confirmation, settlement finality.
*Energy*: battery discharged, kWh metered, custody transferred.
*Habitat*: occupant checked in, rent paid, cooperative membership activated.

This five-step structure is the invariant skeleton of every packet transition. What varies is the domain, the technology, the economics, and the resistance.

---

## 5. Completed Transitions: The Reference Cases

Two packet transitions are complete enough to serve as analytical references.

### 4.1 Information (ARPANET 1969 → Internet 2024)

The telephone network was a circuit-switched system: a dedicated physical path was established and held for the duration of each call, reserving bandwidth regardless of actual traffic. ARPANET demonstrated that information could be routed as packets without dedicated circuits. The transition took approximately thirty years from first demonstration to universal adoption.

Resistance encountered:
- **Technical**: early packet networks were slower and less reliable than circuit-switched voice for real-time applications. Solved by protocol engineering (TCP, QoS).
- **Economic**: telecommunications incumbents held circuit-switched monopolies. Solved by regulatory unbundling and internet bypass.
- **Cognitive**: the idea that a voice call could survive packet loss and reordering was genuinely inconceivable to telephony engineers trained on circuit guarantees. Solved by demonstration — once people experienced voice over IP working, the circuit assumption dissolved.

### 4.2 Money (Bitcoin 2009 → DeFi 2024)

The banking system is a circuit-switched network: money moves through correspondent relationships, clearing houses, and settlement systems that require synchronized, bilateral trust chains. Bitcoin demonstrated that monetary value could be transferred as a discrete signed packet — a transaction — without any trusted intermediary holding the circuit open.

The transition is ongoing and contested. The cognitive barrier was particularly strong: the idea that money could exist without a trusted third party was not merely unfamiliar — it was actively classified as impossible by mainstream economists and central bankers for the first decade.

---

## 6. Emerging Transitions: Energy and Habitat

### 5.1 Energy (FractaVolta, 2024)

The electrical grid is a circuit-switched system in the precise technical sense: it requires continuous synchronization of frequency (50/60 Hz), phase, and voltage across all connected generators and loads. Deviation from synchronization causes faults, cascades, and blackouts.

The Energy Packet Network (EPN) [3] proposes to replace a portion of this circuit with store-and-forward logic: electrochemical batteries are charged from renewable sources, transported physically to points of consumption, and discharged — without any continuous electrical connection between source and destination.

The technical preconditions are met:
- **Discretization**: LFP battery modules, EV packs, ISO container storage systems
- **Storage**: lithium iron phosphate cells at €80–150/kWh (2024), falling
- **Addressing**: UUID, BMS metadata, BLE and LoRa tracking
- **Routing**: ferry networks, road logistics, price signals, AI dispatch (Cogentia [4])
- **Delivery**: DC discharge at point of use, kWh metering, custody transfer

The DC-native architecture [5] is the natural electrical form of the EPN: photovoltaics generate DC, batteries store DC, electronic loads consume DC. AC becomes a boundary protocol rather than the universal substrate.

### 5.2 Habitat (Mariani Village, 2025)

The housing system is a circuit-switched network in a sociological sense: dwellings are fixed, permanently connected to urban infrastructure (electricity, water, sewage, internet), and allocated through long-term contractual relationships (ownership, lease) that assume spatial permanence.

Mariani Village [6] proposes to replace a portion of this circuit with a packet model: ISO 20-foot container units are configured as minimal self-sufficient dwellings, deployed on host sites that provide variable infrastructure (from bare land to full network connection), and repositioned annually according to seasonal demand — students in Corte during the academic year, tourists on the Corsican coast in summer.

The technical preconditions are met:
- **Discretization**: the ISO 20-foot container as the universal minimal dwelling unit
- **Storage**: the container on site, awaiting occupancy; the LFP battery, awaiting discharge
- **Addressing**: container serial number, Cogentia occupancy profile, BLE tracking
- **Routing**: annual repositioning by crane truck, site selection by seasonal demand
- **Delivery**: occupant checked in, cooperative membership activated, energy autonomy confirmed

The smallest packet in the Mariani Village system is a portable 700 Wh power station with an integrated inverter and a BLE beacon — borrowed from the shared charging station when 230V AC is needed, returned when done. The student carrying it between their unit and the station re-enacts exactly the gesture of a ferry transporting an LFP container between islands. It is the same protocol at a different scale.

---

## 7. The Taxonomy of Candidate Networks

The following matrix classifies candidate networks by transition stage and by the type of barrier currently preventing or delaying the packet transition.

### 6.1 Barrier typology

Five barrier types are identified:

| Code | Type | Description | Lifted by |
|---|---|---|---|
| B1 | Technical | Storage or discretization technology unavailable or immature | Engineering |
| B2 | Economic | Storage cost above viable threshold | Market (cost curves) |
| B3 | Regulatory | Incumbent protection, licensing, or explicit prohibition | Policy, bypass, or disruption |
| B4 | Cultural | Continuous flow is a social norm or identity marker | Education, generational change |
| B5 | Cognitive — the unthought | The packet hypothesis is not formed; the question is absent | Physical demonstration only |

**B5 — the unthought — requires special attention.**

The unthought is not ignorance. An ignorant actor lacks information. An actor in the grip of the unthought possesses all the relevant information — knows that batteries exist, that containers can be moved, that DC loads work — but cannot *assemble the hypothesis* because the circuit model occupies the entire cognitive space available for thinking about the domain.

The unthought is not incredulity. An incredulous actor has formed the hypothesis and rejected it. The actor in the grip of the unthought has never formed it. The question — *"what if we did not need the wire?"* — does not arise.

The unthought is the deepest barrier because:
- it cannot be lifted by information (the actor already has the information)
- it cannot be lifted by argument (there is no position to argue against)
- it cannot be lifted by demonstration alone (the demonstration must first make the question *conceivable*)
- it is lifted only when an actor encounters a physical reality that their existing conceptual framework cannot absorb — and is forced to generate a new one

This is what Thomas Kuhn called a paradigm shift [7], what Gaston Bachelard called an epistemological obstacle [8], and what Edward de Bono called the target of lateral thinking [9]. But none of these frameworks captures the specifically *network* form of the unthought: the impossibility of imagining a packet where only a circuit has ever been seen.

> *The most effective argument against the unthought is not a paper. It is a container you can walk into, sleep in, and charge your laptop from, powered entirely by stored sunlight, with no wire connecting it to anything.*

### 6.2 The transition matrix

| Network | Current form | Packet unit | Stage | B1 | B2 | B3 | B4 | B5 |
|---|---|---|---|---|---|---|---|---|
| Information | ~~circuit~~ | IP packet | ✅ Complete | ✅ | ✅ | ✅ | ✅ | ✅ |
| Compute | ~~local~~ | Cloud/edge instance | ✅ Complete | ✅ | ✅ | ✅ | ✅ | ✅ |
| Telecoms rural | ~~fixed~~ | LoRa / satellite packet | ✅ Complete | ✅ | ✅ | ✅ | ✅ | ✅ |
| Money | circuit → packet | Signed transaction | 🔄 In progress | ✅ | ✅ | ❌ | ⚠️ | ⚠️ |
| Energy electric | circuit | LFP container | 🔄 Emerging | ✅ | ✅ | ❌ | ⚠️ | ❌ |
| Habitat | fixed | ISO container unit | 🔄 Emerging | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Transport fret urbain | hub & spoke | autonomous micro-delivery | 🔄 Emerging | ⚠️ | ⚠️ | ❌ | ⚠️ | ⚠️ |
| Finance / credit | bank circuit | DeFi protocol | 🔄 In progress | ✅ | ✅ | ❌ | ⚠️ | ❌ |
| Eau urbaine | pipe circuit | water packet (tanker, bottle) | 💤 Latent | ✅ | ⚠️ | ❌ | ❌ | ❌ |
| Alimentation froide | supply chain | cold packet (autonomous container) | 💤 Latent | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| Santé primaire | hôpital fixe | mobile clinic packet | 💤 Latent | ⚠️ | ⚠️ | ❌ | ❌ | ❌ |
| Éducation | école fixe | MOOC / mobile classroom | 💤 Latent | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Énergie thermique | réseau chaleur | PCM thermal packet | 🔬 Speculative | ⚠️ | ❌ | ⚠️ | ❌ | ❌ |
| Eau insulaire | inexistant | drone-delivered water packet | 🔬 Speculative | ❌ | ❌ | ⚠️ | — | ❌ |
| Gaz naturel | pipeline circuit | LNG / H2 packet | 🔄 Partial | ✅ | ⚠️ | ❌ | ⚠️ | ⚠️ |

*(✅ barrier lifted, ⚠️ partially lifted, ❌ barrier active)*

### 6.3 Reading the matrix

**Networks where B5 is the last active barrier** are the closest to transition. The technical, economic, and regulatory conditions are met — only the unthought remains. Energy and habitat are in this position. A credible physical demonstration tips them.

**Networks where B3 and B5 are both active** face a double lock: political protection of circuit incumbents *and* cognitive invisibility of the packet alternative. Urban water and institutional credit are in this position. Transition requires both regulatory disruption and cognitive re-framing — a harder combination.

**Networks where B1 or B2 remain active** are genuinely immature. The packet transition cannot be forced by cognitive intervention alone; the enabling technology must first arrive. Thermal energy packets (phase-change materials at viable cost) and drone-delivered water are in this position.

**Networks where B4 is active** transition slowly even after all technical and cognitive barriers are lifted. Cultural attachment to continuous flow — the habit of turning on a tap and expecting water, the expectation of a permanent address — requires generational change, not just demonstration.

---

## 8. The Role of Lateral Thinking

Edward de Bono introduced lateral thinking in 1967 as a method for generating ideas that cannot be reached by sequential logical steps from existing premises [9]. Vertical thinking deepens the existing framework. Lateral thinking abandons it and looks for a different starting point.

The circuit-to-packet transition is a canonical object of lateral thinking because:

- The circuit model *internally generates no reason to question itself*. Within the circuit paradigm, every problem has a circuit solution: more capacity, better synchronization, smarter control.
- The packet hypothesis cannot be *derived* from circuit premises. It requires stepping outside the framework entirely and asking: *what if the continuous connection were optional?*
- Once the packet hypothesis is formed in one domain, it becomes a *lateral reading tool* for other domains. The analyst who has seen the information packet transition can *look for* the packet in energy, in habitat, in water — not because the physics is the same, but because the structural pattern is.

This is the generative power of the pattern identified in this paper. It is not a theory of physics or economics. It is a **lateral reading instrument**: once internalized, it allows practitioners to scan any circuit network and ask, systematically, *where is the packet that this circuit is suppressing?*

The question itself is the intervention. Forming the question breaks the unthought.

---

## 9. Implications for FractaVolta and Mariani Village

FractaVolta [3] and Mariani Village [6] are not primarily commercial ventures. They are, first, *demonstrations that make the packet conceivable* in domains where the unthought has held the circuit in place for more than a century.

Their strategic logic follows directly from the analysis of B5:

**A paper does not break the unthought.** An engineer who reads about energy packets may find the idea interesting, file it as speculative, and return to optimizing the grid. The circuit paradigm absorbs the paper without structural damage.

**A container breaks the unthought.** An engineer who walks into a Mariani Village unit — charges their laptop from a USB-C port powered by stored Corsican sunlight, with no wire connecting the container to any grid — cannot file the experience as speculative. The packet has become physically real. The unthought has a hole in it.

This is why the first Mariani Village container in Corte is not a pilot project in the conventional sense. It is an epistemological intervention.

And this is why the FractaVolta corpus — the papers, the GitHub repositories, the Cogentia software, the Charte du Soleil Méditerranéen — accompanies rather than precedes the physical demonstration. The papers give the experience a name, a framework, and a set of connections to other domains. But the experience comes first.

> *The theory makes the demonstration legible. The demonstration makes the theory real.*

---

## 10. Conclusion

The circuit-to-packet transition is a universal pattern in network evolution. It has completed in information and is completing in money. It is emerging in energy and habitat. It is latent in water, food cold chains, primary healthcare, and education. It is speculative in thermal energy and drone-delivered resources.

The pattern has an invariant structure: discretization, storage, addressing, routing, delivery. Its preconditions are measurable: technical maturity, storage cost, regulatory openness, cultural readiness, cognitive availability.

Its deepest barrier is the unthought — the absence of the question itself in the cognitive field of practitioners whose entire formation has been built around the circuit.

The unthought is not lifted by information, argument, or even demonstration alone. It is lifted when demonstration makes the question *unavoidable* — when the packet is not a hypothesis but a physical reality that the circuit framework cannot absorb.

FractaVolta and Mariani Village are designed, first, to be that physical reality: a battery container that stores Mediterranean sunlight, a housing container that needs no wire, a portable power station borrowed like a library book and tracked like a network packet.

They are also, secondarily, a lateral reading instrument: once the energy packet and the habitat packet are real, the analyst can turn the same reading to water, to healthcare, to cold chains, to education — and ask, in each case, *where is the unthought, and what physical demonstration would break it?*

That question is, we believe, one of the more productive questions available to network engineers, policy designers, and cooperative entrepreneurs in the Mediterranean region and beyond.

---

## References

[1] Baran, P. *On Distributed Communications*. RAND Corporation, RM-3420-PR, 1964.

[2] Leiner, B.M. et al. *A Brief History of the Internet*. ACM SIGCOMM Computer Communication Review, 39(5), 2009.

[3] Robert, J.H.N. *The Unconscious Grid: On Store-and-Forward as the Repressed Solution to Energy Sovereignty*. FractaVolta, 2024.
https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md

[4] github.com/JeanHuguesRobert/cogentia — Cogentia open-source energy routing and inference layer, MIT licence.

[5] Robert, J.H.N. *DC-Native Energy Packet Networks: How Far Can Electricity Return from Alternating Current to Direct Current?* Institut Mariani / FractaVolta, 2026.

[6] Robert, J.H.N. *Mariani Village: A Relocatable DC-Native Housing Fleet*. Institut Mariani / Dilorta, 2026.

[7] Kuhn, T.S. *The Structure of Scientific Revolutions*. University of Chicago Press, 1962.

[8] Bachelard, G. *La Formation de l'esprit scientifique*. Vrin, Paris, 1938.

[9] De Bono, E. *The Use of Lateral Thinking*. Cape, London, 1967.

[10] Nakamoto, S. *Bitcoin: A Peer-to-Peer Electronic Cash System*. 2008.
https://bitcoin.org/bitcoin.pdf

[11] Gelenbe, E. *Energy Packet Networks: ICT-Based Energy Allocation and Storage*. Proceedings of the 2nd International Workshop on GreenCom, 2012.

[12] Nardelli, P.H.J. et al. *Energy Internet via Packetized Management: Enabling Technologies and Deployment Challenges*. IEEE Access, 7, 2019.
