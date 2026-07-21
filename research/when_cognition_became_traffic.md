---
title: "When Cognition Became Traffic"
subtitle: "A Sequel to The Unconscious Grid"
description: "From generalized packet networks to cognitive packets: how purposeful cognitive work can leave home, follow informational gravity, survive interchangeable processors, and return with its trace."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
address: "1 cours Paoli, F-20250 Corte, Corsica, France"
email: "jhr@baronsmariani.org"
website: "https://fractavolta.com"
repository: "https://github.com/JeanHuguesRobert/FractaVolta"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/when_cognition_became_traffic.md"
sequel_of: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/UNCONSCIOUS_GRID.md"
version: "0.4"
status: "draft for adversarial review"
date: "2026-07-20"
last_modified_at: "2026-07-21"
license: "CC BY-SA 4.0"
layout: default
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
tags:
  - cognitive-packets
  - generalized-packet-networks
  - fractanet
  - cogentia
  - cop
  - ai-safety
keywords:
  - cognitive packets
  - cognitive packet networks (Gelenbe)
  - informational gravity
  - continuations
  - agent orchestration
  - distributed cognition
  - human sovereignty
  - generalized packet networks
---

# When Cognition Became Traffic

## A Sequel to *The Unconscious Grid* — On Purposeful Work as Store-and-Forward Traffic

**Jean Hugues Noël Robert, baron Mariani**
Institut Mariani / C.O.R.S.I.C.A. / FractaVolta
1 cours Paoli, F-20250 Corte, Corsica, France
jhr@baronsmariani.org

---

## Abstract

*The Unconscious Grid* argued that electrical energy already travels as discrete physical packets whenever a charged battery is carried rather than discharged through a continuously synchronized wire, and that packetization is a general transition — from continuous dedicated circuits to bounded, autonomous, store-and-forward units — that applies to matter, stored energy, computation, and other capacities. That paper mentioned cognitive packets, but treated them as one application among others, in a single clinical vignette near its end. This sequel reverses the perspective. It asks what becomes visible when cognition recognizes itself as traffic — and it observes, in the psychoanalytic sense the first paper established, that the analysis has turned upon the analyst: the inquiry that produced *The Unconscious Grid* was itself a packet journey, externalized, transported, and reconstructed across humans, models, tools, and repositories, and the paper described its own mode of production without making that fact central. The proposed unit is not a prompt, message, model invocation, task, or autonomous agent. A **cognitive packet** is a bounded and durable unit of purposeful cognitive work: it leaves a home context with a goal, a mandate, relevant state, and return conditions; it may be processed by several interchangeable humans, artificial agents, tools, or institutions; it may pause, branch, fail, or generate sub-packets; it follows gradients of relevant and admissible capability — what this paper calls **informational gravity** — and it returns home with results, artifacts, provenance, and an explicit unresolved remainder. The term has a genealogy that must be confronted rather than avoided: Gelenbe's Cognitive Packet Networks (1999) placed cognition in the *routing* while the payload remained ordinary data; this paper performs the inversion — the payload is the cognition, and the network may be as dumb as it likes. The operational boundary is the substitution test: cognitive work is packetized to the degree that another admissible processor can resume it without access to the previous processor's private state. The architectural consequence is that agents become replaceable processors rather than owners of cognitive continuity — the current agent stack being, in this reading, the X.25 of cognition: packetized in form, circuit in spirit. The political consequence is a deliberate discontinuity: artificial agents may process cognitive packets, but only living humans constitute the demos, on the basis of one human, one vote. This is a democratic commitment, not a theorem. A condensed version for artificial agents closes the document.

**Keywords:** cognitive packets; generalized packet networks; distributed cognition; continuations; agent orchestration; informational gravity; AI safety; human sovereignty; one human one vote

---

## 1. The Analyst Was the Patient

Some discoveries are difficult because their object is remote. Others are difficult because their object is too close.

*The Unconscious Grid* was built on the second kind. The battery in a mobile telephone is plainly a container of stored energy; carry the telephone from a photovoltaic charger to another location and the energy has moved without crossing a transmission line. Billions of such objects had been built before one was recognized as a packet, and their carriers as an uncoordinated network. The paper named that non-recognition a repression, traced the circuit-switched habit from Baran's 1964 memoranda through the X.25 failure of nerve to the saturated SARCO cable, and proposed the datagram for energy: autonomous battery packets, routerless physical transport, stigmergic self-organisation. Near its end, in a section on the wider family of circuit-switched patients, it devoted one clinical vignette to the cognitive grid — the session as dedicated circuit, the cognitive packet as datagram — and moved on, because energy was its visible subject.

In retrospect, the hierarchy was inverted. The energy packet was not the final discovery. It was what psychoanalysis calls a screen memory: vivid, innocent, load-bearing — remembered in place of something closer and more difficult to admit.

For the inquiry that produced *The Unconscious Grid* had itself travelled. An observation moved from a physical battery into a conversation, from a conversation into notes, from notes into a public corpus, from one artificial agent to another, through objections and revisions, and finally into an article. No single processor contained the complete journey. The author persisted; the tools changed. The working state was repeatedly externalized, transported, and reconstructed — copied out of a session before it closed, pasted into a rival provider, committed to a repository so that a later reader, human or artificial, could resume where a former one had stopped. The paper was describing its own mode of production, in the third person, about batteries.

This is deferred action in the strict Freudian sense — *Nachträglichkeit*: the meaning of the first scene is constituted only by the second. The grid was unconscious because cognition had not yet recognized itself as traffic.

The reflexive step, once taken, must be disciplined. This paper does not begin by asserting that everything is a packet, still less that thought is literally a computer network. It asks a narrower question:

> What is the smallest durable unit of purposeful cognition that can continue its journey when the person, model, process, or institution currently handling it is replaced?

If such a unit can be defined operationally, then distributed cognition need not mean a collection of agents exchanging opaque messages. It can mean a network in which cognitive work itself has identity, state, direction, and a trace.

---

## 2. Two Primal Scenes, Both Dated 1999

Every analysis returns, eventually, to a scene. This one returns to two, and they carry the same date.

### 2.1 The circuit that became a service

At the end of the 1990s, at Odisei, the author and Thierry Parmentelat were building what the industry would later call a hosted PBX — telephony as a network service, during the first practical transition to Voice over IP. The essential move was not compression. It was detachment: the voice service was separated from the dedicated telephone circuit.

In circuit-switched telephony, the call and the reserved path appeared inseparable. Packetized voice divided the signal into independently transported units, and once the bearer was no longer a dedicated circuit, everything the private branch exchange had done — routing, presence, forwarding, numbering, policy — could itself become network software. The PBX ceased to be primarily a box in a building. It became a service. The same architectural instinct produced, that year, the author's autodiscover protocol (US patent US7606221B2, priority 1999): endpoints locating distributed infrastructure autonomously, without a capturable central registry. The lesson, lived rather than read, was that the function survives the substrate once the state is made to travel.

The analogy to cognition must be handled precisely. Voice packets carry encoded samples; cognitive packets carry neither consciousness nor an intrinsic guarantee of meaning. The parallel lies in the separation, not in the cargo.

### 2.2 The packet that thought — about its route

The same year, at the other end of the same discipline, Erol Gelenbe introduced **Cognitive Packet Networks** (Gelenbe, Xu & Seref, 1999; Gelenbe, Lent & Xu, 2001). In a CPN, *smart packets* explore the network and learn routes by reinforcement, using random neural networks at each node; acknowledgement packets carry the discovered route information back; *dumb packets* then follow the learned paths, carrying the actual payload. The network's intelligence is decentralized into the traffic itself, driven by quality-of-service goals.

The term of this paper's title is therefore not free, and the debt must be stated exactly. In Gelenbe's architecture, the cognition is in the *routing*. The application payload remains ordinary data. The packet thinks about its journey; it does not think about anything else — and "thinks" is a bounded metaphor: the learning is realized jointly by the packets and the random-neural-network mailboxes of the nodes, and it aims at routing and quality of service, never at the meaning of the cargo. It was a profound inversion of the classical picture — the network dumb, the traffic smart — and it stopped, deliberately and productively, at the transport layer.

This paper performs the mirror inversion. Here the *payload* is the cognition: a bounded unit of purposeful work — a question under investigation, an objection awaiting resolution, a decision carrying its mandate — and the network may be as dumb as it likes, provided the packet's identity, state, and return address survive each hop. Gelenbe put the mind in the routing and kept the cargo dumb. We keep the routing as simple as honesty permits and put the mind in the cargo.

The symmetry is worth savouring. *The Unconscious Grid* met Gelenbe at the energy layer, through his Energy Packet Networks (2012). This sequel meets him again at the cognitive layer, through his Cognitive Packet Networks (1999) — from the opposite direction. The packetization corpus encounters the same author at both of its poles. That is not coincidence. It is what a genuinely scale-invariant principle looks like when two people approach it from different ends.

### 2.3 What both scenes teach

Packetizing voice did not eliminate speakers, telephones, codecs, or networks; it made each replaceable within a wider architecture. Packetizing routing intelligence did not eliminate the payload; it freed the payload from the pre-computed path. Packetizing cognitive work would not eliminate humans, models, agents, or institutions. It would prevent any one of them from owning continuity merely because it happens to be the current processor.

---

## 3. The Repression: The Agent as Virtual Circuit

This observation is not without antecedents, and — exactly as in the energy case — the antecedents are genuine contributions that dreamed the right dream and woke before its most radical implication.

The lineage is long. Newell (1962) already worried about how problem-solving work should be organized across components. Hewitt, Bishop and Steiger (1973) gave computing the actor model: isolated processors communicating by messages, no shared state. Blackboard systems externalized the problem state itself, so that heterogeneous specialists could contribute to a common representation. Gelernter's Linda (1985) separated coordination from process identity: tuples persist in a space, indifferent to which process wrote them and which will consume them. Workflow engines persisted steps and retries. Suchman (1987) demonstrated that plans are resources for situated action rather than programs that execute; Clark and Brennan (1991) showed that meaning is grounded incrementally between interlocutors; Hutchins (1995) established that cognition in the wild spans people, instruments, and artifacts — that the cockpit remembers its speeds. Schmidt and Simone (1996) gave CSCW its coordination mechanisms. One tradition came closer than all of these, and must be named rather than absorbed: the mobile-agent systems of the 1990s — General Magic's Telescript (White, 1994), IBM's Aglets, Agent Tcl, CNRI's Knowbot Programs. They moved purposeful programs together with execution state, itineraries and, in Telescript's case, explicit authority and permits: proto-mandates enforced at each destination (Thorn, 1997). What they made persistent, however, was the mobile program itself. The agent *was* the processor, resuming only inside a compatible runtime; replace the runtime with a human, another model, or an incompatible tool, and the journey ended. The present proposal makes the opposite object persistent — the work, separated from every processor that serves it. Each of these traditions externalized a fragment of what this paper assembles: the replaceable processor, the shared state, the coordination artifact, the travelling program, the distributed cognitive system.

None of them made *the travelling work itself* the persistent unit — a unit that carries its own purpose, mandate, and return address across all of them. The useful elements exist, scattered across five decades of literature. They have not been reorganized around the object that travels.

And the contemporary agent stack — the layer where this reorganization ought to be happening — has instead reproduced, with great sophistication, the X.25 of cognition.

Consider what a cognitive process is commonly bound to today: a chat session and its context window; a particular model or provider; an agent process holding transient state; a workflow engine with proprietary persistence; an employee's memory; an institutional procedure whose continuity depends on whoever happens to be in the room. When the session ends, the model changes, the employee leaves, or the workflow crashes, the path disappears. The systems compensate — transcripts are copied, summaries written, prompts reconstructed, state rebuilt in the next tool — and these repairs are filed under memory management. They are better understood as symptoms: evidence that the wrong object has been made persistent. The orchestration frameworks persist the *orchestrator*; the providers persist the *session*; nobody persists the work. Packets in form, circuits in spirit. The virtual circuit of 1978, rebuilt in 2026, with better marketing.

The agent is not the cognition, just as the circuit was not the conversation.

The deeper project is broader still, and it is the project of the whole corpus. FractaNet is not only a cognitive network; it is a proposed network of packetized capacities. Matter can be bounded in containers and routed through logistics. Energy can be stored in batteries and routed without continuous wires. Computation can be packaged and routed toward available execution. Inference can be routed toward models under constraints of cost, latency, provenance, and jurisdiction. Cognition can be routed toward capable processors while preserving purpose and state. Mandates and votes can be represented as traceable civic acts without conferring political personhood on the processors that carry them. Cognitive packets sit at the top of this stack because they may coordinate the layers beneath: a cognitive packet can request evidence, reserve compute, seek energy, invoke a model, delegate a subproblem to a human, and evaluate whether its own goal has been reached. But it is not the only packet in the architecture, and the general move is therefore not "packetize cognition." It is:

> Generalize packetization to capacity itself — up to cognition.

---

## 4. The Return of the Repressed: The Work as Packet

The term *cognitive packet* risks becoming an attractive metaphor attached to an ordinary task object. A useful definition must impose a boundary.

### 4.1 Definition

A **cognitive packet** is a bounded, addressable, durable, and routable unit of purposeful cognitive work whose externalized state is sufficient for an admissible processor to continue that work without access to the private state of the previous processor.

At minimum, it contains or references:

1. **Identity** — a stable packet identifier and version history.
2. **Home** — the topic, person, corpus, institution, or parent packet to which the outcome belongs.
3. **Goal** — the condition the journey is meant to advance or satisfy.
4. **Mandate** — what processors may do, what they may not do, and under whose authority.
5. **State** — relevant context, prior steps, artifacts, and known constraints.
6. **Needs** — missing evidence, capabilities, decisions, or resources.
7. **Routing policy** — admissibility rules involving confidentiality, jurisdiction, cost, latency, competence, or trust.
8. **Completion conditions** — tests that distinguish progress, acceptable completion, exhaustion, and failure.
9. **Return path** — where results and unresolved remainder must be reintegrated.
10. **Trace** — processors visited, transformations performed, evidence used, errors encountered, and decisions made.

A packet may carry some items directly and address others by content-stable reference. It need not be self-contained in the sense of duplicating an entire corpus. It must, however, remain intelligible enough to be resumed.

### 4.2 The boundary rule: substitution

Not every thought is a packet. An unarticulated sensation, a tacit skill, a fleeting association, an embodied judgment may not be externalizable without destructive loss. Even an explicit task may remain too underspecified to survive its current actor. The operational test is substitution:

> Can the current processor be replaced by another human, model, agent, or tool without changing the packet's identity and without reconstructing its purpose from an inaccessible private state?

If yes, the work is packetized to that degree. If no, it remains processor-bound. The test is not binary in practice. A packet may be resumable for a narrow operation but not for the entire judgment. The correct response is not to pretend that all state has been captured. It is to mark what remains tacit, unavailable, or dependent on a named person. The substitution test must permit the honest answer *not yet portable* — that honesty is what separates an infrastructure boundary from a metaphor.

### 4.3 Minimal example

Consider a public working paper requiring adversarial review — this one, for instance. The packet's goal is not "write text." It is:

```text
Determine whether claim C4 survives informed criticism,
identify the strongest counterexample,
and return a proposed revision or an explicit unresolved objection.
```

Its home is the paper and its claim manifest in a versioned repository. Its mandate authorizes analysis and drafting but not publication. It references the relevant section, the definitions, the cited literature, and earlier objections. It requires a reviewer competent in distributed systems. It forbids disclosure of a confidential annex. Completion requires either a cited counterexample, a reasoned finding that none was located within the search boundary, or a declaration of insufficient evidence. The packet may visit a search tool, an artificial agent, and a human reviewer, and it returns to the paper with the three contributions distinguished by provenance.

The packet is not the prompt sent to the model — that prompt is one serialization used at one hop. Nor is it the model's response. The packet persists before and after both.

### 4.4 Relation to existing objects

A cognitive packet may contain a task, but it is more than a task because it preserves origin, mandate, accumulated state, and return conditions. It may use a message, but it is more than a message because its identity survives multiple transmissions. It may trigger a compute job, but it is more than a job because semantic completion is not reducible to successful execution. It may be handled by an autonomous agent, but it is not the agent, because it must survive the agent's replacement. The traditions surveyed in Section 3 supply the parts — isolated processors, externalized state, coordination artifacts, provenance records, distributed cognitive systems. The claim here is not that those fields failed to notice distribution. It is that their useful elements can be reorganized around a stricter persistent unit: purposeful cognitive work that travels and returns.

The comparison can be made compact:

| Unit | Continuity lives in | Goal and mandate | Substitution test | Accountable return |
|---|---|---|---|---|
| Actor message | consumed on delivery | implicit in the sender | not applicable | none |
| Linda tuple | the tuple space | absent by design | anonymous by design | none |
| Blackboard entry | one shared system | shared problem state, no mandate | within that system only | no return concept |
| Task / ticket | one tracker | goal often, mandate rarely | fails across tools | rare |
| Workflow state | the engine | the workflow's, under engine policy | fails across engines | engine-internal |
| Autonomous agent | the agent process | its own | fails — the agent *is* the state | none |
| **Cognitive packet** | the packet itself | explicit and versioned | passes by definition | mandatory, with trace |

The table wrongs each tradition the way every summary does. The point is not that these objects are defective — each was right for its layer. It is that each anchors continuity somewhere other than the travelling work itself: in the delivery, the space, the system, the engine, or the agent. The cognitive packet anchors it in the work.

---

## 5. Informational Gravity

An ordinary network routes toward an address. A cognitive network often does not know the correct address in advance.

A packet may require knowledge of Corsican energy regulation, access to a GPU, experience with Byzantine fault tolerance, a witness's recollection, or a democratic decision. The name of the appropriate processor may be unknown when the packet leaves home. What is known is the shape of what is missing.

The term **informational gravity** denotes the tendency of a cognitive packet to move toward reachable sources of relevant and admissible resolution. Those sources — people, corpora, instruments, datasets, models, tools, institutions, other packets — function as informational attractors because they can make a verifiable contribution to the packet's goal.

The metaphor has limits, and they should be stated before the formalism. Physical gravity is universal and indifferent to purpose. Informational attraction is relational, policy-dependent, and partly constructed. A medical record may be highly relevant to a diagnosis but inadmissible to a processor lacking authorization. A famous model may be capable but too expensive. A nearby expert may be trusted but unavailable. An institution may advertise competence that its past results do not support.

No universal scalar "gravity score" is therefore proposed. Routing is multi-dimensional. For packet \(p\), candidate attractor \(a\), and policy \(\pi_p\), a routing decision may consider a vector such as:

\[
\Gamma_{\pi_p}(p,a) =
\langle
r, c, e, t, v, q, \ell, k, \rho
\rangle
\]

where \(r\) is estimated relevance; \(c\) demonstrated capability; \(e\) evidential proximity or possession; \(t\) trust derived from provenance and past performance; \(v\) current availability; \(q\) expected quality of service; \(\ell\) latency; \(k\) monetary, energetic, or opportunity cost; and \(\rho\) confidentiality, jurisdictional, mandate, or capture risk. The packet's policy does not necessarily combine these dimensions into a permanent ranking. It may impose hard admissibility constraints, maintain a Pareto set, select diverse parallel routes, or deliberately explore an uncertain attractor to improve future routing knowledge.

Attractors should publish claims that can be tested:

```text
I hold corpus X at version Y.
I can execute capability Z under conditions C.
I previously processed packets of type T with these traces.
I am available for this cost and latency range.
I operate under this jurisdiction and confidentiality profile.
```

The claims are signals, not truth. Routing improves when the network compares advertised capability with observed outcomes:

```text
route → process → observe → update trust → reroute
```

This is the same discipline the energy paper called stigmergy with honest price signals. The CXU was the pheromone of the energy network; the trust gradient is the pheromone of the cognitive one — and it is honest for the same Talebian reason: the attractors must pay for their advertisements. Informational gravity is thus not mystical attraction. It is a name for capability discovery under uncertainty, constrained by mandate and corrected by traceable experience.

A worked example keeps the vector honest, and the nearest packet at hand is this paper's own review packet. Its goal: determine whether the claims of the previous version survive informed criticism, and return either revisions or explicit objections. Three attractors were reachable: an artificial reviewer with a demonstrated trace on this corpus; a human expert with deep evidential proximity to the distributed-systems and CPN literature but availability measured in weeks; and a local sovereign model with immediate availability, negligible cost, and no retention risk, but weaker demonstrated capability. Hard admissibility eliminated none of them — the mandate authorized all three. The policy then refused a scalar ranking and chose diverse parallel routing: the artificial reviewer first, because low latency and an existing trust trace made it the cheapest test of the packet's *form*; the human deliberately later, because evidential proximity matters most once the form has stabilized; the local model held in reserve as consolidation processor. The first route has since returned; its findings were reintegrated; its trust score rose. No dimension was collapsed into another, and no attractor was chosen for being famous.

This is also why informational gravity does not collapse into a recommender or reputation system, and the difference is structural rather than cosmetic. Hard admissibility precedes any ranking. Exploration is mandated by policy rather than left to emerge. And \(\Gamma\) is evaluated under the packet's own policy — never as a global score attached to the attractor, ready to be optimized, purchased, or gamed at network scale.

One asymmetry deserves emphasis. The packet's return path also exerts a gravity of its own, and it must be the stronger force. A powerful processor must not capture a packet merely because it contributed to it. The mandate remains attached; attraction determines where transformation may occur; it does not transfer legitimate ownership of the goal.

---

## 6. The Journey: Departure, Transformation, Suspension, Return

### 6.1 Leaving home

The idea of *home* distinguishes a cognitive packet journey from indefinite circulation. Home is not necessarily a server or a geographical location. It is the context that can legitimately interpret and reintegrate the result: a question in a person's Cogentia, a topic in the Cognitive Orchestration Protocol, an issue in a public repository, a scientific paper awaiting review, a municipal proposal, an institution acting under an explicit mandate, a parent packet waiting for a sub-result. Home supplies three things that no processor can invent for itself: why the journey began, what counts as a relevant return, and who has authority to accept the result.

This does not require centralization. Internet packets have source and destination addresses without implying that all traffic is governed by a central machine. A cognitive packet can return to a distributed corpus or a collectively governed topic. Home establishes accountability to an origin, not ownership by an infrastructure operator.

Nor need home be unique. A packet may legitimately concern a personal corpus, a public repository, and a municipal mandate at once. The resolution is declared at packaging, not discovered in transit: one **home of record** — the context whose acceptance completes the packet — and any number of subscribing homes that receive the result without authority over completion. Where authority is genuinely shared, the federation names its acceptance rule — unanimity, quorum, precedence — and the rule travels in the packet like any other clause of the mandate. What is forbidden is silence. A packet with an ambiguous home is malformed, because ambiguity of return is how capture begins.

Before departure, the home context performs a packaging operation: it converts an unresolved cognitive situation into a transportable form. Packaging is necessarily selective. The packet does not contain everything its originator knows; it contains what the originator believes is sufficient, references what can be retrieved, and declares relevant omissions when possible. This is the first source of error. A malformed packet may omit the very fact required to resolve it. A biased originator may encode a goal that excludes unwelcome answers. A mandate may be ambiguous. A completion test may reward fluent closure over truth. Packetization exposes these problems; it does not remove them. The advantage is that the initial framing becomes inspectable. A conventional agent session conceals its assumptions in a long prompt or in transient state. A cognitive packet treats the framing as part of the durable object, so that later processors can object not only to an answer but to the packet's goal, mandate, evidence boundary, or completion condition.

Departure is therefore not merely dispatch. It is the first accountable cognitive act.

### 6.2 Transformation along the route

A data packet is normally intended to arrive with its payload unchanged. A cognitive packet is valuable precisely because its state changes. At each hop, a processor may add evidence, test a claim, produce an artifact, expose a contradiction, refine or challenge the goal, decompose the packet, request a human judgment, translate between representations, declare inability or refusal, or propose that the packet return incomplete. The packet therefore requires versioning and causal relations: a processor should not silently replace the received state; it should emit a transformation whose relation to prior state is inspectable. When a journey crosses capability regimes — from exploratory drafting to binding commitment, for instance — the crossing is itself such a transformation, recorded rather than implied, in the sense the corpus develops under Capability Regimes.

The Cognitive Orchestration Protocol (COP) supplies one possible vocabulary — Event, Topic, Task, Step, Artifact, Continuation. Cogentia's `cogentia.continuation.v1` supplies a concrete, provider-neutral resumption object. [Cognitive Packets](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md) generalizes that object into an envelope and typed payload — continuations, objections, hypotheses, decisions, failures, routing records. These are early implementations, not proof that the full network exists. Their importance is narrower and real: they demonstrate that at least some cognitive state can be made durable enough to cross provider and process boundaries without reducing the packet to a transcript.

### 6.3 Suspension

Store-and-forward matters most when immediate forwarding is impossible. A cognitive packet may wait because the required human is unavailable, because no admissible model has the necessary context window, because the evidence has not yet been produced, because the budget is exhausted, because a legal deadline has not arrived, because it depends on another unresolved packet, or because action is forbidden until a mandate is renewed. Suspension is not failure if the packet preserves why it stopped, what would unblock it, and where it belongs. This converts an abandoned conversation into an explicit continuation — the battery on the shelf, charged and addressed, waiting for its carrier.

### 6.4 Branching and sub-packets

A packet may discover that its goal contains separable questions. It can generate sub-packets with bounded mandates and return addresses pointing to the parent, and the parent should not be considered complete until required sub-results return or are explicitly waived. Branching creates familiar distributed-systems problems — duplicate work, inconsistent results, cycles, resource exhaustion, premature aggregation — and adds semantic ones: two correct sub-results may rest on incompatible assumptions; a summary may erase a minority objection; a parent may accept the first fluent response and cancel a slower but better route. The architecture does not make these problems trivial. It gives them persistent objects and traces.

### 6.5 Failure as payload

Systems often hide intermediate failures behind a successful fallback. That produces an answer while destroying knowledge about fragility. A cognitive packet should be able to return both a result and the errors encountered on the way: a provider refusal, an unavailable source, a contradictory datum, a failed tool call, an exceeded budget. The packet may still succeed, but home should know under what conditions. Failure is not noise around cognition. Properly represented, it is cognitive evidence — the RAIB principle transposed: a fleet of inexpensive attempts whose individual failures are continuous, low-magnitude, and informative. The trace discipline this requires — provenance that survives the journey and returns to the corpus — is the one Reality Safety formalizes for the corpus at large.

### 6.6 Returning home

The return journey is the feature that turns distributed processing into a cognitive loop. A compute job returns bytes. A cognitive packet returns with a proposed change relative to the context from which it departed: a result, supporting and opposing evidence, artifacts created, the provenance of each contribution, a confidence statement or uncertainty boundary, failures and routes attempted, mandate deviations or requested extensions, the unresolved remainder, and suggested continuation packets.

Home then performs reintegration — and reintegration is not automatic acceptance. The home context may reject the result, request another route, preserve competing versions, escalate to a human decision, or change the original goal in light of what was learned. This closes the loop:

```text
home state
→ packet formation
→ outward routing
→ distributed transformation
→ return
→ accountable reintegration
→ changed home state
```

The changed home state may generate further packets. The architecture is recursive, but the recursion is anchored. Without return, packets accumulate as disconnected outputs. With return, the corpus learns.

The idea is older than digital networks. A message in a bottle is a bounded payload released without a dedicated circuit, carried opportunistically, possibly discovered by an unknown recipient. A scientific question sent through correspondence, a diplomatic mission, a sailor returning with charts — all have the store-and-forward structure. What the formal packet adds is not the existence of journeys. It adds explicit identity, mandate, state, routing evidence, completion, and return. And the joke contains a serious boundary: a bottle that never returns may still communicate, but a cognitive packet whose result cannot be reintegrated may have produced intelligence without completing its accountable journey.

---

## 7. From Distributed Compute to Distributed Cognition

The distinction between these two architectures is easily obscured, because both use networks, heterogeneous machines, and artificial intelligence.

A distributed compute system asks:

```text
Where can these instructions run under these resource constraints?
```

A distributed cognitive system asks:

```text
What purposeful cognitive state must persist,
what transformation is currently needed,
which processors are admissible,
and where must the result return?
```

Projects such as Inria's CUPSELI challenge with Hivenet — successor to their Alvearium collaboration on distributed storage, Hivenet itself now part of Antimatter — address important problems in heterogeneous and volatile computation: scheduling, storage, communication, confidentiality, fault tolerance, frugal machine learning. These are plausible substrates for cognitive packet processing. Their public descriptions, however, treat the workloads as computation, model training, inference, messages, or data. They do not define a durable semantic packet that can cross machines, models, artificial agents, and humans while retaining goal, mandate, and home.

This is not a criticism that distributed-systems researchers are confused about their own problems. It is a claim about abstraction level. Resource orchestration, model routing, agent orchestration, and cognitive orchestration are distinct:

| Layer | Central question | Persistent unit |
|---|---|---|
| Resource orchestration | Where can execution occur? | job, container, VM, allocation |
| Model routing | Which inference endpoint should answer? | request and response |
| Agent orchestration | Which actor performs the next step? | task or workflow state |
| Cognitive orchestration | What meaningful work must survive all processors? | cognitive packet |

Lower layers remain necessary. A cognitive packet cannot run on an absent machine, and informational gravity cannot ignore bandwidth, energy, or jurisdiction. But optimizing the substrate does not define what must persist above it. The relationship is therefore complementary rather than competitive: Antimatter can provide distributed execution capacity; Magistral can route among model endpoints and fallbacks; COP and cognitive packets can carry durable work across those processors; Cogentia can reintegrate the returned artifacts into a governed corpus. None of these layers should pretend to be the others.

---

## 8. Resistances and Their Resolution

In psychoanalytic practice, resistances are not obstacles to be dismissed; they are the shape of the problem, the material that must be worked through before the insight can be integrated. The first paper worked through the resistances of the energy patient — efficiency, density, reliability, regulation. The cognitive patient has its own, and several are harder, because they concern meaning rather than joules. The framing proposed here is useful only if it survives the cases where it should not be applied or trusted.

### 8.1 Lossy externalization

Tacit, embodied, emotional, or contextual knowledge may be lost during packaging. A formally complete packet may be cognitively inadequate. The resolution is not denial but honesty: the substitution test must permit the answer *not yet portable*, and the packet must mark what remains bound to a named person. A network that pretends everything travels is worse than one that knows what does not.

### 8.2 Goal corruption

A packet can faithfully pursue a harmful, biased, or badly framed goal. Traceability does not confer legitimacy. Processors need the ability to object to the goal itself and return the objection without executing it — which is why the objection is a first-class payload kind, not an error condition.

### 8.3 False completion

Machine-generated fluency can satisfy superficial completion tests. Completion conditions must distinguish the production of an answer from the resolution of the underlying question. A packet that returns quickly, elegantly, and wrongly has failed better than one that returns honestly incomplete — and the architecture must be able to say so.

### 8.4 Manipulation of informational gravity

Attractors can fabricate credentials, purchase visibility, collude on reputation, or optimize for routing metrics. A gravitational field built from unverified claims becomes advertising infrastructure. Diversity of routes, signed traces, independent audits, and deliberate exploration are defenses, not guarantees. The pheromone stays honest only while the ants pay for their mistakes.

### 8.5 Packet capture

A processor or platform may retain the packet, obscure its state, or make export costly. This is the cognitive form of the enclosure the energy paper called circuit capture. Open formats and explicit return paths reduce it only when users retain practical exit capacity — the protocol must remain a commons even when the processors are commercial.

### 8.6 Trace overload and surveillance

Complete traceability can expose private reasoning, chill dissent, and create an irresistible surveillance archive. The system must distinguish proof of process from disclosure of content, support selective revelation, and permit legitimate forgetting where law and ethics require it. A trace is an instrument of accountability; it must not become an instrument of dossier.

### 8.7 Recursive packet explosion

Unbounded decomposition can generate more sub-packets than the network can process. Budgets, depth limits, cancellation rules, and parent responsibility are necessary. Recursion is anchored at home or it is not anchored at all.

### 8.8 Semantic interoperability

Two processors may parse the same schema while interpreting its concepts differently. Syntactic portability is not semantic continuity. Ontologies, examples, tests, and human review remain necessary; the envelope can guarantee delivery, never understanding. The minimal executable mitigation is for packets to carry tests as well as definitions: worked examples whose expected outcomes a receiving processor must reproduce before trusting its own reading. Interoperability is then demonstrated per packet rather than assumed per schema.

### 8.9 Majority capture

One human, one vote prevents synthetic votes. It does not prevent domination by a human majority, coordinated misinformation, or exclusion from participation. Democratic equality requires constitutional rights and anti-capture mechanisms beyond counting — the mandate, trace, imputability, and revocation grammar developed elsewhere in this corpus.

### 8.10 What this paper does not claim

This paper does **not** claim: that the human mind literally operates as a packet network; that consciousness has been explained or digitized; that all cognition can or should be externalized; that cognitive packets guarantee correctness, intelligence, or moral value; that informational gravity is a physical force or a finished routing algorithm; that existing distributed cognition, workflow, or multi-agent research is superseded; that the current COP, Cogentia, or Magistral implementations constitute a production-scale cognitive network; that one human, one vote is derivable from technical architecture; or that packetization is preferable when a stable circuit is simpler, safer, or more efficient. The proposal is an infrastructure hypothesis with partial implementations and a testable boundary, not a completed theory of cognition.

---

## 9. The Constitutional Boundary: Intelligence Without Synthetic Sovereignty

Packetization changes how cognitive capacity can scale. It does not answer who has the right to govern.

The distinction is routinely blurred in discussions of artificial intelligence. Superior prediction is treated as a claim to decision authority; ownership of compute becomes agenda control; a corporation that can instantiate millions of agents acquires the appearance of a numerical constituency; automated agreement is mistaken for consent. The constitutional answer proposed here is intentionally simple:

> Cognitive packets may be processed by machines. Collective political authority belongs to living humans: one human, one vote.

This is not a theorem derived from packet networks. It is a democratic commitment. Humans differ in knowledge, attention, virtue, wealth, eloquence, and computational assistance; democracy refuses to translate those differences into unequal fundamental political personhood. The rule creates a deliberate discontinuity between scalable cognition and sovereignty: one person operating one million agents remains one political person; one corporation owning one million GPUs receives no additional votes; an artificial agent may produce decisive evidence but does not become a citizen by doing so; delegation of cognitive labor does not transfer the delegator's political personhood; expertise may influence a decision without constituting a superior title to rule.

The rule does not solve every problem of AI safety. It does not prevent manipulation, concentration of agenda-setting power, coercion, propaganda, surveillance, or fraudulent claims of personhood. One human, one vote requires resistant identity mechanisms, transparent mandates, revocable delegation, rights that constrain majorities, and infrastructure that cannot silently privilege its owners — the anti-capture architecture that DHITL and the mandate–trace–imputability–revocation grammar develop within this corpus: no mandate, no act; no trace, no imputability; no imputability, no legitimate power. Nor does the rule imply that every operational decision should be submitted to a universal ballot. Institutions need delegated roles, expertise, and bounded authority. The invariant is that delegated power remains traceable to human political equality and cannot reproduce itself through synthetic agents.

The architecture thus separates an epistemic network from a constitutional boundary:

```text
many humans, models, agents, and tools may process cognition
→ their contributions return with provenance
→ living humans retain equal political standing
```

In compact form:

> Packetize cognition. Equalize sovereignty.

The first is an engineering programme. The second is an act of faith in democracy.

---

## 10. A Falsifiable Research Programme

The next step is not another analogy. It is an experiment. Six, in fact — each designed so that the framing can lose.

**Processor substitution.** Construct a packet containing a bounded research question, mandate, source references, budget, and completion conditions. Send it successively through one artificial model provider; a second provider with no access to the first provider's private session state; a human reviewer; and a local or sovereign model for final consolidation. Measure whether each processor can resume from the externalized packet alone, which context must be reconstructed, and what semantic loss occurs.

**Journey integrity.** Verify that the packet retains stable identity across serializations, causal ordering of transformations, distinguishable provenance, mandate constraints, unresolved objections, a valid return address, and reproducible reintegration into home.

**Informational routing.** Provide several attractors with different capabilities, costs, availability, and trust histories. Compare fixed routing, declared-capability routing, observed-performance routing, and diverse parallel routing. Measure goal satisfaction, cost, latency, failure recovery, and capture concentration.

**Suspension.** Pause a packet after partial work. Resume it after a significant delay with a different processor. Determine whether the packet carries enough state to continue without reading the complete historical transcript.

**Adversarial conditions.** Introduce a falsely advertised expert; a processor that returns a persuasive but unsupported conclusion; a route that violates jurisdictional policy; a sub-packet loop; a platform that withholds intermediate state; a human reviewer who disputes the original goal. Observe whether the trace makes each failure visible and whether the packet can return incomplete rather than manufacture success.

**Constitutional boundary.** Run a collective decision process in which artificial agents may generate evidence, objections, forecasts, and formulations but cannot vote. Test whether provenance remains intelligible to participants, whether owners of more compute gain de facto agenda control, and whether revocable human delegation preserves equal standing.

These experiments can run on ordinary computers before any specialized FractaNet infrastructure exists. Later, the same packets could traverse heterogeneous compute supplied by SLICES, Antimatter, local sovereign nodes, or other providers. The point of the architecture is that changing the substrate must not change the packet's identity.

**First result (2026-07-21).** The processor-substitution experiment has run once, on this paper's own claim C11 (packet CPKT-2026-001). The packet crossed two providers under three isolation conditions — an anonymous session, an account-bound session, and a previously engaged reviewer — with the human author as physical carrier; one further platform comprehended the packet without enrolling in it. Portability scores ranged from 8.5 to 9.5 out of 10; semantic drift on the goal restatements was low; the hops converged unanimously, by parametric memory and by live search alike, on the disposition reflected in the manifest above: C11 narrowed, the mobile-agent lineage named. The journey also produced five findings the protocol had not anticipated: hop fragmentation under retransmission without deduplication; portability flattered by side-channel co-transport of documents; role capture by platform wrappers; the unverifiability of self-declared isolation, which must instead be established by construction; and citation loss at platform boundaries, where evidence links did not survive export. Failure returned as payload, exactly as Section 6.5 requires.

---

## 11. Claim Manifest — v0.3

| Claim | Status | Description |
|---|---|---|
| C1 | Observation | Purposeful cognitive work already moves among humans, tools, documents, models, and institutions, but its continuity is commonly bound to processors or applications. |
| C2 | Definition | A cognitive packet is a bounded, addressable, durable, and routable unit of purposeful cognitive work with enough externalized state to survive processor replacement. |
| C3 | Operational rule | Packetization is tested by whether another admissible processor can resume the work without access to the prior processor's private state. |
| C4 | Architectural hypothesis | Making the cognitive packet persistent can reduce provider lock-in, context loss, hidden failure, and dependence on individual agents. |
| C5 | Definition | Informational gravity names policy-constrained routing toward reachable sources of relevant and verifiable resolution. |
| C6 | Non-claim | Informational gravity is not a physical force or a universal scalar ranking. |
| C7 | Implementation claim | COP, `cogentia.continuation.v1`, Cognitive Packets, and Magistral implement partial elements of the proposed architecture; they do not yet constitute the full network. |
| C8 | Normative proposition | Artificial agents may process cognitive packets, while political personhood remains reserved to living humans on the basis of one human, one vote. |
| C9 | Non-claim | Democratic equality is a normative commitment, not a conclusion derived from packetization. |
| C10 | Research programme | Multi-provider, human-in-the-loop journey experiments should test substitution, suspension, routing, provenance, return, and semantic loss. |
| C11 | Historical/architectural claim | Gelenbe's CPN (1999) placed adaptive cognition in transport control while application payloads remained ordinary data; this paper performs a *relative* inversion, making the payload itself the durable unit of purposeful cognitive work. Unlike mobile-agent systems (Telescript), which migrated executable programs inside compatible runtimes, the cognitive packet keeps the work object distinct from every current processor. Narrowed per substitution experiment CPKT-2026-001. |

---

## 12. Conclusion: Wo Es War

The history of packet switching is often told as a history of efficiency. It is more accurately a history of separation.

The message was separated from the circuit. Voice was separated from the telephone exchange. Stored energy can be separated from the transmission line. Computation can be separated from the machine. The next separation is between purposeful cognitive work and the temporary processor that performs it.

Once this separation is made, familiar problems change shape. Context loss becomes packet-state loss. Vendor lock-in becomes packet capture. Agent orchestration becomes routing among replaceable processors. Human-in-the-loop ceases to be an exception injected into an automated workflow: a human is one admissible cognitive processor, with distinct authority. Memory becomes durable packet state and reintegration at home. Failure becomes a payload rather than an embarrassment hidden behind fallback.

None of this makes cognition correct. A packet can carry a false premise, follow a manipulated gradient, and return with an elegant error. The contribution is not an oracle. It is an accountable journey.

And the journey reveals a boundary that engineering alone cannot supply. If cognitive capacity can scale through machines while political authority scales with it, the owners of compute become sovereign. A democratic system must refuse that conversion. Intelligence may circulate through as many processors as are useful. Political personhood does not multiply with processors.

The complete proposal can be stated without ceremony:

> Packetize capacity, up to cognition.
> Route cognitive packets by informational gravity.
> Return them home with their trace.
> Let living humans remain political equals.

The surprising part is not that this architecture can be imagined. It is that most of it was already operating, in fragments, unconsciously. Every battery carried stored energy. Every container moved bounded capacity. Every suspended task waited to be resumed. Every question passed from one mind to another. Every citation pointed toward an informational attractor. Every issue returned work to a repository. Every old colleague who could still recognize a problem carried part of the network's memory.

The packets were already moving. What was missing was the decision to treat their journeys as the system.

Freud gave the whole programme its sentence, and it happens to be an architectural one: *Wo Es war, soll Ich werden* — where it was, I shall come to be. Where the unconscious grid was, a conscious network shall come to be. The datagram won for information. It is winning for energy. Let it now carry the work of thinking — and let every packet travel with a return address.

---

## Acknowledgements and Disclosure

This paper continues *The Unconscious Grid* and the public FractaVolta, MareNostrum, Cogentia, and Inseme corpora. Its central formulation emerged through iterative exchanges between Jean Hugues Noël Robert and OpenAI's ChatGPT/Codex, including comparison with the Inria–Hivenet (now Antimatter) CUPSELI partnership and recollection of earlier work with Thierry Parmentelat at Odisei during the emergence of Voice over IP and hosted PBX services. ChatGPT/Codex assisted with research, structure, and the v0.1 draft. The present version was restructured and rewritten with Claude (Anthropic, claude.ai) in the register of *The Unconscious Grid*, following the corpus's standard multi-agent adversarial method. A structured adversarial review of v0.2 by xAI's Grok (2026-07-21) was integrated into this version; its principal requests — the comparative table of Section 4.4, the worked gravity example of Section 5, and the multi-home clarification of Section 6.1 — are now part of the text. Claim C11, Section 2.2, and Section 3 were subsequently revised following the first processor-substitution experiment (packet CPKT-2026-001, 2026-07-21), whose hops were processed by ChatGPT/Codex (OpenAI) and Grok (xAI), with a failed hop by Perplexity logged as data and the human author acting as physical carrier between providers. The author remains responsible for the concepts, claims, normative positions, and final text. This version is deliberately marked for adversarial review by independent artificial agents and human readers.

---

## References

- Baran, P. (1964). *On Distributed Communications*. RAND Corporation, Memoranda RM-3420-PR through RM-3440-PR.
- Cerf, V., & Kahn, R. (1974). A protocol for packet network intercommunication. *IEEE Transactions on Communications*, 22(5), 637–648.
- Clark, H. H., & Brennan, S. E. (1991). Grounding in communication. In L. B. Resnick, J. M. Levine, & S. D. Teasley (Eds.), *Perspectives on Socially Shared Cognition*. American Psychological Association.
- Gelenbe, E., Xu, Z., & Seref, E. (1999). Cognitive packet networks. In *Proceedings of the 11th IEEE International Conference on Tools with Artificial Intelligence (ICTAI'99)*, 47–54.
- Gelenbe, E., Lent, R., & Xu, Z. (2001). Design and performance of cognitive packet networks. *Performance Evaluation*, 46(2–3), 155–176.
- Gelenbe, E. (2012). Energy Packet Networks: ICT-based energy allocation and storage. In *Green Communications and Networking*, Springer LNICST, Vol. 51, 186–195.
- Gelernter, D. (1985). Generative communication in Linda. *ACM Transactions on Programming Languages and Systems*, 7(1), 80–112.
- Hewitt, C., Bishop, P., & Steiger, R. (1973). A universal modular ACTOR formalism for artificial intelligence. In *Proceedings of IJCAI'73*, 235–245.
- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press.
- Milojičić, D. S., Douglis, F., Paindaveine, Y., Wheeler, R., & Zhou, S. (2000). Process migration. *ACM Computing Surveys*, 32(3), 241–299.
- Newell, A. (1962). Some problems of basic organization in problem-solving programs. In *Proceedings of the Second Conference on Self-Organizing Systems*, 393–423.
- Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.
- Robert, J. H. N. (2026). *The Unconscious Grid: On Store-and-Forward as the Repressed Solution to Energy Sovereignty*. Institut Mariani / C.O.R.S.I.C.A. / FractaVolta. Available: github.com/JeanHuguesRobert/FractaVolta.
- Robert, J. H. N. (2026). *Agent-Resumable CLI: Externalized Judgment, Continuations, and Provider-Neutral Resumption for AI-Compatible CLI Tools*. Cogentia Commons. Available: github.com/JeanHuguesRobert/cogentia.
- Robert, J. H. N. (2026). *Cognitive Packets: An Envelope and Payload Format for Human–AI and Multi-Agent Cooperation*. Cogentia Commons. Available: github.com/JeanHuguesRobert/cogentia.
- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.
- Schmidt, K., & Simone, C. (1996). Coordination mechanisms: Towards a conceptual foundation of CSCW systems design. *Computer Supported Cooperative Work*, 5, 155–200.
- Smith, R. G. (1980). The contract net protocol: High-level communication and control in a distributed problem solver. *IEEE Transactions on Computers*, C-29(12), 1104–1113.
- Suchman, L. A. (1987). *Plans and Situated Actions*. Cambridge University Press.
- Thorn, T. (1997). Programming languages for mobile code. *ACM Computing Surveys*, 29(3), 213–239.
- White, J. E. (1994). *Telescript Technology: The Foundation for the Electronic Marketplace*. General Magic.
- Wooldridge, M. (2009). *An Introduction to MultiAgent Systems* (2nd ed.). Wiley.

---

## Optimized condensed version for AI agents

**Cognition, like energy, is commonly bound to circuits** (session, provider, agent process, workflow engine, employee memory — the path dies with its holder; transcript-copying and prompt-reconstruction are symptoms that the wrong object has been made persistent).

**The repressed unit is the cognitive packet**: a bounded, addressable, durable, routable unit of purposeful cognitive work carrying identity, home, goal, mandate, state, needs, routing policy, completion conditions, return path, and trace.

### Operational boundary

- **Substitution test**: work is packetized to the degree that another admissible processor (human, model, agent, tool) can resume it without the prior processor's private state. The honest answer *not yet portable* is permitted and required.
- **Genealogical inversion**: Gelenbe's CPN (1999) = cognition in the routing, payload dumb. Cognitive packets = cognition in the payload, routing simple and accountable.

### Routing

- **Informational gravity**: policy-constrained, multi-dimensional attraction toward admissible sources of verifiable resolution — Γ = ⟨relevance, capability, evidence, trust, availability, QoS, latency, cost, risk⟩; no universal scalar score; feedback loop route → process → observe → update trust → reroute; attractors pay for their advertisements (skin in the game).
- **Return-path gravity dominates**: contribution never transfers ownership of the goal; the mandate stays attached.

### Journey

departure (packaging = first accountable cognitive act) → transformation (versioned, causal, objection as first-class payload) → suspension (store-and-forward with preserved why/unblock/home) → branching (sub-packets with return addresses) → failure as payload → return → accountable reintegration → changed home state. Without return, outputs; with return, a corpus that learns.

### Layering

resource orchestration (job) < model routing (request) < agent orchestration (workflow state) < **cognitive orchestration (cognitive packet)**. Substrates (Antimatter/CUPSELI, SLICES, local nodes) and routers (Magistral) are complementary; COP + Cognitive Packets carry the work; Cogentia reintegrates it.

### Constitutional boundary

**Machines may process cognitive packets; only living humans vote — one human, one vote.** Normative commitment, not theorem. Compute ownership confers zero additional political personhood.

### Axiomatic summary (for agent reasoning)

**Cognitive packet = purposeful work with externalized state passing the substitution test + informational-gravity routing under mandate + traced journey with mandatory return home + human-only sovereignty at the political layer.**

---

## Potential Target Journals

- *AI & Society* (Springer) — primary target; explicitly welcomes interdisciplinary work on the social and political architecture of artificial intelligence
- *Minds and Machines* (Springer) — for the conceptual boundary between cognition, computation, and infrastructure
- *ACM Transactions on Autonomous and Adaptive Systems* — for the routing, substitution, and orchestration claims
- *Computer Supported Cooperative Work* (Springer) — for the coordination-mechanism lineage and the human-in-the-loop architecture

---

## Continuation

Review status: v0.2 reviewed by Grok (2026-07-21); its requests are integrated in v0.3. C11 narrowed in v0.4 following substitution experiment CPKT-2026-001 (2026-07-21) — the paper's Continuation item 7 now has experimental backing. Next admissible processors: independent reviews by other artificial agents, and at least one human reader with distributed-systems competence — the experiment's remaining decorrelated hop.

This draft should receive adversarial review focused on:

1. whether the cognitive packet differs materially from tasks, messages, workflow state, actors, tuples, and blackboard objects;
2. whether the substitution test is sufficiently crisp;
3. whether "home" adds a necessary invariant or merely renames an origin/destination;
4. whether informational gravity can be operationalized without collapsing into a recommender or reputation score;
5. whether the packet journey preserves semantic identity across transformation;
6. whether the relation to generalized packet networks is technically useful rather than metaphorical;
7. whether the Gelenbe CPN genealogy and its claimed inversion (C11) are stated fairly and add real content;
8. whether the democratic safety argument follows cleanly while remaining explicitly normative;
9. which claims should be removed, narrowed, measured, or cited before publication;
10. whether the comparative table in Section 4.4 is fair to the traditions it summarizes;
11. a bullshit score from 0 to 10, with exact passages responsible for every point above zero.
