---
title: For deployers
subtitle: Concrete materials for getting a Mariani Village (or comparable DC-native deployment) off the ground.
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/for-deployers.md
last_stamped_at: 2026-05-15
---

## Mariani Village in one paragraph

ISO 20-foot container units configured as DC-native minimal dwellings (<14 m²), deployed on host sites, repositioned annually between student occupancy (Corte, academic year) and tourist occupancy (Corsican coast, summer). No grid connection required. No licensed electrician. No CONSUEL. Total electrical cost per unit: €2,740–4,080. Commercialised through **Dilorta SAS** (*di l'Orta* — of the Orta river, Minesteggio, Corsica).

Read the full habitat paper: [mariani_village.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/mariani_village.md).

---

## What a unit contains

| Component | Spec |
|---|---|
| Container | ISO 20-foot, structural; SELV-certified electrical fit-out |
| PV array | Roof-mounted, sized to seasonal load |
| Storage | LFP battery bank, 48V SELV bus |
| Distribution | DC-first; USB-C PD 3.1 (240W) as the human interface |
| AC capability | Portable 700 Wh battery packet, BLE-tracked, borrowed from a shared charging station |
| Compute | Edge inference node when the stack closes (Ophélia + Agora on-site) |
| Connectivity | Mesh-capable, low-power radio + opportunistic WAN |

The 48V SELV bus is the spine. AC is an adapter protocol at the boundary, not the substrate. USB-C PD 3.1 — operating at exactly 48V DC, up to 240W — is touch-safe, power-negotiated, and already in every user's pocket.

See the full layered analysis in [dc_native_epn.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md).

---

## Regulatory navigation

The reason the unit avoids the licensed-electrician / CONSUEL path is precisely because it stays below the SELV threshold. This is engineering, not loophole exploitation: a 48V DC bus with current-limited outlets is genuinely touch-safe and falls under different regulatory frameworks than a 230V AC installation.

What we navigate for you:

- **SELV electrical codes** (NF C 15-100 part 7-701 and related) — keeping the installation below the licensed-installation threshold while meeting safety standards
- **IMDG maritime framework** for the LFP container packets traversing ferry routes
- **RGPD/GDPR** for any installed sensing (BLE tracking, occupancy, the Atlas of Biodiversity layer if you choose to deploy it)
- **Local zoning** — ISO container deployment, host-site agreements, seasonal repositioning permits

---

## The full-stack option

A Mariani Village is wired to be a complete sovereignty site. If you want to close the stack:

- **Inseme Agora** locally — assemblies, instant voting, digital gestures for resident deliberation
- **Kudocracy.Survey** for consultations across the village
- **Ophélia AI mediator** — running on the on-site edge inference node, powered by the on-site PV-backed battery. No vendor API call leaves the site for the mediation work.
- **Atlas of Biodiversity** — if your host site has biodiversity observation potential (Corsica almost always does)

This is not required. You can run a Mariani Village as pure housing. But when you do close the stack, every layer is owned and auditable by the residents — and that's the differentiator.

---

## Step-by-step pointers

1. **Read the habitat paper** — [mariani_village.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/mariani_village.md). It's the single source of truth on the deployment.
2. **Read the DC architecture** — [dc_native_epn.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/dc_native_epn.md). Needed if your site engineer is going to do anything beyond bolt-on.
3. **Read the founding EPN paper** — [UNCONSCIOUS_GRID.md](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md). The theory under the practice — useful when objections come in from grid-trained engineers.
4. **For the platform side** — see the [inseme README](https://github.com/JeanHuguesRobert/inseme). Apps, briques, multi-instance configuration, Ophélia.
5. **For the knowledge production side** — [cogentia.js](https://github.com/JeanHuguesRobert/cogentia) is the CLI; the Commons methodology is documented in the [working paper](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/Cogentia_Commons_Working_Paper.md).

---

## Cost envelope

Per-unit electrical: €2,740–4,080 (depending on PV/battery sizing). Per-unit total including container, fit-out, and tracking infrastructure varies by site.

The full-stack option (edge inference + civic platform) adds an edge compute node and software integration — quoted per project, since the integration depth varies.

---

## How to engage

We help you with:

- Site survey and feasibility
- DC-native node design and bill of materials
- Deployment supervision and operational training
- Integration with the cognitive and civic layers if you want the full stack
- Ongoing operations (optional)

Dilorta SAS is the commercial vehicle for the housing deployment specifically. For other deployment patterns (academic, industrial, cooperative), engagement is direct with FractaVolta.

---

## Contact

📧 jhr@baronsmariani.org
🌐 [FractaVolta on GitHub](https://github.com/JeanHuguesRobert/FractaVolta)
