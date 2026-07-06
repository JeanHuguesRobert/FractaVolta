---
title: "Ownership Packets and the Cognitive Orchestration Protocol"
subtitle: "Agents, identities, assets, mandates, custody, and ownership state in Fractanet"
description: "Working note v0.1 defining ownership as a versioned relation between identities and assets, represented in COP through events, proofs, projections, mandates, capabilities, claims, and disputes."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/ownership_packets_and_cop.md"
version: "0.1"
status: "working-note"
date: "2026-07-06"
license: "CC BY-SA 4.0"
tags:
  - ownership
  - cop
  - cognitive-orchestration-protocol
  - fractanet
  - identity
  - assets
  - mandates
  - distributed-systems
document_role: "source"
document_kind: "architecture-note"
visibility: "public"
lifecycle_state: "working"
ai_readability: "high"
---

# Ownership Packets and the Cognitive Orchestration Protocol

## Agents, identities, assets, mandates, custody, and ownership state in Fractanet

*Working note — v0.1 — 2026-07-06*  
*License: CC BY-SA 4.0*

---

## AI Navigation Map

This document is intentionally structured for both humans and AI agents.

Use this map first:

1. Core thesis: §1.
2. What COP is: §2.
3. Vocabulary: §3.
4. Ownership model: §4.
5. Asset typology: §5.
6. COP event model: §6.
7. Distributed consistency: §7.
8. Minimal schemas: §8.
9. Implementation rules: §9.
10. References: §13.

Core invariant:

```text
agent acts
identity answers
asset is affected
mandate authorizes
capability enables
custody records holding
ownership imputes title or share
claim asserts uncertainty
dispute exposes conflict
event records change
projection derives current state
```

---

## Abstract

The Cognitive Orchestration Protocol (COP) needs a precise model of ownership.

Fractanet routes and coordinates heterogeneous packets: data, energy, heat, matter, inference, cognition, money, votes, mandates, permissions, responsibilities, and physical goods. Some packets are fungible. Some are unique. Some can be fractioned. Some cannot. Some are consumed. Some are transferred. Some represent rights. Some represent claims.

This note proposes that **ownership is not a static field attached to an object**. In COP, ownership is a **versioned, provable, contestable relation between an identity and an asset**, produced by accepted events, constrained by domain rules, and projected into current state.

The model separates:

- the **agent** that acts;
- the **identity** that is recognized or held responsible;
- the **asset** that is owned, held, transferred, consumed, or disputed;
- the **mandate** that authorizes action on behalf of another identity;
- the **capability** that enables a limited operation;
- the **custody** relation that records practical holding;
- the **ownership event** that changes title or share;
- the **projection** that derives current ownership from the event log.

This distinction is essential for distributed systems. A person can own an asset without holding it. A service can operate on an asset without owning it. An AI agent can act without being the principal. A co-owner can own a share of title without owning a detachable part of the thing. A token can represent a claim without automatically settling legal ownership.

---

## 1. Core Thesis

### 1.1 Short form

```text
Ownership is a relation, not a property field.
```

More precisely:

```text
Ownership is a versioned, provable, contestable relation between an identity and an asset.
It is produced by events.
It is constrained by policies.
It is evidenced by proofs.
It is interpreted by registries.
It is projected into current state.
It can be disputed.
It can be corrected.
It should not be silently overwritten.
```

### 1.2 COP formula

```text
The network gives topology.
The packet gives operation.
Ownership gives imputation.
Mandate gives authority.
Capability gives executable power.
Trace gives verifiability.
```

### 1.3 Design rule

Do **not** model ownership only as:

```json
{
  "assetId": "X",
  "owner": "Y"
}
```

That representation hides:

- who changed ownership;
- who authorized the change;
- what proof exists;
- whether the object is fungible or non-fungible;
- whether ownership is shared;
- whether the change is accepted, provisional, claimed, or disputed;
- whether the actor was owner, custodian, delegate, service, or AI agent;
- whether the current state can be reconstructed.

A COP representation should instead use:

```text
stable asset identity
+ append-only ownership events
+ explicit authority and proof
+ validation rules
+ current-state projection
+ dispute and correction events
```

---

## 2. What COP Is

The **Cognitive Orchestration Protocol** is a protocol for coordinating cognitive, digital, institutional, and operational work across humans, AI agents, software services, registries, and physical systems.

COP is not merely a message format. It is a grammar of accountable action.

It answers:

```text
Who acted?
In which role?
On behalf of whom?
On what asset?
Using which mandate?
With which capability?
Under which rules?
Producing which effect?
Leaving which trace?
Replayable how?
Contestable by whom?
```

A minimal COP system contains:

```text
COPEvent        append-only record of something that happened
COPArtifact     durable object produced, used, or referenced by events
COPAgent        actor capable of performing steps
COPIdentity     subject recognized in a domain
COPMandate      explicit delegation from principal to delegate
COPCapability   limited executable authorization
COPProjection   derived view reconstructed from events
COPPolicy       rules used to validate or interpret events
COPStore        persistent event/artifact substrate
```

This note adds:

```text
COPAsset
COPOwnershipEvent
COPOwnershipState
COPCustody
COPClaim
COPDispute
```

In Fractanet, COP belongs primarily to the **control plane**.

```text
data plane:
  energy, heat, packets, goods, inference requests, files, messages, physical flows

control plane:
  identities, mandates, ownership, routing rules, proofs, events, policies, accountability
```

The data plane moves or transforms things. The control plane decides, records, authorizes, verifies, disputes, and reconstructs what happened.

---

## 3. Core Vocabulary

### Agent

An **agent** is an entity capable of acting within COP.

Examples:

```text
human user
AI assistant
software service
energy controller
registry node
automation
association officer
```

An agent performs operations. An agent is not necessarily the principal.

### Identity

An **identity** is a stable or verifiable designation of a subject in a domain.

Examples:

```text
person
association
company
public body
AI agent identity
device identity
household
collective
DID subject
```

An identity answers:

```text
Who or what is recognized as the subject of rights, duties, claims, mandates, or accountability?
```

### Asset

An **asset** is any thing, resource, right, claim, or operational unit over which COP may need to record ownership, custody, use, transfer, consumption, or dispute.

Examples:

```text
money
battery module
container
solar panel
land parcel
file
dataset
license
vote
mandate
energy packet
thermal packet
inference credit
water right
ticket
share
heritage object
```

### Ownership

**Ownership** is the recognized relation between an identity and an asset.

It may be:

```text
exclusive
shared
fractional
beneficial
legal
operational
provisional
claimed
disputed
non-transferable
```

### Control

**Control** is the practical ability to affect an asset.

Control is not ownership.

### Custody

**Custody** is physical or operational holding.

Custody is not ownership.

### Mandate

A **mandate** is an explicit authorization from a principal to a delegate.

It answers:

```text
Who is allowed to act for whom?
For what purpose?
On which assets?
During which period?
Under which constraints?
With which accountability?
```

### Capability

A **capability** is a limited executable authorization.

It answers:

```text
What operation can the holder perform?
```

A mandate is normative and relational. A capability is operational and executable.

### Claim

A **claim** is an assertion that may or may not be accepted as authoritative.

### Dispute

A **dispute** is an explicit conflict between claims, events, states, identities, or authorities.

COP should represent disputes directly. It should not erase them by forcing premature consistency.

---

## 4. Ownership Model

### 4.1 Fundamental separation

| Relation | Question answered | Example |
|---|---|---|
| Identity | Who is recognized? | Alice |
| Agency | Who acted? | AI worker 7 |
| Ownership | Who owns? | Alice owns asset X |
| Custody | Who holds? | Carrier holds parcel X |
| Control | Who can operate? | Service can execute action Y |
| Mandate | Who may act for whom? | Bob may sell X for Alice |

### 4.2 Core invariant

```text
An identity can own without direct control.
An agent can control without owning.
A custodian can hold without owning.
A mandate can authorize action without transferring ownership.
A capability can enable action without proving legitimacy.
A claim can assert ownership without settling it.
```

### 4.3 Ownership as bundle

Ownership may include several separable dimensions:

```text
title
benefit
use
revenue
transfer
exclusion
consumption
administration
custody
control
```

This avoids confusing:

```text
owner
possessor
user
administrator
beneficiary
custodian
mandatary
operator
licensee
controller
```

### 4.4 Ownership is domain-relative

Ownership is interpreted in a domain.

Examples:

```text
legal domain:      title
software domain:   maintainer or package owner
energy domain:     right to consume or allocate energy units
logistics domain:  custody and delivery responsibility
AI domain:         authority to use a corpus or invoke a service
political domain:  mandate, vote, delegation, revocation
heritage domain:   possession, stewardship, inalienability
```

COP should record:

```text
ownershipKind
domain
registry
policy
proofs
jurisdictionOrScope
```

### 4.5 Ownership is temporal

COP must distinguish:

```text
validAt       when the relation is asserted to be valid
recordedAt    when the COP event was recorded
observedAt    when the fact was observed
acceptedAt    when the event was accepted
supersededAt  when a later event changed the projection
```

---

## 5. Asset Typology

| Class | Definition | Examples | COP rule |
|---|---|---|---|
| Fungible | Units interchangeable | money, credits, kWh | balance ledger |
| Non-fungible | Unique object | container, land parcel, serial device | move semantics |
| Semi-fungible | Fungible before use, unique after reservation | ticket, quota, voucher | lifecycle state |
| Composite | Made of sub-assets | kit, building, battery pack | composition graph |
| Consumable | Destroyed or reduced by use | fuel, water, credits | consumption events |
| Claim | Right asserted against another party | invoice, debt, receivable | debtor/creditor model |
| Mandate | Delegated authority | proxy, delegation | revocable authority |
| Credential | Assertion about a subject | membership, certificate | issuer trust model |
| Commons | Shared resource | water source, shared battery pool | governance policy |
| Non-transferable | Attached to subject | personal identity, vote already cast | transfer forbidden |

### Fungible assets

Invariant:

```text
For every accepted transfer:
source balance decreases by quantity Q
destination balance increases by quantity Q
sum is conserved
unless mint or burn is explicitly authorized
```

### Non-fungible assets

Invariant:

```text
A non-fungible asset cannot be duplicated by transfer.
Transfer has move semantics, not copy semantics.
```

### Co-owned non-fungible assets

Co-ownership does not necessarily split the thing. It splits the ownership relation.

Example:

```text
Asset: house H
H remains one indivisible asset.
Ownership relation:
  Alice: 1/2
  Bob:   1/4
  Clara: 1/4
```

Invariant:

```text
sum(ownerShares) = 1
asset remains one thing
transfer of a share does not physically split the asset
policy determines decisions requiring unanimity, majority, or mandate
```

---

## 6. COP Event Model

COP should treat ownership as event-sourced.

```text
Never silently overwrite ownership.
Append events.
Validate events.
Project current state.
Keep the chain replayable.
```

Recommended event families:

```text
cop.asset.created
cop.asset.described
cop.asset.composed
cop.asset.decomposed
cop.asset.consumed
cop.asset.retired

cop.ownership.assigned
cop.ownership.transferred
cop.ownership.shared
cop.ownership.corrected
cop.ownership.revoked
cop.ownership.disputed
cop.ownership.settled

cop.custody.received
cop.custody.released
cop.custody.delivered
cop.custody.lost

cop.mandate.granted
cop.mandate.invoked
cop.mandate.revoked
cop.mandate.expired

cop.capability.issued
cop.capability.delegated
cop.capability.invoked
cop.capability.revoked
cop.capability.expired

cop.claim.asserted
cop.claim.accepted
cop.claim.rejected
cop.claim.superseded

cop.dispute.opened
cop.dispute.evidence_added
cop.dispute.settled
cop.dispute.closed
```

Every ownership-affecting event should include:

```text
eventId
eventType
assetId
actorAgentId
principalIdentityId
authority
proofs
previousStateRef or previousEventRef
assertedAt
recordedAt
policyRef
registryRef
status
```

Authority answers:

```text
Why was this actor allowed to cause this effect?
```

Possible authority kinds:

```text
owner_signature
co_owner_policy
mandate
capability
registry_admin
contract_execution
consensus_decision
governance_vote
correction_policy
```

Correction rule:

```text
wrong event remains visible
correction event references wrong event
projection uses correction policy
history remains auditable
```

---

## 7. Distributed Consistency Rules

Different assets need different consistency guarantees.

| Asset or relation | Recommended consistency | Reason |
|---|---|---|
| Money balance | strict ledger / consensus | prevent double spend |
| Non-fungible asset title | authoritative ordered log | prevent double title |
| Co-ownership shares | strict share-sum validation | prevent over-allocation |
| Custody handoff | signed event pair or lease | clarify responsibility |
| Metadata | eventual consistency | conflicts tolerable |
| Annotations | CRDT | collaborative edits |
| Claims | append-only, possibly conflicting | conflict must remain visible |
| Disputes | append-only with status projection | preserve procedural history |
| Capabilities | revocable, expiring, policy-checked | limit executable power |
| Locks or reservations | lease/TTL | avoid permanent blocking |

### Scarce assets

Scarce examples:

```text
money
unique asset
exclusive lease
reserved slot
vehicle booking
battery module
vote
capacity reservation
```

Validation rule:

```text
An accepted event must not create two simultaneous exclusive owners, users, or reservations for the same scarce asset unless the policy explicitly allows sharing.
```

### CRDT-safe zone

CRDT-like approaches are appropriate for:

```text
collaborative descriptions
annotations
local observations
non-exclusive tags
claim sets
evidence lists
read models
non-scarce metadata
```

They are not sufficient alone for:

```text
exclusive title
money balances
unique transferable assets
exclusive reservations
legal finality
```

---

## 8. Minimal Schemas

These schemas are illustrative.

### COPAsset

```json
{
  "type": "COPAsset",
  "assetId": "copasset:fractanet:container-hotcold-001",
  "assetKind": "physical_equipment",
  "fungibility": "non_fungible",
  "fractionability": "indivision_allowed",
  "transferability": "conditional",
  "unit": "unit",
  "issuerIdentityId": "did:example:fractavolta",
  "registryRef": "cop://fractanet/corte/registry/assets",
  "policyRef": "cop://policy/assets/non_fungible_equipment/v0.1",
  "metadata": {
    "label": "Camping hot/cold utility container",
    "serial": "FV-CAMP-001"
  },
  "createdAt": "2026-07-06T00:00:00+02:00"
}
```

### COPOwnershipEvent

```json
{
  "type": "COPOwnershipEvent",
  "eventType": "cop.ownership.transferred",
  "eventId": "urn:uuid:ownership-event-001",
  "assetId": "copasset:fractanet:container-hotcold-001",
  "from": [
    {
      "identityId": "did:example:fractavolta",
      "share": "1/1",
      "role": "owner"
    }
  ],
  "to": [
    {
      "identityId": "did:example:camping-orta",
      "share": "1/1",
      "role": "owner"
    }
  ],
  "actorAgentId": "copagent:contract-service-001",
  "principalIdentityId": "did:example:fractavolta",
  "authority": {
    "kind": "mandate",
    "mandateId": "copmandate:fractavolta-sales-2026-001",
    "capabilityId": "copcap:transfer-container-001",
    "proofRefs": [
      "copartifact:signature-owner-001",
      "copartifact:contract-001"
    ]
  },
  "time": {
    "assertedAt": "2026-07-06T00:00:00+02:00",
    "recordedAt": "2026-07-06T00:00:05+02:00",
    "acceptedAt": "2026-07-06T00:00:08+02:00"
  },
  "registryRef": "cop://fractanet/corte/registry/assets",
  "policyRef": "cop://policy/assets/non_fungible_equipment/v0.1",
  "status": "accepted"
}
```

### COPOwnershipState

```json
{
  "type": "COPOwnershipState",
  "assetId": "copasset:fractanet:container-hotcold-001",
  "owners": [
    {
      "identityId": "did:example:camping-orta",
      "share": "1/1",
      "role": "owner"
    }
  ],
  "currentCustodians": [],
  "activeMandates": [],
  "activeCapabilities": [],
  "openClaims": [],
  "openDisputes": [],
  "derivedFrom": [
    "urn:uuid:ownership-event-001"
  ],
  "version": 17,
  "consistency": "linearized",
  "validAt": "2026-07-06T00:00:08+02:00"
}
```

---

## 9. Validation Invariants

### Non-fungible exclusive ownership

```text
IF asset.fungibility == non_fungible
AND ownershipPolicy == exclusive
THEN accepted projection MUST contain exactly one owner relation with share 1/1
UNLESS dispute status explicitly suspends finality.
```

### Co-ownership

```text
IF asset.fractionability == indivision_allowed
THEN sum(owner.share) MUST equal 1
AND asset remains a single asset
AND policy MUST define decision thresholds.
```

### Fungible balances

```text
FOR every accepted fungible transfer
source.quantity -= Q
destination.quantity += Q
Q > 0
asset unit MUST match
mint/burn MUST require explicit authority.
```

### Mandate invocation

```text
A mandate invocation is valid only if:
- mandate exists;
- mandate is active at assertedAt;
- principal matches required authority;
- delegate matches actor or actor's controlling identity;
- action is in scope;
- asset is in scope;
- limits are not exceeded;
- revocation has not occurred.
```

### Custody versus ownership

```text
A custody event MUST NOT change ownership unless it explicitly contains or references an accepted ownership event.
```

### Correction

```text
A correction MUST reference the event it corrects.
A correction MUST state whether it changes projection, evidence, metadata, or interpretation.
The corrected event SHOULD remain auditable.
```

---

## 10. Worked Examples

### Money transfer

```text
Asset type: fungible
Unit: currency or credit
Model: account balance
Consistency: strict ledger
Event: debit + credit
Risk: double spend
Projection: balances
```

### Battery module transfer

```text
Asset type: non-fungible
Unit: serial device
Model: unique asset
Consistency: authoritative registry
Event: ownership transfer
Custody: may differ from owner
Risk: double title, loss, physical mismatch
Projection: current owner + current custodian
```

### Camping container leased to a campsite

```text
Asset type: composite non-fungible equipment
Ownership: FractaVolta or financing entity
Custody: campsite
Use right: campsite during lease period
Maintenance mandate: service provider
Capability: local controller operates within policy
```

The campsite may operate the container without owning it.

### Co-owned house

```text
Asset type: non-fungible immovable
Ownership: indivision
Shares: Alice 1/2, Bob 1/4, Clara 1/4
Custody/use: may be assigned separately
Transfer: share transfer possible under policy
Physical split: no automatic split
```

### AI agent acting on behalf of a human

```text
Agent: AI assistant
Principal identity: human user
Mandate: draft, classify, propose
Capability: create an artifact or request an external action
Ownership: unchanged unless explicitly authorized
Responsibility: principal or supervising identity according to policy
```

The AI agent should not self-authorize substantive side effects.

---

## 11. Relationship to Generalized Packet Networks

The Generalized Packet Networks framework studies systems through bounded, addressable, storable, routable, transformable, or governable units.

Ownership adds an imputation layer to packets.

A packet may carry:

```text
payload
route
priority
freshness
custody
owner
beneficiary
mandate
capability
proof
liability
settlement rule
```

A Fractanet packet may change:

```text
location
custody
state
owner
beneficiary
liability
freshness
value
```

COP must make these transitions explicit.

---

## 12. Implementation Checklist

A COP runtime that supports ownership should implement:

```text
append-only event log
content-addressed artifacts
projection store
index by assetId
index by identityId
index by mandateId
index by capabilityId
index by disputeId
schema validation
proof validation
mandate validation
capability validation
asset policy validation
share-sum validation
anti-double-spend validation
anti-double-title validation
temporal validity validation
```

Every ownership-affecting event should be explainable as:

```text
At time T,
agent A,
acting for identity P,
under mandate M or authority K,
changed relation R
between identity I and asset X,
from previous state S1 to new state S2,
with proofs E,
under policy P0,
recorded in registry R0.
```

---

## 13. State of the Art References

This note draws practical lessons from the following external models:

- W3C, Decentralized Identifiers (DIDs) v1.0: https://www.w3.org/TR/did-core/
- W3C, Verifiable Credentials Data Model v2.0: https://www.w3.org/TR/vc-data-model-2.0/
- RFC 6749, OAuth 2.0 Authorization Framework: https://www.rfc-editor.org/rfc/rfc6749
- RFC 7519, JSON Web Token: https://www.rfc-editor.org/rfc/rfc7519
- W3C Credentials Community Group, Authorization Capabilities for Linked Data: https://w3c-ccg.github.io/zcap-spec/
- Rust Book, What is Ownership?: https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html
- ERC-20 Token Standard: https://eips.ethereum.org/EIPS/eip-20
- ERC-721 Non-Fungible Token Standard: https://eips.ethereum.org/EIPS/eip-721
- ERC-1155 Multi Token Standard: https://eips.ethereum.org/EIPS/eip-1155
- Martin Fowler, Event Sourcing: https://martinfowler.com/eaaDev/EventSourcing.html
- Ongaro and Ousterhout, Raft: https://raft.github.io/raft.pdf
- etcd API documentation: https://etcd.io/docs/v3.5/learning/api/
- Apache ZooKeeper Recipes: https://zookeeper.apache.org/doc/r3.9.3/recipes.html
- Conflict-free Replicated Data Types survey: https://arxiv.org/abs/1805.06358

---

## 14. One-Page Summary

COP needs ownership because Fractanet does not merely move packets. It moves and transforms things that may belong to someone, be held by someone else, be operated by a service, be delegated to an agent, be consumed by a beneficiary, or be disputed by a third party.

The minimal model is:

```text
Asset: what is affected.
Identity: who is recognized.
Agent: who acts.
Ownership: who owns.
Custody: who holds.
Mandate: who may act for whom.
Capability: who can do what within limits.
Event: what happened.
Proof: why the event is credible.
Policy: why the event is valid.
Projection: what the current state is.
Dispute: why the current state may be contested.
```

Core rule:

```text
Do not overwrite ownership.
Record events.
Validate authority.
Project state.
Preserve disputes.
Keep replay possible.
```

This makes ownership compatible with distributed systems, human accountability, AI-assisted operations, Fractanet packet routing, and Autonomy of Capability.
