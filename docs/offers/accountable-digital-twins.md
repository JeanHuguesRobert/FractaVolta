---
title: "Digital Twins responsables"
subtitle: "Mandats, traçabilité des actes, budgets, comptabilité et rapprochement"
status: "derived commercial offer — draft"
version: "0.1"
date: "2026-08-08"
last_modified_at: "2026-08-08"
language: fr
document_role: "derived"
document_kind: "commercial-offer"
target_audience: "entreprises, laboratoires, associations, fondations, institutions et partenaires professionnels"
target_scene: "FractaVolta commercial offer"
document_function: "present a bounded accountable Digital Twin proposition without overstating maturity"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
human_validation_required: true
canonical_path: "FractaVolta/docs/offers/accountable-digital-twins.md"
canonical_url: "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/offers/accountable-digital-twins.md"
provenance:
  origin_type: "derived-from-source"
  origin_repository: "JeanHuguesRobert/FractaVolta"
  origin_ref: "FractaVolta#17"
  origin_date: "2026-08-08"
  derived_from:
    - "../../research/accountable_digital_twin_commercial_thesis.md"
    - "https://github.com/JeanHuguesRobert/inseme/blob/main/research/cogentia_accounting_architecture.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Digital Twins responsables

Un Digital Twin professionnel ne devrait pas seulement être capable d'agir. Il devrait permettre de reconstruire **qui l'a autorisé à agir, dans quelles limites, ce qu'il a effectivement fait, quelles ressources il a consommées, quel effet s'est produit et comment les coûts ont finalement été rapprochés de la réalité financière**.

FractaVolta étudie une offre construite autour de cette chaîne de responsabilité :

```text
Principal
→ Mandat
→ Agent / acteur
→ Capacité appelée
→ Acte
→ Effet / preuve
→ Écriture comptable
→ Imputation analytique
→ Rapprochement
```

## Deux briques complémentaires

### Traçabilité des actes — Archia

Archia vise à conserver une trace exploitable de l'autorité et de l'action :

- qui donne le mandat ;
- qui agit ;
- dans quelles limites ;
- avec quelle capacité ;
- quelle action engageante est exécutée ;
- quel résultat ou effet externe est observé ;
- quelles preuves permettent de le vérifier ;
- quelles corrections, objections ou révocations interviennent ensuite.

### Comptabilité des conséquences — COP/Accounting

COP/Accounting vise à conserver la trace équilibrée des ressources et obligations :

- budgets applicables au traitement ;
- réservations avant consommation engageante ;
- ressources réellement mesurées ;
- engagements et règlements ;
- coûts provisoires ;
- ventilation par projet, client, paquet, fournisseur ou bénéficiaire ;
- rapprochement ultérieur avec les factures et autres preuves financières ;
- écritures de compensation plutôt qu'effacement de l'historique.

## Pourquoi cette combinaison est utile

Un journal technique peut dire qu'un appel API a eu lieu.

Un tableau de coûts peut dire combien un fournisseur a facturé.

Un système d'approbation peut montrer qu'une demande a été validée.

L'objectif de Cogentia est plus transversal : **relier l'autorisation, l'acte, la preuve de son effet et ses conséquences comptables dans une même chaîne vérifiable**.

C'est particulièrement pertinent lorsque l'IA intervient dans des opérations qu'une organisation devra ensuite pouvoir expliquer, auditer ou comptabiliser.

## Cas d'usage envisagés

L'offre vise notamment :

- les PME qui délèguent progressivement des tâches à des agents IA ;
- les équipes de R&D utilisant plusieurs modèles et fournisseurs ;
- les recherches de brevet et les processus où la contribution humaine doit rester documentée ;
- les laboratoires et bureaux d'études ;
- les associations, fondations et fonds qui doivent rendre compte de l'emploi de ressources ;
- les prestations nécessitant une imputation fine par client ou projet ;
- les organisations cherchant à maîtriser leurs coûts IA sans dépendre d'un fournisseur unique ;
- les infrastructures privées, locales ou souveraines pour lesquelles la continuité et la traçabilité sont importantes.

## Comptabilité générale et comptabilité analytique

Le Digital Twin ne remplace pas la personne juridique qui porte légalement les comptes.

Cogentia distingue donc :

- **la comptabilité générale de la personne juridiquement responsable** ;
- **la comptabilité de ressources interne à Cogentia** ;
- **la comptabilité analytique**, qui ventile les coûts et ressources selon plusieurs axes ;
- **la comptabilité budgétaire**, qui contrôle ce qu'un traitement est autorisé à engager.

Une même dépense peut ainsi rester dans un compte général stable tout en étant ventilée selon :

```text
entité juridique
Digital Twin
mandat
paquet / traitement
projet
client ou bénéficiaire
fournisseur
modèle
capacité
source de financement
statut de valorisation
```

Cette séparation évite de transformer le plan comptable général en une arborescence illisible simplement pour obtenir une information de gestion fine.

## Du coût estimé à la facture réelle

Lors d'une opération IA, Cogentia peut connaître immédiatement le nombre de tokens, le temps GPU ou d'autres ressources mesurées alors que la facture du fournisseur n'arrivera que plus tard.

Le système peut donc conserver :

```text
usage mesuré
→ coût provisoire estimé
→ imputation au paquet/projet/client
→ facture fournisseur
→ rapprochement
→ écriture de compensation éventuelle
```

L'estimation initiale n'est pas effacée. Elle reste la trace de l'information disponible au moment de la décision.

La facture apporte ensuite une information financière plus forte et permet de corriger l'imputation par de nouvelles écritures.

## Interopérabilité avec la comptabilité légale

Cogentia est conçu pour rester indépendant d'un plan comptable national particulier.

Des adaptateurs pourront rapprocher ses comptes sémantiques et ses traces avec le référentiel applicable à l'entité juridiquement responsable.

Cette architecture peut faciliter le travail comptable et le contrôle interne, mais **elle ne constitue pas en elle-même une certification comptable, fiscale ou réglementaire**.

Les écritures légales peuvent en outre nécessiter des décisions propres : amortissements, provisions, rattachements, inventaires, fiscalité ou autres traitements de clôture.

## Ce que FractaVolta pourrait facturer

Le coeur logiciel et documentaire reste destiné à demeurer ouvert.

La valeur professionnelle se situe dans la mise en oeuvre :

- intégration et déploiement ;
- hébergement privé ou restreint ;
- intégration des identités et mandats ;
- politiques d'accès, de conservation et de confidentialité ;
- connecteurs fournisseurs ;
- rapprochement des usages et factures ;
- tableaux analytiques ;
- intégration avec les outils comptables ;
- infrastructures locales ou souveraines ;
- exploitation, support et SLA ;
- adaptations métier.

L'hypothèse économique est que ces prestations professionnelles puissent contribuer à financer une **offre individuelle de base largement accessible, idéalement gratuite**, dont le périmètre exact reste à définir.

## Une promesse à démontrer, pas un slogan

FractaVolta ne prétend pas à ce stade être un logiciel comptable certifié ni disposer d'une exclusivité sur ces mécanismes.

Le différenciateur à démontrer est plus précis :

> **conserver une chaîne vérifiable allant du mandat et de l'acte jusqu'à la preuve de son effet et à ses conséquences en ressources, puis rapprocher les estimations provisoires de la vérité financière sans effacer l'histoire.**

Le premier démonstrateur commercial devra montrer cette chaîne de bout en bout sur un acte réel et borné.

## Sources

- [Thèse commerciale — Accountable Digital Twins](../../research/accountable_digital_twin_commercial_thesis.md)
- [Architecture comptable Cogentia](https://github.com/JeanHuguesRobert/inseme/blob/main/research/cogentia_accounting_architecture.md)
- [COP/Accounting](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/COP_ACCOUNTING.md)

Human validation required: yes.
