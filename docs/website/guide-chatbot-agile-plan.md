---
title: "Plan site — Guide chatbot FractaVolta"
subtitle: "Roadmap agile pour un guide public du corpus FractaVolta/Cogentia"
status: "implementation started"
version: "0.3"
date: "2026-06-30"
language: "fr"
document_role: "operational"
document_kind: "roadmap"
visibility: "public"
human_validation_required: true
related:
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/docs/connect-mcp-clients.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/digital_twin_trust_model.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/docs/digital-twin-agile-roadmap.md"
---

# Plan site — Guide chatbot FractaVolta

## Objectif

Ajouter au site public `fractavolta.com` un **Guide** capable d'orienter les
visiteurs dans le corpus public FractaVolta/Cogentia.

Ce Guide est une **instance publique, immature et strictement limitee** du
jumeau numerique du proprietaire. Il n'est pas le noyau prive du jumeau, et il
ne parle pas avec toute l'autorite du proprietaire. C'est une face publique
infant/child au sens du modele de maturite Cogentia :

```text
autorisé : orienter, chercher, citer, expliquer, proposer une lecture
interdit : agir, muter, publier, depenser du quota hors politique, exposer du prive
```

Le Guide doit aider un visiteur à comprendre :

- ce qu'est FractaVolta ;
- le lien entre énergie, calcul, paquets et capacité territoriale ;
- le rôle de Cogentia, Fractanet, Fracta, Inseme et MareNostrum ;
- où lire ensuite ;
- ce que le corpus affirme, et ce qu'il ne permet pas encore d'affirmer.

## Principe agile

Le plan avance par petites tranches réversibles.

```text
Quand l'erreur est réversible, apprendre par action traçable.
Quand l'erreur touche la confiance publique, filtrer avant exposition.
```

Le Guide public doit donc commencer sobrement. Il ne doit pas promettre une
conversation intelligente complète avant que les frontières de confiance,
d'usage de quota, de citation et de confidentialité soient vérifiées.

Mise a jour v0.2 : la tranche demonstrative cible directement une route
publique gouvernee `POST /guide/chat`. Cette route reste cote serveur, utilise
la vue publique Cogentia et peut appeler Magistral comme routeur d'intelligence
sans exposer de cle API au navigateur.

Mise a jour v0.3 : le Guide est decrit comme une instance publique du jumeau,
pas comme un simple chatbot separe. Cette instance a son propre mandat, sa vue
du corpus, sa maturite et son autorite.

## Contraintes de confiance

Le Guide public :

- utilise uniquement la vue publique ;
- cite les sources quand il répond depuis le corpus ;
- affiche quand il ne sait pas ;
- ne présente pas des hypothèses comme des capacités réalisées ;
- ne crée pas de compte utilisateur ;
- ne collecte pas de données personnelles en v0.1 ;
- ne déclenche pas d'action administrative ou commerciale ;
- ne contacte pas directement de fournisseur d'IA depuis le navigateur ;
- passe par le point public Cogentia MCP/API gouverné.

## Architecture cible

```text
fractavolta.com
  -> widget Guide public
  -> endpoint public Cogentia /guide/chat
  -> mandat d'instance public: infant, read-only, public corpus
  -> Cogentia Context Gateway sur Fracta
  -> index public du corpus
  -> Magistral local si synthese conversationnelle disponible
  -> sources citées GitHub/fractavolta.com
```

Plus tard :

```text
Guide public
  -> retrieval public
  -> génération conversationnelle gouvernée
  -> réponses sourcées + limites visibles
```

La première version peut rester extractive : recherche, contexte, extraits et
liens. La génération libre n'est pas obligatoire pour prouver l'utilité.

## Parcours utilisateur v0.1

Bouton flottant ou bloc visible :

```text
Guide
```

Panneau :

```text
Ask the public FractaVolta Guide
Answers are grounded in the public corpus.
```

Prompts proposés :

- What is FractaVolta?
- What is Fractanet?
- How does Cogentia relate to FractaVolta?
- Give me a 10-minute reading path.
- What does the corpus say about Fracta, Caddy and MCP?

Réponse attendue :

- résumé court ;
- 3 à 5 sources ;
- liens vers les pages/documents ;
- mention explicite si la réponse est seulement partielle.

## Tranches

### Tranche 0 — Préparation documentaire

Objectif : stabiliser l'intention avant de coder.

Acceptation :

- ce plan existe ;
- les frontières public/privé/action sont explicites ;
- le Guide est defini comme instance publique du jumeau, pas comme noyau prive ;
- les prompts de test sont listés.

Statut : fait.

### Tranche 1 — Widget et prompts

Objectif : ajouter une présence visible reliee a la route publique gouvernee.

Implémentation :

- inclure un bouton/panneau Guide dans le layout ;
- afficher les prompts proposés ;
- chaque prompt peut appeler la route publique gouvernee ;
- afficher les erreurs et les sources.

Acceptation :

- le site reste deployable comme site statique ;
- le Guide ne contacte pas directement un fournisseur d'IA ;
- le panneau fonctionne mobile/desktop ;
- le texte public reste sobre et non commercialement excessif.

Statut : implemente localement dans le layout Jekyll.

### Tranche 2 — Recherche publique via Cogentia

Objectif : brancher le Guide sur la recherche publique sans génération libre.

Implémentation possible :

- appel direct à `https://cogentia.fractavolta.com/mcp` avec `cogentia_search`;
- ou petite façade `/guide/search` si CORS, format ou sécurité exigent un proxy ;
- affichage des résultats avec source id, titre, extrait et lien.

Acceptation :

- `cogentia_search` fonctionne depuis le site ;
- les résultats affichent repo, chemin, lignes et lien ;
- aucune clé API n'est exposée ;
- les erreurs réseau sont affichées simplement ;
- le Guide reste utilisable sans JavaScript comme liste de liens de départ.

Statut : premiere version via `POST /guide/chat`, avec fallback extractif cote
serveur si la synthese conversationnelle n'est pas disponible.

Mise a jour : le widget propose aussi des questions de depart plus explicites
et des suggestions de suivi apres chaque reponse. Ces suggestions restent
simples et publiques : elles guident doucement le visiteur vers un prochain
angle de lecture, sans pretendre personnaliser ou decider a sa place.

Mise a jour v0.5 : les suggestions de depart tiennent compte de la page et de
la langue. La version francaise reste orientee Corse, communes, agriculteurs,
installateurs, marches locaux et prototypes terrain. La version anglaise guide
plus directement vers les couches recherche, partenaires, deployeurs, papiers
et jumeau public. Les suggestions de suivi utilisent aussi le sujet detecte et
signalent explicitement quand une recherche web n'a pas apporte de resultat
exploitable.

Mise a jour v0.6 : le Guide propose aussi un passage vers l'agent du visiteur
avec "Approfondir avec votre propre agent". Le site ne paie pas une synthese
longue et couteuse pour chaque visite ; il produit un prompt portable qui
embarque la question, la reponse, les sources publiques et les consignes de
prudence. Le prompt demande aussi a l'agent externe de finir par une question
precise que l'usager pourra recoller dans le Guide, afin de garder une boucle
utile entre exploration personnelle et corpus public.

### Tranche 3 — Context packs et lignes citées

Objectif : permettre au Guide de construire une réponse plus utile sans
halluciner.

Implémentation :

- `cogentia_context_pack` pour les questions larges ;
- `cogentia_get_lines` pour vérifier un résultat ;
- UI qui montre les sources avant ou avec la réponse.

Acceptation :

- une question large produit un pack limité ;
- l'utilisateur peut ouvrir les sources ;
- le Guide peut dire "insufficient public corpus evidence";
- pas de mutation, pas de session privée.

Statut : en cours via les context packs que la route Cogentia construit avant
la synthese.

### Tranche 4 — Réponse conversationnelle gouvernée

Objectif : transformer les résultats en réponse synthétique, avec prudence.

Précondition :

- une politique claire de coût/provider ;
- une route conversationnelle publique gouvernée ;
- citations obligatoires ;
- limites visibles ;
- logs non sensibles.

Acceptation :

- la réponse cite les sources ;
- les sources sont consultables ;
- les réponses non sourcées sont refusées ou marquées comme orientation ;
- quota et provider calls passent par la politique Cogentia/Magistral prévue.

Mise a jour v0.4 :

- le widget peut etre agrandi a la taille de la fenetre ;
- les reponses du Guide sont rendues en Markdown cote client, sans `innerHTML`
  arbitraire ;
- la conversation est memorisee dans `localStorage` cote visiteur, avec TTL
  d'environ une semaine et bouton d'effacement ;
- le client transmet un historique borne au serveur pour la continuite
  conversationnelle ; cet historique n'est pas une source probante ;
- la route `/guide/chat` peut enrichir une question actuelle par une recherche
  web Brave bornee. Cette recherche est configuree cote serveur par
  `BRAVE_SEARCH_API_KEY`, `COGENTIA_BRAVE_SEARCH_API_KEY` ou
  `COGENTIA_GUIDE_WEB_SEARCH_API_KEY`; elle reste separee du corpus et cite des
  sources `web:*`.

### Tranche 5 — Feedback public

Objectif : recueillir les corrections sans ouvrir un canal de capture.

Implémentation possible :

- bouton "This answer needs correction";
- lien vers GitHub issue préremplie ;
- ou formulaire public limité, modéré, sans données personnelles inutiles.

Acceptation :

- aucun feedback ne modifie le corpus directement ;
- les objections deviennent des traces ;
- les corrections utiles peuvent devenir issues ou continuations.

## Questions de conception ouvertes

- Faut-il un widget global ou une page `/guide` dédiée d'abord ?
- Le premier appel doit-il viser `/mcp` ou une façade `/tools/cogentia_search` ?
- Faut-il une version française dès v0.1 ou après la tranche 2 ?
- Le Guide doit-il afficher "beta", "infant" ou une autre maturité publique ?
- Quel volume de logs publics est acceptable sans tracking intrusif ?

## Prompts de validation

```text
What is FractaVolta?
What is Fractanet?
How does Cogentia relate to FractaVolta?
Give me a 10-minute reading path about FractaVolta.
What does the corpus say about Fracta, Caddy and MCP?
What is the link between energy packets and cognitive infrastructure?
```

Pour chaque prompt, le Guide doit :

- répondre brièvement ;
- montrer les sources ;
- ne pas inventer de capacité opérationnelle ;
- proposer une prochaine lecture.

## Prochain pas recommandé

Continuer par le durcissement de la route publique :

```text
deployer /guide/chat sur Fracta, verifier CORS, tester une question publique
```

Puis brancher Magistral/OpenAI via la politique serveur, avec mesure de quota et
fallback local.
