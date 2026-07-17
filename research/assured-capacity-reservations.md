---
title: "Assured Capacity Reservations"
subtitle: "SLA priority, insurance chains, skin in the game, and the anti-arson invariant"
description: "Source architecture and market-design note defining traceable capacity promises, reservations, SLA priority, degraded delivery, insurance and reinsurance, settlement, and structural protections against profiting from self-created scarcity."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
date: "2026-07-17"
version: "0.1-draft"
status: "source working paper — business and governance hypothesis under human validation"
license: "CC BY-SA 4.0"
language: "en"
repository: "JeanHuguesRobert/FractaVolta"
canonical_path: "FractaVolta/research/assured-capacity-reservations.md"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/assured-capacity-reservations.md"
document_role: "source"
document_kind: "architecture-and-market-design"
visibility: "public"
lifecycle_state: "working"
source_or_derived: "source-document"
human_validation_required: true
related_documents:
  - "FractaVolta/research/garanteed_inference.md"
  - "FractaVolta/research/capability_regimes.md"
  - "FractaVolta/research/generalized_packet_networks.md"
  - "FractaVolta/research/ownership_packets_and_cop.md"
  - "FractaVolta/research/fractanet.md"
  - "FractaVolta/research/fractalog.md"
  - "Inox/research/inox-images-lineages-and-hibernation.md"
  - "inseme/packages/cop-core/Invariants.md"
  - "cogentia/COGENTIA.md"
provenance:
  origin_type: "conversation"
  origin_repository: "unknown"
  origin_ref: "Conversation checkpoint on SLA priority, paid time-to-action, reservations, insurance/reinsurance, skin in the game, degraded recovery, informational asymmetry, and the anti-pompier-pyromane requirement — 2026-07-16/17"
  origin_date: "2026-07-16"
  derived_from:
    - "FractaVolta/research/garanteed_inference.md"
    - "FractaVolta/research/capability_regimes.md"
    - "FractaVolta/research/generalized_packet_networks.md"
    - "FractaVolta/research/ownership_packets_and_cop.md"
    - "inseme/packages/cop-core/Invariants.md"
    - "cogentia/COGENTIA.md"
review:
  status: "unreviewed"
  reviewed_by: []
update_policy: "UP-DEFAULT-REVIEWED"
tags:
  - assured-capacity
  - reservation
  - sla
  - priority
  - insurance
  - reinsurance
  - skin-in-the-game
  - anti-capture
  - anti-arson
  - degraded-mode
  - fractanet
---

# Assured Capacity Reservations

## SLA priority, insurance chains, skin in the game, and the anti-arson invariant

*Source working paper — v0.1-draft — business and governance hypothesis — human validation required*

---

## 1. Purpose

FractaVolta and Fractanet describe infrastructures in which energy, compute,
inference, logistics, storage, and other capabilities can be routed as bounded,
traceable units. `Guaranteed Inference` already states the market intuition:
critical users do not merely buy a cheap operation; they buy assurance that an
operation remains possible when the optimized path is unavailable.

This document generalizes that intuition into a capacity-reservation model and
adds the missing governance constraint.

The desired chain is:

```text
declared capacity
  -> verified capacity
  -> reservation
  -> promise / SLA
  -> activation request
  -> prioritized or degraded delivery
  -> trace
  -> settlement
  -> penalty or reward
  -> insurance / reinsurance feedback
```

The economic proposition is attractive because it sells something almost every
actor values: the power to act in time.

The same proposition is dangerous if the actor selling protection can create,
aggravate, hide, or prolong the crisis against which protection is sold.

The central invariant is therefore:

> No actor should be able to increase its net revenue, power, priority, or
> control by creating, aggravating, concealing, or strategically prolonging the
> scarcity or degradation against which it sells protection.

This is the **anti-arson invariant**, corresponding to the French expression
*pompier pyromane*.

The document treats that invariant as an architectural requirement, not a moral
promise about the present operator.

---

## 2. Status and claim discipline

This is a source architecture and market-design hypothesis.

It does not claim that:

- a regulated insurance product already exists;
- any FractaVolta entity is licensed as an insurer or reinsurer;
- the mechanisms satisfy French, European, or other insurance law;
- all causes of scarcity can be attributed perfectly;
- reserves eliminate correlated or systemic risk;
- a cryptographic proof proves physical availability by itself;
- nonprofit destination makes extraction automatically ethical;
- crisis priority should always be auctioned to the highest bidder;
- every scarce capability should be commercialized.

Legal, actuarial, competition, safety, and sector-specific review remain
necessary before deployment.

---

## 3. The time-to-action proposition

### 3.1 What the customer buys

The customer does not merely buy a resource unit. The customer buys a bounded
claim about future action:

- that capacity has been reserved;
- that a request will enter a defined service class;
- that fallback paths exist;
- that degraded alternatives are known;
- that delivery and failure will be measured;
- that failure has consequences for the promisor;
- that a claim can be reviewed and settled.

The core value can be summarized as:

```text
ordinary market:      buy a unit when available
assured-capacity:     buy a governed option to act within constraints
```

### 3.2 Museum ticket analogy

A priority museum ticket is a useful low-stakes analogy. The customer pays more
to spend less time in the ordinary queue. The museum can sell that promise only
because it controls admission capacity and queue policy.

The analogy exposes the abuse risk: the museum must not deliberately slow the
ordinary queue merely to make premium tickets more valuable.

Critical infrastructure raises the stakes:

- inference needed during an incident;
- emergency energy;
- compute needed for recovery;
- cold storage preserving medicine;
- communications during a disaster;
- transport or logistics capacity;
- restoration of a dormant digital capability.

In extreme cases the choice is not convenience versus delay. It is action now
versus irreversible loss.

### 3.3 Priority is not capacity

Priority changes ordering. It does not create physical capacity.

An honest product must distinguish:

- **queue priority** — earlier service from shared capacity;
- **reserved capacity** — capacity withheld or protected for a class;
- **redundant capacity** — an independent fallback resource;
- **reconstructible capacity** — a slower path that can be rebuilt;
- **substitutable capability** — a different service that achieves a bounded
  acceptable outcome;
- **financial compensation** — money after failure, which is not equivalent to
  timely action.

---

## 4. Vocabulary

### 4.1 Capacity

**Capacity** is the bounded ability of a resource or network to perform a
declared class of useful work under stated conditions.

### 4.2 Capability

**Capability** combines capacity with authority, interface, constraints, and
an executable path. Potential becomes capability only when it can be activated
legitimately and operationally.

### 4.3 Reservation

A **reservation** is an exclusive or quantified claim on future capacity for a
declared beneficiary, interval, service class, and trigger policy.

### 4.4 Promise

A **promise** is a traceable commitment by a responsible identity. It is not the
capacity itself. It becomes credible through evidence, exposure to loss, and a
settlement mechanism.

### 4.5 Service-level objective

A **service-level objective** (SLO) is a measurable target such as latency,
throughput, availability, restoration time, proof level, or degraded outcome.

### 4.6 Service-level agreement

An **SLA** is a governed agreement that binds SLOs to parties, measurement,
exceptions, remedies, and evidence.

### 4.7 Assurance

**Assurance** is justified confidence based on observable mechanisms and
evidence. It is stronger than assertion and weaker than absolute certainty.

### 4.8 Insurance

**Insurance** mutualizes defined financial consequences of specified failures.
It does not manufacture the missing physical capacity after the fact.

### 4.9 Reinsurance

**Reinsurance** transfers part of the insurer's aggregate exposure to another
capital and risk pool. It must not conceal correlated dependence behind several
nominally distinct entities.

### 4.10 Degraded service

A **degraded service** preserves a declared minimum outcome with reduced speed,
quality, scale, convenience, or feature set while keeping integrity and safety
constraints.

### 4.11 Trigger

A **trigger** is an observable condition that permits activation of a reserved
or exceptional service path.

### 4.12 Settlement

**Settlement** applies the agreed economic and governance consequences to the
observed delivery, failure, contribution, or dispute.

---

## 5. Roles

The architecture distinguishes roles even when one legal entity initially
performs several of them.

| Role | Responsibility |
|---|---|
| Capacity owner | controls or owns the underlying scarce resource |
| Operator | runs the resource or routing service |
| Promisor | signs the reservation/SLA commitment |
| Beneficiary | receives the promised capability |
| Principal | authorizes purchase or activation |
| Broker/router | matches demand to capacity |
| Meter | produces measurements |
| Trigger oracle | attests activation conditions |
| Auditor | checks evidence and controls |
| Insurer | mutualizes specified financial failure consequences |
| Reinsurer | absorbs defined aggregate insurer exposure |
| Adjudicator | resolves disputed facts or contract interpretation |
| Regulator/governor | sets admissibility and public-interest constraints |
| Risk contributor | actor whose actions affect scarcity probability/severity |

Role identity and conflicts MUST be disclosed in the promise record.

---

## 6. Capacity packet model

A reservation can be represented as a governed packet or packet family:

```text
CapacityDeclaration
  -> CapacityEvidence
  -> ReservationOffer
  -> ReservationCommitment
  -> ActivationRequest
  -> DeliveryEvent | DegradedDelivery | FailureEvent
  -> Claim
  -> Settlement
```

Each packet occupies resources and has:

- identity;
- issuer;
- beneficiary;
- validity interval;
- quantity and units;
- service class;
- dependencies;
- proof level;
- freshness;
- price and exposure;
- authority and mandate;
- causal links;
- trace requirements.

The transport mechanism may vary. The logical event and evidence model must
remain portable.

---

## 7. Reservation lifecycle

### 7.1 Declare

The owner or operator declares potential capacity with units, location,
interval, constraints, and dependencies.

### 7.2 Verify

Evidence supports the declaration. Evidence may include:

- telemetry;
- inventory;
- test activation;
- energy/storage state;
- maintenance condition;
- dependency status;
- independent attestation;
- historical delivery record.

### 7.3 Offer

The promisor publishes a bounded reservation offer with price, SLOs, trigger,
exclusions, remedy, and expiry.

### 7.4 Reserve

Capacity is allocated, leased, withheld, or otherwise protected according to
the offer. Overbooking policy is explicit.

### 7.5 Underwrite

The promisor, insurer, and optionally reinsurer accept defined exposure.
Collateral, capital, or another loss-bearing mechanism is locked or evidenced.

### 7.6 Activate

An authorized request presents the reservation identity and required trigger
evidence.

### 7.7 Deliver

The operator provides full, degraded, substituted, or failed service. The exact
outcome is recorded.

### 7.8 Settle

Measurements are compared with contractual objectives. Payment, refund,
penalty, insurance claim, clawback, reputation update, or dispute follows.

### 7.9 Learn

Capacity estimates, prices, risk models, and admissibility policy are corrected
without rewriting prior events.

---

## 8. Promise backing and skin in the game

A promise that exposes only the beneficiary to loss is not assurance.

The promisor should have measurable downside when an avoidable promise fails.
Possible backing mechanisms include:

- prepaid capacity held in reserve;
- collateral or escrow;
- performance bond;
- mutual guarantee fund;
- retained earnings or regulatory capital;
- reputation stake with real access consequences;
- insurer coverage;
- reinsurer coverage;
- contractual liability;
- public-service duty.

The backing must be proportional to the plausible consequence and must not be
illusory, circular, or controlled entirely by the promisor.

### 8.1 Skin in the game boundary

Skin in the game is appropriate at the action and promise layer: the actor who
signs a consequential commitment should bear consequences for abuse or
negligence.

It must not become a rule that political voice or basic human protection belongs
only to actors wealthy enough to stake capital.

### 8.2 Nonprofit destination is insufficient

Using profits for nonprofit or public-interest purposes may improve the
distribution of benefits. It does not remove the need for anti-abuse structure.

The architecture must remain acceptable if:

- leadership changes;
- the operator is sold;
- incentives become hostile;
- a subsidiary seeks profit maximization;
- a crisis concentrates power;
- mission claims are false.

Ethics must survive changes of intention.

---

## 9. The anti-arson invariant

### 9.1 Normative statement

> A participant MUST NOT obtain a greater net benefit from an avoidable scarcity
> or degradation to which it materially contributed than it would have obtained
> from honest ordinary operation, after applying attributable costs, penalties,
> clawbacks, and liability.

This is a mechanism-design objective, not a claim that causality or intent can
always be determined perfectly.

### 9.2 Why traces alone are insufficient

An immutable log can faithfully record an abusive system. Traceability is
necessary, not sufficient.

The system also needs:

- limits on role concentration;
- precommitted rules;
- independent measurements;
- economic exposure;
- review and contestability;
- remedies;
- alternative routes and providers.

### 9.3 Formal incentive target

Let:

- `B_i(s)` be actor `i`'s gross benefit in state `s`;
- `C_i(s)` be the attributable cost imposed by actor `i`;
- `P_i(s)` be penalties, clawbacks, and liability;
- `R_i(s)` be legitimate reservation revenue;
- `s0` be the counterfactual honest-operation state;
- `s1` be a scarcity state materially worsened by actor `i`.

The design target is:

```text
Net_i(s1) = B_i(s1) + R_i(s1) - C_i(s1) - P_i(s1)

Net_i(s1) <= Net_i(s0)
```

when the additional scarcity is avoidable and materially attributable to the
actor under the agreed evidence standard.

No formula eliminates factual dispute. The formula states which incentive the
architecture is trying to remove.

---

## 10. Anti-arson controls

### AA-01 — Pre-event capacity evidence

A promisor MUST record capacity evidence before the trigger window. Evidence
created only after failure has weaker assurance.

### AA-02 — Separation of critical roles

For high-consequence promises, the same uncontrolled identity SHOULD NOT be the
sole operator, meter, trigger oracle, auditor, and adjudicator.

### AA-03 — No self-triggered premium without independent evidence

An actor that benefits from crisis pricing or priority MUST NOT unilaterally
declare the trigger that unlocks that benefit.

### AA-04 — Baseline and counterfactual

The agreement MUST define an ordinary-operation baseline and the evidence used
to detect avoidable capacity withdrawal, queue degradation, or price inflation.

### AA-05 — Reservation terms fixed before crisis

Quantity, measurement method, priority rule, remedy, and price formula SHOULD be
committed before the activation event. Emergency amendments require enhanced
trace and review.

### AA-06 — Withdrawal trace

Capacity removal, maintenance, reprioritization, and dependency loss MUST leave
timely, attributable records. Silent withdrawal is a contract failure.

### AA-07 — Gain escrow and clawback

Extra crisis-derived revenue MAY be held in escrow until review. Avoidable or
manipulated scarcity MUST support clawback beyond a simple refund where law and
contract permit.

### AA-08 — Liability follows control and contribution

Liability SHOULD follow the degree of control, knowledge, contribution, and
failure to mitigate. Diffuse subcontracting MUST NOT erase responsibility.

### AA-09 — Portability and exit

Beneficiaries SHOULD be able to export reservation records, evidence, and
claims, and to route toward alternative providers where technically possible.

### AA-10 — Minimum ordinary service protection

Priority products MUST declare their effect on ordinary users. They MUST NOT
create hidden starvation of essential baseline service.

### AA-11 — Independent replication of evidence

Consequential measurements and promise records SHOULD be replicable or anchored
outside the promisor's sole control.

### AA-12 — Contestability

Affected actors MUST have a route to challenge trigger, measurement, causality,
priority, or settlement decisions.

### AA-13 — Conflict graph

Material ownership, control, underwriting, data-provider, and adjudication
relationships MUST be disclosed as a conflict graph for critical commitments.

### AA-14 — Correlated-risk disclosure

Nominally independent fallbacks, insurers, or data sources MUST disclose shared
energy, network, cloud, ownership, geography, software, and financing
dependencies.

### AA-15 — No sabotage by interface

The operator MUST NOT make ordinary interoperability artificially fragile in
order to increase dependence on its emergency service.

### AA-16 — Crisis authority expires

Exceptional routing, pricing, access, or control powers MUST carry expiry,
scope, and review conditions. Crisis mode MUST NOT silently become permanent.

---

## 11. Queue priority and fairness

### 11.1 Priority classes

A service may define classes such as:

| Class | Example | Admission basis |
|---|---|---|
| Vital | life/safety preservation | public mandate and verified trigger |
| Critical | irreversible high-cost failure prevention | reservation + trigger |
| Recovery | restoration of wider service | regime-aware policy |
| Reserved commercial | contracted latency/capacity | reservation and price |
| Ordinary | normal best effort | fair queue |
| Opportunistic | interruptible surplus use | low price, preemptible |

Payment alone SHOULD NOT outrank legally or democratically protected vital
service.

### 11.2 Priority budget

Priority consumes other users' waiting time. The queue policy SHOULD expose:

- maximum reserved share;
- maximum preemption duration;
- starvation bound;
- class-specific queue delay;
- emergency override conditions;
- compensation or public-interest rules where appropriate.

### 11.3 Priority admission

A ticket proves eligibility for a class. It does not authorize arbitrary
resource seizure beyond the ticket's quantity, interval, and scope.

### 11.4 Protected commons

Some capacity may be held as a commons or civil reserve rather than auctioned.
The architecture must support non-market mandates alongside paid reservations.

---

## 12. Full, degraded, substituted, and failed delivery

Delivery is not binary.

| Outcome | Meaning | Settlement implication |
|---|---|---|
| Full | all required SLOs met | ordinary payment |
| Degraded-accepted | declared minimum outcome met | adjusted payment/trace |
| Substituted-accepted | alternate capability achieved agreed purpose | contract-specific |
| Late-useful | late but still valuable | partial remedy |
| Late-useless | action arrived after utility window | failure despite completion |
| Refused-safe | unsafe or unauthorized action correctly refused | not necessarily provider failure |
| Failed-capacity | promised resource unavailable | remedy/claim |
| Failed-integrity | result cannot be trusted | severe failure |

### 12.1 Time matters

For critical capacity, utility may decay sharply with time.

```text
value(t) -> 0 after the action window
```

A refund after the deadline does not restore lost agency. This is why physical
reserve, fallback, and proof are distinct from financial insurance.

### 12.2 Degraded integrity rule

Degraded operation MAY reduce speed, fidelity, scale, redundancy, or
convenience. It MUST NOT silently relax safety, identity, authorization, or
evidence requirements declared as invariant.

---

## 13. Assurance stack

Assurance should be layered:

```text
physical or computational capacity
  + measured current state
  + protected reservation
  + independent fallback
  + activation authority
  + queue policy
  + trace and proof
  + financial backing
  + insurance
  + reinsurance
  + adjudication
```

No layer should claim to substitute for every other layer.

### 13.1 Proof of capacity

Evidence may include:

- periodic challenge execution;
- signed telemetry;
- fuel/energy/storage state;
- reserved inventory;
- independent network reachability;
- successful failover rehearsal;
- maintenance and incident history;
- dependency graph and correlated-risk analysis.

Evidence has freshness and confidence. Old proof is not current capacity.

### 13.2 Proof of reservation

Proof of capacity does not prove that capacity remains unallocated. A
reservation registry must prevent incompatible double commitments or disclose
overbooking explicitly.

### 13.3 Proof of delivery

Proof should bind:

- request identity;
- reservation identity;
- accepted trigger;
- start/end times;
- resource path;
- result or refusal;
- quality and degraded flags;
- measurement identities;
- relevant trace anchors.

---

## 14. Insurance and reinsurance chain

### 14.1 Physical promise versus financial promise

The operator promises an action path. The insurer promises financial settlement
for specified failure. Those are different products.

### 14.2 Chain of value

```text
beneficiary pays reservation premium
  -> operator protects capacity
  -> promisor accepts performance exposure
  -> insurer mutualizes defined failures
  -> reinsurer absorbs aggregate tail exposure
  -> auditor/adjudicator supports settlement
```

### 14.3 Skin in the chain

Every promisor in the chain SHOULD retain some exposure. Complete risk transfer
can destroy diligence.

The retained layer must be large enough to matter but not so large that one
failure collapses the service needed for recovery.

### 14.4 Circular guarantees

The chain is not independent if:

- operator, insurer, and reinsurer are the same economic controller;
- all depend on one bank, cloud, grid, or data source;
- collateral is issued by the same failing party;
- the fallback depends on the primary path;
- claims are adjudicated solely by the promisor.

Circularity must be represented in the conflict and dependency graph.

### 14.5 Mutual and public forms

Assurance may be commercial, mutual, cooperative, civic, or public. The same
trace, exposure, and anti-arson questions apply, although pricing and governance
may differ.

---

## 15. Measurement and evidence

### 15.1 Measurement plan

Every SLA should define before activation:

- metric name and unit;
- observation window;
- clock source and synchronization tolerance;
- measurement point;
- acceptable uncertainty;
- missing-data policy;
- independent witness policy;
- retention period;
- privacy classification;
- dispute procedure.

### 15.2 Evidence accessibility

Trace existence is insufficient when only the promisor can query or interpret
it.

Consequential evidence should be:

- attributable;
- time-bounded;
- exportable;
- machine-readable;
- explainable to affected humans;
- independently verifiable where feasible;
- protected against unilateral deletion;
- privacy-aware;
- linked to correction events.

### 15.3 Symmetry of observability

The promisor should not possess a decisive informational advantage merely
because it controls the instrumentation. Beneficiaries and authorized auditors
need sufficient access to test the promise.

This does not require publishing private data. It requires a governed evidence
surface adequate for accountability.

---

## 16. Pricing

### 16.1 Price components

A reservation price may reflect:

- capacity opportunity cost;
- storage or standby cost;
- expected activation frequency;
- maintenance and rehearsal;
- fallback independence;
- energy and network cost;
- proof and audit cost;
- capital at risk;
- insurance and reinsurance premium;
- expected degradation;
- scarcity externalities;
- public-interest subsidy or mandate.

### 16.2 Do not price only the happy path

The marginal cost of an ordinary API call is not the cost of retaining capacity
under stress. Honest pricing must expose the reserve and assurance layers.

### 16.3 Crisis pricing boundary

Price may signal real scarcity, but unlimited crisis pricing can reward
withholding and exploit actors with no alternative.

Possible controls include:

- precommitted formulas;
- maximum multipliers;
- public/vital service classes;
- audited cost basis;
- windfall escrow;
- ex-post review;
- competition and portability;
- prohibition of self-created scarcity gains.

The correct mix is sector- and jurisdiction-specific.

### 16.4 Payment for speed

The legitimate product is a prior reservation or independently justified
priority, not a ransom extracted after the provider has created dependence.

---

## 17. Trigger governance

Triggers may be:

- objective threshold;
- beneficiary declaration;
- public authority declaration;
- multi-source attestation;
- automated regime transition;
- operator incident declaration;
- contract schedule;
- combination of the above.

High-consequence triggers SHOULD use more than one evidence source when delay
does not create greater harm.

### 17.1 Fast action

Emergency systems sometimes cannot wait for full adjudication. They may permit
optimistic activation followed by review.

The activation must still have:

- bounded scope;
- accountable principal;
- expiry;
- preserved evidence;
- reversible components where possible;
- mandatory after-action review.

### 17.2 False positive and false negative

Trigger design must price both:

- activating scarce reserve unnecessarily;
- refusing reserve when it was needed.

The acceptable balance depends on consequence, reversibility, and regime.

---

## 18. Dependency and correlated-risk graph

Every critical offer should disclose material dependencies:

```text
capacity resource
  -> energy
  -> network
  -> cooling
  -> identity
  -> storage
  -> software
  -> personnel
  -> finance
  -> legal authority
```

Two providers are not independent merely because they have different brands.

A machine-readable dependency graph can support:

- concentration limits;
- route diversity;
- insurer accumulation analysis;
- crisis simulation;
- anti-capture review;
- honest availability claims.

Unknown dependencies must remain `unknown`, not silently independent.

---

## 19. Settlement and remedies

Remedies may include:

- service credit;
- refund;
- penalty;
- collateral release to beneficiary;
- insurance payment;
- clawback of crisis premium;
- loss of future reservation eligibility;
- reputation event;
- mandatory remediation;
- public incident report;
- governance intervention;
- legal claim.

### 19.1 Remedy proportionality

The remedy should reflect:

- harm and lost utility;
- provider control;
- avoidability;
- disclosure quality;
- mitigation effort;
- repeated behavior;
- intentional manipulation;
- systemic consequence.

### 19.2 No cheap breach option

If the maximum penalty is lower than the profit from withholding reserved
capacity for another buyer, breach becomes a rational option. Exposure must be
large enough to resist profitable diversion.

### 19.3 Preserve disputes

Settlement must not erase the original claim, counter-evidence, or dissent.
Corrections are new events.

---

## 20. Anti-capture and market structure

Assured capacity can concentrate power because the reserve operator becomes
indispensable during crisis.

Countermeasures include:

- open event and manifest formats;
- interoperable activation interfaces;
- portable reservation records;
- multiple independent operators;
- transparent queue policy;
- public-interest reserve;
- separation of commercial and adjudication roles;
- time-limited emergency authority;
- audit by affected communities;
- local degraded capability;
- exit and reconstruction paths.

The system should make dependence visible before crisis.

---

## 21. Example: guaranteed inference

```text
hospital reserves inference capacity
  -> operator proves target model/profile and fallback hardware
  -> insurer underwrites defined non-delivery loss
  -> regional outage triggers multi-source attestation
  -> request routes to fallback node
  -> provenance and latency recorded
  -> full or degraded result delivered
  -> SLA settled
```

Anti-arson questions:

- Did the fallback operator contribute to primary-route fragility?
- Was capacity genuinely reserved before the outage?
- Could the operator profit by withholding ordinary capacity?
- Are primary and fallback paths actually independent?
- Can the hospital inspect the evidence?

---

## 22. Example: energy reserve

```text
critical cold store reserves battery/energy packet capacity
  -> state of charge and inverter condition attested
  -> capacity cannot be double-reserved silently
  -> grid event activates reserve
  -> delivered energy and losses measured
  -> ordinary, degraded, or failed outcome settled
```

The energy provider must not create artificial local scarcity by exporting or
withholding committed reserve to increase emergency prices.

---

## 23. Example: Inox wake from cold storage

```text
critical actor needs to wake
  -> hot native image missing
  -> assured artifact retrieval class invoked
  -> semantic base and snapshot fetched
  -> hashes and authority verified
  -> native materialization rebuilt
  -> actor wakes later but correctly
```

The SLA can price expected wake time and replicas. It cannot authorize bypassing
hash verification to meet the deadline.

---

## 24. Minimum event envelopes

### 24.1 Reservation commitment

```yaml
kind: fractanet.capacity-reservation.v1
reservation_id: urn:uuid:...
promisor: <identity>
beneficiary: <identity>
capacity_ref: <logical capability>
quantity: 100
unit: inference-request
valid_from: <time>
valid_until: <time>
service_class: critical
slos:
  activation_latency_ms: 5000
  minimum_result_profile: <profile>
trigger_policy: <digest or reference>
measurement_plan: <digest or reference>
price_terms: <digest or protected reference>
remedy_terms: <digest or protected reference>
capacity_evidence: []
conflict_graph: <digest>
dependency_graph: <digest>
mandate: <reference>
signature: <signature>
```

### 24.2 Delivery event

```yaml
kind: fractanet.capacity-delivery.v1
reservation_id: urn:uuid:...
activation_id: urn:uuid:...
request_time: <time>
start_time: <time>
finish_time: <time>
outcome: full | degraded | substituted | refused-safe | failed
metrics: {}
resource_path: []
proof_refs: []
regime: ordinary | perturbed | degraded | critical | vital | recovery
```

### 24.3 Settlement event

```yaml
kind: fractanet.capacity-settlement.v1
reservation_id: urn:uuid:...
delivery_event: <digest>
claim_refs: []
decision: paid | adjusted | refunded | penalized | disputed
payment: {}
penalty: {}
clawback: {}
insurer_event: <reference or null>
reinsurer_event: <reference or null>
adjudicator: <identity or unknown>
evidence_refs: []
```

These are conceptual envelopes, not final legal schemas.

---

## 25. Required tests and simulations

Before real deployment, a prototype should test:

- double reservation;
- capacity withdrawal before activation;
- stale capacity evidence;
- false crisis trigger;
- conflicting trigger sources;
- operator as sole meter;
- insurer sharing the primary dependency;
- profitable breach attempt;
- queue starvation from premium load;
- ordinary-service degradation before premium sales;
- missing evidence;
- interrupted delivery;
- degraded but useful delivery;
- late useless delivery;
- dispute and correction;
- operator insolvency;
- insurer insolvency;
- correlated regional failure;
- portability to another provider;
- emergency power expiry;
- clawback after attributed manipulation.

Adversarial simulation is part of the architecture, not optional polish.

---

## 26. Implementation sequence

### C0 — Contract vocabulary and fixtures

- accept the vocabulary for experiment;
- create example reservation/delivery/settlement events;
- create negative fixtures;
- keep commercial terms fictitious;
- perform legal-category review before real offers.

### C1 — Reservation registry prototype

- capacity declarations;
- exclusive/quantified reservations;
- TTL and expiry;
- double-reservation prevention;
- append-only events and projections;
- exportable evidence.

### C2 — Queue and degraded-service simulator

- ordinary and priority classes;
- starvation bounds;
- reserved-share limits;
- activation windows;
- degraded outcomes;
- utility decay with time;
- transparent scenario replay.

### C3 — Anti-arson controls

- independent trigger adapter;
- capacity-withdrawal events;
- conflict/dependency graph;
- crisis-revenue escrow simulation;
- profitable-withholding tests;
- contestation workflow.

### C4 — Insurance-chain experiment

- fictitious insurer/reinsurer identities;
- retained exposure;
- aggregate-risk calculation;
- correlated dependency disclosure;
- claim and settlement events;
- insolvency and recovery scenarios.

### C5 — Domain pilot

Choose one bounded, non-life-critical pilot such as:

- artifact retrieval/wake SLA;
- interruptible compute with reserved fallback;
- laboratory inference queue;
- simulated energy-storage reservation.

Do not begin with a claim whose failure could injure people.

---

## 27. Acceptance criteria for an experimental profile

An experimental implementation is acceptable only if:

- capacity and reservation are distinct objects;
- incompatible double reservation is rejected or explicit overbooking is shown;
- every promise has a responsible identity and mandate;
- measurement and remedy are committed before activation;
- full, degraded, substituted, refused, and failed outcomes are distinct;
- queue effects on ordinary users are measurable;
- crisis triggers cannot be controlled solely by the main beneficiary of crisis
  pricing;
- capacity withdrawal is traceable;
- conflict and dependency graphs are inspectable;
- the promisor bears meaningful downside for avoidable failure;
- profitable withholding scenarios fail economically after penalties;
- evidence can be exported and contested;
- exceptional authority expires;
- no production, insurance, or regulatory readiness is implied.

---

## 28. Proposed decisions

| ID | Decision | Status |
|---|---|---|
| ACR-001 | Treat assured capacity as a governed option to act, not merely a resource unit | proposed |
| ACR-002 | Distinguish queue priority, physical reserve, fallback, substitution, and financial compensation | proposed |
| ACR-003 | Require traceable promise backing and meaningful promisor downside | proposed |
| ACR-004 | Represent reservations, deliveries, claims, and settlements as immutable events | proposed |
| ACR-005 | Preserve integrity and authority constraints in degraded delivery | proposed |
| ACR-006 | Adopt the anti-arson invariant as a normative design objective | proposed |
| ACR-007 | Separate or independently attest critical operator, meter, trigger, audit, and adjudication roles | proposed |
| ACR-008 | Protect a minimum ordinary/vital service from hidden priority starvation | proposed |
| ACR-009 | Require conflict and correlated-dependency disclosure | proposed |
| ACR-010 | Make crisis-derived windfall subject to escrow, review, and possible clawback | proposed |
| ACR-011 | Treat evidence accessibility and contestability as part of assurance | proposed |
| ACR-012 | Make exceptional crisis authority scoped, expiring, and reviewable | proposed |

Human acceptance moves these decisions to `accepted-for-experiment`. It does
not authorize a regulated or life-critical service.

---

## 29. Open legal, actuarial, and governance questions

- When does a reservation become an insurance product under applicable law?
- Which remedies are enforceable versus merely reputational?
- How should force majeure interact with avoidable underinvestment?
- Which evidence standard establishes material contribution to scarcity?
- How is intent treated differently from negligence or unavoidable failure?
- Which entity may hold crisis-revenue escrow?
- What capital and liquidity requirements apply to each promise class?
- How are public-service obligations protected from premium starvation?
- How are insurer and reinsurer correlated exposures measured?
- Which data may be public, shared with auditors, or kept private?
- How are community harms represented when the direct contract has only two
  parties?
- Which governance body can invalidate an abusive queue or pricing policy?
- How is emergency action kept fast without making adjudication meaningless?
- Which promises should remain non-market public capabilities?

These questions require qualified legal and actuarial work before production.

---

## 30. Definition of success

The architecture succeeds experimentally when a reproducible scenario shows:

```text
capacity declared and tested
  -> reservation recorded without hidden double allocation
  -> promisor exposure locked
  -> independent trigger occurs
  -> request receives its declared service class
  -> full or degraded outcome measured
  -> ordinary queue impact visible
  -> evidence exportable
  -> failure produces automatic provisional remedy
  -> dispute can add evidence without rewriting history
  -> insurer/reinsurer exposure updates
  -> a simulated capacity-withholding strategy is less profitable than honest operation
```

The important result is not merely that premium customers are served first. It
is that future agency can be reserved while the seller remains unable to profit
from manufacturing the emergency.

---

## 31. Compact doctrine

```text
Potential is not capacity.
Capacity is not capability.
A promise is not a reserve.
A reserve is not a fallback.
A fallback is not insurance.
Insurance is not timely action.

Assurance requires evidence.
Promises require exposure.
Priority requires limits.
Crisis authority requires expiry.
Traces require access and contestability.

Sell the power to act.
Do not sell the fire after lighting it.
```
