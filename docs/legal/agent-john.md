---
layout: default
title: Agent John — privacy and terms
subtitle: Browser-local conversations, public corpus only, no account.
lang: en
alternate_url: /fr/legal/agent-john
description: "Privacy notice and terms for the public Agent John conversation on fractavolta.com. Association C.O.R.S.I.C.A., FractaVolta operator, Cogentia Digital Twin, open source."
canonical_url: https://fractavolta.com/legal/agent-john
date: "2026-08-22"
status: "active — public agent surface"
---

You are about to talk to **an agent**, not a person. Its name is **John**. It is a **public, read-only** face of a [Cogentia Digital Twin](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia-digital-twin.md), offered by **FractaVolta**, with software developed **open source** by the association **C.O.R.S.I.C.A.**

This page is the legal notice for [Agent John](/john). It is **not** the account-based policy of other C.O.R.S.I.C.A. services such as [Olé Olé](https://oleole.acorsica.org).

## Who is responsible

- **Publisher / controller (v1):** association **C.O.R.S.I.C.A.**, Corte, Corsica. Contact: [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org).
- **Operator of the inference host:** FractaVolta, on the **fracta** VPS (public Guide endpoint).
- **Software:** open source (MIT for code; documentation often CC BY-SA). Sources: [Cogentia](https://github.com/JeanHuguesRobert/cogentia), [FractaVolta](https://github.com/JeanHuguesRobert/FractaVolta).

This wording is the operational v1 notice. If the association later names a DPO or a distinct controller, that update will appear here with a new consent version.

## What the agent does — and does not

John on this site answers from the **public corpus** through the same governed route as the [Public Guide](/guide) (`POST https://cogentia.fractavolta.com/guide/chat`). It cites sources when it can. It can be wrong. It does **not** open an account, take a mandate from you, deploy infrastructure, publish, spend budget, or speak with the owner's private authority.

The personal / owner boundary of John lives elsewhere ([jhn.baronsmariani.org](https://jhn.baronsmariani.org)). This page is the **public FractaVolta** subset.

## Personal data we process

| Data | Where | Why | Legal basis (GDPR) |
|---|---|---|---|
| Your question, locale, page path | Sent to the fracta Guide endpoint | Produce an answer | Consent (required checkbox) |
| Optional conversation thread | **Your browser only** (`localStorage`) | Let you keep, reread, export, or delete the chat | Consent (optional checkbox) |
| Technical request metadata | Existing Guide/host logs on fracta | Operate and secure the public endpoint | Legitimate interest in running a public service, minimised |

We do **not** create a user profile, do **not** use advertising cookies, and do **not** sell data. Optional memory never leaves your device except when you send a follow-up: recent turns go verbatim, and older turns as a continuity brief (extractive immediately, then a Guide rewrite in the background). That brief is for coherence, not as a cited source.

## Retention

- Browser thread: until you delete it, or after about seven days of inactivity, or when you withdraw memory consent.
- Server: no extra conversation store for this page. Standard web/server logs on fracta follow the operator's existing retention, not a named John mailbox.

## Your rights

You can, from this browser, **export** the stored thread (JSON) and **erase** it. You can refuse processing (then the agent will not send). To withdraw consent: use the controls on [Agent John](/john) or clear site data for fractavolta.com.

For access or erasure that would concern **server logs**, email [jhr@baronsmariani.org](mailto:jhr@baronsmariani.org). We will not pretend logs never exist.

## Transfers

Inference runs on the fracta VPS (Oracle Cloud, public HTTPS). The static page is served from GitHub Pages. No extra processors are added by this UI.

## Terms of use

The service is provided **as is**, for information about the public corpus. French law applies. Do not use it for emergency, medical, legal, or binding decisions. Do not submit special-category data or secrets.

## Related notices

- [Public Guide](/guide) — same engine, corpus-tool framing.
- [Olé Olé](https://oleole.acorsica.org) — another public C.O.R.S.I.C.A. service (presence map; different data, including durable storage).
- [FractaVolta Digital Twins offer (draft)](/offers/accountable-digital-twins).
