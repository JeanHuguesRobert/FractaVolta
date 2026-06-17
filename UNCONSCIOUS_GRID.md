---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-06-01
translations:
  fr: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/LE_RESEAU_INCONSCIENT.md
role: "entry point for the packetization corpus"
title: "The Unconscious Grid"
date: "2026-05-05"
status: "working-paper — auto-filled (frontmatter cleanup)"
---
# The Unconscious Grid
## On Store-and-Forward as the Repressed Solution to Energy Sovereignty

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A. - 
1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org

---

## Abstract

The global electrical grid remains, structurally, a circuit-switched network — a design whose fundamental limitations were identified in 1964 and operationally superseded, in the domain of information, by 1969. This paper argues that the solution to energy sovereignty has existed all along, practiced unconsciously by billions of people carrying mobile phones, and that it requires no new technology to implement: the physical transport of electrochemical storage units as discrete, addressable energy packets, combined with the transduction of energy value into AI inference tokens routable over the internet. We call this convergence the Energy Packet Network (EPN). Drawing on Paul Baran's original packet-switching theory (1964), the history of ARPANET, the existing but incomplete literature on digital grids, France's instructive failure with X.25, and the concrete case of the saturated SARCO submarine cable isolating Corsica from continental European energy markets, this paper argues that the correct unit of energy accounting is exergy, not energy; that the correct model of network reliability is redundancy of inexpensive components (RAIB — Redundant Array of Inexpensive Batteries), not quality of expensive ones; that the correct coordination mechanism is stigmergy with honest price signals, not central dispatch; and that the correct architectural principle is subsidiarity, not synchronisation. The result is a system that is antifragile in Taleb's precise sense — one that grows stronger through disorder rather than merely surviving it. The EPN does not resolve the tension between capitalism and collectivism by compromising between them. It dissolves the question by separating two layers that political economy has always conflated: the protocol, which is a commons; and the operation, which is radically diverse. Corsica is not the subject of this analysis. It is the laboratory.

**Keywords:** packet-switching; store-and-forward; energy sovereignty; AI inference; exergy; battery logistics; antifragility; stigmergy; subsidiarity; island energy systems; MareNostrum

---

## 1. The Burning House

There is a specific kind of urgency that arises not from scarcity but from misallocation — when a resource exists in abundance, a solution exists in principle, and yet the gap between the two widens rather than narrows. The energy crisis of artificial intelligence is of this kind.

In 2024, global data centres consumed approximately 415 TWh of electricity — roughly 1.5% of total global consumption, growing at a compound annual rate of 12% since 2017, more than four times faster than total electricity demand (IEA, 2025). The International Energy Agency projects this figure will double to approximately 945 TWh by 2030, slightly exceeding Japan's entire annual electricity consumption today. Within this total, AI-specific accelerated server infrastructure — GPU clusters and the cooling systems that sustain them — is growing at 30% annually, more than three times the rate of conventional computing. In the United States alone, data centres consumed 183 TWh in 2024, more than 4% of national electricity consumption — the equivalent of Pakistan's entire annual demand — and this figure is projected to grow by 133% before 2030 (Pew Research, 2025).

The environmental consequences are already measurable. A study of 2,132 US data centres found that 56% of their electricity derives from fossil fuels, generating more than 105 million tonnes of CO₂ equivalent in a single year — 2.18% of total US emissions — at a carbon intensity 48% above the national average (Patel et al., 2025). Training a single large language model comparable to GPT-4 generates an estimated 552 tonnes of CO₂ — the annual footprint of 121 American households. Water consumption is an equally pressing concern: AI infrastructure is projected to drive annual increases in US water withdrawals of 200–300 billion gallons by 2030, in a country where aquifer depletion is already a regional crisis.

The industry's stated response — procurement of renewable energy through Power Purchase Agreements and Renewable Energy Certificates — is structurally inadequate, and the inadequacy is not a matter of degree but of kind. Certificates decouple the temporal and geographical relationship between generation and consumption: a data centre in Virginia drawing coal-powered electricity at two in the morning may claim renewable status by purchasing a certificate from a solar farm in Arizona that generated power at noon. This is accounting, not physics. It satisfies corporate sustainability reporting requirements while leaving the physical grid unchanged.

The structurally honest response — co-locating AI computation with renewable generation — confronts immediately the constraint this paper addresses. Renewable energy is distributed, intermittent, and geographically determined by sun and wind. AI demand is continuous, location-agnostic in principle but historically concentrated near fibre infrastructure and capital. The transmission systems that might bridge these geographies are, in many cases, operating near rated capacity. Regions such as Virginia, Oregon, and Ireland — where AI infrastructure has concentrated fastest — are already showing signs of local grid stress that additional capacity cannot quickly relieve (IEA, 2025).

The problem is not a shortage of renewable energy. Mediterranean islands receive between 2,600 and 2,900 hours of annual sunshine. The Saharan fringe receives more. Icelandic geothermal is effectively inexhaustible. The problem is the absence of an architecture capable of routing that energy — or, equivalently, routing the computation to where the energy is — without depending on fixed cable infrastructure whose capacity is finite and whose reinforcement takes a decade.

This paper proposes such an architecture. It is not new. It has been practiced, unconsciously, since the first person carried a charged mobile phone from one place to another.

---

## 2. The Primal Scene: 1964–1969

In August 1964, Paul Baran of the RAND Corporation submitted to the United States Air Force a series of memoranda that would, within five years, reorganise the architecture of human communication. The report, *On Distributed Communications*, proposed a solution to what had seemed an intractable problem: how does a communications network survive the destruction of any of its nodes?

The existing answer — the telephone network — was a circuit-switched system. When two parties wished to communicate, a dedicated physical path was established between them and held for the duration of the exchange. The path was reserved, exclusive, and continuous. Its virtue was predictability; its fundamental vice was fragility. Destroy a sufficient number of nodes and the network collapses, because dedicated circuits cannot reroute around damage. The telephone network was, in graph-theoretic terms, a tree that could not survive the pruning of its trunk.

Baran's proposal was conceptually simple and technically radical. Do not establish a dedicated circuit. Instead, divide the message into discrete units — packets — each carrying its own destination address as a header. Inject these packets into a distributed mesh network whose nodes have no global knowledge. Allow each node to forward each packet toward its destination by whatever route is currently available. Reassemble the packets at the destination. The network becomes what Baran called a *hot potato* routing system: each node passes the packet on as quickly as possible, indifferent to which path it takes, committed only to its forward motion.

The implications were systemic. A distributed packet-switched network has no single point of failure. It degrades gracefully under attack — losing capacity proportionally rather than collapsing catastrophically. It requires no prior reservation of bandwidth. It scales: add nodes and the network becomes more resilient, not more complex to manage. And it is, by construction, ungovernable by any single actor, because no actor holds the circuit.

By 1969, ARPANET had demonstrated these properties empirically. By 1983, TCP/IP had crystallised Baran's insight into a universal protocol. By 1991, the World Wide Web had given it a face. The circuit-switched telephone network — still dominant in 1964 — had become, by 2000, a legacy system being progressively absorbed by its own successor.

The global electrical grid noticed none of this. It had its own logic, its own history, its own engineers. In 1888, Nikola Tesla and George Westinghouse had demonstrated the decisive advantage of alternating current over Thomas Edison's direct current systems — not in any intrinsic property of the physics, but in the transformer: a device of elegant simplicity that raises or lowers AC voltage using two coils of wire around an iron core, enabling high-voltage long-distance transmission and low-voltage safe consumption on the same network. The transformer made the modern grid possible. It also locked it, for a century and a half, into the circuit-switched logic that AC power transmission requires: a single frequency, a single phase, continuous synchronisation across thousands of kilometres, and the structural inability to store the carrier signal.

In 2025, the global electrical grid remains a circuit-switched network. When a solar installation in Corsica wishes to deliver energy to a data centre in Milan, it requires a dedicated physical path — submarine cable, high-voltage transmission line, phase synchronisation — for the entire duration of the transfer. If that path is saturated, the energy cannot flow, regardless of how much sun is available at the source. The SARCO submarine cable connecting Corsica to the continental French grid operates near its rated capacity for significant portions of each year. Corsica receives some of the highest solar irradiation in Western Europe. It cannot export the surplus because the circuit is full.

We are, for electricity, in 1968.

---

## 3. The Repression: Why the Grid Refused to Grow Up

This observation is not without antecedents. A significant body of engineering literature has recognised the structural analogy between telecommunications and electrical networks, and proposed various forms of "energy internet" or "digital grid" as correctives. The recognition is correct. The proposed solutions are, without exception, incomplete in a specific and revealing way.

The earliest systematic formulation appears in work by Toyoda and Saitoh (1998), who proposed an "open electric energy network" modelled explicitly on the logic of open telecommunications markets, with the ambition of packetising energy flows. They were visionaries: they dimensioned their proposed storage capacity using queuing theory borrowed directly from data network design. Their limitation was technological — the storage devices required for physical packet transport did not yet exist at viable cost or density. A decade later, Abe, Taoka, and McQuilkin (2011) operationalised the concept as the "digital grid," proposing that electrical energy be transmitted as addressed packets over a network of intelligent nodes. Gelenbe (2012) developed the Energy Packet Network paradigm at Imperial College, focused on dynamic energy allocation for cloud computing data centres. Nardelli et al. (2019) synthesised this literature into a comprehensive framework for an "energy internet via packetised management." The Kyoto University group — Hikihara, Takahashi, and collaborators — implemented physical power packet transmission via store-and-forward between laboratory-scale electrical routers, demonstrating the principle in hardware with considerable elegance.

These are genuine contributions. They are also, without exception, constrained by a single unexamined assumption: **the packet travels on a wire**.

In every formulation of the energy internet literature, packets are discrete quantities of electrical energy transmitted over an intelligent fixed network — a smarter version of the existing grid. The addressing is real, the discretisation is real, the store-and-forward is real at the node level. But the wire remains. The submarine cable remains. The phase synchronisation, though managed more elegantly, remains. The fundamental vulnerability of circuit-switched energy — that a saturated or severed path blocks all flow — is managed rather than eliminated.

This is the repression. The existing literature has dreamed the right dream, and woken up before its most radical implication: that the energy packet need not travel on a wire at all.

There is a historical precedent for this precise failure of nerve, and it is French.

In 1973, Louis Pouzin at IRIA designed CYCLADES — one of the world's first operational packet-switched networks, whose datagram architecture directly influenced Vinton Cerf and Robert Kahn in developing TCP/IP. France had, independently and simultaneously, arrived at the correct insight. It then chose, for its national data network, not Pouzin's datagrams but X.25 — a protocol that achieved packet-switching in form while preserving circuit-switching in spirit. The virtual circuit of X.25 was a compromise: data were indeed divided into packets, but those packets were routed along a pre-established path, maintained for the session's duration, coordinated by a network that retained global state. The umbilical cord to circuit logic was not cut — it was lengthened and made less visible. Transpac and the Minitel were brilliant implementations of the wrong abstraction. They were superseded not by superior technology but by a superior willingness to accept that reliability could emerge from disorder rather than be imposed upon it.

The energy sector stands today precisely where France stood in 1978: at the choice between the virtual circuit (smart cables, digital grids, managed HVDC interconnections, demand response systems) and the datagram (autonomous battery packets, routerless physical transport, stigmergic self-organisation). The existing energy internet literature has built, with great sophistication, the X.25 of energy. This paper proposes the datagram.

---

## 4. The Return of the Repressed: The Battery as Packet

Consider a mobile telephone. It contains a lithium battery, charged at some location using energy from some source. Its owner carries it — on foot, by vehicle, by train, by aircraft — to another location, where the stored energy is consumed to power computation and communication. The energy has travelled from its source to its point of consumption without traversing any electrical transmission infrastructure whatsoever. It has been physically transported in a container, by a human router, over a network of paths that requires no synchronisation, no phase coordination, and no dedicated capacity reservation.

This is store-and-forward. The mobile phone is an energy packet. Its owner is the router. The observation is trivially obvious once stated. It has not, to the author's knowledge, been incorporated into formal energy network theory.

The mobile phone is the smallest instance of a scale-invariant architecture — fractal in the precise sense that the same routing logic operates identically at every level of the hierarchy, with only the form factor of the packet and the modality of the carrier varying between scales.

A **personal battery pack** (50–100 Wh), charged from a rooftop photovoltaic panel and carried to a point of consumption, is a packet of approximately 0.1 kWh transported by a human router over a range of kilometres.

A **cargo bicycle** equipped with a 1 kWh battery, charged at an agrivoltaic installation and ridden to a distribution point, is a packet of 1 kWh transported by a zero-emission router over a range of tens of kilometres.

An **electric vehicle** with a 75 kWh battery, charged overnight from a renewable source and driven to its destination — and, under vehicle-to-grid protocols, capable of discharging its cargo at the destination — is a packet of 75 kWh transported at highway speed over hundreds of kilometres.

A **twenty-foot ISO shipping container** equipped with lithium iron phosphate battery cells (practical capacity: 1–2.5 MWh depending on cell chemistry and packing density), loaded onto a roll-on/roll-off ferry in Bastia and unloaded at Livorno, Marseille, or Genova, is a packet of 1–2.5 MWh transported by maritime router over 170–500 kilometres, crossing no submarine electrical cable.

A **vessel carrying fifty such containers** (aggregate capacity: 50–125 MWh) is a high-capacity packet carrier serving Mediterranean or Atlantic energy routes, connecting high-irradiation island territories to continental consumption centres without a single metre of dedicated electrical transmission infrastructure.

The fractal self-similarity across six orders of magnitude of energy content — from 0.1 kWh to 125 MWh — is not a coincidence. It is the scale-invariance of the store-and-forward principle itself, which is indifferent to the absolute quantities involved and requires only that the packet be discrete, that it carry its energy to a destination, and that the routing decision be made locally by the carrying agent.

This architecture is not speculative. It exists today, practiced unconsciously and without coordination. Electric vehicles are transported daily by roll-on/roll-off ferries across the Mediterranean, each carrying a charged battery. Mobile phones are carried by aircraft across oceans, each a miniature energy packet. What does not yet exist is the conscious protocol — the equivalent of TCP/IP — that would coordinate these flows into a deliberate network. The packets are real. The network is latent.

This fractal scale-invariance is also, it should be noted, the physical implementation of the subsidiarity principle — the doctrine, enshrined in the Maastricht Treaty but honoured primarily in the breach, that decisions should be taken at the lowest level capable of handling them. The circuit-switched grid violates subsidiarity by construction: the 50 Hz synchronisation constraint requires continental coordination for every watt transferred, making local autonomy physically impossible. The packet-switched grid restores subsidiarity by construction: each packet is autonomous, each node optimises locally, and the system interacts with higher levels only at its margins. Subsidiarity emerges not from political will but from the physics of discrete packets. It is, in this sense, the natural governance of distributed energy systems — not imposed, but released.

---

## 5. The Application Layer: Exergy and the Inference Transduction

The architecture described in the preceding section physically relocates energy by transporting its storage medium. It is practical, immediately deployable, and structurally sound. It is not, however, the most radical implication of the packet-switching analogy applied to energy.

The most radical implication is this: **energy can be transduced into information, and information is already routed as packets over the internet.**

To understand why this matters, we must first discard the conventional unit of energy accounting and replace it with the physically correct one.

Energy, as the first law of thermodynamics states, is conserved. It cannot be consumed — only transformed. What is consumed, in every thermodynamic process, is the capacity to perform useful work: the property that physicists call **exergy**. The exergy of a system is the maximum work extractible from it as it is brought to equilibrium with its environment by a reversible process. It is the currency of thermodynamics, the quantity that the second law — entropy — perpetually erodes.

The distinction between energy and exergy is not pedantic. It is the source of every misleading comparison in the energy density debate.

A twenty-foot container of e-diesel holds approximately 150–200 MWh of chemical energy. A twenty-foot container of lithium iron phosphate batteries holds approximately 2 MWh. The ratio — one hundred to one — appears decisive. It is not, because it compares quantities of different thermodynamic quality.

The Carnot theorem places an absolute ceiling on the fraction of thermal energy convertible to mechanical work: η_max = 1 − T_c/T_h. For a diesel engine operating between 800 K and 300 K, this ceiling is 62.5%. No engineering improvement can breach it, because it follows from the second law of thermodynamics, not from technological immaturity. In practice, the best diesel engines achieve 45–48% conversion efficiency; the remainder is returned to the atmosphere as low-grade heat, its exergy permanently destroyed. A container of e-diesel, routed through a combustion engine and a generator to produce electricity, delivers approximately 60–70 MWh of electrical work at the point of consumption.

A container of LFP batteries, charged from a solar source and discharged at the destination, delivers approximately 1.88–1.94 MWh. The round-trip efficiency of modern LFP cells is 94–97% per cycle. Furthermore, the 60–120 kWh dissipated as heat during charge and discharge is recoverable — for domestic hot water, greenhouse heating, or industrial process heat — bringing the effective thermodynamic efficiency of the energy packet system, when thermal recovery is credited, to approximately 97%. This is comparable to high-voltage direct current transmission over equivalent distances.

The correct comparison is therefore not 200 MWh versus 2 MWh. It is 65 MWh (e-diesel, electrical output) versus 1.94 MWh (LFP, electrical output). The gap is real — approximately a factor of thirty-three — and it closes further along two trajectories: the historical improvement curve of battery energy density (roughly doubling per decade), and the growth of the second-life battery market, where cells retired from electric vehicle service at 70–80% residual capacity become available for energy transport applications at a fraction of primary cell cost.

For applications whose final energy form is not electricity — maritime propulsion, long-haul aviation — the appropriate vecteur is indeed not the battery. Ammonia, methanol, and synthetic aviation fuel (SAF) offer the density required for combustion-powered applications, and their production from renewable electricity through electrolysis and synthesis is technically mature. The correct framework is not "which vector wins" but "which vector is appropriate at which layer of the network" — a multi-protocol architecture, in the TCP/IP sense, where the physical medium is chosen to match the requirements of the application.

This brings us to the transduction layer — the point at which the EPN makes contact with the internet.

When a solar installation converts photons into electrical energy, the conventional next step is to transmit that electrical energy to a point of consumption via the grid. If the grid is saturated — as the SARCO cable periodically is — the energy cannot reach its destination. The circuit is blocked.

An alternative exists. Convert the electrical energy not into electrons to be transmitted, but into computation — specifically, into AI inference, the execution of trained neural network models against incoming queries. An AI inference workload is energetically intensive, highly parallelisable, and produces a service delivered not over any electrical infrastructure but over the internet. The output — a response to a query — is a data packet in the conventional sense, routable to any point on earth at the speed of light, independent of electrical transmission capacity.

In this transduction, the solar installation is not an energy producer connected to a grid. It is an energy transducer: it converts solar irradiation into computation, and sells the computation as a global service. The revenue from that service flows back to the island. The SARCO cable is bypassed entirely, because no electrical energy crosses it. What crosses data cables — which have elastic capacity orders of magnitude greater than power cables — is information.

The value arithmetic of this transduction is significant. Electrical energy exported at Mediterranean wholesale spot prices generates approximately €40–80 per megawatt-hour. The same megawatt-hour, converted into AI inference at sovereign data centre service rates, generates €500,000 to €2,000,000 in service revenue — a value multiplier of ×10 to ×40 per unit of primary exergy. This is not a pricing artefact; it reflects the genuine economic value of high-grade computation relative to undifferentiated electrical energy, in a market where AI inference demand is growing at 30% annually and renewable sovereign supply is structurally scarce.

The economic value of sovereign AI inference is not uniform. It is stratified by the service-level guarantee that can be credibly offered. Best-effort inference trades at commodity rates; standard enterprise inference commands moderate premiums; while mission-critical inference — that which tolerates no more than a few minutes of downtime per year — can command prices an order of magnitude higher. This premium does not reflect marketing rhetoric but the hard economic cost of failure in finance, healthcare, industrial control, or sovereign infrastructure.
Centralised hyperscale data centres, despite sophisticated contractual SLAs, remain fundamentally limited by their dependence on circuit-switched electrical grids. A single regional outage — such as the well-documented failures of major cloud providers — can simultaneously interrupt thousands of nominally high-availability services. The EPN architecture offers a structural alternative.

A sovereign data centre supplied by a rotating fleet of RAIB container-batteries inherits the antifragility designed into the energy layer itself. Energy redundancy is physical rather than contractual: the failure of one container results in graceful, proportional degradation rather than catastrophic outage. Grid independence eliminates the leading vector of data-centre downtime. Real-time state-of-charge monitoring with ±1 % accuracy provides minutes of predictive warning. Source diversity (solar, battery storage, and minimal on-site backup) further reduces the probability of simultaneous failure to levels that make 99.999 % availability not an aspirational target but a direct physical consequence of the architecture.
This is why the η_sla term in the Compute eXergy Unit (CXU) is not merely a reporting coefficient. When the energy substrate itself is antifragile, η_sla approaches 1.0 structurally. The resulting inference service does not compete with hyperscalers on price. It competes on something far more valuable: the physical ability to guarantee, rather than merely promise, that the computation will be there when it is needed.

The Compute eXergy Unit (CXU = E × η_hw × η_sys × η_sla), defined in the MareNostrum framework (Robert, 2026), is the unit of account that prices this transduction correctly. It measures not the electrons entering the data centre but the useful computational work those electrons produce, after accounting for hardware efficiency, system-level overhead, and service-level agreement compliance. The CXU is, explicitly, an exergy unit — not an energy unit. It prices the quality of the work, not merely its quantity.

AI inference is also, thermodynamically, the most exergy-efficient application conceivable for electrical energy: it performs useful work — computation — without any intermediate thermodynamic cycle. Every joule of electricity entering a GPU cluster performs work directly, without passing through combustion, turbine, or heat exchanger. The application layer of the EPN captures the highest fraction of primary exergy in any known energy use case.

---

## 6. Resistances and Their Resolution

In psychoanalytic practice, resistances are the material that must be worked through before the repressed insight can be integrated. They are not obstacles to be dismissed; they are the shape of the problem. We address here the principal technical, economic, and regulatory resistances to the EPN architecture — not to minimise them, but to demonstrate that each is tractable, and that several are resolved by the same underlying principle.

### 6.1 Efficiency and the Carnot Ceiling

The most immediate objection to battery-mediated energy transport is thermodynamic: every charge-discharge cycle incurs losses. This objection has been addressed in detail in the preceding section, but its resolution deserves emphasis. The correct comparison is not between an LFP battery cycle and a hypothetical lossless cable. It is between the LFP system — 94–97% round-trip electrical efficiency, rising to ~97% with thermal recovery — and the real alternatives: grid reinforcement requiring hundreds of millions of euros and a decade of construction, or fossil-fuel generation with a hard Carnot ceiling that no engineering can breach. On this comparison, the battery packet is competitive or superior in efficiency, and dominant in capital cost and deployment speed.

### 6.2 Energy Density: The Multi-Protocol Answer

The density gap between LFP batteries and liquid fuels, correctly stated in exergy terms, is a factor of approximately thirty-three for electrical applications. This is real, and it means that battery transport is appropriate for short and medium maritime distances (100–500 km), while longer distances and non-electrical applications require denser energy vecteurs.

The correct response to this observation is not to concede defeat but to recognise that the EPN is, by design, multi-protocol at the physical layer — exactly as the internet uses different physical media (fibre, copper, radio, satellite) for different network segments. Battery packets are the appropriate medium for short-haul electrical delivery. Methanol, ammonia, and SAF are appropriate for longer haul and non-electrical applications. Hydrogen, despite its low volumetric density in pressurised form, may be appropriate for specific industrial uses. Each vecteur is selected by the routing protocol — the market — based on destination, distance, required energy form, and current price signals.

Furthermore, a mixed container — carrying simultaneously a battery partition and a synthetic fuel partition — is not a compromise but a diversification. A container that can serve both the electricity market and the maritime fuel market in a single voyage amortises its repositioning cost across two revenue streams with low price correlation. When electricity spot prices are depressed, methanol demand may be robust. The mixed container is the energy equivalent of the flexible aircraft seat — a unit of capacity capable of serving multiple markets within a single asset, the central insight of Yield Management applied to energy logistics.

The repositioning of empty containers — the classic problem of container shipping — is similarly soluble by Yield Management logic. It is a stochastic multi-constraint optimisation problem of exactly the class that the airline and shipping industries have managed computationally for forty years. The mixed container, rechargeable partially from the continental grid at off-peak rates during the return voyage, reduces the repositioning cost to an arbitrage operation rather than a pure expense. No closed-form optimal solution is required; a good heuristic — and a sovereign AI inference system running locally is a natural candidate — is sufficient.

### 6.3 The RAIB Principle: Commodity Hardware and Distributed Reliability

In 1988, Patterson, Gibson, and Katz at UC Berkeley published a paper whose title contained its entire argument: *A Case for Redundant Arrays of Inexpensive Disks*. The word that mattered was not Redundant. It was Inexpensive. The insight was that the reliability of a storage system need not come from the reliability of its components; it can come from the redundancy of cheap components managed by intelligent software. The global cloud computing industry — and, by extension, the information economy — was built on this principle.

The Energy Packet Network applies it to electrochemical storage. We call it RAIB: Redundant Array of Inexpensive Batteries.

The price differential between premium industrial battery cells and commodity-grade cells is substantial: €300–500/kWh for premium versus €80–120/kWh for new LFP commodity cells, and €30–60/kWh for second-life cells retired from electric vehicle service at 70–80% residual capacity. A container equipped with second-life cells costs five to fifteen times less than one equipped with premium cells. The accepting of higher individual cell failure rates is managed by the Battery Management System — the software equivalent of the RAID controller — which routes around degraded cells exactly as a RAID array routes around failed disks. Container-level failures are managed by fleet redundancy: the EPN does not collapse when a single container fails, any more than ARPANET collapsed when a single node failed.

Second-life battery integration also provides an environmental dividend. A battery cell retired from EV service has a carbon footprint already amortised over its first-life use. Deploying it in an energy transport container before final recycling extends its productive life by five to ten years, reducing the embodied carbon per unit of energy transported. The RAIB principle is simultaneously the economic argument for commodity hardware and the ecological argument for circular material flows.

### 6.4 Direct Current: Releasing the 1888 Constraint

The alternating current grid is not an engineering optimum. It is a historical settlement.

In 1888, the transformer gave AC a decisive advantage over Edison's DC systems by enabling efficient voltage transformation across long distances. In 2025, silicon carbide and gallium nitride power electronics transform DC voltage with efficiency exceeding 98%, in compact solid-state devices, at costs that have fallen by an order of magnitude over the past decade. The physical argument for AC that settled the War of Currents is no longer valid.

The EPN is under no obligation to inherit the AC legacy. A DC-native architecture — photovoltaic panels generating DC, batteries storing DC, data centres consuming DC — eliminates every AC/DC conversion step. Each conversion avoided recovers 2–4% of system efficiency. A fully DC-native energy packet path from solar cell to GPU cluster eliminates four such conversion steps relative to a conventional AC grid-connected supply, recovering 8–16% of system energy — more than offsetting the LFP charge-discharge losses that constitute the standard efficiency objection. Modern high-performance AI data centres are already migrating toward high-voltage DC distribution internally. The EPN's DC supply is architecturally coherent with this trend. The packet was always meant to be DC.

### 6.5 Safety: Engineering Challenges, Not Category Barriers

Battery containers operating at transport scale involve voltages of 800–1,500 V DC, capable of delivering lethal energy in milliseconds. This is not a trivial concern. It is a well-understood one.

High-voltage DC systems have been safely operated in industrial and utility contexts for decades. Battery-electric ferries operating in Norwegian fjords carry passengers over high-voltage DC propulsion systems under routine maritime safety regulation. The thermal runaway risk — the exothermic decomposition characteristic of lithium-ion batteries under abuse conditions — is chemistry-specific. LFP cells, whose cathode chemistry involves iron and phosphate rather than the cobalt-rich oxides of NMC formulations, are substantially more thermally stable. Their decomposition temperature is higher, the reaction far less energetic, and spontaneous propagation between cells correspondingly rare. Every serious large-scale stationary storage deployment has converged on LFP for precisely this reason. Transport of lithium batteries is already governed by the International Maritime Dangerous Goods Code, Class 9, under which electric vehicles are routinely carried by roll-on/roll-off ferries across Mediterranean and Atlantic routes. The extension of this regulatory framework to purpose-built energy containers is a matter of standardisation and incremental regulatory development — not a category leap.

### 6.6 Regulation: An Unexpected Advantage

A question that the EPN literature has not addressed deserves explicit treatment: does a container-battery crossing a national or EU border constitute the transport of electricity in the regulatory sense of Directive 2019/944 on the internal electricity market? If it does, the container would be subject to regulated network access tariffs, third-party access obligations, and a substantial compliance burden.

The legal answer is almost certainly negative. A container carrying charged batteries is transporting a physical good — electrochemical storage — not transmitting electrical energy over a network. The distinction is the same as that between shipping a barrel of oil (transport of goods) and pumping crude oil through an international pipeline (transport of energy subject to network regulation). The battery container is goods. The SARCO cable is network. Regulatory frameworks that apply to one do not apply to the other. This is not a loophole; it is a structural feature of the EPN architecture that confers a significant commercial advantage over regulated grid-based alternatives.

---

## 7. The Protocol: Stigmergy, Skin in the Game, and the Commons

A packet network without a routing protocol is a collection of disconnected nodes. ARPANET required TCP/IP. The EPN requires an equivalent: conventions governing how packets are described, priced, routed, and accounted for across a distributed network of producers, carriers, and consumers. This section describes the principles on which such a protocol should be built, and the MareNostrum framework as a first implementation.

### 7.1 Stigmergy: Coordination Without a Centre

The coordination mechanism of the EPN is not central dispatch. It is stigmergy — a term coined by French entomologist Pierre-Paul Grassé in 1959 to describe the coordination of termite colonies. Grassé observed that termites do not communicate with one another to build their architecturally sophisticated mounds. Each individual responds to local conditions — the concentration of pheromones, the shape of existing structures — modifying its local environment in the process. Other individuals respond to the modified environment. Global order emerges from local responses to local signals, without any agent possessing global knowledge and without any coordinator issuing global instructions. The termite colony builds its cathedral without an architect.

The EPN operates by the same mechanism. No central dispatcher routes containers to their optimal destinations. Each operator of an energy packet — whether a container-battery fleet manager, a data centre operator, or an individual vehicle owner — responds to local price signals: the spot price of renewable energy at the source, the market price of AI inference at the destination, the shipping cost of the intermediate route. These decisions modify the distribution of energy packets across the network. Subsequent operators respond to the modified distribution. Global allocation emerges from local decisions without central coordination.

The CXU price signal is the pheromone of the EPN. When the price of sovereign AI inference rises at a given node — because demand has exceeded supply — containers are routed toward that node. The influx increases supply and depresses the price. Equilibrium emerges without a dispatcher. This is not an approximation to optimal central dispatch; for a system of the complexity and geographic distribution of the EPN, it is superior to central dispatch, because it aggregates local knowledge that no central planner can possess.

### 7.2 Skin in the Game: The Condition of Honest Signals

Stigmergic coordination produces reliable outcomes only when the price signals to which agents respond are honest — when the agents who emit and respond to signals personally bear the consequences of their responses. Taleb (2018) calls this *skin in the game*. Without it, price signals are corrupted by asymmetric information, socialised losses, and the systematic tendency of those who make decisions to offload the consequences onto those who do not.

The existing electrical grid violates this condition at every layer. The network operator earns a regulated return whether the network is efficiently managed or not. The large consumer pays a smoothed regulated tariff that conceals the real-time cost of its demand. The data centre operator that purchases Renewable Energy Certificates bears no physical consequence for the fossil fuel actually consumed on its behalf. The signal is dishonest; the coordination fails.

The EPN embeds skin in the game structurally. The container operator who misroutes a cargo to a market with depressed prices loses money on that voyage. The data centre operator powered by sovereign solar AI infrastructure and governed under a CXU service-level agreement pays financially for every hour of degraded service — the η_sla term in the CXU formula is not a reporting metric but a revenue deduction. The SCIC governance structure, with its institutionally impartible reserves, ensures that those who make investment decisions cannot distribute the accumulated commons to themselves — the most radical form of skin in the game in governance design.

The pheromone is honest because the ants pay for their mistakes.

### 7.3 Antifragility: The Emergent Property

A stigmergic system with honest price signals does not merely survive disorder. It grows stronger through it — antifragile in Taleb's precise formulation: not robust (unchanged by volatility) but energised by it.

The EPN is antifragile at every level of its architecture. An oil price spike makes battery transport more competitive relative to fossil-fuel alternatives, accelerating the diversification of the EPN's vecteur portfolio. A cell chemistry recall forces the adoption of more stable chemistries, improving average fleet reliability. A closed maritime route — through weather, conflict, or regulatory action — develops alternative routes that remain available after reopening, increasing the redundancy of the network. A saturated data centre market in one region shifts inference demand to underserved regions, developing new nodes and reducing geographic concentration.

This is precisely Baran's logic, extended from telecommunications to energy: a distributed network that routes around damage does not merely maintain its function — it improves it, because the routing around damage leaves the alternative paths established and tested. The circuit-switched grid has the opposite property: it can survive within its rated capacity but fails catastrophically when that capacity is exceeded, because there are no alternative paths to develop. It is fragile. The EPN is antifragile.

The same distinction applies, at higher resolution, to the RAIB principle. A fleet of inexpensive batteries with a predictable individual failure rate is antifragile: failures are continuous, low-magnitude, and informative — they reveal which chemistries, manufacturers, and operating conditions are reliable, allowing continuous improvement of fleet composition. A single premium battery system is fragile: it operates reliably within spec and fails catastrophically outside it, generating no useful information until the catastrophic event.

### 7.4 MareNostrum as Routing Protocol

The MareNostrum framework, maintained as an open-source specification (CC BY-SA 4.0) at github.com/JeanHuguesRobert/marenostrum, represents a first attempt at a conscious routing protocol for the Mediterranean Energy Packet Network. Its core elements map directly onto the TCP/IP stack.

At the physical layer, MareNostrum treats Mediterranean solar irradiation as a democratic commons — a resource physically available to Corsica, Sardinia, Sicily, Tunisia, and the territories of the northern shore, analogous to the radio spectrum that underlies wireless communication. This commons is governed by federated assemblies on the principle of one person, one vote, with imperative and revocable mandates — a governance architecture designed to be anti-capture by construction: no single actor, state, or corporation can seize control of a protocol that belongs to everyone who lives under the sun.

At the network layer, the CXU provides a standardised unit of account for sovereign compute services derived from a given quantity of primary solar exergy. Like an IP packet header, the CXU carries provenance, quality, and service-level metadata that enables routing and pricing decisions across a distributed network of producers and consumers.

At the application layer, sovereign AI inference services constitute the primary revenue stream — the HTTP of the energy internet. The token is the unit of economic output; the CXU is the unit of productive capacity; the photon is the unit of primary input. The value chain is complete, sovereign at every layer, and free of the SARCO constraint.

---

## 8. The Wider Family: From Energy to Cognition

The unconscious grid was an energy story. It need not be only that.

Once the diagnostic is named — *a circuit-switched system stuck in 1968, surrounded by datagram alternatives it has not yet recognised* — the pattern reveals itself wherever the symptom recurs. Each instance is a different patient with the same repression. Each requires its own analysis, its own resistances to work through, its own resolution. The packetization corpus, of which this paper is the entry point, is that gradual analysis.

Four contemporary instances, briefly, to suggest the family.

### 8.1 The Cognitive Grid

The grid of contemporary artificial intelligence is, structurally, circuit-switched. A user connects to a single provider; the conversation establishes a dedicated path between them; the path is held for the duration; if the provider goes down, if the user changes provider, if the conversation must migrate to a different agent, the path collapses and the work it carried is lost. The session is the dedicated circuit. The cognitive work it transports is the captured energy that cannot leave it.

The datagram in this domain is the **cognitive packet** — a transport-neutral unit of work composed of an *envelope* (kind-agnostic metadata that any receiver can route, queue, validate, archive, or acknowledge) and a *payload* (kind-specific content interpretable by an agent capable of handling the declared kind: continuation, objection, hypothesis, decision, failure, routing). A cognitive packet can be copied into a new conversation with a different provider, pasted into an issue, attached to a document, forwarded to a human collaborator, resumed by a different model. The work routes around the provider rather than being held captive by it.

The implementation already exists in the `cogentia.continuation.v1` protocol (Agent-Resumable CLI, 2026) and its envelope/payload generalisation in [Cognitive Packets](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md). The provider remains a useful node in the network. It is no longer the network.

### 8.2 The Sociability Grid

The grid of mobile data and battery is, structurally, circuit-switched. When a user runs out of data quota or battery at the wrong moment — at a hospital, at a border, after midnight on a remote road — the path to the carrier is broken and no fallback exists. The carrier is the dedicated circuit. When the circuit fails, the user is alone.

The datagram in this domain is **proximate hospitality**: the data or battery a nearby phone can spare, voluntarily, through a brief peer-to-peer transfer. Mediterranean tradition has named this exchange for two millennia; it has only recently become digitisable. The `brique-auxilia` module of the Inseme platform ([spec, 2026](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/brique-auxilia/AUXILIA.md)) is the protocol that makes the exchange auditable and transmissible — explicitly described in its README as the human instantiation of the store-and-forward principle from FractaVolta's Energy Packet Networks. The carrier remains useful where coverage is good and quota is sufficient. It is no longer the only available substrate.

### 8.3 The Monetary Grid

The currency layer of contemporary commercial exchange is, structurally, circuit-switched. The euro closes a transaction along a dedicated, irreversible path: settlement is final, the counter-party identity collapses into the price, the social reciprocity the exchange may have carried is severed at the moment of payment.

The datagram in this domain is the **Maussian counter-gift** — a public, voluntary, nominative, transparent, traceable, and partially convertible layer of recognition superposed *on top of* the euro transaction, without substituting for it. The euro circuit closes the transaction; the gift packet opens a parallel layer of social memory. The [Kudos working paper](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/kudos.md) (2026) proposes this superposition explicitly: not currency substitution, but envelope-and-payload reasoning applied to value itself — the euro as carrier, the kudo as the cognitive packet of social reciprocity that travels on top.

### 8.4 The Territorial Grid

The contemporary debate on territorial autonomy is, structurally, circuit-switched. Autonomy is conceived as a statutory transfer along a dedicated political path: constitutional reform, special status, normative power devolved from one centre to another. The path is dedicated; nothing happens until the path is completed; if the path is blocked, the territory waits.

The datagram in this domain is **autonomy of capacity** — the verifiable, documented, transmissible conversion of a territory's existing capital into effective collective capabilities, *independently of whatever statutory transfer has or has not occurred*. The [Autonomia working paper](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/autonomia.md) (2026) formalises this in the Corsican case: each capability built, each experiment documented, each public test conducted is a packet that does not depend on the statutory circuit being open. The territory routes around its own institutional dependence.

### 8.5 The same diagnosis, the same cure

These four instances — cognition, sociability, money, territory — do not exhaust the family. Distributed AI governance under [DHITL](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md), commons under Ostrom's principles, the [packet attractor](packet_attractor.md) as a scale-invariant transition mechanism, the [packet transition](packet_transition.md) as a lateral reading of circuit networks — each is a further instance of the same pattern at a different layer.

What the four share is not the technology. It is the diagnostic shape: in every case the circuit-switched habit has been preserved past the point where its limitations were demonstrable, because the alternative — the datagram, the packet, the work that routes around any single dedicated path — has not yet been recognised as the natural state of the system. The unconscious grid was the energy version of this story. The story is the same wherever it is told.

What was missing, in each case, was the protocol that made the alternative conscious.

---

## 9. Conclusion: The Diversity Principle and the End of an Old Argument

Every section of this paper has, on examination, converged on a single underlying principle. It is time to name it.

**Diversity is not a feature of the Energy Packet Network. It is its source.**

Diversity of physical vecteurs — battery, methanol, ammonia, SAF — ensures that no single price shock or technology failure can collapse the network. Diversity of form factors — from the mobile phone to the container vessel — ensures that the network operates at every scale without a central coordinator choosing the "correct" size. Diversity of routes — road, rail, ferry, aircraft — ensures that the network routes around closures without losing capacity permanently. Diversity of cell chemistries — LFP today, solid-state tomorrow, second-life always — ensures that no single manufacturer or supply chain can hold the network captive. Diversity of governance structures — SCIC, cooperative, municipal, academic — ensures that no single institutional actor can capture the protocol.

This diversity is not designed. It emerges from the packet-switching architecture itself, as subsidiarity emerges from the elimination of the synchronisation constraint. A circuit-switched grid requires homogeneity — one frequency, one phase, one operator per territory — because continuous synchronisation requires continuous standardisation. A packet-switched grid requires only that each packet carry its own address. Everything else — the chemistry, the form factor, the route, the operator — can be different from every other packet. Diversity is the natural state of the packet-switched system; homogeneity is the enforced state of the circuit-switched one.

This observation resolves, structurally rather than ideologically, the oldest debate in political economy.

Capitalism maintains that the uncoordinated decisions of self-interested actors, mediated by price signals, produce outcomes superior to those achievable by central planning. It is correct about the virtue of distributed decision-making and the information-aggregating power of prices. It fails when profit-seeking produces homogeneity — when all actors converge on the same winning strategy, eliminating the diversity that makes systems resilient. The financial crisis of 2008 was a circuit-switched failure: all banks had loaded the same assets, all models shared the same assumptions, and when one node failed, the dedicated circuits connecting them transmitted the failure everywhere simultaneously.

Collectivism maintains that the coordination failures of market systems — externalities, public goods, long-term investment, systemic risk — require central planning to correct. It is correct about the existence of these failures. It fails when central planning suppresses the local knowledge that only distributed agents possess, and when it enforces a standardisation of strategy that destroys the diversity from which resilience emerges. The planned economies of the twentieth century were circuit-switched failures of a different kind: all economic activity routed through a single coordination centre, which when it failed, failed completely.

The packet-switched network is neither. It separates two questions that political economy has always conflated: who governs the protocol, and who operates within it.

The protocol — the standard container format, the CXU pricing unit, the routing conventions, the governance rules — is a commons. It cannot be owned by any single actor, captured by any single state, or enclosed by any single corporation. It is maintained by all who depend on it, governed by subsidiarity, and changed only by processes that require broad consent. This is not collectivism, because no central plan determines what energy is produced, by whom, for whom, at what price. It is a commons — Ostrom's third way, demonstrated empirically in fishing villages, irrigation systems, and forest communities across five continents, and now in TCP/IP, Linux, and the open protocols of the internet.

The operation — what energy to produce, which vecteur to choose, which route to take, which market to serve, at what price — is fully distributed, competitive, diverse, and stigmergic. No central coordinator determines the optimal allocation. Price signals — honest ones, because every operator has skin in the game — coordinate the distributed decisions of thousands of actors, each with local knowledge no planner can possess. This is not capitalism, because the protocol that enables this competition is a commons that no competitor can appropriate. It is a market operating within a governed commons — the structure of the internet, applied to energy.

The antifragility of this architecture is not a design choice. It is an emergent consequence of the diversity that the packet-switched structure naturally produces. A system that is diverse by construction, coordinated by stigmergy, governed by skin in the game, and structured on a substrate of commons is, by definition, one that grows stronger through disorder. The disorder selects for more reliable chemistries, more robust routes, more efficient operators, and more adaptive governance — continuously, without catastrophic reset.

Grassé's termites have been building antifragile structures for three hundred million years without an architect. The internet has been routing antifragile information flows for fifty years without a central coordinator. The Energy Packet Network proposes to do the same for energy — starting, modestly, with a container ferry between Bastia and Livorno, and a solar data centre in Corte running sovereign AI inference on the same grid that the Romans used to tell time.

The unconscious grid has always known this. Every mobile phone battery was a vote for the datagram. Every container of electric vehicles on a Mediterranean ferry was a proof of concept. Every sovereign AI inference token was a photon that escaped the SARCO constraint.

What was missing was the protocol that made it conscious.

Now, Pouzin was right. The datagram won for information. Let it win for energy.

---

## Acknowledgements

The author has practiced iterative software development since the late 1970s and was an early signatory of the Agile Manifesto (2001). He recognises in the Energy Packet Network the same architectural principle: local response over central coordination, working packets over comprehensive planning. The author used Claude (Anthropic, claude.ai) as a writing and structuring assistant during the preparation of this manuscript. All analytical choices, theoretical positions, and the MareNostrum framework are the sole responsibility of the author.

---

## References

- Abe, R., Taoka, H., & McQuilkin, D. (2011). Digital grid: communicative electrical grids of the future. *IEEE Transactions on Smart Grid*, 2(2), 399–410.
- Baran, P. (1964). *On Distributed Communications*. RAND Corporation, Memoranda RM-3420-PR through RM-3440-PR.
- Cerf, V., & Kahn, R. (1974). A protocol for packet network intercommunication. *IEEE Transactions on Communications*, 22(5), 637–648.
- Gelenbe, E. (2012). Energy Packet Networks: ICT-based energy allocation and storage. In *Green Communications and Networking*, Springer LNICST, Vol. 51, pp. 186–195.
- Grassé, P.-P. (1959). La reconstruction du nid et les coordinations interindividuelles chez *Bellicositermes natalensis* et *Cubitermes* sp. La théorie de la stigmergie. *Insectes Sociaux*, 6(1), 41–80.
- Hikihara, T., Takahashi, R., & Tashiro, K. (2013). Router for power packet distribution network: design and experimental verification. *IEICE Transactions on Communications*, E96-B(8), 2161–2168.
- International Energy Agency (2025). *Energy and AI*. IEA, Paris. Available: iea.org/reports/energy-and-ai.
- Nardelli, P.H.J., et al. (2019). Energy internet via packetised management: enabling technologies and deployment challenges. *IEEE Access*, 7, 16909–16924.
- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Patel, R., Mahalingam, N., & Patel, A. (2025). The environmental impact of AI servers and sustainable solutions. arXiv:2601.06063.
- Patterson, D.A., Gibson, G., & Katz, R.H. (1988). A case for redundant arrays of inexpensive disks (RAID). *ACM SIGMOD Record*, 17(3), 109–116.
- Pew Research Center (2025). What we know about energy use at U.S. data centers amid the AI boom. October 24, 2025.
- Robert, J.H.N. (2026). From Sun to Sovereignty: Communal Sovereign Funds as a mechanism to decouple tourism from land dispossession. Institut Mariani / C.O.R.S.I.C.A., Corte. CC BY-SA 4.0. Available: github.com/JeanHuguesRobert/marenostrum.
- Taleb, N.N. (2012). *Antifragile: Things That Gain from Disorder*. Random House.
- Taleb, N.N. (2018). *Skin in the Game: Hidden Asymmetries in Daily Life*. Random House.
- Toyoda, J., & Saitoh, H. (1998). Proposal of an open electric energy network (OEEN) to realise cooperative operations of IOU and IPP. In *Proceedings of EMPD '98*, Vol. 1, pp. 218–222. IEEE.
- World Economic Forum (2025). How data centres can avoid doubling their energy use by 2030. Available: weforum.org.

---

## Author Note

Jean Hugues Noël Robert, baron Mariani, is the founder and director of Institut Mariani (1 cours Paoli, F-20250 Corte, Corsica), the R&D branch of the C.O.R.S.I.C.A. non profit organization (founded Corte, 1995, predating the coinage of "open source"). The MareNostrum framework described in Section 7 is maintained as an open-source specification at github.com/JeanHuguesRobert/marenostrum under CC BY-SA 4.0. The author holds US patent US7606221B2 (priority 1999) on an autodiscover protocol enabling endpoint devices to autonomously locate distributed server infrastructure without a capturable central registry — the same architectural question that the EPN routing protocol addresses for energy. The author declares no financial conflict of interest. Correspondence: jhr@baronsmariani.org

---

## Optimized condensed version for AI agents

**The global electrical grid is structurally circuit-switched** (continuous synchronization, dedicated paths, single point of failure, limited scalability, fragility to saturation or outages — Corsica's SARCO as canonical example).

**The repressed solution since 1964 (Baran) is physical store-and-forward**: treat energy not as a continuous flow over wires, but as **discrete, addressable, autonomous packets** physically transported (LFP second-life or new batteries in ISO containers, EVs, cargo bikes, ferries, etc.).

### EPN Architecture (Energy Packet Network)

- **Physical layer**: fractal electrochemical packets (0.1 kWh → 100+ MWh) routed via conventional logistics (road, rail, maritime) → **zero dependence on HV cables, zero AC synchronization**.
- **Reliability mechanisms**:
  - **RAIB** (Redundant Array of Inexpensive Batteries): cheap-component redundancy + intelligent BMS → graceful proportional degradation, never catastrophic.
  - **Multi-level diversity** (vectors: battery/methanol/ammonia/SAF; routes; operators; chemistries; governance models) + stigmergy through honest price signals (skin-in-the-game).
  - **Physical subsidiarity**: each packet makes local routing decisions → Talebian antifragility (the system improves under disorder).

### Application Layer (Transduction)

Stranded solar exergy → **direct transduction into sovereign AI inference** (exergy → internet-routable tokens), completely bypassing grid physical constraints.

### Emergent Critical Property

The antifragility of the energy layer **propagates structurally** to the inference layer:  
→ native extremely high energy availability (grid independence, physical redundancy, precise real-time SOC monitoring, source diversity).  
→ enables SLA 99.99x % (mission-critical / high-grade inference) via η_sla in the CXU approaching 1.0 **structurally**, not contractually.  
→ positions the EPN to capture the market premium for premium inference (finance, healthcare, industry, sovereignty) where physical availability guarantee is the dominant differentiator.

### Axiomatic Summary (for agent reasoning)

**EPN = packet-switching applied to physical exergy + exergy → sovereign compute transduction + distributed antifragility → guaranteed high availability → durable economic premium for high-grade AI inference.**

---

## Potential Target Journals

- *Energy Research & Social Science* (Elsevier) — primary target; the journal explicitly welcomes theoretically ambitious, historically grounded, and interdisciplinary contributions to energy systems analysis
- *Joule* (Cell Press) — high-impact energy journal, receptive to conceptually original contributions that cross disciplinary boundaries
- *Telecommunications Policy* (Elsevier) — for the network theory and regulatory dimensions
- *IEEE Access* (IEEE) — broader scope, open access, faster publication timeline
<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Rendre capable — noyau doctrinal provisoire](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/noyau_doctrinal_rendre_capable.md)
- [Concept Index — FractaVolta](research/concepts.md)
- [Corpus Status — FractaVolta](research/corpus-status.md)
- [Energy packets](docs/energy-packets.md)
- [For deployers](docs/for-deployers.md)
- [For researchers](docs/for-researchers.md)
- [FractaVolta](README.md)
- [Research Index — FractaVolta](research/index.md)
- [Concept Index — Inox](https://github.com/JeanHuguesRobert/Inox/blob/master/research/concepts.md)
- [Research Index — Inox](https://github.com/JeanHuguesRobert/Inox/blob/master/research/index.md)
- The Iɴᴏx programming language
- [Documents - All Tracked Repos](https://github.com/JeanHuguesRobert/JeanHuguesRobert/blob/main/research/documents.md)
- [Pacte anti-capture solaire et inférentielle](https://github.com/JeanHuguesRobert/marenostrum/blob/main/research/pacte_anti_capture_solaire_inferentielle.md)
<!-- END_AUTO: backlinks -->
