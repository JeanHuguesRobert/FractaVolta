---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/packet_attractor.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-06-01
title: "The Packet as Evolutionary Attractor: Scale-Invariant Transitions in Complex Networks"
date: "2026-05-06"
status: "draft — auto-filled (frontmatter cleanup)"
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
---
# The Packet as Evolutionary Attractor: Scale-Invariant Transitions in Complex Networks

**Version 2 — Revised following peer critique**

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A. / FractaVolta

1 cours Paoli, F-20250 Corte, Corsica, France

jhr@baronsmariani.org | fractavolta.com

---

## Abstract

Complex networks — whether informational, monetary, energetic, or social — appear to undergo a recurrent structural transition as they mature: from continuous circuit-switched flow to discrete store-and-forward packet routing. This paper asks whether this convergence is accidental or reflects an underlying invariant.

Two levels of claim are carefully distinguished throughout. The first is a *structural observation*: discrete units appear independently as fundamental structures across multiple domains — physics, biology, linguistics, computer science, and network engineering. This observation is established and not contested. The second is a *causal hypothesis*: these discretizations may share a common underlying mechanism, and the circuit-to-packet transition in engineering may be a macroscopic instance of a discretization principle that operates across scales. This hypothesis is not established. It is the question this paper poses.

The paper does not claim that the universe is computational, discrete at a fundamental level, or information-theoretic. It does not assert that photons, codons, and IP packets are the same phenomenon. It asks whether the engineering transition from circuit to packet — observed independently in information, monetary, energy, and habitat networks — exhibits structural properties worth investigating formally. The mathematics required for that investigation is beyond the author's formation. The question is offered to those who have it.

**Conflict of interest declared**: the author has a direct commercial interest in the packet energy thesis through FractaVolta and Mariani Village. This conflict is declared explicitly. The theoretical hypothesis should be evaluated independently of its commercial applications. The empirical instances (FractaVolta, Mariani Village) are offered as observable, measurable cases — not as proof of the theoretical claim.

**Keywords:** packet switching; complex networks; evolutionary attractor; discretization; store-and-forward; scale invariance; network evolution; FractaVolta; Mariani Village; open question

---

## 1. Two Disclosures

### 1.1 The author's formation

The central intuition of this paper — that complex systems tend toward discrete packet architectures as they mature — originates in a career in computer science. The computer scientist thinks in state transitions. Every algorithm is a sequence of discrete state changes under rule-governed control. This formation creates a predisposition: the trained computer scientist tends to see discrete structures everywhere.

This predisposition may be a bias that projects discretization onto a continuous reality. Or it may be a sensitivity that detects a real structure that other disciplinary formations miss. The argument for the latter is the convergence described in §3: physicists, biologists, linguists, and economists — none of them computer scientists — independently arrived at discrete structures as fundamental to their domains. When the same structure appears independently across disciplines with no shared formation, the probability that it is a projection of any single discipline's bias decreases. But it does not reach zero. The bias remains a possibility and is declared as such.

### 1.2 The author's interest

FractaVolta and Mariani Village — both cited in this paper as empirical instances of the packet transition — are projects in which the author has a direct commercial and institutional interest. This conflict is not hidden. It is declared here, at the opening, so that the reader can weight the argument accordingly.

The consequence is not that the hypothesis is wrong. It is that the hypothesis requires a higher standard of independent scrutiny than a paper without conflict of interest would require. The author accepts this asymmetry. The question stands or falls on its own merits, not on the author's interests.

---

## 2. What This Paper Does Not Claim

Precision requires stating what is not claimed before stating what is.

**This paper does not claim** that the universe is computational, that reality is fundamentally discrete, or that information is more fundamental than matter. These claims have been made seriously by Zuse [1], Fredkin [2], Wolfram [3], Wheeler [4], Lloyd [5], and Tegmark [6]. They are contested and unresolved. This paper takes no position on them.

**This paper does not claim** that photons, codons, and IP packets are the same phenomenon. They are not. The quantum of energy is a property of the electromagnetic field with no routing protocol, no address header, and no reassembly at the destination. The codon is a triplet of nucleotides that evolution did not *discover* through a transition from continuous to discrete — it *began* discrete. The IP packet is an engineering artifact with an explicit address, checksum, and time-to-live field. These are structurally analogous in one narrow sense — they are all discrete units — and radically different in every other sense.

**This paper does not offer** a formal model, equations, simulations, or empirical measurements. The author does not have the mathematical formation to produce these. Borrowing the vocabulary of phase transitions, order parameters, universality classes, and scaling laws without providing the corresponding formalism would be intellectually dishonest. Where this vocabulary appears, it is qualified explicitly as pointing toward questions, not asserting results.

**What this paper does claim** is narrow: the circuit-to-packet transition has been observed independently in information networks, monetary networks, energy networks, and habitat networks. This convergence is real, documented, and not yet formally explained. A formal investigation of whether it constitutes a universal evolutionary attractor — with the tools of complexity science, network theory, and statistical physics — seems warranted. The author cannot conduct that investigation. This paper is an invitation to those who can.

---

## 3. The Structural Observation: Independent Convergences

The following five convergences are offered as a *structural observation* — established facts, not hypotheses. The causal interpretation of these convergences is the hypothesis, addressed separately in §4.

### 3.1 Physics: energy is quantized at small scales

Classical physics described energy as a continuous quantity. Planck's 1900 hypothesis — that blackbody radiation could only be explained if energy is emitted in discrete quanta of magnitude *hν* — resolved the ultraviolet catastrophe [7]. Einstein's 1905 photoelectric paper established that light is composed of discrete photons [8]. Subsequent quantum mechanics generalized this: charge, spin, angular momentum are all quantized at small scales.

**Important distinction**: the quantum is not the result of an evolutionary transition from continuous to discrete. It is a fundamental property of matter at small scales, discovered by physicists who expected continuity and found discreteness. The continuous description of classical physics is an approximation that holds at large scales and breaks down at small ones.

This is noted not as an analogy with packet networks but as a datum: discreteness is not an artifact of engineering choices. It appears at the foundation of physical reality, at scales far below any engineering intervention.

### 3.2 Biology: genetic information is encoded discretely

The genetic code maps discrete triplets of nucleotides (codons) to discrete amino acids. There are 64 codons and 20 amino acids plus stop signals. The mapping is discrete, redundant, and universal across all known life [9].

**Important distinction**: biology did not transition from continuous to discrete encoding. The discrete codon structure is as old as life itself — at least 3.5 billion years old. There is no known precursor continuous encoding system. Biology began with the packet.

Again, this is noted as a datum, not an analogy. The engineering packet was invented in 1964. The biological packet predates it by 3.5 billion years. If there is a connection, it is not one of historical influence.

### 3.3 Linguistics: phonemes are discrete perceptual units

Spoken language is a continuous acoustic waveform. Meaning is not carried continuously — it is carried by discrete phonemes, the smallest units that distinguish meaning in a given language. Continuous variation within a phoneme category is perceptually absorbed; crossing a category boundary changes meaning discontinuously [10].

**Important distinction**: the phoneme is a perceptual category, not a physical object. It is the outcome of a perceptual system that discretizes a continuous acoustic signal. This is a different kind of discretization from the quantum or the codon — it is cognitive rather than physical.

### 3.4 Computer science: the bit as optimal discrete unit

Shannon's 1948 information theory [11] established that any information channel can be characterized by a capacity in bits — discrete binary units — and that optimal encoding approaches this capacity. The continuous analog signal is not the fundamental unit. The bit is. This was not a choice of convenience but a mathematical theorem.

### 3.5 Network engineering: packet architectures outperform circuit architectures

In every domain where both circuit-switched and packet-switched architectures have been deployed at scale, the packet architecture has proven more robust, more efficient under variable load, and more resilient to partial failure:

- **Information networks**: ARPANET (1969) → internet (2024). The telephone circuit-switched network coexisted with the packet-switched internet for thirty years before losing ground [12].
- **Monetary networks**: correspondent banking (circuit) → Bitcoin and DeFi (packet, 2009–2024) [13]. The transition is ongoing and contested.
- **Energy networks**: AC grid (circuit) → Energy Packet Network (packet, proposed) [14]. The transition is in early stages.
- **Habitat**: permanent dwelling (circuit) → relocatable container unit (packet, proposed) [15]. The transition is in prototype stage.

**The critical distinction between §3.1–3.4 and §3.5**: the first four convergences describe discreteness as a *discovered property* of natural systems. The fifth describes discreteness as an *engineering choice* that proves superior to the continuous alternative when tried. These are different kinds of convergence. The connection between them — if any — is the hypothesis of §4.

---

## 4. The Causal Hypothesis: A Question, Not an Answer

The structural observation of §3 raises a question. The five convergences involve different kinds of discreteness, different mechanisms, and different scales. Are they connected, or is their apparent similarity a coincidence — an artifact of the word "discrete" being applied to very different phenomena?

This paper cannot answer that question. It can formulate it.

### 4.1 The engineering question (tractable)

Within the domain of engineering networks alone — setting aside quantum physics, biology, and linguistics — a well-defined question exists:

> *Why does the packet architecture consistently outperform the circuit architecture in every domain where both have been tried, regardless of what the network carries?*

This question does not require any claim about the nature of physical reality. It is a question about network dynamics. It has a partial answer in information theory (Shannon capacity, queuing theory, resilience under partial failure) but no unified formal account that applies across information, monetary, energy, and habitat networks simultaneously.

A unified formal account would be a contribution to network science. It would not require the physics of §4.2 and could stand independently.

### 4.2 The physical question (speculative but precisely formulated)

The more ambitious question is whether the engineering convergence toward packet architectures is related to the natural convergence toward discreteness observed in physics and biology.

This question *resembles* questions that have been asked in statistical physics about universality: why do systems with very different microscopic physics exhibit identical macroscopic behavior near critical points? The renormalization group [16] provides a mathematical framework for answering such questions — but applying it to network transitions requires a formal model that this paper cannot provide.

The question is therefore stated as an open invitation, not a claim:

> *Does the circuit-to-packet transition in engineering networks exhibit structural properties — sharpness of transition, scaling behavior, independence from microscopic details — that would justify a formal investigation using the tools of statistical physics? If so, what is the appropriate model?*

This is a question a complexity theorist or statistical physicist could evaluate. It may turn out to be well-formed and answerable. It may turn out to be a category error — applying physical concepts to social and engineering systems where they do not belong. The author cannot determine which. The invitation is genuine.

### 4.3 What would falsify the hypothesis

A hypothesis that cannot be falsified is not a scientific hypothesis. The following observations would weaken or falsify the claim that the packet transition is a universal evolutionary attractor:

- A mature, large-scale network in which the circuit architecture outperforms the packet architecture under realistic operating conditions, after both have been optimized
- Evidence that the packet transitions in information, monetary, and energy networks occurred through different mechanisms with no shared structural properties
- A formal proof that the engineering packet transition cannot be mapped onto any known universality class in statistical physics, for principled mathematical reasons

The author does not know whether any of these falsifying observations exist. Identifying them is part of the research program being invited.

---

## 5. The Perceptual Continuity Observation

A subsidiary observation, offered with less formal ambition.

Human perception integrates discrete events into continuous experience. The retina integrates photons over approximately 50 milliseconds — producing the persistence of vision that makes cinema possible. The cochlea integrates acoustic compressions — producing the smooth experience of sound from discrete pressure waves. Below the integration threshold, events are discrete. Above it, they appear continuous.

This is not a new observation. It is well-established in sensory neuroscience. What is less often noted is that the same integration pattern appears in institutional perception:

- The electrical grid appears continuous to the consumer. The underlying reality is a sequence of discrete generator dispatch decisions, tap-changer operations, and protection relay events.
- The monetary system appears continuous to the account holder. The underlying reality is a sequence of discrete ledger entries and settlement cycles.
- The housing market appears permanent to the tenant. The underlying reality is a sequence of discrete contractual events.

In each case, the circuit model is the *experienced* form of a system whose underlying dynamics are discrete. The packet model makes those dynamics visible.

This observation does not prove the causal hypothesis of §4. It suggests that the distinction between circuit and packet may be, in part, a distinction between the observer's integration scale and the system's operational scale. When the observer's integration window is large relative to the packet duration, the system appears continuous. When it is small, the packets become visible.

This is offered as an observation worth noting, not as a conclusion.

---

## 6. The Research Program

This paper has posed questions it cannot answer. What it can do is specify what a research program addressing these questions would look like.

**Step 1 — The engineering question** (addressable with existing tools):

Define a quantitative measure of "packetness" for a network — the fraction of traffic that is discretized, addressed, and asynchronously routed. Apply this measure to historical data on the information network transition (1969–2000) and the monetary network transition (2009–2024). Characterize the transition: is it sharp or gradual? Does it exhibit hysteresis? What are the control parameters?

**Step 2 — Cross-domain comparison** (requires interdisciplinary collaboration):

Apply the same measure to energy networks (FractaVolta deployment data, when available) and habitat networks (Mariani Village occupancy and routing data). Do the transitions in different domains share structural properties, or are they domain-specific?

**Step 3 — The physical question** (requires statistical physics expertise):

If Steps 1 and 2 reveal shared structural properties across domains, ask whether these properties can be mapped onto a known class of transitions in statistical physics. This step requires expertise the author does not have. It is the step for which a collaborator is sought.

**Step 4 — Falsification**:

Design observations that would falsify the hypothesis at each step. Conduct them before advancing to the next step.

---

## 7. Conclusion

This paper has posed questions, acknowledged its limitations, and declared its conflicts of interest.

The structural observation is established: discrete units appear independently as fundamental structures across physics, biology, linguistics, computer science, and network engineering. This convergence is real.

The causal hypothesis is not established: whether these convergences reflect a common underlying mechanism, and whether the engineering circuit-to-packet transition is a universal evolutionary attractor, remains an open question. The author cannot answer it. The mathematics required is beyond the author's formation — a situation analogous to Einstein's need for Grossmann's tensor calculus, without the Grossmann.

The empirical program is concrete: FractaVolta and Mariani Village will generate measurable data on the packet transition in energy and habitat networks. That data will be made available. Whether it contributes to a formal theoretical account depends on whether the research program of §6 attracts the collaboration it requires.

The question is on the table. The container is in Corte. The measurement can begin.

---

## References

[1] Zuse, K. *Rechnender Raum*. Friedrich Vieweg & Sohn, 1969.

[2] Fredkin, E. *Digital Mechanics*. Physica D, 45(1–3), 254–270, 1990.

[3] Wolfram, S. *A New Kind of Science*. Wolfram Media, 2002.

[4] Wheeler, J.A. *Information, Physics, Quantum: The Search for Links*. In Zurek, W.H. (ed.), *Complexity, Entropy, and the Physics of Information*. Addison-Wesley, 1990.

[5] Lloyd, S. *Programming the Universe*. Knopf, 2006.

[6] Tegmark, M. *Our Mathematical Universe*. Knopf, 2014.

[7] Planck, M. *Zur Theorie des Gesetzes der Energieverteilung im Normalspektrum*. Verhandlungen der Deutschen Physikalischen Gesellschaft, 2, 237–245, 1900.

[8] Einstein, A. *Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt*. Annalen der Physik, 17, 132–148, 1905.

[9] Watson, J.D. and Crick, F.H.C. *Molecular Structure of Nucleic Acids*. Nature, 171, 737–738, 1953.

[10] Liberman, A.M. et al. *Perception of the Speech Code*. Psychological Review, 74(6), 431–461, 1967.

[11] Shannon, C.E. *A Mathematical Theory of Communication*. Bell System Technical Journal, 27, 379–423, 1948.

[12] Leiner, B.M. et al. *A Brief History of the Internet*. ACM SIGCOMM Computer Communication Review, 39(5), 2009.

[13] Nakamoto, S. *Bitcoin: A Peer-to-Peer Electronic Cash System*. 2008. https://bitcoin.org/bitcoin.pdf

[14] Robert, J.H.N. *The Unconscious Grid*. FractaVolta, 2024.
https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/UNCONSCIOUS_GRID.md

[15] Robert, J.H.N. *Mariani Village: A Relocatable DC-Native Housing Fleet*. Institut Mariani / Dilorta, 2026.

[16] Wilson, K.G. *Renormalization Group and Critical Phenomena*. Physical Review B, 4(9), 3174–3205, 1971.

[17] Barabási, A.L. and Albert, R. *Emergence of Scaling in Random Networks*. Science, 286(5439), 509–512, 1999.

[18] Mandelbrot, B.B. *The Fractal Geometry of Nature*. W.H. Freeman, 1982.

[19] Feigenbaum, M.J. *Quantitative Universality for a Class of Nonlinear Transformations*. Journal of Statistical Physics, 19(1), 25–52, 1978.

[20] Schrödinger, E. *What is Life?* Cambridge University Press, 1944.

[21] Baran, P. *On Distributed Communications*. RAND Corporation, RM-3420-PR, 1964.
<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Concept Index — FractaVolta](concepts.md)
- [Corpus Status — FractaVolta](corpus-status.md)
- [For researchers](../docs/for-researchers.md)
- [FractaVolta](../README.md)
- [Le Réseau Inconscient](LE_RESEAU_INCONSCIENT.md)
- [MareNostrum](../docs/marenostrum.md)
- [Research Index — FractaVolta](index.md)
- [The Packet as Evolutionary Attractor — moved](../packet_attractor.md)
- [The Unconscious Grid](UNCONSCIOUS_GRID.md)
- [Documents - All Tracked Repos](https://github.com/JeanHuguesRobert/JeanHuguesRobert/blob/main/research/documents.md)
<!-- END_AUTO: backlinks -->
