---
title: "Corpus Status — FractaVolta"
description: "Current state of the FractaVolta knowledge corpus — what is proved, what is open, what remains possible"
layout: default
nav_order: 2
last_modified_at: 2026-06-08
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/corpus-status.md
last_stamped_at: 2026-06-01
license: CC BY-SA 4.0
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
date: 2026-05-27
creator: Jean Hugues Noël Robert, baron Mariani (généré automatiquement par les outils du corpus)
---

# Corpus Status — FractaVolta

*Auto-refreshed by `cogentia.js corpus-status`. The structural sections —*
*Registered Repositories, Cross-Reference Graph, Published, What Remains Possible —*
*are regenerated from the registry and from [`research/index.md`](index.md) on every run.*
*The substantive sections — What Is Proved and Open Objections —*
*are manually curated and preserved across refreshes.*

*See also the distributed corpus map in [`barons-Mariani/research/corpus-status.md`](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/corpus-status.md).*

---

## Registered Repositories

<!-- BEGIN_AUTO: registered_repos -->
| Repository | research/index.md | Branch | Last commit |
|---|---|---|---|
| cogentia | ✅ | main | 2026-06-08 |
| FractaVolta | ✅ | main | 2026-06-08 |
| marenostrum | ✅ | main | 2026-06-08 |
| barons-Mariani | ✅ | main | 2026-06-08 |
| inseme | ✅ | main | 2026-06-08 |
| Inox | ✅ | master | 2026-06-08 |
| JeanHuguesRobert | ✅ | main | 2026-06-08 |
<!-- END_AUTO: registered_repos -->

---

## Cross-Reference Graph

<!-- BEGIN_AUTO: graph -->
```mermaid
graph LR
  cogentia["📄 cogentia"]
  FractaVolta["📄 FractaVolta"]
  marenostrum["📄 marenostrum"]
  barons-Mariani["📄 barons-Mariani"]
  inseme["📄 inseme"]
  Inox["📄 Inox"]
  JeanHuguesRobert["📄 JeanHuguesRobert"]
  cogentia --> marenostrum
  cogentia --> JeanHuguesRobert
  cogentia --> barons-Mariani
  cogentia --> FractaVolta
  cogentia --> inseme
  cogentia --> Inox
  FractaVolta --> marenostrum
  FractaVolta --> JeanHuguesRobert
  FractaVolta --> barons-Mariani
  FractaVolta --> cogentia
  FractaVolta --> inseme
  FractaVolta --> Inox
  marenostrum --> barons-Mariani
  marenostrum --> JeanHuguesRobert
  marenostrum --> FractaVolta
  marenostrum --> cogentia
  marenostrum --> inseme
  marenostrum --> Inox
  barons-Mariani --> marenostrum
  barons-Mariani --> JeanHuguesRobert
  barons-Mariani --> FractaVolta
  barons-Mariani --> cogentia
  barons-Mariani --> inseme
  barons-Mariani --> Inox
  inseme --> cogentia
  inseme --> JeanHuguesRobert
  inseme --> marenostrum
  inseme --> FractaVolta
  inseme --> barons-Mariani
  inseme --> Inox
  Inox --> marenostrum
  Inox --> JeanHuguesRobert
  Inox --> FractaVolta
  Inox --> cogentia
  Inox --> barons-Mariani
  Inox --> inseme
  JeanHuguesRobert --> cogentia
  JeanHuguesRobert --> marenostrum
  JeanHuguesRobert --> FractaVolta
  JeanHuguesRobert --> barons-Mariani
  JeanHuguesRobert --> inseme
  JeanHuguesRobert --> Inox
  click cogentia "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/index.md" "Open research/index.md"
  click FractaVolta "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/index.md" "Open research/index.md"
  click marenostrum "https://github.com/JeanHuguesRobert/marenostrum/blob/main/research/index.md" "Open research/index.md"
  click barons-Mariani "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/index.md" "Open research/index.md"
  click inseme "https://github.com/JeanHuguesRobert/inseme/blob/main/research/index.md" "Open research/index.md"
  click Inox "https://github.com/JeanHuguesRobert/Inox/blob/main/research/index.md" "Open research/index.md"
  click JeanHuguesRobert "https://github.com/JeanHuguesRobert/JeanHuguesRobert/blob/main/research/index.md" "Open research/index.md"
```
<!-- END_AUTO: graph -->

---

## Concepts

<!-- BEGIN_AUTO: concepts -->
| Concept | Scope | Status | Type |
|---|---|---|---|
| [Cogentia](./concepts.md#cogentia) | Global | Working | abstract concept / agentivity class |
| [Cogentigram](./concepts.md#cogentigram) | Global | Working | representation / map |
| [IPN (Inference Packet Network)](./concepts.md#ipn-inference-packet-network) | Global | Defined | network architecture |
| [EPN (Energy Packet Network)](./concepts.md#epn-energy-packet-network) | Global | Defined | network architecture |
| [PGN (Power Generation Node)](./concepts.md#pgn-power-generation-node) | Global | Working | infrastructure component |
| [Packet Attractors](./concepts.md#packet-attractors) | Global | Working | system dynamics |
| [The Unconscious Grid](./concepts.md#the-unconscious-grid) | Global | Working | abstract concept |
| [Mariani Village](./concepts.md#mariani-village) | Global | Working | project |
| [Value-Shaped Solar](./concepts.md#value-shaped-solar) | project-specific | Working | energy strategy |
| [Containerized Compute (Tera)](./concepts.md#containerized-compute-tera) | repository-specific | Defined | infrastructure format |
| [Traceable Governance](./concepts.md#traceable-governance) | repository-specific | Working | administrative protocol |
<!-- END_AUTO: concepts -->

## Concept Graph

<!-- BEGIN_AUTO: concept_graph -->
```mermaid
graph LR
  c_machine_a_explorer["Machine à explorer"]
  c_machine_a_empecher["Machine à empêcher"]
  c_effet_ubik["Effet Ubik"]
  c_stabilisateurs_anti_ubik_proceduraux["Stabilisateurs (anti-Ubik / procéduraux)"]
  c_cogentia["Cogentia"]
  c_cogentigram["Cogentigram"]
  c_continuation_protocol["Continuation Protocol"]
  c_non_deterministic_cognitive_step_agentic_step["Non-deterministic Cognitive Step (Agentic Step)"]
  c_human_enacted_decision_artifact["Human Enacted Decision Artifact"]
  c_causal_trace_replay_auditable_causal_reconstruction["Causal Trace Replay (Auditable Causal Reconstruction)"]
  c_cognitive_packet["Cognitive Packet"]
  c_cogentia_commons["Cogentia Commons"]
  c_cogentia_pipeline["Cogentia Pipeline"]
  c_derived_product["Derived Product"]
  c_agent_resumable_cli["Agent-Resumable CLI"]
  c_infrastructure_is_all_you_need["Infrastructure is All You Need"]
  c_possibilism["Possibilism"]
  c_territoires_possibilistes["Territoires Possibilistes"]
  c_autonomie_de_capacite["Autonomie de capacité"]
  c_kudocracy["Kudocracy"]
  c_kudos["Kudos"]
  c_pathologie_du_secret["Pathologie du secret"]
  c_the_second_method["The Second Method"]
  c_cop_invariants["COP Invariants"]
  c_concatenative_language["Concatenative language"]
  c_stack_vm["Stack VM"]
  c_controldata_plane_separation["Control/data plane separation"]
  c_named_values["Named values"]
  c_actors["Actors"]
  c_fractanet["Fractanet"]
  c_possibilism --> c_machine_a_explorer
  c_democratic_ai_safety["democratic ai safety"]
  c_democratic_ai_safety --> c_machine_a_explorer
  c_cogentia_commons_declinaison_manuelle["cogentia commons declinaison manuelle"]
  c_machine_a_explorer --> c_cogentia_commons_declinaison_manuelle
  c_fractanet_cop_declinaison_automatisee["fractanet cop declinaison automatisee"]
  c_machine_a_explorer --> c_fractanet_cop_declinaison_automatisee
  c_stabilisateurs_anti_ubik["stabilisateurs anti ubik"]
  c_machine_a_explorer --> c_stabilisateurs_anti_ubik
  c_machine_a_explorer -.-> c_continuation_protocol
  c_machine_a_explorer -.-> c_cognitive_packet
  c_dhitl_couches_45["dhitl couches 45"]
  c_machine_a_explorer -.-> c_dhitl_couches_45
  c_effet_ubik_oppose["effet ubik oppose"]
  c_machine_a_explorer -.-> c_effet_ubik_oppose
  c_machine_a_empecher -.-> c_effet_ubik
  c_machine_a_explorer_oppose_symetrique["machine a explorer oppose symetrique"]
  c_machine_a_empecher -.-> c_machine_a_explorer_oppose_symetrique
  c_fm_11_outer_optimizer_capture["fm 11 outer optimizer capture"]
  c_machine_a_empecher -.-> c_fm_11_outer_optimizer_capture
  c_concentration_de_compute_85_frontier["concentration de compute 85 frontier"]
  c_machine_a_empecher -.-> c_concentration_de_compute_85_frontier
  c_effet_ubik -.-> c_stabilisateurs_anti_ubik
  c_effet_ubik -.-> c_pathologie_du_secret
  c_invidia_densite_sociale_destructrice["invidia densite sociale destructrice"]
  c_effet_ubik -.-> c_invidia_densite_sociale_destructrice
  c_machine_a_explorer --> c_stabilisateurs_anti_ubik_proceduraux
  c_stabilisateurs_anti_ubik_proceduraux -.-> c_effet_ubik
  c_stabilisateurs_anti_ubik_proceduraux -.-> c_continuation_protocol
  c_stabilisateurs_anti_ubik_proceduraux -.-> c_cognitive_packet
  c_dhitl_compute_exergy_comme_unite_tracable["dhitl compute exergy comme unite tracable"]
  c_stabilisateurs_anti_ubik_proceduraux -.-> c_dhitl_compute_exergy_comme_unite_tracable
  c_cogentia --> c_cogentigram
  c_map_vs_territory["map vs territory"]
  c_cogentigram -.-> c_map_vs_territory
  c_operational_memory["operational memory"]
  c_cogentigram -.-> c_operational_memory
  c_traceable_agency["traceable agency"]
  c_cogentigram -.-> c_traceable_agency
  c_agent_resumable_cli --> c_continuation_protocol
  c_non_deterministic_cognitive_step["non deterministic cognitive step"]
  c_continuation_protocol -.-> c_non_deterministic_cognitive_step
  c_continuation_protocol -.-> c_human_enacted_decision_artifact
  c_causal_trace_replay["causal trace replay"]
  c_continuation_protocol -.-> c_causal_trace_replay
  c_machine_a_explorer --> c_non_deterministic_cognitive_step_agentic_step
  c_non_deterministic_cognitive_step_agentic_step -.-> c_human_enacted_decision_artifact
  c_non_deterministic_cognitive_step_agentic_step -.-> c_causal_trace_replay
  c_non_deterministic_cognitive_step_agentic_step -.-> c_continuation_protocol
  c_machine_a_explorer --> c_human_enacted_decision_artifact
  c_cophitl_profile["cophitl profile"]
  c_cophitl_profile --> c_human_enacted_decision_artifact
  c_human_enacted_decision_artifact -.-> c_non_deterministic_cognitive_step
  c_rule_0_seconde_methode["rule 0 seconde methode"]
  c_human_enacted_decision_artifact -.-> c_rule_0_seconde_methode
  c_dhitl_layer_5["dhitl layer 5"]
  c_human_enacted_decision_artifact -.-> c_dhitl_layer_5
  c_cop_invariants --> c_causal_trace_replay_auditable_causal_reconstruction
  c_machine_a_explorer --> c_causal_trace_replay_auditable_causal_reconstruction
  c_causal_trace_replay_auditable_causal_reconstruction -.-> c_continuation_protocol
  c_causal_trace_replay_auditable_causal_reconstruction -.-> c_non_deterministic_cognitive_step
  c_continuation_protocol --> c_cognitive_packet
  c_agent_resumable_cli --> c_cognitive_packet
  c_envelope_kind_agnostic_metadata_layer["envelope kind agnostic metadata layer"]
  c_cognitive_packet --> c_envelope_kind_agnostic_metadata_layer
  c_payload_kind_specific_content_layer["payload kind specific content layer"]
  c_cognitive_packet --> c_payload_kind_specific_content_layer
  c_continuation_payload["continuation payload"]
  c_cognitive_packet --> c_continuation_payload
  c_objection_payload["objection payload"]
  c_cognitive_packet --> c_objection_payload
  c_hypothesis_payload["hypothesis payload"]
  c_cognitive_packet --> c_hypothesis_payload
  c_decision_payload["decision payload"]
  c_cognitive_packet --> c_decision_payload
  c_failure_payload["failure payload"]
  c_cognitive_packet --> c_failure_payload
  c_routing_payload["routing payload"]
  c_cognitive_packet --> c_routing_payload
  c_cognitive_packet -.-> c_cogentia_commons
  c_cogentia_commons --> c_cogentia_pipeline
  c_cognitive_packet --> c_cogentia_pipeline
  c_source_document["source document"]
  c_cogentia_pipeline --> c_source_document
  c_cogentia_pipeline --> c_derived_product
  c_derived_product -.-> c_source_document
  c_traceable_agency --> c_cogentia
  c_cogentia --> c_operational_memory
  c_dhitl["dhitl"]
  c_dhitl --> c_infrastructure_is_all_you_need
  c_possibilism --> c_autonomie_de_capacite
  c_capabilities_approach_sen_nussbaum["capabilities approach sen nussbaum"]
  c_capabilities_approach_sen_nussbaum --> c_autonomie_de_capacite
  c_specificite_de_phase["specificite de phase"]
  c_autonomie_de_capacite --> c_specificite_de_phase
  c_flexibilite_dusage_redistributive_vs_predatory["flexibilite dusage redistributive vs predatory"]
  c_autonomie_de_capacite --> c_flexibilite_dusage_redistributive_vs_predatory
  c_autonomie_de_capacite -.-> c_territoires_possibilistes
  c_auto_institution_democratique_castoriadis["auto institution democratique castoriadis"]
  c_autonomie_de_capacite -.-> c_auto_institution_democratique_castoriadis
  c_possibilism --> c_kudocracy
  c_auto_institution_democratique_castoriadis --> c_kudocracy
  c_kudocracy -.-> c_autonomie_de_capacite
  c_kudocracy -.-> c_kudos
  c_kudocracy -.-> c_pathologie_du_secret
  c_kudocracy -.-> c_cognitive_packet
  c_possibilism --> c_kudos
  c_communs_ostrom["communs ostrom"]
  c_communs_ostrom --> c_kudos
  c_kudos -.-> c_kudocracy
  c_kudos -.-> c_autonomie_de_capacite
  c_mauss_gift_counter_gift["mauss gift counter gift"]
  c_kudos -.-> c_mauss_gift_counter_gift
  c_democratic_ai_safety_thesis_kernel["democratic ai safety thesis kernel"]
  c_democratic_ai_safety_thesis_kernel --> c_pathologie_du_secret
  c_the_second_method --> c_pathologie_du_secret
  c_dhitl_democratic_humans_in_the_loop["dhitl democratic humans in the loop"]
  c_pathologie_du_secret -.-> c_dhitl_democratic_humans_in_the_loop
  c_cogentia_commons_auditable_knowledge["cogentia commons auditable knowledge"]
  c_pathologie_du_secret -.-> c_cogentia_commons_auditable_knowledge
  c_tracabilite_civique_anti_mafieuse["tracabilite civique anti mafieuse"]
  c_pathologie_du_secret -.-> c_tracabilite_civique_anti_mafieuse
  c_machine_a_explorer --> c_cop_invariants
  c_stabilisateurs_anti_ubik_proceduraux --> c_cop_invariants
  c_deterministic_replay_protocol_layer_only["deterministic replay protocol layer only"]
  c_causal_trace_replay_auditable_causal_reconstruction -.-> c_deterministic_replay_protocol_layer_only
  c_concatenative_language -.-> c_stack_vm
  c_concatenative_language -.-> c_named_values
  c_stack_vm -.-> c_concatenative_language
  c_stack_vm -.-> c_controldata_plane_separation
  c_stack_vm -.-> c_named_values
  c_energy_packet_network_fractavolta["energy packet network fractavolta"]
  c_controldata_plane_separation -.-> c_energy_packet_network_fractavolta
  c_cognitive_packet_envelopepayload_cogentia["cognitive packet envelopepayload cogentia"]
  c_controldata_plane_separation -.-> c_cognitive_packet_envelopepayload_cogentia
  c_fractanet -.-> c_energy_packet_network_fractavolta
  c_auxilia_inseme_brique_human_scale_fractanet_exchange["auxilia inseme brique human scale fractanet exchange"]
  c_fractanet -.-> c_auxilia_inseme_brique_human_scale_fractanet_exchange
  c_fractanet -.-> c_actors
  click c_machine_a_explorer "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#machine-a-explorer" "Open Machine à explorer"
  click c_machine_a_empecher "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#machine-a-empecher" "Open Machine à empêcher"
  click c_effet_ubik "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#effet-ubik" "Open Effet Ubik"
  click c_stabilisateurs_anti_ubik_proceduraux "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#stabilisateurs-anti-ubik-proceduraux" "Open Stabilisateurs (anti-Ubik / procéduraux)"
  click c_cogentia "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/concepts.md#cogentia" "Open Cogentia"
  click c_cogentigram "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#cogentigram" "Open Cogentigram"
  click c_continuation_protocol "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#continuation-protocol" "Open Continuation Protocol"
  click c_non_deterministic_cognitive_step_agentic_step "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#non-deterministic-cognitive-step-agentic-step" "Open Non-deterministic Cognitive Step (Agentic Step)"
  click c_human_enacted_decision_artifact "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#human-enacted-decision-artifact" "Open Human Enacted Decision Artifact"
  click c_causal_trace_replay_auditable_causal_reconstruction "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#causal-trace-replay-auditable-causal-reconstruction" "Open Causal Trace Replay (Auditable Causal Reconstruction)"
  click c_cognitive_packet "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#cognitive-packet" "Open Cognitive Packet"
  click c_cogentia_commons "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#cogentia-commons" "Open Cogentia Commons"
  click c_cogentia_pipeline "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#cogentia-pipeline" "Open Cogentia Pipeline"
  click c_derived_product "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#derived-product" "Open Derived Product"
  click c_agent_resumable_cli "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/concepts.md#agent-resumable-cli" "Open Agent-Resumable CLI"
  click c_infrastructure_is_all_you_need "https://github.com/JeanHuguesRobert/marenostrum/blob/main/research/concepts.md#infrastructure-is-all-you-need" "Open Infrastructure is All You Need"
  click c_possibilism "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/concepts.md#possibilism" "Open Possibilism"
  click c_territoires_possibilistes "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/concepts.md#territoires-possibilistes" "Open Territoires Possibilistes"
  click c_autonomie_de_capacite "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/concepts.md#autonomie-de-capacite" "Open Autonomie de capacité"
  click c_kudocracy "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/concepts.md#kudocracy" "Open Kudocracy"
  click c_kudos "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/concepts.md#kudos" "Open Kudos"
  click c_pathologie_du_secret "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/concepts.md#pathologie-du-secret" "Open Pathologie du secret"
  click c_the_second_method "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/concepts.md#the-second-method" "Open The Second Method"
  click c_cop_invariants "https://github.com/JeanHuguesRobert/inseme/blob/main/research/concepts.md#cop-invariants" "Open COP Invariants"
  click c_concatenative_language "https://github.com/JeanHuguesRobert/Inox/blob/main/research/concepts.md#concatenative-language" "Open Concatenative language"
  click c_stack_vm "https://github.com/JeanHuguesRobert/Inox/blob/main/research/concepts.md#stack-vm" "Open Stack VM"
  click c_controldata_plane_separation "https://github.com/JeanHuguesRobert/Inox/blob/main/research/concepts.md#controldata-plane-separation" "Open Control/data plane separation"
  click c_named_values "https://github.com/JeanHuguesRobert/Inox/blob/main/research/concepts.md#named-values" "Open Named values"
  click c_actors "https://github.com/JeanHuguesRobert/Inox/blob/main/research/concepts.md#actors" "Open Actors"
  click c_fractanet "https://github.com/JeanHuguesRobert/Inox/blob/main/research/concepts.md#fractanet" "Open Fractanet"
```

*Orphan concepts (no parents / children / related): `Civilizational Stakes` (cogentia), `Sovereign Digital Twin` (cogentia), `Kernel Extractor` (cogentia), `KYS (Know Your System) / Psychocognitive Analysis` (cogentia), `Cogentia Workflows` (cogentia), `IPN (Inference Packet Network)` (FractaVolta), `EPN (Energy Packet Network)` (FractaVolta), `PGN (Power Generation Node)` (FractaVolta), `Packet Attractors` (FractaVolta), `The Unconscious Grid` (FractaVolta), `Mariani Village` (FractaVolta), `Value-Shaped Solar` (FractaVolta), `Containerized Compute (Tera)` (FractaVolta), `Traceable Governance` (FractaVolta), `DHITL (Democratic Human In The Loop)` (marenostrum), `CXU (Compute and Exergy Unit)` (marenostrum), `Safe Compute Exergy` (marenostrum), `Constellia` (marenostrum), `Corsica Forest Synergies` (marenostrum), `Sun to Sovereignty` (marenostrum), `Potentics` (barons-Mariani), `Cognitive Waves` (barons-Mariani), `Mimetic Desynchronization` (barons-Mariani), `Invidia` (barons-Mariani), `Transition Markets` (barons-Mariani), `The Uchronian Museum` (barons-Mariani), `Projet Minesteggio` (barons-Mariani), `Discret Holography` (barons-Mariani), `COP (Continuous Operation Protocol)` (inseme), `Briques` (inseme), `Agora` (inseme), `Ophélia` (inseme), `COP (Cognitive Orchestration Protocol)` (inseme), `Brique Spec / Multi-Instance` (inseme), `Modular System` (inseme), `Reactive sets` (Inox), `Dialects` (Inox). Re-include with `--include-orphans`.*
<!-- END_AUTO: concept_graph -->

---

## Published in this repo

<!-- BEGIN_AUTO: published -->
| Title | Location | Date |
|---|---|---|
| [Lien avec C.O.R.S.I.C.A. et l’Institut Mariani](acorsica-institut-mariani.md) *(institutional boundary note — documentary link without institutional confusion)* | this repo | 2026-06-03 |
| [Packetized Gravity Networks](../PGN.md) | this repo | 2026-05-08 |
| [The Packet as Evolutionary Attractor — Scale-Invariant Transitions in Complex Networks](../packet_attractor.md) | this repo | 2026-05-08 |
| [The Packet Transition — A Lateral Reading of Circuit Networks](../packet_transition.md) | this repo | 2026-05-08 |
| [Inference Packet Networks — A RAID/ARPANET Continuity Layer for Sovereign AI Infrastructure](inference_packet_network.md) | this repo | 2026-05-14 |
| [Guaranteed Inference — A Resilient, Routable and Traceable Fallback Layer for Critical AI Workloads](garanteed_inference.md) *(working paper v0.3-market)* | this repo | 2026-05-18 |
| [DC-Native Energy Packet Networks](../dc_native_epn.md) | this repo | 2026 |
| [Electricity in Containers — Store-and-Forward Energy Logistics](../electricity_in_containers.md) | this repo | 2026-05-06 |
| [The Unconscious Grid — Store-and-Forward as the Repressed Solution](../UNCONSCIOUS_GRID.md) *(entry point for the packetization corpus ; §8 extends the diagnosis from energy to cognition, sociability, money, and territory)* | this repo | 2026-05-21 |
| [Le Réseau Inconscient — De la commutation *store-and-forward* comme solution refoulée (FR)](../LE_RESEAU_INCONSCIENT.md) *(version française sémantiquement identique à [`UNCONSCIOUS_GRID.md`](../UNCONSCIOUS_GRID.md))* | this repo | 2026-05-21 |
| [Value-Shaped Solar and Containerized Compute](../value_shaped_solar_and_containerized_compute.md) | this repo | 2026-05-06 |
| [Mariani Village — A Relocatable DC-Native Housing Fleet](../mariani_village.md) | this repo | 2026-05-08 |
| [FractaTera — Fractal Terrestrial Awareness Network](../tera.md) | this repo | 2026-05-06 |
| [Fractal Architectures for Traceable Governance](../traceable_governance.md) | this repo | 2026 |
| [FractaVolta White Paper](../fractavolta_paper.md) | this repo | 2026 |
| [FractaVolta Partner Brief — Agrivoltaics Pilot Opportunity](../partner_brief.md) | this repo | 2026-05-06 |
| [Generalized Packet Networks — A Framework for Heterogeneous Packets, Resource Occupancy, and Cross-Domain Operational Recurrence](generalized_packet_networks.md) *(working paper v0.3 — the cross-domain abstraction that EPN, PGN, IPN, Thermal Packets all instantiate)* | this repo | 2026-05-22 |
| [Thermal Packet Networks — A Multi-Scale Store-and-Forward Architecture for Low-Exergy Heat and Cold Distribution](thermal_packet_networks.md) *(working paper v0.2)* | this repo | 2026-05-22 |
| [Packet Paper Template — A Minimal Method for Declining Generalized Packet Networks into Substrate-Specific Papers](packet_paper_template.md) *(method-template working paper v0.2)* | this repo | 2026-05-22 |
| [Fractanet — Working paper](fractanet.md) *(working paper, draft v0.1)* | this repo | 2026-05-31 |
| [Bonne Marque](bonne_marque_mvp.md) *(conceptual MVP source document v0.2)* | this repo | 2026-06-03 |
| [Corpus Status](corpus-status.md) *(living view — auto-refreshed by `cogentia.js corpus-status`)* | this repo | refreshable |
| [Concept Index](concepts.md) *(typed concept registry — mapped by `cogentia.js concepts`)* | this repo | refreshable |
<!-- END_AUTO: published -->

---

## What Is Proved

*Manually curated: claims demonstrated by the published work in this corpus.*

| Claim | Status | Evidence |
|---|---|---|
| Gravity as territorial memory (PGN framework) | ✅ Documented | [PGN.md](../PGN.md) |
| Hydraulic CXU extends MareNostrum exergy chain | ✅ Documented | [PGN.md](../PGN.md) § Hydraulic CXU |
| IEV node model (turbine + pump + control + comms) | ✅ Documented | [PGN.md](../PGN.md) § IEV Architecture |
| Corsica as PGN case study | ✅ Documented | [PGN.md](../PGN.md) § Corsica |
| Packet-as-evolutionary-attractor framework | ✅ Documented | [packet_attractor.md](../packet_attractor.md) |
| Store-and-forward as repressed energy-sovereignty solution | ✅ Documented | [UNCONSCIOUS_GRID.md](../UNCONSCIOUS_GRID.md), [electricity_in_containers.md](../electricity_in_containers.md) |
| Value-shaped solar + containerized compute | ✅ Documented | [value_shaped_solar_and_containerized_compute.md](../value_shaped_solar_and_containerized_compute.md) |
| IEV prototype deployed | ❌ Not yet | Hardware V0 pending |
| Tavignano valley pilot operational | ❌ Not yet | Site identified, not built |

---

## Open Objections

*Manually curated: objections received publicly, not yet fully resolved.*

| Objection | Status |
|---|---|
| IEV hardware spec not yet public | 🔄 In progress |
| Hydraulic CXU formal model needs mathematical validation | 🔄 Open |
| Water rights as executable constraints — legal framework incomplete | 🔄 Open |

---

## What Remains Possible

<!-- BEGIN_AUTO: possibilities -->
- PGN × V2G: electric vehicle fleet as mobile hydraulic complement
- Seasonal complementarity model: solar + hydraulic + wind at Mediterranean scale
- `fracta-wiki` as distributed knowledge substrate for PGN territorial governance
- SimpliJs revival: wiki + governance as interface layer for FractaVolta corpus
<!-- END_AUTO: possibilities -->

---

*Generated with `cogentia.js corpus-status` — [scripts/cogentia.js](https://github.com/JeanHuguesRobert/cogentia/blob/main/scripts/cogentia.js)*
*Challenge via issues. Fork to explore alternatives.*


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [DC-Native Energy Packet Networks](../dc_native_epn.md)
- [Electricity in Containers](../electricity_in_containers.md)
- [FractaVolta](../fractavolta_paper.md)
- [Le Réseau Inconscient](../LE_RESEAU_INCONSCIENT.md)
- [Mariani Village: A Relocatable DC-Native Housing Fleet](../mariani_village.md)
- [The Packet as Evolutionary Attractor: Scale-Invariant Transitions in Complex Networks](../packet_attractor.md)
- [The Packet Transition: A Lateral Reading of Circuit Networks](../packet_transition.md)
- [FractaVolta – Partner  Brief](../partner_brief.md)
- [Packetized Gravity Networks: Distributed Hydro-Energetic Infrastructure for Resilient Renewable Integration](../PGN.md)
- [Concept Index — FractaVolta](concepts.md)
- [Corpus Status — FractaVolta](corpus-status.md)
- [Guaranteed Inference](garanteed_inference.md)
- [Research Index — FractaVolta](index.md)
- [Inference Packet Networks](inference_packet_network.md)
- [FractaTera](../tera.md)
- [FractaVolta traceable gouvernance](../traceable_governance.md)
- [The Unconscious Grid](../UNCONSCIOUS_GRID.md)
- [Value-Shaped Solar and Containerized Compute](../value_shaped_solar_and_containerized_compute.md)

<!-- END_AUTO: backlinks -->
