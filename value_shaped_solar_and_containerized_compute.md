# Value-Shaped Solar and Containerized Compute

## Toward Temporal Agrivoltaics as Infrastructure for Dispatchable Intelligence

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani — C.O.R.S.I.C.A.

1 cours Paoli, F-20250 Corte. jhr@baronsmariani.org institutmariani@gmail.com

Working Paper — April 2026

*Part of the FractaVolta & Mare Nostrum research program.*
[github.com/JeanHuguesRobert/FractaVolta](github.com/JeanHuguesRobert/FractaVolta)
[github.com/JeanHuguesRobert/marenostrum](github.com/JeanHuguesRobert/marenostrum)

*Cross-reference:*
- Robert & Valdes (2026), "Constellia: A Fractal Architecture for Energy,
Food, and Digital Sovereignty in Island Territories."
[github.com/JeanHuguesRobert/marenostrum/blob/main/constellia.md](github.com/JeanHuguesRobert/marenostrum/blob/main/constellia.md)
- *Robert (2026), "Electricity in Containers. [github.com/JeanHuguesRobert/FractaVolta/blob/main/electricity_in_containers.md](github.com/JeanHuguesRobert/FractaVolta/blob/main/electricity_in_containers.md)
- *Robert (2026b), "DHITL." [github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md](github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md)
---

## Working Status Note

This is a discussion draft inviting critique before publication. It synthesises empirical findings from the vertical bifacial agrivoltaic literature with concepts from the FractaVolta distributed inference framework and the Constellia Mediterranean energy architecture. The core novelty claim is narrow: the paper does not originate the concepts of agrivoltaics, flexible compute, or energy-compute co-design. It proposes their structural integration under a unified optimisation objective and introduces three concepts — *value-shaped generation*, *Grid Value Yield*, and *Compute-Coupled Agrivoltaics* — as potentially publishable contributions to two literatures that currently do not speak to each other.

---

## Abstract

Conventional photovoltaic optimisation treats electricity as a homogeneous commodity measured in annual kilowatt-hour yield. This paper argues that this paradigm is incomplete in two directions simultaneously.

First, recent empirical evidence from vertical bifacial agrivoltaic systems confirms that east-west oriented panels produce a characteristic **double-peaked diurnal profile** — enhanced morning and evening generation, reduced midday output — whose temporal structure correlates strongly with high-value hours in electricity spot markets. A kilowatt-hour at 07:30 or 18:30 is not economically equivalent to one at 13:00. The relevant optimisation variable is not yield alone, but *value-shaped generation*.

Second, flexible containerised computing loads — inference tasks, asynchronous AI workloads, scientific computation — can be temporally dispatched to absorb otherwise curtailed or undervalued renewable output. When compute is treated as controllable demand rather than passive load, it becomes *virtual storage*: a mechanism for absorbing intermittent supply without electrochemical conversion. This is not metaphorical. It is architectural.

The conjunction of these two observations suggests a new infrastructure class: **Compute-Coupled Agrivoltaics (CCA)** — systems in which photovoltaic design is optimised jointly for crops, electricity value, and computational workload absorption. We propose a four-dimensional objective function — energy yield, market value yield, grid system value yield, and computational value yield — and introduce **Grid Value Yield (GVY)** as a candidate metric capturing the third and fourth dimensions.

The paper connects to the FractaVolta distributed inference architecture (which provides the routing and dispatch layer for flexible compute), the Constellia Mediterranean energy architecture (which provides the physical deployment context and verified field numbers), and the DHITL framework (which provides the Compute Exergy Unit as the economic denominator for computational value).

**Keywords:** agrivoltaics; vertical bifacial photovoltaics; value-shaped generation; temporal agrivoltaics; flexible compute; containerised computing; compute-coupled agrivoltaics; Grid Value Yield; FractaVolta; Constellia; energy-compute co-design; dispatchable intelligence.

---

## 1. Introduction

Photovoltaic systems are evaluated almost universally through a small set of metrics:

- Levelised Cost of Energy (LCOE)
- Annual specific yield (kWh/kWp/year)
- Capacity factor
- Land Equivalent Ratio (LER, in agrivoltaic contexts)

These metrics share a common implicit assumption: **a kilowatt-hour is a kilowatt-hour**. Annual energy yield treated as a homogeneous scalar.

This assumption was approximately correct when photovoltaics were a marginal fraction of the energy mix and grid operators could absorb their output at whatever time it appeared. It is becoming structurally incorrect as solar penetration deepens.

Two phenomena are driving the correction:

**Temporal price divergence.** As midday solar generation saturates grid capacity in high-solar regions, spot electricity prices during peak irradiance hours collapse — sometimes to zero or negative values — while morning and evening hours, when demand is high and solar generation is low, command premium prices. The duck curve, now well documented in California, Spain, Italy, and increasingly Germany, is the market expression of this divergence. A photovoltaic system that produces heavily at noon generates electricity when it is least valuable; one that produces at shoulder hours generates electricity when it is most valuable.

**Follow-the-power computing.** Switzer et al. (2021) argue that the growing problem is not a shortage of wind and solar power, but too much generation at the wrong times and in the wrong places, and propose a geographically-distributed zero-carbon compute infrastructure — TerraWatt — that uses surplus renewable energy and older hardware to absorb otherwise curtailed generation. This is the origin of the *follow-the-power* paradigm: move compute to where and when renewable energy is surplus, rather than moving renewable energy to where compute is.

This paper proposes that these two phenomena, taken together, suggest a structural redesign of how agrivoltaic systems are conceived and optimised. The question is not "how much electricity can this system produce per year?" It is: "what temporal profile of electricity production maximises total value, including the value that flexible computational demand can extract from otherwise undervalued output?"

---

## 2. Empirical Foundation: The Double-Peaked Profile

### 2.1 The Diurnal Signature of Vertical East-West Bifacial Systems

The temporal profile of a vertical east-west bifacial photovoltaic system differs fundamentally from that of a south-facing tilted system. This is not a modelling assumption; it is a well-documented empirical finding.

Kumar, Singh, and Chander (2026), in a year-long experimental assessment at IIT Bhilai, confirm that east-west facing vertical bifacial modules produce two production peaks — one in the morning and one in the evening — as compared to the single notable rise at midday observed for a monofacial south-facing module.

A comprehensive study at the University of York (Badran & Dhimish, 2024) finds that vertical bifacial systems outperform conventional tilted monofacial systems by +26.91% during early morning hours and +22.88% during late afternoon hours — the precise windows of highest electricity market value.

SkyGre (Sentnet Engineering), in field deployment data from operational vertical agrivoltaic installations, reports that east-west oriented bifacial panels generate two daily peaks in energy output at morning and evening, producing up to 20% more energy than standard systems via these morning and evening peaks, with this setup aligning better with typical electricity demand patterns.

The annual yield trade-off is real and should not be minimised. A comparative study in Jordan finds that the vertical east-west system achieves approximately 35% lower annual specific yield than the south-facing tilted alternative, while exhibiting more uniform diurnal output and enhanced early-morning and late-afternoon generation. This yield penalty may be partially or wholly compensated by the value premium of shoulder-hour generation — whether that trade-off is positive depends on market structure, grid conditions, and the presence of flexible computational demand. This is the central empirical question of the paper.

### 2.2 The Market Value of Temporal Structure

European electricity spot markets exhibit systematic temporal price patterns. On the EPEX SPOT Day-Ahead market in France, Germany, and Italy, average hourly prices over 2023–2024 show:

- Peak morning hours (07:00–10:00): typically €80–140/MWh
- Midday solar saturation (11:00–15:00): frequently €20–60/MWh, and occasionally zero or negative during high-solar days
- Evening peak (17:00–21:00): typically €90–160/MWh
- Overnight (22:00–06:00): €30–70/MWh

The spread between midday and shoulder-hour prices — routinely €60–100/MWh on normal days, and €200–400/MWh on days of high solar irradiance combined with low demand — represents the economic opportunity that temporal shaping addresses.

A system producing 100 MWh at midday earns roughly €3,000–6,000. The same 100 MWh produced during morning and evening shoulder hours earns €8,000–14,000 — a factor of 2–4 difference in revenue for identical energy output.

The vertical bifacial east-west profile does not merely avoid curtailment; it actively targets the highest-value hours of the diurnal cycle.

### 2.3 Market-Scale Implications

Szabo et al. (2024), in *Nature Communications*, study the impacts of large-scale deployment of vertical bifacial photovoltaics on European electricity market dynamics, finding significant market-level effects from the temporal redistribution of solar generation. This study confirms that the value-shaping effect is not merely a microeconomic arbitrage available to early adopters, but a structural property of the technology that alters market dynamics at scale — and which therefore deserves treatment as an infrastructure design variable rather than a performance metric.

---

## 3. From Energy Maximisation to Value Shaping

### 3.1 The Conventional Optimisation

Traditional photovoltaic optimisation maximises:

$$\max_{(\text{tilt}, \text{azimuth}, \text{technology})} \int_0^{8760} P(t)\, dt$$

where $P(t)$ is instantaneous power output and the integral is annual energy yield in kWh/kWp. This is equivalent to maximising the area under the production curve, with no weighting for time of day.

The south-facing tilted system wins this optimisation decisively, because it maximises capture of peak-irradiance noon solar radiation.

### 3.2 The Value-Shaped Optimisation

The first extension weights production by its market price:

$$\max_{(\text{design})} \int_0^{8760} P(t) \cdot \lambda(t)\, dt$$

where $\lambda(t)$ is the day-ahead spot price at hour $t$. This is the **Market Value Yield** objective. Under this objective, the optimal design shifts toward temporal shapes that correlate positively with $\lambda(t)$ — morning and evening peaks rather than noon peaks.

We define:

$$V_m = \int_0^{8760} P(t) \cdot \lambda(t)\, dt \quad [\text{€/year}]$$

as the **Market Value Yield** of the system. For a south-facing tilted system and a vertical east-west system with identical installed capacity $P_{rated}$, the ratio $V_m^{\text{vertical}} / V_m^{\text{tilted}}$ may exceed 1.0 even when the energy ratio $E^{\text{vertical}} / E^{\text{tilted}} < 1.0$, depending on the price structure $\lambda(t)$.

The hypothesis is that this ratio exceeds 1.0 in Mediterranean markets under current and projected price structures. This is empirically testable from PVGIS production data combined with EPEX historical prices.

### 3.3 The Temporal Agrivoltaic Frame

We call this design philosophy **Temporal Agrivoltaics**: the explicit co-optimisation of the temporal structure of PV production with its economic value, rather than its total volume.

Temporal agrivoltaics is not merely a different parameter choice within existing optimisation frameworks. It is a different objective function — one that treats the time-domain as a primary design variable rather than an incidental consequence of geographic and technical constraints.

This shift has a parallel in telecommunications: the transition from circuit-switching (which maximises channel utilisation without regard to traffic timing) to packet-switching (which treats timing and routing as primary design variables). The analogy with store-and-forward energy logistics, developed in the companion paper *Electricity in Containers* (Robert, 2026), is intentional.

---

## 4. Compute as Virtual Storage

### 4.1 The Core Insight from TerraWatt

Switzer et al. (2021) propose that flexible compute workloads — containerised tasks that can be delayed, relocated, or rate-adjusted — provide a mechanism for absorbing surplus renewable generation without electrochemical conversion, effectively acting as demand-side storage for otherwise curtailed power.

This insight is correct and underutilised in the agrivoltaic literature, which has focused almost exclusively on grid-side effects and agricultural coexistence. The conjunction of temporal agrivoltaics with flexible compute is the novel contribution of this paper.

### 4.2 What "Compute as Virtual Storage" Means

When a data centre shifts an AI inference job from a peak-price hour to a shoulder hour where local agrivoltaic generation is surplus, it is performing the same economic function as a battery that charges at low price and discharges at high price — but without the round-trip efficiency losses of electrochemical storage (typically 80–90% for Li-ion) and without the capital cost of the battery.

The "storage" is temporal displacement of demand rather than physical accumulation of charge. The mechanism is identical in economic function:

| Mechanism | Charges (absorbs excess) | Discharges (reduces demand) | Round-trip efficiency |
|---|---|---|---|
| Li-ion BESS | During surplus generation | During deficit | 85–92% |
| Pumped hydro | During surplus generation | During deficit | 70–85% |
| Flexible compute | Runs during surplus hours | Foregoes running during deficit hours | ~100% (no conversion loss) |

The third row is structurally superior on efficiency. Its constraint is not thermodynamic but logistical: compute jobs must be genuinely deferrable, and the deferral must be manageable at scale without degrading service quality.

### 4.3 Workload Classes and Deferability

Not all compute is equally deferrable. A useful taxonomy:

| Class | Examples | Deferability | Value capture |
|---|---|---|---|
| Hard real-time | Interactive inference, live transactions | None | Not relevant |
| Soft real-time | Batch inference, API responses | Minutes–hours | Limited |
| Deferrable | Training runs, scientific simulation | Hours–days | Significant |
| Fully flexible | Model pre-computation, data processing, archival | Days–weeks | Maximum |

The FractaVolta distributed inference architecture is designed for the third and fourth classes: workloads that can be routed to nodes with surplus renewable generation at the moment of execution, without pre-committed execution schedules.

### 4.4 The Containerised Compute Layer

The companion paper *Electricity in Containers* (Robert, 2026) develops the store-and-forward analogy for physical energy logistics. The present paper proposes its *computational analogue*: just as physical energy can be accumulated in a battery container and transported to where it is needed, computational workloads can be accumulated in a job queue and dispatched to where renewable energy is surplus.

In both cases, the "container" is a unit of deferred value — energy in chemical form, or compute in queued form — that can be released when and where conditions are most favourable. The FractaVolta inference layer provides the routing intelligence for both: tracking renewable generation forecasts, job queue states, and price signals to optimise dispatch across both physical and computational dimensions.

This is what the draft correctly identifies as *compute as virtual storage*. It is architectural, not metaphorical.

---

## 5. The Three-Dimensional Optimisation Problem

### 5.1 Current Practice: One Dimension

Traditional PV design optimises energy yield E alone:

$$\text{Objective: } \max\; E = \int P(t)\, dt$$

### 5.2 Temporal Agrivoltaics: Two Dimensions

Temporal agrivoltaics optimises energy yield and market value yield:

$$\text{Objective: } \max\; (E,\; V_m) \text{ subject to agronomic constraints}$$

This is already a Pareto front problem: the vertical east-west system may achieve lower E but higher $V_m$ than a tilted south system, and the optimal design depends on the relative weights of the two objectives.

### 5.3 Compute-Coupled Agrivoltaics: Four Dimensions

We propose that the full optimisation problem for CCA systems is:

$$\max\; F = w_E \cdot E + w_m \cdot V_m + w_g \cdot V_g + w_c \cdot C$$

where:

- $E$ = energy yield [kWh/year] — physical production
- $V_m$ = market value yield [€/year] — production weighted by spot price
- $V_g$ = grid system value yield [€/year] — avoided system costs (curtailment, congestion, storage, backup)
- $C$ = computational value yield [CXU/year or €/year] — value of absorbed flexible compute workloads

and $w_E, w_m, w_g, w_c$ are weights reflecting the system designer's objective function. Traditional PV design sets $w_m = w_g = w_c = 0$. Temporal agrivoltaics sets $w_g = w_c = 0$. CCA design uses all four.

### 5.4 Grid Value Yield

We define **Grid Value Yield (GVY)** as:

$$V_g = \Delta C_{\text{curtailment}} + \Delta C_{\text{congestion}} + \Delta C_{\text{storage}} + \Delta C_{\text{backup}} + \Delta C_{\text{balancing}}$$

where each term is the system-level cost avoided by the temporal profile of the CCA system compared to a baseline design. This metric is not directly observable at the project level — it requires a system model — but it is in principle computable from grid operator data.

GVY captures externalities that market value yield $V_m$ does not. In a perfectly functioning electricity market, $V_m$ would fully capture $V_g$. In practice, market prices imperfectly reflect system costs, particularly:

- curtailment costs (excess renewable generation that must be wasted because no flexible load or storage is available)
- congestion costs (transmission constraints that prevent renewable energy from reaching loads)
- capacity costs (investment in backup thermal generation that is only needed because renewable generation is non-dispatchable)

These costs are real and growing. A CCA system that systematically shifts demand to surplus-generation hours internalises these externalities without requiring their explicit pricing. This makes GVY a relevant metric even in markets where system cost pricing is incomplete.

### 5.5 Computational Value Yield

The fourth dimension, $C$, connects to the companion paper DHITL (Robert, 2026b), which formalises the **Compute Exergy Unit (CXU)** as the economic unit of governance-certified computation:

$$X_c = E \times \eta_{hw} \times \eta_{sys} \times \eta_{sla} \times \eta_{gov}$$

In the CCA context, the compute absorbed during surplus generation hours has a value that includes not merely the raw energy cost saved, but the governance premium associated with computation that is: (a) powered by certified renewable energy, (b) executed at a node with verified energy provenance, and (c) subject to democratic accountability requirements. This is the $\eta_{gov}$ factor in the Xc formula.

The market expression of this premium is the ×4-to-×31 spread between uncertified batch compute (€350/MWh equivalent) and sovereign-critical certified compute (€2,800/MWh equivalent) documented in the Constellia architecture (Robert & Valdes, 2026). A CCA system that directly powers compute at the point of surplus renewable generation, with full energy provenance certification, captures this premium without transmission losses or intermediary costs.

---

## 6. Compute-Coupled Agrivoltaics as an Infrastructure Class

### 6.1 The Definition

**Compute-Coupled Agrivoltaics (CCA)** is an infrastructure class in which:

1. Photovoltaic generation is co-located with agricultural production (the agrivoltaic layer);
2. The temporal profile of PV generation is designed to correlate with high-value electricity market hours (the value-shaping layer);
3. Flexible containerised computing workloads are co-located or logistically coupled to the site, and dispatched to absorb surplus generation that would otherwise be curtailed or sold at depressed prices (the computational layer);
4. A distributed inference system — the FractaVolta layer — routes workloads across the computational layer in response to real-time and forecast renewable generation, price signals, and job queue states.

### 6.2 The Physical Architecture

A CCA site minimally comprises:

| Component | Function |
|---|---|
| Vertical east-west bifacial array | Value-shaped generation, agronomic compatibility |
| Agricultural production | Primary land use, crop income, water management |
| On-site BESS (hours-scale) | Buffer between generation and compute |
| Compute nodes (edge or containerised) | Flexible workload execution |
| FractaVolta inference layer | Routing, dispatch, provenance certification |
| Energy provenance registry | Governance coupling, $\eta_{gov}$ certification |

The interaction between components is managed by the FractaVolta distributed inference layer, which tracks generation forecasts, battery state, compute queue depth, and market prices simultaneously — routing workloads to the moments of maximum system value.

### 6.3 Vineyards as a Privileged Testbed

Among agricultural contexts, vineyards offer an unusually strong combination of enabling conditions for CCA deployment:

**Geometric compatibility.** Vineyard rows are already oriented for solar access, typically east-west or slightly off-axis. Vertical bifacial panels can be installed along existing row structures with minimal modification to row geometry. Panel spacing compatible with standard viticultural machinery (inter-row spacing typically 2.5–3.5 m) is achievable.

**High land value.** Vineyard land in Mediterranean appellations commands €20,000–150,000/ha in Corsica, Sardinia, and Tuscany. The economic return required from agrivoltaic installation to be financially material is correspondingly modest relative to land value.

**Irrigation relevance.** East-west vertical panels reduce irradiance on inter-row soil, decreasing evapotranspiration by an estimated 15–30% in Mediterranean climates (Marrou et al., 2013). In a context of increasing summer drought stress on Mediterranean viticulture, this microclimate benefit is potentially transformative for yield quality even if aggregate biomass is unchanged.

**Distributed rural compute opportunities.** Vineyards are typically distributed across landscapes rather than concentrated at a single site. A network of vineyard CCA nodes — each with modest compute capacity — constitutes exactly the distributed low-K infrastructure described in the MareNostrum governance framework: no single node dominates, and compute provision is geographically and institutionally distributed.

**Friches viticoles.** In Corsica specifically, approximately 30,000 ha of formerly productive vineyard land has been abandoned over the past four decades following the collapse of mass wine production. These *friches viticoles* are not active SAU (surface agricole utile) and do not conflict with food production. They represent the primary deployment surface in the Constellia architecture (Robert & Valdes, 2026): 10.8 GWp of installed agrivoltaic capacity on 21,000 ha, generating 13.8 TWh/year of surplus electricity for compute export.

### 6.4 The FractaVolta Routing Layer

The FractaVolta architecture (Robert, 2026) defines a distributed inference system for transforming physical reality into actionable probabilistic decisions. In the CCA context, it serves specifically as:

**Generation forecasting.** Using distributed meteorological sensors, satellite irradiance data, and historical production patterns, the FractaVolta layer predicts generation at each CCA node at 15-minute resolution up to 48 hours ahead. This forecast drives workload pre-scheduling.

**Workload dispatch.** Job queues at each node are managed to absorb forecast surplus generation: large, deferrable jobs (model training, scientific simulation) are scheduled for high-generation periods; time-sensitive inference tasks retain priority at all times.

**Provenance certification.** Each compute operation is linked to a specific generation event at a specific node with a specific energy provenance chain. This produces the governance certification that activates the $\eta_{gov}$ premium in the CXU formula.

**Cross-node routing.** When a single node has insufficient surplus to absorb a large job, the FractaVolta layer routes the job across multiple nodes, treating the network of CCA sites as a single distributed compute resource. This is the "follow-the-power" paradigm at the network level.

---

## 7. The Research Hypothesis

**Hypothesis:** A vertical east-west agrivoltaic system coupled to flexible containerised compute can achieve higher total system value $F$ than a conventional south-facing agrivoltaic system with equivalent installed capacity and land area — even at equal or lower annual energy yield — when the full four-dimensional objective function is evaluated.

This hypothesis is testable. It requires:

1. Simultaneous measurement of PV production and market price for matched vertical and tilted systems (E and $V_m$)
2. System-level modelling of grid cost impacts ($V_g$)
3. Economic modelling of compute workload absorption value ($C$)
4. A defined weighting vector $(w_E, w_m, w_g, w_c)$ reflecting the system designer's objective

Partial tests are possible with existing data:

- The $V_m$ comparison can be computed from PVGIS production profiles combined with EPEX historical prices — no new field experiment required.
- The $V_g$ computation requires a grid model but can use published curtailment and congestion data from RTE (France), Terna (Italy), or CAISO (California).
- The $C$ valuation requires the CXU pricing model from DHITL and an empirical estimate of workload deferability rates.

The hypothesis is stated in falsifiable form. If the south-facing system achieves higher $F$ even under the four-dimensional objective, the paper's recommendation is wrong. If it achieves lower $F$, a publishable empirical result follows.

---

## 8. Limitations and Open Questions

**The yield trade-off may dominate in some markets.** In markets with flat or uninformative price signals — regulated tariffs, power purchase agreements at fixed prices — the temporal value of production is not captured, and the vertical system's lower annual yield is an uncompensated disadvantage. The CCA value proposition is conditional on market design that prices temporal variation.

**Flexible compute demand may not be locally available.** A vineyard CCA node in a rural Mediterranean area does not inherently have access to deferrable AI training workloads. The system requires logistics: a mechanism for connecting surplus renewable generation at rural nodes to compute demand that can tolerate geographic and temporal displacement. The FractaVolta layer provides the technical routing infrastructure; the commercial mechanisms for this market are not yet established.

**The $V_g$ term is difficult to internalise.** Grid system value is a public good. Without appropriate market instruments — capacity markets, curtailment compensation, system service contracts — the CCA site cannot capture $V_g$ as revenue. This is a regulatory gap, not a technical one.

**Provenance certification at scale is unsolved.** The $\eta_{gov}$ premium in the CXU formula requires that every compute operation be traceable to a specific renewable energy event at a certified site. The technical architecture for this certification at scale — append-only provenance registries linked to energy production meters — exists in principle but has not been deployed.

**Agronomic interactions require site-specific study.** The literature on vertical bifacial agrivoltaics is growing but geographically concentrated in northern Europe and Asia. Mediterranean vineyard applications, with their specific microclimate, crop physiology, and soil conditions, represent a research gap. The Muscat de Corse variety, grown on existing Constellia deployment surfaces, is an unstudied candidate.

---

## 9. Conclusion

The central claim of this paper is simple to state and potentially consequential to verify:

*The future problem of solar energy is not maximising kilowatt-hours. It is optimising when electricity appears and what flexible infrastructures can absorb it.*

The vertical east-west bifacial agrivoltaic system, combined with flexible containerised computing workloads managed by a distributed inference layer, offers a candidate answer to both parts of that question simultaneously. It produces electricity when it is most valuable. It dispatches compute to absorb what would otherwise be undervalued surplus. It certifies the energy provenance of the resulting compute, capturing the governance premium that sovereign-critical compute commands in current markets.

If the full four-dimensional objective function is evaluated, the system may outperform conventional agrivoltaic designs on total value even at lower annual energy yield. That proposition is falsifiable, and testing it is the research programme proposed here.

---

## Glossary of Introduced Terms

| Term | Definition |
|---|---|
| **Value-shaped generation** | PV system design optimised for the temporal value of production rather than its annual volume |
| **Temporal agrivoltaics** | Co-optimisation of PV temporal profile with electricity market value, as a design variable alongside agronomic and technical constraints |
| **Compute as virtual storage** | Deferrable computing workloads that absorb surplus renewable generation without electrochemical conversion, achieving equivalent economic function to demand-side storage |
| **Grid Value Yield (GVY)** | The aggregate system-level cost avoided by the temporal profile of a CCA system, including curtailment, congestion, storage, backup, and balancing costs |
| **Compute-Coupled Agrivoltaics (CCA)** | An infrastructure class integrating agrivoltaic generation, value-shaped temporal design, flexible compute absorption, and distributed inference routing |

---

## References

Badran, G., & Dhimish, M. (2024). Comprehensive study on the efficiency of vertical bifacial photovoltaic systems: a UK case study. *Scientific Reports* 14, 18374. https://doi.org/10.1038/s41598-024-68018-1

Dupraz, C., Marrou, H., Talbot, G., Dufour, L., Nogier, A., & Ferard, Y. (2011). Combining solar photovoltaic panels and food crops for optimising land use: towards new agrivoltaic schemes. *Renewable Energy* 36(10), 2725–2732.

JRC PVGIS. (2023). *Photovoltaic Geographical Information System*. European Commission Joint Research Centre. https://re.jrc.ec.europa.eu/pvg_tools/

Kumar, N., Singh, S. K., & Chander, N. (2026). Assessment of East–West and South-North facing vertical bifacial photovoltaic modules for agrivoltaics and dual-land use applications in India. *Transactions of the Indian National Academy of Engineering*. https://doi.org/10.1007/s41403-026-00568-4

Marrou, H., Guilioni, L., Dufour, L., Dupraz, C., & Wery, J. (2013). Microclimate under agrivoltaic systems: is crop growth rate affected in the partial shade of solar panels? *Agricultural and Forest Meteorology* 177, 117–132.

OREGES. (2023). *Bilan énergétique de la Corse 2022*. Observatoire Régional de l'Énergie, des Gaz à effet de serre et de l'Air de Corse, Ajaccio.

Robert, J.-H. N. (2026). Electricity in containers: A note on store-and-forward energy logistics. FractaVolta Working Paper. `github.com/JeanHuguesRobert/FractaVolta/blob/main/electricity_in_containers.md`

Robert, J.-H. N. (2026). FractaVolta: Distributed infrastructure for physical flow, sensing, and probabilistic inference. `github.com/JeanHuguesRobert/FractaVolta/blob/main/fractavolta_paper.md`

Robert, J.-H. N. (2026b). Democratic Humans in the Loop (DHITL): Why infrastructure is all you need for AI safety. MareNostrum Working Paper. `github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md`

Robert, J.-H. N., & Valdes, G. (2026). Constellia: A fractal architecture for energy, food, and digital sovereignty in island territories. *Proceedings of ICOME'26* (submitted, not yet accepted). Université de Corse Pasquale Paoli, Corte.

Sentnet Engineering. (2026). SkyGre vertical agrivoltaic system. Product documentation and field data. https://www.sentnet-engineering.com/solutions/skygre.html

Szabo, L., et al. (2024). Impacts of large-scale deployment of vertical bifacial photovoltaics on European electricity market dynamics. *Nature Communications* 15, 6681.

Switzer, J., McGuinness, R., Pannuto, P., Porter, G., Schulman, A., & Raghavan, B. (2021). TerraWatt: Sustaining sustainable computing of containers in containers. *arXiv preprint* arXiv:2102.06614.

Weselek, A., Ehmann, A., Zikeli, S., Lewandowski, I., Schindele, S., & Högy, P. (2019). Agrophotovoltaic systems: applications, challenges, and opportunities. *Agronomy for Sustainable Development* 39(4), 35.

Willockx, B., Lavaert, C., & Cappelle, J. (2023). Performance evaluation of vertical bifacial and single-axis tracked agrivoltaic systems on arable land. *Renewable Energy* 217, 119181.

*(Full BibTeX to be added before release.)*

---

## Questions for Reviewers

1. **Is the "compute as virtual storage" claim architecturally precise or merely analogical?** At what deferability rate and job-size distribution does the economic equivalence with BESS break down?

2. **Is the four-dimensional objective function $F$ tractable?** Or does combining market, grid, and computational value into a single scalar obscure important trade-offs that should remain as a Pareto front?

3. **Is Grid Value Yield a useful concept or a restatement of existing externality pricing literature?** Does it add anything to what Hirth (2013) and others have already done on the "market value" of variable renewables?

4. **Does the vineyard framing help or narrow the paper's audience?** Mediterranean viticulture is a plausible testbed; is it convincing as a scientific setting or does it read as local interest advocacy?

5. **What is the correct relationship between this paper and the TerraWatt paper?** This paper proposes the *supply-side* complement (value-shaped generation) to TerraWatt's *demand-side* proposal (follow-the-power compute). Is this framing accurate and useful?

6. **Is the CXU integration (the $\eta_{gov}$ governance premium) a genuine contribution to the economics of CCA, or does it import too much of the DHITL framework?** Can the CCA proposition stand independently of the MareNostrum governance architecture?

---

*© 2026 Jean Hugues Noël Robert, baron Mariani — Institut Mariani / C.O.R.S.I.C.A.*
*Published under CC0-1.0 (as per FractaVolta repository licence).*
*Repository: https://github.com/JeanHuguesRobert/FractaVolta*
*Contact: jhr@baronsmariani.org*
