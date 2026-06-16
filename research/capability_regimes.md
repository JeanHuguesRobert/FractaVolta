---
title: "Capability Regimes"
subtitle: "Fractal decision under constraints of uncertainty in RAIX-COP-Fractanet architectures"
description: "Source working paper defining capability regimes as graded, fractal operating regimes for Fractanet: ordinary, perturbed, degraded, critical, vital and recovery. It connects RAIX, COP, Cognitive Packets, allostasis, traces, mandates and decision under uncertainty."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
x-address: "1 cours Paoli, F-20250 Corte, Corsica, France"
x-email: "jhr@baronsmariani.org"
x-website: "https://fractavolta.com"
canonical_path: "FractaVolta/research/capability_regimes.md"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/capability_regimes.md"
version: "0.1-draft"
status: "source working paper — draft under human validation"
date: "2026-06-15"
last_modified_at: "2026-06-15"
license: "CC BY-SA 4.0"
language: "en"
type: "source-document"
source_or_derived: "source-document"
repository: "FractaVolta"
related_documents:
  - "FractaVolta/research/fractanet.md"
  - "FractaVolta/research/generalized_packet_networks.md"
  - "FractaVolta/research/inference_packet_network.md"
  - "FractaVolta/research/thermal_packet_networks.md"
  - "FractaVolta/research/packet_paper_template.md"
  - "FractaVolta/research/index.md"
  - "Inox/research/inox-spec.md"
  - "cogentia/research/cognitive_packets.md"
  - "cogentia/research/cognitive_packet_switching.md"
  - "cogentia/research/cogentia_continuation_packet_routing.md"
  - "inseme/packages/cop-core/Invariants.md"
  - "inseme/packages/cop-core/ImplementationProfiles.md"
tags:
  - fractanet
  - capability-regimes
  - decision-under-uncertainty
  - raix
  - cop
  - cognitive-packets
  - crisis-regime
  - allostasis
  - homeostasis
  - traceability
  - anti-capture
  - preemption
  - local-first
  - fallback
human_validation_required: true
review_status: "initial ChatGPT-assisted draft produced from conversation on 2026-06-15; human validation remains required"
---

# Capability Regimes

## Fractal decision under constraints of uncertainty in RAIX-COP-Fractanet architectures

**Jean Hugues Noël Robert, baron Mariani**  
Institut Mariani / C.O.R.S.I.C.A. / FractaVolta  
1 cours Paoli, F-20250 Corte, Corsica, France  

*Working paper — v0.1 draft — 2026-06-15*  
*License: CC BY-SA 4.0*  
*Repository: `JeanHuguesRobert/FractaVolta` — target path: `research/capability_regimes.md`*

---

## 0. Status and corpus role

This document is a **source working paper** for the Fractanet corpus. It should not replace `research/fractanet.md`; it should specialize and clarify one architectural commitment that the central Fractanet document can only state briefly:

> **Fractanet does not route capacity in an abstract vacuum. It routes capacity under regimes of constraints, uncertainty, urgency, responsibility and correction.**

The practical objective is to turn the intuitive distinction between "normal" and "crisis" into a graded, fractal and packet-readable concept: **capability regimes**.

This draft is not a safety standard, not an autonomous-vehicle specification, not a hospital resilience standard, and not a legal framework. It is a conceptual and architectural source document intended to support later technical specifications, design notes and public explanations.

---

## 1. Core thesis

A capable system should not be designed only for ordinary operation. It should also be able to recognize when ordinary operation is no longer sufficient, shift regime, mobilize additional capacities, strengthen traces, preserve local safety invariants, and return to a lower regime after correction or recovery.

The first formulation was binary:

```text
normal regime
→ crisis regime
```

The more accurate formulation is graded:

```text
ordinary
→ perturbed
→ degraded
→ critical
→ vital
→ recovery
```

The underlying claim is:

> **A decision is not good in the abstract. It is admissible, or not, within a given regime of time, uncertainty, stakes, resources, mandate, reversibility and responsibility.**

Fractanet, understood as a programmable network of capacity packets, must therefore be able to route not only by destination, cost, latency or exergy, but also by regime.

---

## 2. Definition

A **capability regime** is a provisional operating state of a system, defined by the constraints under which a capability must act.

Those constraints include at least:

- time available;
- uncertainty;
- stakes;
- reversibility;
- locality;
- resources;
- mandate;
- preemption rights;
- trace requirements;
- escalation rules;
- fallback options;
- post-event correction.

Short definition:

> **A capability regime is the constraint-context in which a capability must decide, act, trace and remain correctable.**

The regime is not merely a risk level. It is a configuration of admissible action.

---

## 3. Why the binary normal/crisis distinction is insufficient

The binary distinction is useful as a first intuition. A vehicle normally drives within its operational domain; sometimes an abnormally complex situation appears. An ambulance normally circulates under road rules; sometimes it must preempt ordinary traffic. A hospital normally consumes power through ordinary electrical architecture; sometimes a power failure must preserve an active operating room.

But real systems do not simply flip from "normal" to "crisis". They usually pass through intermediate regimes:

- slight anomaly;
- rising uncertainty;
- degraded information;
- shortage of resource;
- increased stakes;
- reduced reversibility;
- need for external capacity;
- threshold for preemption;
- post-event recovery.

The architecture must therefore support **regime gradients**, not just emergency switches.

---

## 4. Regime ladder

The following ladder is provisional. It should be adapted by domain.

| Regime | Description | Typical action pattern |
|---|---|---|
| **Ordinary** | expected conditions; local capability sufficient | local action, ordinary trace |
| **Perturbed** | anomaly or weak uncertainty appears | slow down, observe, add trace, prepare escalation |
| **Degraded** | local information, resource or capability is impaired | conservative action, fallback route, external query if time allows |
| **Critical** | safety, continuity or mission is at risk | prioritized routing, reinforced trace, external capacity, possible preemption |
| **Vital** | life, irreversibility, sovereignty or existential continuity is at stake | hard invariants, reserved capacity, mandatory trace, human/institutional escalation where possible |
| **Recovery** | immediate danger has passed; system must reintegrate traces and restore ordinary operation | audit, repair, reintegration, rule update, return to lower regime |

The ladder is not a universal ontology. It is a first practical grammar.

---

## 5. Fractal invariant

The same regime logic appears at multiple scales.

```text
perceive
→ qualify regime
→ select admissible action
→ act
→ trace
→ correct
→ learn
```

This motif can appear in:

- an ESP32 sensor node;
- an Inox micro-runtime;
- a programmable gateway;
- an autonomous vehicle;
- an ambulance corridor;
- a hospital power system;
- a local energy network;
- a cognitive workflow;
- a public institution;
- a democratic emergency mandate.

The invariants are not identical in implementation, but their function recurs:

| Invariant | Low-level example | Higher-level example |
|---|---|---|
| Perception | sensor reading | institutional signal |
| Regime qualification | threshold crossed | public emergency declared |
| Local action | actuator command | local administrative decision |
| Escalation | edge compute request | regional/state intervention |
| Fallback | safe stop | minimal service continuity |
| Trace | event log | public audit record |
| Correction | firmware/rule update | legal or procedural revision |

This is why the concept is Fractanet-native: it is **fractal decision under constraints of uncertainty**.

---

## 6. Relation to RAIX

RAIX is the redundancy principle:

```text
Redundant Array of Independent X
```

where `X` may be compute, model, agent, gateway, route, cache, trace, policy, energy source, institution or human reviewer.

Capability regimes add one crucial point:

> **RAIX capacity does not need to be active everywhere all the time. It must be mobilizable when the regime requires it.**

This matters economically. A system should not always embed maximal intelligence in every unit. It should embed enough local capability for ordinary and fallback regimes, then mobilize stronger or rarer capacities when the regime changes and the deadline allows.

Formula:

```text
Do not overbuild every node for every exceptional case.
Do not centralize every critical decision either.
Prepare graded, redundant, traceable capacity mobilization.
```

RAIX therefore becomes regime-sensitive:

| Regime | RAIX role |
|---|---|
| Ordinary | efficiency, ordinary redundancy, local autonomy |
| Perturbed | alternative routes, additional observation, trace strengthening |
| Degraded | fallback capacity, degraded service, local-first resilience |
| Critical | prioritized compute, preemptive routing, external capacity surge |
| Vital | reserved capacity, hard invariants, mandatory trace, human/institutional escalation |
| Recovery | trace replication, audit, repair, rule update |

---

## 7. Relation to COP

COP — Cognitive Orchestration Protocol — should not merely supervise execution. It should help qualify the regime in which execution occurs.

COP should therefore support events such as:

```text
regime.observed
regime.classified
regime.escalated
regime.deescalated
deadline.set
uncertainty.raised
fallback.entered
preemption.requested
preemption.granted
preemption.denied
trace.reinforced
human.escalation.requested
recovery.started
recovery.completed
postmortem.required
```

COP becomes the protocol of:

- regime qualification;
- routing under uncertainty;
- escalation;
- fallback;
- preemption;
- trace reinforcement;
- post-event recovery.

Short formula:

> **COP qualifies the regime, routes the packet, preserves the trace, and makes the act reviewable.**

---

## 8. Cognitive Packet regime field

A Cognitive Packet or capability packet should carry enough information for regime-sensitive routing.

Minimal sketch:

```yaml
cognitive_packet:
  id:
  task:
  regime:
    level: ordinary | perturbed | degraded | critical | vital | recovery
    uncertainty: low | medium | high | extreme
    deadline_ms:
    reversibility: reversible | partially_reversible | irreversible
    stakes: comfort | cost | continuity | safety | life | sovereignty
  constraints:
    max_latency_ms:
    max_cost:
    privacy_level:
    legal_mandate:
    energy_budget:
  routing:
    local_first: true
    escalation_allowed: true
    external_compute_allowed:
    human_review_required:
  invariants:
    - preserve_life
    - preserve_trace
    - preserve_fallback
  trace_policy:
    level: minimal | normal | reinforced | forensic
  fallback_policy:
    if_no_answer:
  recovery_policy:
    post_event_review_required:
```

The packet does not ask only:

```text
What should be done?
```

It asks:

```text
What action is admissible under this regime of uncertainty, deadline, stakes, mandate and reversibility?
```

---

## 9. Decision under constraints of uncertainty

The general problem is decision under uncertainty, but with explicit operational constraints.

A Fractanet decision is constrained by:

```text
uncertainty
+ deadline
+ stakes
+ available capability
+ energy/cost budget
+ locality
+ privacy
+ legal mandate
+ reversibility
+ trace requirement
+ human responsibility
```

The system should not seek perfect decision. It should seek **admissible decision**.

Definition:

> **An admissible decision is an action that satisfies the hard invariants of the current regime, uses available capacity proportionately, remains traceable, and preserves correction or fallback when possible.**

This is not pure optimization. It is constrained action under uncertainty.

---

## 10. Deadline as a first-class constraint

The shorter the deadline, the more local the decision must be.

| Deadline | Typical admissible layer |
|---:|---|
| 1–50 ms | embedded/local only |
| 50–150 ms | local + very near edge if already available |
| 150–1000 ms | edge / roadside / local cell / nearby gateway |
| seconds | regional compute, remote assistance, human confirmation in limited cases |
| minutes/hours | cloud, large models, deeper review, audit |

Formula:

> **The shorter the deadline, the more the system must rely on local invariants. The longer the deadline, the more collective intelligence can be mobilized.**

This prevents a dangerous confusion: external intelligence can augment crisis handling, but it cannot replace hard local fallback when the deadline is below communication and decision latency.

---

## 11. Preemption under mandate

In higher regimes, some capacities must preempt others.

Examples:

- an ambulance creates a dynamic priority corridor;
- a hospital operating room preempts non-critical electrical loads during outage;
- emergency communications preempt ordinary traffic;
- a cybersecurity quarantine preempts ordinary access;
- a local safety invariant preempts a remote optimization request.

But preemption is dangerous. It must be:

- mandated;
- scoped;
- time-bounded;
- traceable;
- auditable;
- revocable where possible;
- reviewed after the event.

Formula:

> **Preemption is acceptable only when the mandate, scope, deadline, trace and recovery path are explicit.**

---

## 12. Examples

### 12.1 Autonomous vehicle

Ordinary regime: the vehicle acts within its operational domain using embedded perception and planning.

Perturbed/degraded regime: uncertainty rises — unusual roadworks, occlusion, sensor disagreement, ambiguous lane, emergency vehicle nearby. The vehicle slows, strengthens trace, and may query nearby edge capacity if deadline allows.

Critical regime: accident risk becomes imminent. Local invariants dominate: braking, safe stop, minimal-risk manoeuvre. External compute may assist only if available within deadline.

Vital regime: life is at stake and irreversibility is high. The system prioritizes life-preserving local actions, preserves forensic trace, and escalates for post-event review.

The architectural rule is:

```text
local safety invariant
+ networked crisis intelligence when time allows
```

not:

```text
cloud-dependent safety
```

### 12.2 Ambulance corridor

An ambulance is not merely a vehicle with a siren. It is a moving crisis packet.

It temporarily changes the regime of nearby traffic:

- ordinary vehicles must yield;
- traffic lights may adapt;
- roadside units may propagate alerts;
- hospital access may prepare;
- the route may become a dynamic corridor.

This is **preemptive capacity under mandate**.

Sketch:

```yaml
crisis_packet:
  type: emergency_medical_corridor
  regime: critical | vital
  priority: vital
  moving_entity: ambulance
  route:
  deadline:
  required_actions:
    - yield
    - clear_lane
    - adjust_signal_phase
    - notify_nearby_agents
  trace_policy:
    level: reinforced
    post_event_review: true
```

### 12.3 Hospital power failure

A hospital is not one electrical consumer. It contains nested regimes.

During an outage, non-critical loads may be shed while vital circuits must be protected:

- operating room;
- intensive care;
- emergency lighting;
- critical communications;
- minimal patient-record access;
- life-support devices.

This is regime-sensitive islanding:

```text
shed non-vital
preserve vital
trace switching
escalate restoration
review after event
```

### 12.4 Cognitive publication workflow

The same regime logic applies to knowledge work.

Ordinary regime: a draft can be produced and revised normally.

Perturbed regime: an objection appears; a source is missing; uncertainty rises.

Critical regime: the publication has legal, political, medical, financial or reputational stakes. Stronger review, source verification, claim registry, human arbitration and correction channels become mandatory.

Recovery regime: public feedback returns to the corpus.

This connects capability regimes with Reality Safety.

---

## 13. Homeostasis and allostasis

Ordinary operation resembles homeostasis: maintaining variables within viable ranges.

Regime transition resembles allostasis: changing the operating mode under stress.

Fractanet should therefore not only maintain an ordinary steady state. It should support controlled shifts of regime.

```text
homeostasis
= keep ordinary variables inside viable bounds

allostasis
= change operating regime when the stressor changes the constraints
```

Capability regimes are the operational expression of allostasis in a packetized architecture.

---

## 14. Reality Safety connection

Capability regimes also matter for Reality Safety.

The higher the stakes and uncertainty, the stronger the required trace should become. Crisis must not become an opaque exception zone. On the contrary:

> **The more constrained the decision, the more recoverable the justification must be after the fact.**

This does not mean every low-level act must be recorded forever. It means trace policy should scale with regime:

| Regime | Trace policy |
|---|---|
| Ordinary | minimal or scoped trace |
| Perturbed | additional observations |
| Degraded | route/fallback trace |
| Critical | reinforced trace |
| Vital | forensic trace, audit path, responsibility record |
| Recovery | correction, reintegration, lessons learned |

---

## 15. Integration into `fractanet.md`

This document should be referenced from `research/fractanet.md` rather than absorbed wholesale.

Recommended minimal integration:

1. Add `FractaVolta/research/capability_regimes.md` to `related_documents` and `related_document_urls`.
2. Add tags: `capability-regimes`, `decision-under-uncertainty`, `allostasis`, `crisis-regime`.
3. Add one reading-guide commitment:

```text
8. Capability regimes — Fractanet does not route capacity in an abstract vacuum. Every packet circulates under a regime of constraints: ordinary, perturbed, degraded, critical, vital or recovery. COP must qualify the regime, route accordingly, preserve local safety invariants, escalate when needed, and reinforce traces as stakes and uncertainty increase.
```

4. Add a short section after `## 8. Dispatch` or after `## 15. COP as supervision plane`:

```markdown
## Capability regimes and decision under uncertainty

Fractanet does not route capacity in an abstract vacuum. A capability is always exercised under constraints: time available, uncertainty, stakes, reversibility, locality, mandate, available resources, preemption rights, trace requirements and fallback options.

The binary distinction between normal and crisis is therefore insufficient. A Fractanet packet may circulate under ordinary, perturbed, degraded, critical, vital or recovery regimes. COP should qualify the regime, route the packet accordingly, preserve local safety invariants, escalate when needed, and reinforce traces as uncertainty and stakes increase.

The companion document [`capability_regimes.md`](capability_regimes.md) develops this doctrine as fractal decision under constraints of uncertainty.
```

This keeps `fractanet.md` readable while making the doctrine central.

---

## 16. Claims

### CR-01 — Regimes are not binary

Capable systems do not simply pass from normal to crisis. They traverse graded regimes of constraint, uncertainty, stakes and reversibility.

### CR-02 — Decisions are regime-relative

A decision is not good in the abstract. It is admissible, or not, in a given regime of deadline, uncertainty, mandate, resources, stakes and reversibility.

### CR-03 — Invariants are fractal

At every scale, the system must preserve some combination of safety, traceability, fallback, responsibility, correction and continuity. Their implementation changes; their function recurs.

### CR-04 — COP orchestrates regime transitions

COP should qualify regimes, route packets, trigger escalation, supervise preemption, preserve traces and support recovery.

### CR-05 — RAIX capacity is regime-sensitive

Redundant capacity should not be active everywhere all the time. It should be mobilizable when the regime requires it.

### CR-06 — Local safety invariants remain hard

Networked crisis intelligence may augment local decision, but should not replace hard local fallback when deadlines are too short or communication is unreliable.

### CR-07 — Higher regimes require stronger traces

Crises should not become opaque exceptions. Higher uncertainty and higher stakes require stronger traceability, within feasible technical and privacy limits.

### CR-08 — Preemption must be governed

A capability may preempt ordinary priorities only under explicit mandate, scope, deadline, trace and recovery rules.

### CR-09 — Recovery is part of the regime architecture

Post-event audit, correction, reintegration and de-escalation are part of the system, not administrative afterthoughts.

---

## 17. Non-claims

This document does not claim that:

- all decisions can be automated;
- external compute can replace local safety;
- every domain can share the same regime thresholds;
- crisis should justify opaque exceptional power;
- all traces should be global or permanent;
- RAIX eliminates the need for domain engineering;
- COP eliminates human responsibility;
- a conceptual regime ladder is enough for safety certification.

The claim is narrower:

> **Fractanet should route and govern capacity according to explicit, graded and traceable regimes of constraint and uncertainty.**

---

## 18. Open questions

1. What is the minimal canonical list of regimes?
2. Should regimes be ordinal, multidimensional, or both?
3. How should regime thresholds be domain-specific?
4. What is the minimum `regime` field for a Cognitive Packet?
5. Which COP events are mandatory for regime transition?
6. How should preemption be represented in the envelope?
7. How should trace policy scale with regime without violating privacy or producing unmanageable logs?
8. How should regime transitions be simulated and tested?
9. How should human override, refusal and appeal be represented in critical or vital regimes?
10. What is the first narrow demonstrator: autonomous vehicle, hospital power, ambulance corridor, API gateway, or cognitive publication workflow?

---

## 19. Continuation

Recommended next actions:

1. Add a short anchor in `research/fractanet.md`.
2. Update `research/index.md`.
3. Extract the `cognitive_packet.regime` sketch into a future packet schema note.
4. Connect this document to future RAIX taxonomy work.
5. Produce one concrete scenario note: autonomous vehicle or hospital power failure.
6. Later, define a simulation profile for regime transitions.

---

## 20. Closing formula

```text
RAIX supplies distributed capacity.
COP qualifies regimes and routes packets.
Fractanet connects the capacities.
Reality Safety keeps the acts traceable, contestable and corrigible.
```

A shorter formula:

> **Deciding means selecting an admissible action under a regime of constraints and uncertainty.**

And the architectural form:

```text
not everything local
not everything central
local invariants
networked capacities
graded regimes
traceable transitions
human responsibility where it matters
```
