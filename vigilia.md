---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/vigilia.md
status: draft
last_stamped_at: 2026-05-16
parent_document: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/tera.md
---

# VIGILIA

**Prévention des collisions entre véhicules et animaux en divagation**

*Jean Hugues Noël Robert — Institut Mariani / C.O.R.S.I.C.A. — FractaVolta*  
*Corte, Corse*

> Projet issu de FractaTera, réseau fractal de perception territoriale probabiliste.

---

## 1. Résumé

VIGILIA est un projet de prévention des collisions entre véhicules et animaux en divagation sur les routes corses.

Le problème est simple : bovins, chevaux, cochons, ânes, sangliers ou autres animaux peuvent se trouver sur la chaussée, notamment de nuit, dans des zones mal éclairées, mal couvertes par les réseaux, et impossibles à équiper partout avec des infrastructures fixes.

La réponse classique consiste à poser davantage de panneaux, de clôtures, de caméras ou de capteurs fixes. Ces solutions ont leur utilité, mais elles restent coûteuses, localisées et souvent insuffisantes.

VIGILIA propose une approche progressive : commencer par le signalement citoyen depuis un téléphone, construire une carte territoriale du risque, puis équiper certains animaux problématiques avec des balises peu coûteuses lorsque cela devient utile.

L’objectif n’est pas de savoir exactement où se trouve chaque animal. L’objectif est plus modeste, donc plus robuste : prévenir le conducteur qu’un animal est probablement proche de la route ou sur sa trajectoire.

---

## 2. Le problème public

La divagation animale est à la fois :

- un problème de sécurité routière ;
- un problème de responsabilité juridique ;
- un problème économique pour les éleveurs ;
- un problème d’image pour les territoires ruraux ;
- un problème de cohabitation entre usages anciens et mobilités modernes.

En Corse, la présence d’animaux semi-libres ou divagants fait partie de la réalité territoriale. Elle ne peut pas être traitée uniquement comme une anomalie à supprimer. Elle doit aussi être comprise comme un fait systémique : routes, élevage, foncier, traditions pastorales, tourisme, vitesse automobile et responsabilité publique se rencontrent sur la chaussée.

Une solution sérieuse doit donc éviter deux erreurs :

1. traiter les animaux comme de simples obstacles ;
2. traiter la route comme un espace abstrait, sans histoire ni usages locaux.

VIGILIA vise une solution pragmatique : réduire le risque sans prétendre effacer la complexité du territoire.

---

## 3. Principe général

VIGILIA repose sur une idée simple : un territoire devient plus sûr lorsqu’il peut transformer des observations dispersées en vigilance partagée.

Le système combine quatre niveaux :

1. signalement manuel depuis un téléphone ;
2. agrégation des signalements récents ;
3. carte de risque territoriale ;
4. détection passive par balises lorsque certains animaux sont équipés.

Le premier niveau suffit déjà à produire une utilité publique. Les niveaux suivants augmentent la précision, la robustesse et la capacité d’anticipation.

Le principe général est cohérent avec la doctrine de traçabilité :

> Un acte sans trace est faible. Un signalement tracé devient un acte civique vérifiable, agrégable et utile.

---

## 4. VIGILIA 0 — Signalement manuel immédiat

La première version de VIGILIA doit permettre à tout conducteur, riverain, agent communal ou éleveur de signaler manuellement un animal potentiellement dangereux ou mal situé.

Le geste doit être aussi simple que possible :

> J’ai vu un animal sur la route ou près de la route.

Depuis le téléphone, l’utilisateur peut envoyer une alerte avec :

- position GPS approximative ;
- heure automatique ;
- type d’animal si connu : bovin, cheval, cochon, âne, sanglier, autre ;
- niveau de danger perçu : sur la chaussée, bord de route, animal agressif, animal blessé, troupeau ;
- photo facultative ;
- commentaire court facultatif.

Le signalement ne doit pas exiger l’identification parfaite de l’animal. Le but n’est pas d’accuser immédiatement un propriétaire. Le but est de produire une information utile, rapide et vérifiable.

Chaque signalement devient une trace horodatée, géolocalisée et qualifiée. Plusieurs signalements proches dans le temps et dans l’espace peuvent être agrégés pour produire une alerte renforcée.

Exemple :

> Trois signalements de bovins sur la même portion de route en moins de trente minutes augmentent le niveau de risque de cette zone.

Le signalement manuel complète les balises. Il permet surtout de démarrer le système avant que les animaux soient équipés.

La trajectoire de déploiement devient alors :

```text
VIGILIA 0
Signalement citoyen simple
→ utile immédiatement
→ zéro balise obligatoire
→ preuve d’usage

VIGILIA 1
Carte de risque territoriale
→ zones chaudes
→ récurrences
→ base de décision communale

VIGILIA 2
Balises sur animaux problématiques
→ bovins récurrents
→ troupeaux identifiés
→ prévention ciblée

VIGILIA 3
FractaTera complet
→ inférence radio
→ détection passive
→ perception territoriale distribuée
```

---

## 5. VIGILIA 1 — Carte de risque territoriale

Les signalements manuels permettent de constituer une carte de risque.

Cette carte ne cherche pas à produire une vérité absolue. Elle cherche à représenter des probabilités utiles :

- route régulièrement signalée ;
- horaires dangereux ;
- présence récurrente d’un troupeau ;
- zone de traversée probable ;
- accumulation d’incidents ou quasi-incidents ;
- besoin éventuel d’intervention communale.

Une carte imparfaite mais vivante peut être plus utile qu’un diagnostic parfait mais trop tardif.

Les données doivent rester proportionnées :

- pas de surveillance généralisée ;
- pas de publication nominative des propriétaires ;
- pas d’identification inutile des conducteurs ;
- agrégation dès que possible ;
- conservation limitée des traces fines ;
- journalisation claire des accès et traitements.

---

## 6. VIGILIA 2 — Balises animales ciblées

Une fois les zones de risque identifiées, certains animaux peuvent être équipés de balises radio basse consommation.

Les animaux concernés ne sont pas nécessairement tous les animaux du territoire. L’équipement doit être ciblé :

- bovins récurrents ;
- troupeaux connus pour fréquenter une route ;
- animaux ayant déjà provoqué des incidents ;
- zones où le signalement manuel montre une répétition forte.

Les balises peuvent utiliser :

- BLE ;
- LoRa ou technologie équivalente ;
- émission basse consommation ;
- identifiant pseudonymisé ;
- autonomie longue ;
- recharge solaire lorsque c’est réaliste.

La balise n’a pas besoin de transmettre une position GPS permanente. Elle peut simplement émettre un signal identifiable.

---

## 7. VIGILIA 3 — Détection passive et inférence FractaTera

Les véhicules participants disposent d’un smartphone ou d’un petit récepteur capable de détecter les signaux proches.

Quand le véhicule avance, l’intensité du signal varie. Cette variation, croisée avec la vitesse, la trajectoire et l’heure, permet d’estimer si l’animal est proche, très proche, ou probablement hors de danger immédiat.

Le principe central est celui de FractaTera :

> Le mouvement transforme le bruit en structure.

Un signal isolé est incertain. Une variation de signal observée par un véhicule en mouvement devient exploitable. Des milliers de variations, agrégées dans le temps, deviennent une carte territoriale du risque.

VIGILIA ne cherche pas à produire une fausse précision du type :

> Animal situé exactement à tel point GPS.

Il produit plutôt une alerte du type :

> Animal probablement proche de la chaussée dans les 200 prochains mètres. Ralentir.

L’alerte est utile même si elle n’est pas parfaite. En sécurité routière, une alerte probabiliste bien calibrée vaut mieux qu’une absence totale d’information.

---

## 8. Pourquoi ce n’est pas seulement une application

VIGILIA n’est pas une simple application mobile. C’est une infrastructure légère de perception territoriale.

Elle combine :

- signalements citoyens ;
- animaux balisés ;
- véhicules participants ;
- observations distribuées ;
- traces horodatées ;
- cartes de risque ;
- apprentissage progressif des zones dangereuses ;
- gouvernance locale des données.

Chaque détection ou signalement peut devenir une trace :

- date ;
- heure ;
- position approximative ;
- type d’animal si connu ;
- intensité du signal si balise détectée ;
- vitesse du véhicule si pertinente ;
- niveau de risque estimé.

Ces traces, agrégées, peuvent aider à identifier :

- les zones de traversée habituelles ;
- les périodes de risque ;
- les troupeaux concernés ;
- les routes prioritaires ;
- les endroits où une clôture, un panneau, un ralentissement ou une action d’éleveur serait réellement utile.

---

## 9. MVP territorial

Le premier MVP doit rester volontairement simple.

### Zone pilote

Une route ou un petit ensemble de routes rurales autour de Corte ou d’une commune volontaire.

Critères :

- présence connue d’animaux ;
- incidents ou quasi-incidents signalés ;
- éleveur ou propriétaire volontaire si possible ;
- commune intéressée ;
- réseau routier suffisamment fréquenté pour générer des observations.

### Matériel minimal

Pour VIGILIA 0 :

- une application ou page web mobile ;
- un formulaire de signalement en deux clics ;
- une carte simple ;
- un tableau de bord communal ;
- export CSV ou GeoJSON ;
- protocole de consentement et de responsabilité.

Pour VIGILIA 2 :

- 10 à 30 balises animales ;
- 5 à 20 véhicules participants ;
- application smartphone capable de détecter les balises ;
- tableau de bord enrichi.

### Fonctionnalités minimales

Pour le conducteur :

- signaler en deux clics un animal sur ou près de la route ;
- recevoir une alerte si d’autres signalements récents existent sur sa trajectoire ;
- confirmer ou infirmer une alerte existante ;
- joindre une photo facultative ;
- rester anonyme ou pseudonyme selon le protocole local ;
- détecter passivement les balises lorsque le système est équipé.

Pour le territoire :

- carte des signalements ;
- carte des détections ;
- historique des alertes ;
- identification des zones chaudes ;
- journal des incidents ;
- statistiques simples.

Pour l’éleveur ou le propriétaire :

- identification approximative des zones de présence ;
- aide à localiser certains animaux ;
- preuve de bonne foi en cas de démarche volontaire de prévention.

---

## 10. Questions juridiques

VIGILIA doit être conçu avec prudence.

Les points à clarifier :

- responsabilité en cas d’absence d’alerte ;
- responsabilité en cas de fausse alerte ;
- statut des données collectées ;
- pseudonymisation des conducteurs ;
- pseudonymisation des animaux et des propriétaires ;
- acceptation par les éleveurs ;
- rôle de la commune ;
- rôle éventuel de la Collectivité de Corse ;
- compatibilité avec la réglementation radio ;
- assurance.

Le système doit être présenté comme une aide à la vigilance, non comme une garantie absolue.

Formule de prudence :

> VIGILIA ne remplace ni la prudence du conducteur, ni les obligations des propriétaires, ni les pouvoirs de police du maire. Il ajoute une couche d’information territoriale destinée à réduire le risque.

---

## 11. Intérêt pour les communes

Pour une commune rurale, VIGILIA peut servir à trois choses.

D’abord, réduire le risque d’accident.

Ensuite, documenter objectivement un problème souvent traité par rumeur, plainte ou conflit.

Enfin, produire une base de décision : où agir, quand agir, avec qui agir, et avec quel budget.

Le système peut aider à sortir du face-à-face stérile entre automobilistes, éleveurs, propriétaires, mairie et assureurs.

La question n’est plus seulement :

> Qui est responsable ?

Elle devient aussi :

> Que savons-nous réellement du risque, et quelle action proportionnée peut le réduire ?

---

## 12. Intérêt pour FractaVolta

VIGILIA est un cas d’usage particulièrement lisible pour FractaTera et FractaVolta.

Il démontre plusieurs principes généraux :

- perception distribuée ;
- infrastructure légère ;
- usage de dispositifs existants ;
- inférence locale ;
- agrégation territoriale ;
- traçabilité des actes ;
- amélioration progressive par densité ;
- utilité dès le petit nombre.

VIGILIA peut donc devenir le premier démonstrateur concret d’un principe plus large : un territoire peut devenir plus intelligent sans devenir plus centralisé.

---

## 13. Extension possible

Une fois validé sur les collisions animaux-véhicules, le même modèle peut être adapté à d’autres objets mobiles :

- conteneurs de stockage ;
- batteries mobiles ;
- matériel agricole ;
- équipements communaux ;
- remorques ;
- outils mutualisés ;
- véhicules légers ;
- ressources de secours.

Dans tous les cas, le principe reste le même :

> Il n’est pas toujours nécessaire de suivre précisément un objet. Il suffit souvent de savoir qu’il a été vu, où, quand, par qui, et avec quel niveau d’incertitude.

Cette approche réduit les coûts, respecte mieux la vie privée et accepte l’imperfection du réel.

---

## 14. Positionnement

VIGILIA n’est pas une solution de surveillance généralisée.

C’est une solution de vigilance distribuée.

Elle doit rester :

- locale ;
- explicable ;
- auditable ;
- proportionnée ;
- utile aux conducteurs ;
- acceptable par les éleveurs ;
- gouvernable par les territoires.

Son ambition n’est pas de remplacer les humains par une infrastructure automatique. Son ambition est de rendre les humains mieux informés, plus tôt, avec moins de moyens.

---

## 15. Prochaine étape

Créer un pilote local.

Livrables immédiats :

1. fiche projet de deux pages pour les communes ;
2. schéma technique simple ;
3. liste de matériel compatible ;
4. estimation budgétaire ;
5. protocole d’expérimentation ;
6. modèle de convention avec une commune et un éleveur volontaire ;
7. dépôt GitHub public pour documenter les essais.

VIGILIA doit rester fidèle à la méthode générale :

> commencer petit, tracer les actes, apprendre du terrain, généraliser seulement ce qui fonctionne.

---

## 16. Relation avec FractaTera

Le document général `tera.md` définit FractaTera comme un réseau fractal de perception territoriale probabiliste.

VIGILIA en est le premier cas d’usage directement compréhensible.

FractaTera répond à la question :

> Comment un territoire peut-il produire une conscience probabiliste de ce qui s’y déplace ?

VIGILIA répond à une question plus concrète :

> Comment éviter qu’un véhicule percute un animal sur une route corse ?

Le passage de l’un à l’autre est volontaire : une architecture générale doit se prouver par un cas d’usage simple, local, utile et vérifiable.
