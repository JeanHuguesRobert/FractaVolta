---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/generalized_packet_networks.md
last_stamped_at: 2026-05-22
---

# Generalized Packet Networks

## A Framework for Heterogeneous Packets, Resource Occupancy, and Cross-Domain Operational Recurrence

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A. / FractaVolta

1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org | fractavolta.com

*Working paper — v0.2 — May 2026*
*License: CC BY-SA 4.0*
*Repository: github.com/JeanHuguesRobert/FractaVolta*

---

## Abstract

Many contemporary systems are described as networks: communication networks, electrical grids, transport systems, logistics chains, social and influence networks, monetary networks, computational infrastructures, and governance structures. These systems differ radically in their physical substrate, institutional rules, and temporal constraints. Yet they often share a common operational grammar: discrete units circulate, occupy limited resources, wait, degrade, are routed, transformed, lost, prioritized, replicated, cached, buffered, or delivered.

This paper proposes the **Generalized Packet Network (GPN)** as a cross-domain analytical framework. A packet is defined as a bounded unit of operational usefulness that occupies constrained resources. A network is defined as a structure that stores, routes, transforms, delays, amplifies, or governs packets. The framework formalizes recurring abstractions — *resource occupancy, congestion elasticity, packet decay and freshness, hot/cold storage gradients, buffer–cache hierarchies, backbone/last-mile decomposition, mesh resilience* — as a *family of operational questions* that apply across heterogeneous domains while preserving substrate-specific constraints.

The framework is positioned with deliberate epistemic discipline. It claims operational recurrence as an *observation*; it does not claim physical identity between heat, information, money, votes, and influence. It distinguishes the theoretical framework (GPN) from its infrastructural instance (Fractanet). It disambiguates its terminology from Gelenbe's *Cognitive Packet Network* (a routing protocol for communication networks) and from the corpus paper on cognitive packets (a continuation-payload format for human–AI cooperation).

Minimal mathematical formulations are provided for resource occupancy (Erlang form), congestion elasticity, and exponential packet decay. The framework is offered as a vocabulary and a research programme, not as a finished theory.

---

## Keywords

Generalized Packet Networks; Fractanet; packet switching; network science; resource occupancy; Erlang; traffic intensity; congestion elasticity; cache hierarchy; buffers; hot data; cold data; logistics; energy packets; thermal packets; inference packets; cognitive packets; social networks; governance; mandates; mesh networks; Seconde méthode.

---

## 1. Introduction

### 1.1 Networks studied through packets

The word *network* is used across many domains. We speak of computer networks, electrical networks, road networks, logistics networks, social networks, influence networks, monetary networks, political networks, neural networks, institutional networks, and ecological networks.

This semantic breadth is not accidental. A network is a general form for organizing relations, flows, dependencies, routes, capacities, and propagation. The concept is often treated structurally, as a set of nodes and links — a graph [1, 2]. That view is necessary but incomplete.

A network does not merely exist. It *operates*.

What makes a network operational is what circulates through it or is addressed within it: data packets, energy packets, thermal packets, parcels, vehicles, money, signals, alerts, posts, inference requests, continuations, votes, mandates, permissions, responsibilities.

This paper proposes to study networks through the packets that activate them, and packets through the networks that make them meaningful. The central thesis:

> The network gives topology. The packet gives operation.

Without packets, a network is a latent structure. Without a network, a packet is an isolated object. Packet and network are mutually defining abstractions.

### 1.2 Packet/network duality

A network can be introduced through its packets. A packet can be introduced through its network.

*From packet to network.* Start with a concrete packet — an insulated bottle of hot water, a data packet, a battery module, a parcel, an AI prompt, a payment, a vote, a mandate — and ask: Where does it come from? Where does it go? What resource does it occupy? How long does it occupy it? Who or what routes it? What can delay it? What can degrade it? What gives it priority? What makes it valid? What makes it useful at delivery? From the packet, the network appears.

*From network to packet.* Start with a network — a road network, the Internet, a district heating system, a social network, an administrative institution, a supply chain, a monetary system, a distributed AI infrastructure — and ask: What actually circulates? What is the minimal unit of operation? What is stored, routed, amplified, delayed, lost, transformed, or governed? From the network, the packet appears.

The dual formulation:

> A packet reveals the network through the resources it occupies, the routes it follows, and the transformations it undergoes. A network reveals its packets by making explicit what is transported, delayed, lost, amplified, transformed, or governed.

This duality is the foundation of GPN.

### 1.3 Research gap and contribution

Each discipline that touches networks has produced powerful tools. Graph theory and network science have characterized topology, centrality, robustness, scale-free distributions, small-world properties, and communities [1, 2, 3, 4]. Teletraffic engineering and queueing theory have formalized arrival processes, holding times, blocking, and waiting [5, 6, 7]. Computer architecture has developed memory hierarchies, caches, buffers, prefetching, and eviction policies [8]. Logistics has matured around hub-and-spoke, last-mile, inventory, and routing optimization. Energy systems theory has integrated grid topology, storage, exergy, and load factor. Social network analysis has studied influence, propagation, weak ties, and contagion [9, 10, 11]. Network economics has formalized network effects and standardization. Governance theory has analyzed mandates, legitimacy, accountability, and revocation.

Two specific lineages have proposed *packet* abstractions outside data networking. Gelenbe's Energy Packet Networks (EPN) treat electrical energy as routable discrete units between distributed renewable sources and points of use [12, 13]. The Packetized Energy Management program (ARPA-E NODES) has developed control-theoretic implementations [14, 15]. The packet transition has also been observed in monetary networks [16] and habitat networks [17].

To our knowledge, however, no existing framework proposes:

1. a **unified cross-domain definition** of a generalized packet that holds across information, energy, heat, matter, inference, cognition, value, attention, and mandate;
2. an explicit **mapping of service-metric vocabulary** — Erlang-form occupancy, congestion elasticity, packet decay, freshness, storage hierarchy, backbone/last-mile, mesh resilience — across these substrates while preserving substrate-specific constraints;
3. an explicit **separation between the theoretical framework (GPN) and its infrastructural instance (Fractanet)**, allowing each to be evaluated on its own terms;
4. a **disciplined scope statement** that distinguishes operational recurrence (a defensible observation) from physical identity (an indefensible claim) and from political prescription (a separate normative question).

These four contributions define the scope of the present paper. The framework is a *vocabulary and a programme*, not a finished theory.

### 1.4 Methodological status

This paper is published as a working draft under the *Seconde méthode* [18]. Claims are versioned. Objections are first-class contributions. The corpus is the evidence.

v0.1 was an intuitive exposition. v0.2 adds disclosures, a "what this paper does not claim" section, explicit naming clarifications (§2), a research gap statement (§1.3), minimal mathematical formulations for the core metrics, scope statements on social and governance packets (§§6.5, 6.6), the GPN/Fractanet separation (§7), an enriched scientific positioning (§8), and a claim manifest (§11).

### 1.5 What this paper does not claim

Precision requires explicit non-claims. The reader is asked to hold these throughout.

**This paper does not claim** that all packets are physically equivalent. They are not. Heat dissipates by Newtonian cooling; information bits do not. A battery self-discharges; a database row does not. A vote expires when its mandate ends; a parcel arrives whenever logistics deliver it.

**This paper does not claim** that information, heat, money, votes, and social influence obey the same laws. They obey different laws. The framework claims that the *operational questions one asks of them are structurally similar*, not that the answers are identical.

**This paper does not claim** that network metaphors are sufficient for technical design. They are not. A thermal engineer needs heat-transfer physics; a network engineer needs queueing theory; a political theorist needs an account of legitimacy. GPN provides a shared *vocabulary*, not a substitute for domain expertise.

**This paper does not claim** that all systems *should* be packetized. Some should not. Continuous flow is optimal where its founding conditions hold [19]. The framework helps identify *when* the circuit-to-packet transition becomes rational; it does not assert that the transition is always desirable.

**This paper does not claim** to justify any particular political form. Treating votes and mandates as packets does not by itself argue for direct democracy, liquid democracy, representative democracy, or technocracy. It clarifies *what is being delegated, traced, revoked, or aggregated*. The normative choice is separate.

**This paper does not claim** a predictive model of viral propagation, market manipulation, or political contagion. The social-packet section (§6.5) introduces vocabulary for analysis; it does not provide a forecasting tool.

**This paper does not claim** that universality erases specificity. It claims that comparison becomes possible when constraints are preserved. The abstraction is useful only insofar as it disciplines itself.

### 1.6 Two disclosures

**On the author's formation.** The author's training is in computer science [20, 21]. The computer scientist sees discrete state transitions everywhere. This may be a sensitivity that detects real architectural recurrences across substrates, or it may be a projection bias of one discipline's habits onto reality. The argument for the former is the convergence noted in [22] — physicists, biologists, linguists, and economists, with no shared formation, independently arrived at discrete structures as fundamental in their domains. The argument for the latter is that confirmation bias is precisely what one would expect from a computer-trained eye. The bias is declared. The reader weighs accordingly.

**On the author's interests.** FractaVolta, Mariani Village, and related projects — referenced in this paper as instances — are projects in which the author holds direct commercial and institutional interests [23]. The conflict is not hidden. The theoretical framework should be evaluated independently of its commercial applications. The empirical instances are offered as observable, measurable cases — not as proof of the theoretical claim.

---

## 2. Naming Clarifications

Three terminologically close concepts coexist in the broader literature and in this corpus. They must be distinguished before the framework is developed.

### 2.1 Gelenbe's Cognitive Packet Network (CPN)

E. Gelenbe and collaborators introduced the **Cognitive Packet Network** in 2001 as a routing protocol for communication networks [24]. In CPN, smart packets traverse the network, collect performance information, and use reinforcement learning (in particular neural networks called Random Neural Networks) to adapt routing decisions to changing conditions. The "cognitive" in CPN refers to *the packets themselves having adaptive routing intelligence*, not to cognition in the human or AI-agent sense.

Gelenbe also developed the related **Energy Packet Network (EPN)** [12, 13], which the present corpus builds upon.

CPN is a specific, published, well-defined networking protocol. It is *not* what this paper or any other paper in the present corpus means by "cognitive packets" or "generalized packets."

### 2.2 Cognitive packets in the present corpus

The corpus paper *Cognitive Packets: A Minimal Continuation Payload for Human–AI and Multi-Agent Cooperation* [25] introduces "cognitive packets" as a structured unit of cognitive work — context, decisions, assumptions, constraints, provenance, next action — sufficient to enable a task to be reliably resumed across humans, artificial agents, tools, conversations, repositories, and workflow systems. Cognitive packets in this sense are a *payload format*, not a routing protocol. They are transmitted by copy (with self-describing protocol header) or by reference.

This is unrelated to Gelenbe's CPN. The terminological proximity is regrettable but unavoidable given that both authors independently appropriated the word "cognitive" for distinct purposes.

### 2.3 Generalized packets (this paper)

In the present paper, **generalized packets** are an abstraction layer above all of the above. A generalized packet is a bounded unit of operational usefulness that occupies constrained resources (§3). Specific instances include data packets, thermal packets, energy packets, gravitational packets [26], inference packets [27], cognitive packets in the sense of [25], parcels, votes, mandates, and so on.

The relationship is hierarchical:

```text
generalized packet (abstract framework, this paper)
├── data packet (TCP/IP)
├── energy packet (EPN, Gelenbe)
├── thermal packet (TPN, [28])
├── gravitational packet (PGN, [26])
├── inference packet (IPN, [27])
├── cognitive packet (continuation payload, [25])
├── routing-intelligence packet (CPN, Gelenbe)
└── ... other instances
```

### 2.4 GPN vs. Fractanet

**Generalized Packet Networks** designate the *theoretical framework* developed in this paper.

**Fractanet** designates the *infrastructure instance* in the FractaVolta / Institut Mariani corpus: a concrete set of repositories, tools (`cogentia.js`), pilot deployments (Mariani Village, agrivoltaic pilots, datacenter pilots), and governance arrangements that instantiate GPN principles in working systems.

The two are not interchangeable. GPN can be evaluated as theory without endorsing Fractanet as infrastructure. Fractanet can be deployed without forcing all its participants to adopt the full theoretical framework. Section 7 develops the distinction.

### 2.5 Summary table

| Term | Author | Object | Status |
|---|---|---|---|
| Cognitive Packet Network (CPN) | Gelenbe et al., 2001 [24] | Routing protocol with adaptive packets | Published, established |
| Energy Packet Network (EPN) | Gelenbe, 2011–2012 [12, 13] | Electrical-energy packet routing | Published, research-stage |
| Cognitive packets (corpus) | Robert, 2026 [25] | Continuation payload for human–AI cooperation | Working paper |
| Thermal Packet Network (TPN) | Robert, 2026 [28] | Heat/cold as discrete packets | Working paper |
| Packetized Gravity Network (PGN) | Robert, 2026 [26] | Hydraulic exergy as discrete packets | Working paper |
| Inference Packet Network (IPN) | Robert, 2026 [27] | Locally executable inference with provenance | Working paper |
| Generalized Packet Network (GPN) | This paper | Cross-domain framework | Working paper, v0.2 |
| Fractanet | This corpus | Infrastructure instance of GPN principles | Operational programme |

---

## 3. Definition of a Generalized Packet

A **generalized packet** is a bounded unit of operational usefulness that occupies constrained resources in order to be stored, routed, transformed, delivered, consumed, amplified, verified, or governed.

The definition deliberately avoids reducing packets to information. A packet may contain bits, energy, heat, cold, matter, food, water, computation, context, value, trust, attention, authority, obligation, or mandate.

A generalized packet has some or all of the following properties:

| Property | Question |
|---|---|
| Content | What does it contain? |
| Carrier | What physically or institutionally holds it? |
| Origin | Where does it come from? |
| Destination | Where should it go? |
| Addressability | How is it identified or routed? |
| Capacity | How much does it contain? |
| Validity | Under what conditions is it valid? |
| Freshness | How fast does it lose usefulness? |
| Priority | How urgent or important is it? |
| Transfer interface | How does it move or change hands? |
| Resource occupancy | What does it occupy, and for how long? |
| Loss mode | How can it be lost or degraded? |
| Governance | Who is responsible for it? |

Not every packet exhibits every property. Operationally, the more of these a system can answer for its packets, the more *programmable* the system is.

---

## 4. Definition of a Generalized Packet Network

A **Generalized Packet Network** is a system in which generalized packets circulate through, or are addressed within, a topology of constrained resources.

The system may include nodes, links, buffers, caches, queues, channels, hubs, ports, protocols, vehicles, storage layers, institutions, agents, ledgers, social relays, and governance procedures.

A GPN is therefore not only a graph. It is a system of:

```text
circulation + occupation + transformation + delay + loss + amplification + governance
```

Table 1 illustrates the diversity of generalized packets and the resources they occupy.

**Table 1.** Generalized packets across domains.

| Domain | Packet | Resource occupied |
|---|---|---|
| Data | IP packet, file, message | link, router, buffer, cache |
| Storage | hot data block, archive object | cache, SSD, HDD, cold storage |
| Electricity | battery, powerbank, EV | charger, grid capacity, station |
| Heat | thermos, hot-water tank, thermal container [28] | port, exchanger, vehicle, storage |
| Cold | ice, chilled water, PCM module | cold chain, refrigerated storage |
| Gravity / hydraulic | water mass at altitude [26] | canal, reservoir, IEV node |
| Logistics | parcel, pallet, container | truck, dock, warehouse, road |
| Mobility | car, bus, train | lane, track, station, parking |
| Inference | prompt, batch, context window [27] | GPU, model, queue, memory, power |
| Cognition | continuation, structured context [25] | attention, working memory, agent state |
| Social media | post, meme, rumor | feed, attention, trust, sharing path |
| Influence | recommendation, endorsement | reputation, access, institutional channel |
| Money | payment, token, credit | account, ledger, liquidity channel |
| Governance | vote, mandate, delegation | procedure, office, representative, registry |
| Law | document, claim, authorization | court, administration, registry, deadline |

The diversity is intentional. The framework does not claim identity between these. It seeks comparable operational questions.

---

## 5. The Core Abstractions

This section develops the operational vocabulary of GPN. Each subsection introduces a concept, gives its minimal formal expression, and notes substrate-specific qualifications.

### 5.1 Resource occupancy: a generalized Erlang form

A packet matters because it occupies a resource for a finite time. A truck occupies road capacity. A data packet occupies link and buffer capacity. A hot-water tanker occupies an unloading port. A request to an AI model occupies GPU time, memory, energy, and queue position. A legal claim occupies administrative processing capacity. A mandate occupies institutional legitimacy.

The abstract measure, in Erlang form [5]:

$$
A = \lambda \cdot \bar{h}
$$

where λ is the arrival rate (packets per unit time), h̄ is the mean holding time per packet, and A is the average number of resource units continuously occupied (in Erlangs).

For c parallel servers and Poisson arrivals, the Erlang B formula gives the blocking probability:

$$
B(A, c) = \frac{A^c / c!}{\sum_{k=0}^{c} A^k / k!}
$$

Examples across domains:

```text
thermal port load     = λ_tankers · h̄_unload
GPU inference load    = λ_requests · h̄_compute
road service load     = λ_vehicles · h̄_occupancy
attention load        = λ_posts · h̄_reading
institutional load    = λ_requests · h̄_processing
```

The name "Erlang" is historically specific to telephony [5]. The underlying construct — **resource–time occupancy** — applies wherever packets arrive and occupy service resources for finite durations.

**Substrate-specific qualification.** The Poisson assumption (memoryless inter-arrival times) is often violated outside telephony. Burst arrivals, self-similar traffic [29], scheduled flows, or strategic timing all break the simple Erlang formulation. GPN inherits the construct, not the assumption.

### 5.2 Traffic intensity, saturation, congestion

Packet systems become difficult near saturation. Relevant concepts: arrival rate, service rate, queue length, waiting time, blocking probability, loss probability, throughput, utilization, saturation, priority inversion, cascading delay.

A system can appear functional at low intensity and become unstable near saturation. This applies to routers, AI inference servers, heat-delivery ports, call centers, warehouses, institutions, and social-attention markets.

> Congestion is the visible symptom of resource occupancy approaching or exceeding service capacity.

The classical queueing-theory result for an M/M/1 queue (Poisson arrivals, exponential service, one server) gives mean waiting time:

$$
W = \frac{\rho}{\mu (1 - \rho)}
$$

where ρ = λ/μ is utilization and μ is the service rate. The denominator (1 − ρ) is what diverges as load approaches capacity. The same structural divergence — near-vertical degradation past a threshold — appears in road congestion, server load, attention markets, and institutional backlogs. Substrate physics changes; the singularity does not.

### 5.3 Congestion elasticity

Average load is insufficient. Two systems can carry the same mean load and respond very differently to fluctuation.

**Congestion elasticity** generalizes economic elasticity to packet systems:

$$
\varepsilon_C = \frac{\partial C / C}{\partial A / A}
$$

where C is a congestion measure (delay, loss, cost-per-packet, quality degradation) and A is traffic intensity.

For the M/M/1 queue above, taking C = W:

$$
\varepsilon_W = \frac{1}{1 - \rho}
$$

so a system at 50 % utilization has ε ≈ 2; at 90 %, ε ≈ 10; at 99 %, ε ≈ 100. The elasticity itself diverges, which is the formal signature of a fragility threshold.

The general framing:

> Intensity measures pressure. Occupancy measures load. Elasticity measures fragility.

### 5.4 Temporal decay and freshness

Packets often degrade with time.

This is physically obvious for heat and cold [28]. Heat dissipates. Cold packets warm. Food spoils. Batteries self-discharge. But the same logic holds in information and institutions. A news item loses freshness. A market signal becomes obsolete. A weather forecast expires. A route plan becomes invalid. A compute result may become stale when context changes. A legal deadline passes. A mandate expires. An idea loses momentum when attention shifts.

A simple exponential decay model:

$$
v(t) = v_0 \cdot e^{-t/\tau}
$$

for value v and characteristic decay time τ. Substrate-specific τ values differ by many orders of magnitude:

- thermal (insulated bottle): τ ≈ hours
- thermal (building thermal mass): τ ≈ days
- battery self-discharge: τ ≈ months
- food/medical: τ varies, hours to years
- news freshness: τ ≈ hours to days
- AI context: τ depends on rate of underlying state change
- legal/mandate validity: τ ≈ statutory term

A more general framing:

$$
v_{\text{delivery}} = v_0 - \Delta_{\text{temporal}} - \Delta_{\text{routing}} - \Delta_{\text{contextual obsolescence}}
$$

Packets therefore need metadata: time of creation, time of charge, expiration, validity conditions, required delivery window, degradation curve, refresh possibility, revalidation procedure, priority under time pressure. Information networks call this **time-to-live (TTL)**.

> A packet is not only what it contains. It is what remains useful at delivery.

### 5.5 Hot, warm, cool, cold packets

Information systems classify data as hot, warm, cool, or cold by access frequency, urgency, storage cost, and retrieval latency [8]. The vocabulary generalizes carefully.

**Table 2.** Hot/warm/cool/cold across domains.

| Domain | Hot | Cold |
|---|---|---|
| Data storage | active database, cache | archive |
| Logistics | goods near user | remote dense warehouse |
| Food | hot meal delivery | frozen / cold chain |
| Social information | breaking news | historical record |
| AI | active context | archived trace |
| Governance | urgent mandate | closed historical record |
| Thermal energy | useful high-temperature heat [28] | low-grade residual heat |

Hot packets justify expensive proximity. Cold packets justify efficient remoteness. The vocabulary is not strictly metaphorical: in thermal systems "hot" is literal; in data systems "hot" is operational. The shared property is *retrieval cost as a function of position in a layered system*.

### 5.6 Buffers, caches, and memory hierarchies

Computer systems have developed powerful patterns for managing heterogeneous access [8]:

```text
registers → L1 cache → L2/L3 → main memory → SSD → HDD → cold storage → archival
```

with replication, prefetching, and eviction policies.

Two adjacent concepts deserve distinction:

- A **buffer** absorbs short-term mismatch between inflow and outflow.
- A **cache** keeps useful packets close to likely demand, reducing access time.

Many physical objects are both. A domestic hot-water tank buffers mismatch between heat production and use, and caches useful heat close to the consumer. A local warehouse buffers fluctuating demand and caches goods near customers. A neural-network KV cache (in transformer inference) buffers in-flight attention computation and caches reusable context.

**Table 3.** Buffer/cache patterns across domains.

| Computing concept | Generalized analogue |
|---|---|
| Cache | nearby stock of likely-needed packets |
| Buffer | temporary absorber of mismatch |
| Prefetch | anticipate demand before explicit request |
| Eviction | remove less useful packets from high-value proximity |
| Replication | copy packet to improve access or resilience |
| Sharding | split packet space among nodes |
| Consistency | ensure copies remain coherent |
| Write-back / write-through | propagation strategy |
| Garbage collection | remove obsolete packets |
| Compression | reduce storage cost at retrieval cost |

The point is not that society is a computer. The point is that computer science has produced reusable operational patterns for managing packets under constraints, which can be borrowed with discipline.

### 5.7 Backbone and last mile

Many networks distinguish backbone (high-capacity long-distance transport) from last mile (connection to end users under fragmented conditions).

**Table 4.** Backbone / last-mile decomposition.

| Domain | Backbone | Last mile |
|---|---|---|
| Internet | fiber, exchange points | home connection, Wi-Fi |
| Electricity | transmission grid | distribution, household wiring |
| Heat [28] | large heat source, main corridor | building tank, radiator |
| Logistics | container shipping, highways | parcel delivery |
| Food | wholesale chain | restaurant/home delivery |
| AI inference [27] | data center | user-facing agent/device |
| Social networks | mass media/platforms | interpersonal relay |
| Governance | constitutional framework | local mandate/action |

Backbone/last-mile decomposition avoids false binaries. A system may use continuous infrastructure at one layer and packet logistics at another:

```text
high-capacity backbone → local hub → packetized last mile
```

or:

```text
packetized backbone → local pipe loop → end-use cache
```

### 5.8 Topology and resilience

Topology shapes resilience, congestion, and power [1, 2].

**Table 5.** Topology trade-offs.

| Topology | Strength | Weakness |
|---|---|---|
| Linear chain | simple | fragile |
| Hub-and-spoke | efficient aggregation | hub capture or failure |
| Tree | hierarchy, clarity | branch isolation |
| Ring | alternate path | limited redundancy |
| Mesh | high resilience | coordination complexity |
| Hybrid | practical compromise | governance complexity |

Mesh is often more robust because packets can be rerouted. Mesh requires protocols, standards, local intelligence, and governance to avoid chaos — which is the operational lesson of the Internet [16, 19].

> Resilience increases when packets have alternative routes, compatible interfaces, local buffers, and enough autonomy to reroute without central failure.

### 5.9 Network effects and packet effects

Network economics has long studied **network effects**: the value of a network increases as the number of participants grows. Telephone networks, social networks, payment systems, marketplaces, open-source ecosystems, currencies, and collaborative platforms exhibit this property.

Network effects are not sufficient. A network becomes operationally powerful when its packets are standardized, routable, traceable, recombinable, and actionable. This suggests a complementary concept:

> **Packet effects**: the value created when packets become easier to create, route, verify, combine, reuse, and transform.

Examples: Git commits, issues, pull requests, and releases packetize software collaboration; standardized payments scale finance; standardized parcels and containers scale logistics; explicit mandates, votes, and delegations scale governance; transferable context packets scale multi-agent cognition [25].

```text
network effect: more nodes → more possible relations
packet effect:  better packets → more programmable operations
```

A mature system requires both.

---

## 6. Domain Instances

This section applies the framework to specific substrates. Each subsection includes a scope statement: what the framework offers, what it does not.

### 6.1 Information and computation packets

The original packet domain. Data packets in TCP/IP, files in distributed storage, messages in queueing systems, KV cache blocks in transformer inference — all are well-formalized [19, 30].

*Scope.* The framework borrows vocabulary *from* this domain rather than imposing it. The contribution of GPN here is mainly to disambiguate: when other substrates borrow "cache," "TTL," or "backbone," they should do so with explicit awareness of the source.

### 6.2 Energy, heat, and matter packets

Physical-substrate packets ground the theory. Batteries, powerbanks, electric vehicles, thermal tanks, cold packs, water bottles, fuel cylinders, containers, parcels, mobile compute modules, emergency kits.

These packets are constrained by mass, volume, energy density, transfer rate, losses, degradation, safety, distance, handling, lifecycle impact, and regulation. The constraints are not weaknesses of the abstraction; they are what *forces* the abstraction to remain operational rather than metaphorical.

Heat is not information. A thermal packet loses usefulness over time because of physical dissipation [28]. Such constraints discipline the framework.

Energy Packet Networks [12, 13] formalize the electrical case. Packetized Gravity Networks [26] formalize the hydraulic-exergy case. Thermal Packet Networks [28] formalize the heat and cold case. Together they cover three major physical substrates.

### 6.3 Inference packets

AI inference introduces new packet types [27]. An inference packet is a versioned, signed, content-addressed bundle that remains fully executable on a target runtime without external network dependencies during a declared outage window. It occupies model access, GPU or accelerator time, memory bandwidth, context window, energy, latency budget, queue position, and may carry verifiable energy provenance.

*Scope.* Inference packets are the subject of a separate paper [27]. GPN places them within a wider taxonomy without duplicating their detailed specification.

### 6.4 Cognitive packets (continuation payload)

Cognitive packets in the corpus sense [25] are structured units of cognitive work carrying enough state — context, decisions, assumptions, constraints, provenance, next action — to enable continuation across humans, artificial agents, tools, conversations, repositories, and workflow systems. They occupy attention, working memory, agent state, task continuity, interpretation capacity, and trust.

*Scope.* See [25] for the full specification. As stressed in §2, this usage is *unrelated* to Gelenbe's CPN [24].

A layered model can be sketched:

```text
prompt / context packet → inference packet → result packet → continuation packet → memory packet
```

with freshness, decay, caching, buffering, priority, routing, traceability, compression, loss, and recombination applying to each.

### 6.5 Social and influence packets — scope and limits

Social systems are networks, but their packets are less obvious. Candidate packets include messages, posts, memes, rumors, endorsements, invitations, recommendations, reputational signals, accusations, narratives, moral frames, symbolic acts, and calls to action [9, 10, 11].

These packets occupy attention and trust. They propagate through relationships, platforms, institutions, and media channels. Viral propagation can be analyzed as packet replication through a social topology. Influence networks can be analyzed as routing systems for legitimacy, access, and agenda-setting.

A social packet exhibits content, emotional charge, credibility, source identity, timing, shareability, compatibility with existing beliefs, risk of distortion, and saturation effects.

**Scope statement.** This section provides *vocabulary* for analysis, not a *predictive model* of social propagation. It does not claim:

- a quantitative theory of contagion equivalent to those in epidemiology;
- a forecasting tool for political movements or market manipulation;
- a normative justification for any platform-design choice (recommendation algorithms, content moderation, ranking).

Social packets are not neutral. They can manipulate, polarize, clarify, coordinate, or mobilize. This links packet theory to ethics and governance, not as a derivation, but as a connection that must be made *separately* with the appropriate ethical and political resources [18].

### 6.6 Governance packets — scope and limits

Governance systems also circulate packets: votes, delegations, mandates, signatures, decisions, authorizations, claims, obligations, public acts, legal documents, budget allocations, reports, minutes, complaints, appeals.

A mandate is a packet of authority. A vote is a packet of preference or decision. A public act is a packet of institutional responsibility.

This framing makes traceability central: who authorized what, under which mandate, for which duration, with what accountability, with what revocation mechanism. A governance packet *should be* explicit, attributable, time-bounded, revocable when appropriate, auditable, linked to a source of legitimacy, and resistant to capture or opacity.

The general rule:

> When authority circulates, it should circulate as a traceable packet, not as opaque influence.

**Scope statement.** This section provides *vocabulary* for analysis of governance flows and a *normative principle* (traceability). It does not claim:

- to derive any particular political form (direct democracy, liquid democracy, representative democracy, technocracy) from the packet abstraction;
- that all mandates *can* be packetized without remainder — some have irreducibly continuous or charismatic dimensions;
- that traceability alone secures legitimacy. Legitimacy requires substantive sources beyond the packet [18].

The packet framing makes certain governance pathologies *visible* (opaque mandates, untraceable delegation, expired authority still acting, captured intermediaries). It does not by itself resolve them. The political work — defended in [18, 23] — is distinct.

---

## 7. Fractanet: Infrastructure Instance

### 7.1 Why Fractanet is not GPN

A frequent source of confusion in earlier drafts of this work was the conflation of the theoretical framework with its infrastructural instance. The two must be separated:

**GPN** is a *framework*: definitions, abstractions, service metrics, scope statements. It can be applied, criticized, extended, or rejected on theoretical grounds. It does not commit anyone to building any particular system.

**Fractanet** is an *infrastructure*: a concrete set of repositories, tools, pilot deployments, and governance arrangements within the FractaVolta / Institut Mariani corpus, instantiating GPN principles in working systems.

The distinction matters for at least four reasons:

1. *Epistemic.* GPN can be wrong without Fractanet being wrong, and vice versa. A flawed framework can host useful infrastructure; a flawed deployment can coexist with a sound framework.
2. *Adoption.* Other groups may adopt GPN vocabulary without adopting Fractanet infrastructure. The conceptual contribution is severable from the institutional one.
3. *Conflict of interest.* The author has a direct interest in Fractanet (declared in §1.6). GPN as theory should be evaluated separately from Fractanet as business.
4. *Falsifiability.* Theoretical and empirical falsifications are different. GPN fails if its abstractions misrepresent operational reality across domains. Fractanet fails if its specific pilots miss measurable targets.

### 7.2 What Fractanet is

Fractanet, as currently defined in the corpus, comprises:

- *Layered substrates*: data, compute, energy (EPN [12, 13]), heat/cold (TPN [28]), hydraulic exergy (PGN [26]), matter, water, logistics, inference (IPN [27]), cognition [25], value, governance, social propagation.
- *Open repositories*: `marenostrum`, `cogentia`, `barons-Mariani`, `FractaVolta` on `github.com/JeanHuguesRobert`.
- *Tooling*: `cogentia.js` for cross-repository navigation [31], the CXU and CXU_th specifications [32, 28].
- *Pilot deployments*: Mariani Village portable AC packet [17, 28], agrivoltaic configurations, datacenter waste-heat shuttles, inference-continuity demonstrators [27].
- *Governance arrangements*: SCIC structures, fonds souverain communal frameworks, the principles articulated in [18].

A concise definition:

> Fractanet is the operational instantiation, within the FractaVolta / Institut Mariani corpus, of Generalized Packet Network principles, linking data, compute, energy, matter, cognition, value, and governance through common conventions for routing, storage, occupancy, traceability, and resilience.

The purpose of Fractanet is not to make everything identical. It is to share a vocabulary and a minimum of conventions across substrates so that interoperability and traceability are operationally achievable.

---

## 8. Scientific Positioning

GPN sits at the intersection of several established disciplines. Table 6 maps the principal contributions GPN inherits.

**Table 6.** Disciplinary lineage.

| Discipline | Contribution inherited | Reference |
|---|---|---|
| Graph theory | formal structure of nodes and edges | [1] |
| Network science | topology, centrality, scale-free, small-world | [2, 3, 4] |
| Teletraffic engineering | Erlang, blocking, waiting, resource occupancy | [5] |
| Queueing theory | arrival, service, delay, congestion | [6, 7] |
| Computer networking | packet switching, routing, buffers, TTL | [16, 19, 30] |
| Computer architecture | caches, memory hierarchy, locality | [8] |
| Logistics | hubs, last mile, routing, storage, delivery | — |
| Energy systems | grids, storage, exergy, load factor | [12, 13] |
| Thermal systems | heat/cold storage, losses, transfer rates | [33, 34] |
| Social network analysis | influence, propagation, weak ties, contagion | [9, 10, 11] |
| Network economics | network effects, standardization, elasticity | — |
| Governance theory | mandates, legitimacy, accountability, traceability | [35, 18] |
| Complex systems | thresholds, cascades, emergence, resilience | [3] |

GPN does not seek to replace any of these. It identifies a *cross-domain operational layer*: the management of heterogeneous packets under resource constraints, expressible in shared vocabulary while remaining accountable to substrate-specific constraints.

The proposed contribution, in short: each discipline already analyzes its own packets. GPN provides a shared framing that lets analyses speak across boundaries without erasing the boundaries.

---

## 9. Scope, Non-Claims, and Conditions of Failure

This paper does not claim that all packets are physically equivalent. It does not claim that information, heat, money, votes, and social influence obey the same laws. It does not claim that network metaphors are sufficient for technical design. It does not claim that all systems should be packetized.

It claims that many systems can be usefully compared by asking a recurring set of operational questions:

```text
What is the packet?
What network makes it useful?
What resources does it occupy?
How does it degrade?
How is it routed?
What delays it?
What gives it priority?
What makes it valid?
How is it traced?
What happens near saturation?
How resilient is the topology?
```

The abstraction is useful only insofar as it remains constrained by domain-specific physics, institutions, and ethics.

**Conditions of failure.** GPN fails as a framework if:

- the operational questions above turn out to be domain-specific rather than recurrent — i.e. if asking them in one domain consistently produces no useful answer in another;
- the formal expressions (§5) do not survive substrate-specific modification — i.e. if the Erlang form, congestion elasticity, or exponential decay must be replaced by entirely unrelated machinery in each domain, rather than parameterized differently;
- the scope statements (§§1.5, 6.5, 6.6, 9) prove insufficient to prevent misuse — i.e. if the framework is read as authorizing claims it explicitly disclaims (predictive social modeling, political prescription, physical identity between substrates).

The corpus is the test. v0.2 stakes the claim. Subsequent versions and external critique will determine whether it survives.

---

## 10. Research Agenda

**10.1 Formal model.** Develop a minimal model for generalized packets:

```text
packet = content + carrier + address + validity + priority + decay + interface + governance
```

with substrate-specific instantiations.

**10.2 Resource occupancy metrics.** Generalize Erlang-form resource occupancy beyond teletraffic, with explicit substrate-specific arrival-process modeling (Poisson, bursty, self-similar, scheduled, strategic).

**10.3 Load elasticity.** Formalize congestion elasticity and fragility thresholds across packet systems. Empirical work needed: measure elasticity in deployed systems (thermal logistics, AI inference clusters, governance backlogs) and test whether the analytical form (5.3) survives.

**10.4 Packet decay and freshness.** Model time-dependent usefulness in thermal, informational, social, computational, and institutional packets. Extend the exponential model (5.4) to non-exponential cases where appropriate.

**10.5 Cache and buffer analogies.** Develop disciplined cross-domain translations of caching, buffering, prefetching, eviction, replication, and consistency, with explicit limits (substrate-specific physics).

**10.6 Topology and resilience.** Compare hub-and-spoke, tree, ring, mesh, and hybrid structures across energy, data, logistics, and governance under common stress tests.

**10.7 Governance of packets.** Define traceability, responsibility, ownership, authority, and revocation for packets carrying value, mandate, or influence. Connect with [18].

**10.8 Fractanet implementation.** Explore how repositories, open standards, local hubs, AI agents, energy modules, and governance protocols instantiate GPN as a practical network of heterogeneous packets.

**10.9 Empirical case studies.** Priority cases: thermal packets [28], inference packets [27], gravitational packets [26], cognitive packets [25], governance mandates [18, 23]. Each is a working paper in the corpus and each can yield measurement targets for v0.3.

---

## 11. Claim Manifest

```yaml
paper_id: generalized_packet_networks
version: 0.2

claims:
  - id: C1
    statement: "Many systems usually studied as networks share a common operational grammar — discrete units occupying constrained resources, with routing, decay, congestion, and governance — that can be formalized as a Generalized Packet Network framework."
    status: definitional

  - id: C2
    statement: "Packet/network duality (a packet reveals its network through occupancy; a network reveals its packets through what circulates) is a productive analytical move across information, energy, heat, gravity, inference, cognition, value, and governance substrates."
    status: argued

  - id: C3
    statement: "Service-metric vocabulary — Erlang-form occupancy, congestion elasticity, exponential decay/freshness, hot-cold storage gradients, buffer-cache hierarchies, backbone/last-mile decomposition, mesh resilience — can be formally adapted across substrates while preserving substrate-specific constraints."
    status: argued

  - id: C4
    statement: "The minimal formal expressions (§5) — A = λh, ε_C = (∂C/C)/(∂A/A), v(t) = v_0 exp(-t/τ) — apply across domains via substrate-specific parameterization rather than requiring unrelated formal machinery in each domain."
    status: hypothesis

  - id: C5
    statement: "The framework should be distinguished from physical-identity claims, predictive social models, and normative political prescription. The scope statements in §§1.5, 6.5, 6.6, 9 are part of the framework, not optional."
    status: scope

  - id: C6
    statement: "GPN (theoretical framework) and Fractanet (infrastructural instance) are distinct objects. Each can be evaluated and falsified independently."
    status: terminological

  - id: C7
    statement: "Generalized packets in this paper are an abstract framework above specific instances: data packets, EPN, TPN, PGN, IPN, cognitive packets (Robert), and CPN (Gelenbe). The terminological proximities are clarified in §2."
    status: terminological

  - id: C8
    statement: "Applying GPN to social and governance packets provides vocabulary for analysis and a principle (traceability) for governance design. It does not provide a predictive model of viral propagation or a derivation of any particular political form."
    status: scope

  - id: C9
    statement: "GPN is offered as a vocabulary and a research programme, not as a finished theory. Subsequent versions will integrate corpus-wide critique and empirical case studies from the pilot deployments listed in §10.9."
    status: methodological
```

---

## 12. Conclusion

Networks are often studied through their structure. This paper has proposed to study them also through their packets.

A packet is not merely a piece of data. It is a bounded unit of operational usefulness. It may contain information, energy, heat, matter, inference, context, attention, value, or mandate. It becomes meaningful through the network that stores, routes, delays, transforms, amplifies, validates, or governs it.

The framework of Generalized Packet Networks does not erase differences between domains. It makes comparison possible while preserving constraints. Heat dissipates. Data becomes stale. Batteries self-discharge. Food spoils. Vehicles congest roads. AI requests occupy compute. Ideas occupy attention. Mandates require legitimacy.

The common grammar is not physical identity. It is *operational recurrence*:

```text
packet → resource occupancy → routing → buffering → caching → congestion → decay → priority → traceability → resilience
```

The framework supports a wider programme. Fractanet, as infrastructure instance, organizes data, compute, energy, heat, gravity, matter, cognition, value, and governance through common conventions for routing, storage, occupancy, traceability, and resilience. The corpus papers — Energy Packet Networks [12, 13], Thermal Packet Networks [28], Packetized Gravity Networks [26], Inference Packet Networks [27], cognitive packets [25], the packet transition [16, 22], the unconscious grid [36], and the Seconde méthode [18] — together populate the framework with substrate-specific cases.

The network gives topology. The packet gives operation. Their interaction gives infrastructure, power, fragility, and possibility.

Whether GPN is a useful framework will be determined by deployment, measurement, and external scrutiny. The corpus is public, versioned, falsifiable. The invitation to critique is structural, not rhetorical.

---

## References

[1] M. E. J. Newman, "The structure and function of complex networks," *SIAM Review*, vol. 45, no. 2, pp. 167–256, 2003.

[2] A.-L. Barabási and R. Albert, "Emergence of scaling in random networks," *Science*, vol. 286, no. 5439, pp. 509–512, 1999.

[3] M. E. J. Newman, *Networks: An Introduction*, Oxford University Press, 2010.

[4] D. J. Watts and S. H. Strogatz, "Collective dynamics of 'small-world' networks," *Nature*, vol. 393, pp. 440–442, 1998.

[5] V. B. Iversen, *Teletraffic Engineering Handbook*, ITU-D, 2001. The Erlang B and C formulas trace to A. K. Erlang's original 1917 work on telephone traffic.

[6] L. Kleinrock, *Queueing Systems, Volume I: Theory*, Wiley, 1975.

[7] L. Kleinrock, *Queueing Systems, Volume II: Computer Applications*, Wiley, 1976.

[8] J. L. Hennessy and D. A. Patterson, *Computer Architecture: A Quantitative Approach*, 6th ed., Morgan Kaufmann, 2017, esp. Chapters 2 and 5 on memory hierarchies.

[9] M. S. Granovetter, "The Strength of Weak Ties," *American Journal of Sociology*, vol. 78, no. 6, pp. 1360–1380, 1973.

[10] E. M. Rogers, *Diffusion of Innovations*, 5th ed., Free Press, 2003.

[11] D. J. Watts, "A simple model of global cascades on random networks," *PNAS*, vol. 99, no. 9, pp. 5766–5771, 2002.

[12] E. Gelenbe, "Energy Packet Networks: ICT based energy allocation and storage," *Lecture Notes in Computer Science*, 2011.

[13] E. Gelenbe, "Energy Packet Networks: adaptive energy management for the cloud," *Proceedings of the 2nd International Workshop on Cloud Computing Platforms*, 2012.

[14] M. R. Almassalkhi et al., "Packetized Energy Management," ARPA-E NODES program.

[15] L. A. Duffaut Espinosa, M. Almassalkhi, P. Hines, and J. Frolik, "System properties of Packetized Energy Management for aggregated diverse resources," *Power Systems Computation Conference*.

[16] P. Baran, *On Distributed Communications*, RAND Corporation, RM-3420-PR, 1964.

[17] J. H. N. Robert, *Mariani Village: Relocatable ISO-Container Habitat as Energy Packet Network Instance*, working paper, 2026.

[18] J. H. N. Robert, *Discours de la seconde méthode*, Institut Mariani, 2026. `github.com/JeanHuguesRobert/barons-Mariani`.

[19] V. G. Cerf and R. E. Kahn, "A Protocol for Packet Network Intercommunication," *IEEE Transactions on Communications*, vol. 22, no. 5, pp. 637–648, 1974.

[20] J. H. N. Robert, *Inox: A Concatenative Programming Language*. `github.com/virteal/Inox`.

[21] US Patent 7,606,221 B2, "Network communications system and method," priority 1999, J. H. Robert et al.

[22] J. H. N. Robert, *The Packet as Evolutionary Attractor: Scale-Invariant Transitions in Complex Networks*, FractaVolta working paper, 2026.

[23] J. H. N. Robert, *Barons-Mariani: A Senatorial Candidacy Programme for Haute-Corse*, Institut Mariani, 2026.

[24] E. Gelenbe, "Steps toward self-aware networks," *Communications of the ACM*, vol. 52, no. 7, pp. 66–75, 2009; and earlier: E. Gelenbe, "Cognitive Packet Network," US Patent 6,804,201, 2004 (priority 2000).

[25] J. H. N. Robert, *Cognitive Packets: A Minimal Continuation Payload for Human–AI and Multi-Agent Cooperation*, Institut Mariani working paper, 2026.

[26] J. H. N. Robert, *Packetized Gravity Networks: Distributed Hydro-Energetic Infrastructure for Resilient Renewable Integration*, FractaVolta working paper, 2026.

[27] J. H. N. Robert, *Inference Packet Networks: A Continuity Layer for Sovereign AI Infrastructure*, FractaVolta working paper, 2026. See also *From Energy Packet Networks to Inference Packet Networks*, same corpus.

[28] J. H. N. Robert, *Thermal Packet Networks: A Multi-Scale Store-and-Forward Architecture for Low-Exergy Heat and Cold Distribution*, FractaVolta working paper v0.2, 2026.

[29] W. E. Leland, M. S. Taqqu, W. Willinger, and D. V. Wilson, "On the self-similar nature of Ethernet traffic," *IEEE/ACM Transactions on Networking*, vol. 2, no. 1, pp. 1–15, 1994.

[30] D. Davies, *Proposal for a Digital Communication Network*, National Physical Laboratory, 1965–1967.

[31] J. H. N. Robert, *Cogentia: A Methodology and CLI for Cross-Repository Corpus Navigation*, MIT-licensed, 2026. `github.com/JeanHuguesRobert/cogentia`.

[32] J. H. N. Robert, *CXU Specification: The Compute eXergy Unit*, MareNostrum repository, 2026.

[33] B. Zalba, J. M. Marín, L. F. Cabeza, and H. Mehling, "Review on thermal energy storage with phase change materials," *Applied Thermal Engineering*, vol. 23, no. 3, 2003.

[34] M. Kuta, "Mobile Thermal Energy Storage — A Review and Analysis," *Energies*, 2025.

[35] E. Ostrom, *Governing the Commons: The Evolution of Institutions for Collective Action*, Cambridge University Press, 1990.

[36] J. H. N. Robert, *The Unconscious Grid: Why Infrastructure Is All You Need for AI Safety*, working paper, 2026.

---

*Comments, objections, and contributions are invited via the project repository. Each will be recorded and addressed in subsequent versions, per the Seconde méthode (Rule 2).*

*Process note: v0.1 was an intuitive exposition. v0.2 introduces methodological framing, naming clarifications (Gelenbe CPN vs. corpus cognitive packets vs. generalized packets, GPN vs. Fractanet), explicit scope statements on social and governance packets, minimal mathematical formulations, an enriched scientific positioning, a research-gap statement, and a claim manifest.*

*The next version will be better. That is the point.*
