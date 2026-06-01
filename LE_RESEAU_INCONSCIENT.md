---
canonical_url: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/LE_RESEAU_INCONSCIENT.md
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
last_stamped_at: 2026-06-01
translations:
  en: https://github.com/JeanHuguesRobert/FractaVolta/blob/main/UNCONSCIOUS_GRID.md
role: "point d'entrée du corpus de packetization"
lang: fr
title: "Le Réseau Inconscient"
date: "2026-05-21"
status: "working-paper — auto-filled (frontmatter cleanup)"
---
# Le Réseau Inconscient
## De la commutation *store-and-forward* comme solution refoulée à la souveraineté énergétique

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A.  
1 cours Paoli, F-20250 Corte, Corse

jhr@baronsmariani.org

---

## Résumé

Le réseau électrique mondial demeure, structurellement, un réseau à commutation de circuits — un schéma dont les limites fondamentales ont été identifiées en 1964 et opérationnellement dépassées, dans le domaine de l'information, dès 1969. Le présent article soutient que la solution à la souveraineté énergétique existe depuis toujours, pratiquée inconsciemment par des milliards de personnes transportant leur téléphone portable, et qu'elle ne requiert aucune technologie nouvelle pour être déployée : le transport physique d'unités de stockage électrochimique comme paquets d'énergie discrets et adressables, combiné à la transduction de la valeur énergétique en jetons d'inférence d'IA routables sur l'internet. Nous appelons cette convergence le Réseau de Paquets d'Énergie (EPN — *Energy Packet Network*). En nous appuyant sur la théorie originelle de la commutation par paquets de Paul Baran (1964), l'histoire d'ARPANET, la littérature existante mais incomplète sur les réseaux énergétiques numériques, l'échec instructif de la France avec X.25, et le cas concret du câble sous-marin SARCO saturé qui isole la Corse des marchés énergétiques continentaux européens, l'article soutient que l'unité correcte de comptabilité énergétique est l'exergie, non l'énergie ; que le modèle correct de fiabilité réseau est la redondance de composants peu coûteux (RAIB — *Redundant Array of Inexpensive Batteries*), non la qualité de composants onéreux ; que le mécanisme correct de coordination est la stigmergie avec des signaux de prix honnêtes, non la répartition centralisée ; et que le principe architectural correct est la subsidiarité, non la synchronisation. Le résultat est un système antifragile au sens précis de Taleb — un système qui se renforce par le désordre plutôt que de simplement y survivre. L'EPN ne résout pas la tension entre capitalisme et collectivisme par compromis. Il dissout la question en séparant deux couches que l'économie politique a toujours confondues : le protocole, qui est un commun ; et l'opération, qui est radicalement diverse. La Corse n'est pas le sujet de cette analyse. Elle en est le laboratoire.

**Mots-clés :** commutation par paquets ; *store-and-forward* ; souveraineté énergétique ; inférence d'IA ; exergie ; logistique des batteries ; antifragilité ; stigmergie ; subsidiarité ; systèmes énergétiques insulaires ; MareNostrum

---

## 1. La maison qui brûle

Il existe un type d'urgence qui ne naît pas de la rareté mais de la mauvaise allocation — quand une ressource existe en abondance, qu'une solution existe en principe, et que l'écart entre les deux s'élargit au lieu de se réduire. La crise énergétique de l'intelligence artificielle est de cet ordre.

En 2024, les centres de données mondiaux ont consommé environ 415 TWh d'électricité — soit 1,5 % de la consommation mondiale, avec un taux de croissance annuel composé de 12 % depuis 2017, plus de quatre fois supérieur à celui de la demande électrique totale (AIE, 2025). L'Agence internationale de l'énergie projette que ce chiffre doublera pour atteindre environ 945 TWh d'ici 2030, dépassant légèrement la consommation électrique annuelle totale du Japon actuel. Au sein de ce total, l'infrastructure serveur accélérée spécifique à l'IA — clusters de GPU et systèmes de refroidissement associés — croît de 30 % par an, plus de trois fois le rythme de l'informatique conventionnelle. Aux seuls États-Unis, les centres de données ont consommé 183 TWh en 2024, soit plus de 4 % de la consommation électrique nationale — l'équivalent de la demande annuelle totale du Pakistan —, chiffre dont on projette une croissance de 133 % avant 2030 (Pew Research, 2025).

Les conséquences environnementales sont déjà mesurables. Une étude portant sur 2 132 centres de données américains a établi que 56 % de leur électricité provient de combustibles fossiles, générant plus de 105 millions de tonnes équivalent CO₂ en une seule année — 2,18 % des émissions totales des États-Unis — à une intensité carbone supérieure de 48 % à la moyenne nationale (Patel et al., 2025). L'entraînement d'un grand modèle de langage comparable à GPT-4 génère environ 552 tonnes de CO₂ — l'empreinte annuelle de 121 ménages américains. La consommation d'eau constitue une préoccupation tout aussi pressante : l'infrastructure d'IA devrait entraîner des augmentations annuelles de prélèvements d'eau aux États-Unis de 200 à 300 milliards de gallons d'ici 2030, dans un pays où l'épuisement des nappes phréatiques constitue déjà une crise régionale.

La réponse affichée par l'industrie — l'achat d'énergie renouvelable via des accords d'achat d'électricité (PPA) et des certificats d'énergie renouvelable — est structurellement inadéquate, et l'inadéquation n'est pas une question de degré mais de nature. Les certificats découplent la relation temporelle et géographique entre génération et consommation : un centre de données en Virginie qui tire son électricité du charbon à deux heures du matin peut revendiquer un statut renouvelable en achetant un certificat à une ferme solaire de l'Arizona qui a généré de l'électricité à midi. C'est de la comptabilité, non de la physique. Cela satisfait les exigences de reporting de durabilité tout en laissant le réseau physique inchangé.

La réponse structurellement honnête — co-localiser le calcul d'IA avec la génération renouvelable — affronte immédiatement la contrainte que cet article aborde. L'énergie renouvelable est distribuée, intermittente, géographiquement déterminée par le soleil et le vent. La demande d'IA est continue, en principe indépendante de la localisation mais historiquement concentrée près des infrastructures de fibre et du capital. Les systèmes de transmission qui pourraient relier ces géographies fonctionnent, dans bien des cas, près de leur capacité nominale. Les régions comme la Virginie, l'Oregon ou l'Irlande — où l'infrastructure d'IA s'est concentrée le plus rapidement — montrent déjà des signes de tension locale du réseau que des capacités additionnelles ne peuvent rapidement soulager (AIE, 2025).

Le problème n'est pas la pénurie d'énergie renouvelable. Les îles méditerranéennes reçoivent entre 2 600 et 2 900 heures d'ensoleillement annuel. La frange saharienne en reçoit davantage. La géothermie islandaise est, dans les faits, inépuisable. Le problème est l'absence d'une architecture capable de router cette énergie — ou, de manière équivalente, de router le calcul vers l'énergie — sans dépendre d'infrastructures câblées fixes dont la capacité est finie et dont le renforcement prend une décennie.

Cet article propose une telle architecture. Elle n'est pas nouvelle. Elle est pratiquée, inconsciemment, depuis la première personne qui a transporté un téléphone portable chargé d'un endroit à un autre.

---

## 2. La scène primitive : 1964–1969

En août 1964, Paul Baran, de la RAND Corporation, soumettait à l'US Air Force une série de mémorandums qui allaient, en cinq ans, réorganiser l'architecture de la communication humaine. Le rapport, *On Distributed Communications*, proposait une solution à ce qui paraissait un problème insurmontable : comment un réseau de communications peut-il survivre à la destruction de l'un quelconque de ses nœuds ?

La réponse existante — le réseau téléphonique — était un système à commutation de circuits. Lorsque deux parties souhaitaient communiquer, un chemin physique dédié était établi entre elles et maintenu pour la durée de l'échange. Le chemin était réservé, exclusif, continu. Sa vertu était la prévisibilité ; son vice fondamental était la fragilité. Détruisez un nombre suffisant de nœuds et le réseau s'effondre, parce que des circuits dédiés ne peuvent contourner les dommages. Le réseau téléphonique était, en termes de théorie des graphes, un arbre qui ne pouvait survivre à l'élagage de son tronc.

La proposition de Baran était conceptuellement simple et techniquement radicale. Ne pas établir un circuit dédié. Au lieu de cela, diviser le message en unités discrètes — des paquets — dont chacune porte sa propre adresse de destination dans un en-tête. Injecter ces paquets dans un maillage distribué dont les nœuds ne possèdent aucune connaissance globale. Permettre à chaque nœud de transmettre chaque paquet vers sa destination par la route disponible à cet instant. Réassembler les paquets à l'arrivée. Le réseau devient ce que Baran appelait un routage *hot potato* : chaque nœud passe le paquet aussi vite que possible, indifférent au chemin emprunté, engagé uniquement dans son mouvement vers l'avant.

Les implications étaient systémiques. Un réseau distribué à commutation par paquets n'a pas de point unique de défaillance. Il se dégrade gracieusement sous attaque — perdant sa capacité de manière proportionnelle plutôt que s'effondrant catastrophiquement. Il ne requiert aucune réservation préalable de bande passante. Il passe à l'échelle : ajoutez des nœuds et le réseau devient plus résilient, non plus complexe à gérer. Et il est, par construction, ingouvernable par un acteur unique, parce qu'aucun acteur ne détient le circuit.

Dès 1969, ARPANET avait démontré empiriquement ces propriétés. Dès 1983, TCP/IP avait cristallisé l'intuition de Baran en protocole universel. Dès 1991, le World Wide Web lui donnait un visage. Le réseau téléphonique à commutation de circuits — encore dominant en 1964 — était devenu, à l'an 2000, un système hérité progressivement absorbé par son propre successeur.

Le réseau électrique mondial n'en a rien remarqué. Il avait sa propre logique, sa propre histoire, ses propres ingénieurs. En 1888, Nikola Tesla et George Westinghouse avaient démontré l'avantage décisif du courant alternatif sur les systèmes à courant continu de Thomas Edison — non par une quelconque propriété intrinsèque de la physique, mais grâce au transformateur : un dispositif d'une simplicité élégante qui élève ou abaisse la tension AC à l'aide de deux bobines de fil enroulées autour d'un noyau de fer, permettant la transmission à haute tension sur longue distance et la consommation à basse tension en toute sécurité sur le même réseau. Le transformateur a rendu possible le réseau moderne. Il l'a aussi enfermé, pour un siècle et demi, dans la logique commutée de circuits que la transmission AC impose : une fréquence unique, une phase unique, une synchronisation continue sur des milliers de kilomètres, et l'incapacité structurelle de stocker le signal porteur.

En 2025, le réseau électrique mondial demeure un réseau à commutation de circuits. Lorsqu'une installation solaire en Corse veut livrer de l'énergie à un centre de données à Milan, elle requiert un chemin physique dédié — câble sous-marin, ligne de transmission haute tension, synchronisation de phase — pour toute la durée du transfert. Si ce chemin est saturé, l'énergie ne peut s'écouler, quelle que soit la quantité de soleil disponible à la source. Le câble sous-marin SARCO reliant la Corse au réseau continental français fonctionne près de sa capacité nominale pendant des portions significatives de chaque année. La Corse reçoit l'un des plus forts ensoleillements d'Europe occidentale. Elle ne peut exporter son surplus parce que le circuit est plein.

Pour l'électricité, nous sommes en 1968.

---

## 3. Le refoulement : pourquoi le réseau a refusé de grandir

Cette observation n'est pas sans antécédents. Un corpus significatif de la littérature d'ingénierie a reconnu l'analogie structurelle entre télécommunications et réseaux électriques, et proposé diverses formes d'« internet de l'énergie » ou de « réseau numérique » comme correctifs. La reconnaissance est juste. Les solutions proposées sont, sans exception, incomplètes d'une manière spécifique et révélatrice.

La première formulation systématique apparaît dans les travaux de Toyoda et Saitoh (1998), qui proposèrent un « réseau ouvert d'énergie électrique » modélisé explicitement sur la logique des marchés ouverts de télécommunications, avec l'ambition de « paquetiser » les flux énergétiques. Ils étaient visionnaires : ils dimensionnaient leur capacité de stockage proposée à l'aide de la théorie des files d'attente directement empruntée à la conception des réseaux de données. Leur limite était technologique — les dispositifs de stockage requis pour le transport physique des paquets n'existaient pas encore à un coût et une densité viables. Une décennie plus tard, Abe, Taoka et McQuilkin (2011) opérationnalisaient le concept sous le nom de « réseau numérique », proposant que l'énergie électrique soit transmise comme des paquets adressés sur un réseau de nœuds intelligents. Gelenbe (2012) développait le paradigme du *Energy Packet Network* à l'Imperial College, centré sur l'allocation dynamique d'énergie pour les centres de données du cloud. Nardelli et al. (2019) synthétisaient cette littérature dans un cadre exhaustif pour un « internet de l'énergie via gestion paquetisée ». Le groupe de l'Université de Kyoto — Hikihara, Takahashi et leurs collaborateurs — implémentait la transmission physique de paquets de puissance par *store-and-forward* entre des routeurs électriques à l'échelle du laboratoire, démontrant le principe matériellement avec une élégance considérable.

Ce sont des contributions authentiques. Elles sont aussi, sans exception, contraintes par une hypothèse non examinée : **le paquet voyage sur un fil**.

Dans chaque formulation de la littérature de l'internet de l'énergie, les paquets sont des quantités discrètes d'énergie électrique transmises sur un réseau fixe intelligent — une version plus astucieuse du réseau existant. L'adressage est réel, la discrétisation est réelle, le *store-and-forward* est réel au niveau du nœud. Mais le fil demeure. Le câble sous-marin demeure. La synchronisation de phase, même gérée plus élégamment, demeure. La vulnérabilité fondamentale de l'énergie à commutation de circuits — un chemin saturé ou rompu bloque tout flux — est gérée plutôt qu'éliminée.

C'est cela, le refoulement. La littérature existante a rêvé le bon rêve, et s'est réveillée juste avant son implication la plus radicale : que le paquet d'énergie n'a aucune obligation de voyager sur un fil.

Il existe un précédent historique à ce défaut de courage précis, et il est français.

En 1973, Louis Pouzin, à l'IRIA, concevait CYCLADES — l'un des premiers réseaux à commutation par paquets opérationnels au monde, dont l'architecture *datagramme* a directement influencé Vinton Cerf et Robert Kahn dans le développement de TCP/IP. La France avait, indépendamment et simultanément, abouti à l'intuition juste. Elle a alors choisi, pour son réseau de données national, non les datagrammes de Pouzin mais X.25 — un protocole qui accomplissait la commutation par paquets dans la forme tout en préservant la commutation par circuits dans l'esprit. Le circuit virtuel de X.25 était un compromis : les données étaient bien divisées en paquets, mais ces paquets étaient routés le long d'un chemin pré-établi, maintenu pour la durée de la session, coordonné par un réseau qui conservait un état global. Le cordon ombilical reliant à la logique commutée de circuits n'a pas été coupé — il a été allongé et rendu moins visible. Transpac et le Minitel furent de brillantes implémentations de la mauvaise abstraction. Ils ont été dépassés non par une technologie supérieure mais par une disposition supérieure à accepter que la fiabilité peut émerger du désordre plutôt qu'être imposée à lui.

Le secteur de l'énergie se trouve aujourd'hui exactement là où la France se trouvait en 1978 : au choix entre le circuit virtuel (câbles intelligents, réseaux numériques, interconnexions HVDC pilotées, systèmes de demand response) et le datagramme (paquets-batteries autonomes, transport physique sans routeur, auto-organisation stigmergique). La littérature existante sur l'internet de l'énergie a construit, avec une grande sophistication, le X.25 de l'énergie. Cet article propose le datagramme.

---

## 4. Le retour du refoulé : la batterie comme paquet

Considérez un téléphone portable. Il contient une batterie au lithium, chargée à un endroit avec de l'énergie d'une certaine source. Son propriétaire le transporte — à pied, en véhicule, en train, en avion — vers un autre endroit, où l'énergie stockée est consommée pour alimenter calcul et communication. L'énergie a voyagé de sa source à son point de consommation sans traverser aucune infrastructure électrique de transmission. Elle a été physiquement transportée dans un contenant, par un routeur humain, sur un réseau de chemins qui ne requiert ni synchronisation, ni coordination de phase, ni réservation de capacité dédiée.

C'est cela, le *store-and-forward*. Le téléphone portable est un paquet d'énergie. Son propriétaire est le routeur. L'observation est trivialement évidente une fois énoncée. Elle n'a, à la connaissance de l'auteur, pas été intégrée à la théorie formelle des réseaux énergétiques.

Le téléphone portable est la plus petite instance d'une architecture invariante d'échelle — fractale au sens précis où la même logique de routage opère identiquement à chaque niveau de la hiérarchie, seuls la forme du paquet et la modalité du porteur variant entre les échelles.

Une **batterie portable personnelle** (50–100 Wh), chargée depuis un panneau photovoltaïque de toit et transportée jusqu'à un point de consommation, est un paquet d'environ 0,1 kWh transporté par un routeur humain sur une portée de kilomètres.

Un **vélo cargo** équipé d'une batterie de 1 kWh, chargée à une installation agrivoltaïque puis pédalé jusqu'à un point de distribution, est un paquet de 1 kWh transporté par un routeur sans émissions sur une portée de dizaines de kilomètres.

Un **véhicule électrique** doté d'une batterie de 75 kWh, chargé durant la nuit à partir d'une source renouvelable et conduit jusqu'à sa destination — et, sous protocoles *vehicle-to-grid*, capable de décharger sa cargaison à la destination — est un paquet de 75 kWh transporté à vitesse autoroutière sur des centaines de kilomètres.

Un **conteneur ISO de vingt pieds** équipé de cellules de batteries lithium-fer-phosphate (capacité pratique : 1 à 2,5 MWh selon la chimie des cellules et la densité de packing), chargé sur un ferry roulier à Bastia et débarqué à Livourne, Marseille ou Gênes, est un paquet de 1 à 2,5 MWh transporté par un routeur maritime sur 170 à 500 kilomètres, sans traverser aucun câble électrique sous-marin.

Un **navire transportant cinquante de ces conteneurs** (capacité agrégée : 50 à 125 MWh) est un porteur de paquets à haute capacité desservant les routes énergétiques méditerranéennes ou atlantiques, connectant les territoires insulaires à fort ensoleillement aux centres de consommation continentaux sans un seul mètre d'infrastructure de transmission électrique dédiée.

L'auto-similarité fractale sur six ordres de grandeur de contenu énergétique — de 0,1 kWh à 125 MWh — n'est pas une coïncidence. C'est l'invariance d'échelle du principe *store-and-forward* lui-même, qui est indifférent aux quantités absolues impliquées et n'exige que ceci : que le paquet soit discret, qu'il porte son énergie jusqu'à une destination, et que la décision de routage soit prise localement par l'agent porteur.

Cette architecture n'est pas spéculative. Elle existe aujourd'hui, pratiquée inconsciemment et sans coordination. Des véhicules électriques sont transportés quotidiennement par des ferries rouliers à travers la Méditerranée, chacun portant une batterie chargée. Des téléphones portables sont transportés par avion à travers les océans, chacun étant un paquet d'énergie miniature. Ce qui n'existe pas encore, c'est le protocole conscient — l'équivalent de TCP/IP — qui coordonnerait ces flux en un réseau délibéré. Les paquets sont réels. Le réseau est latent.

Cette invariance d'échelle fractale est aussi, il faut le noter, l'implémentation physique du principe de subsidiarité — la doctrine, inscrite dans le Traité de Maastricht mais honorée principalement dans son inobservance, selon laquelle les décisions devraient être prises au niveau le plus bas capable de les traiter. Le réseau à commutation de circuits viole la subsidiarité par construction : la contrainte de synchronisation à 50 Hz exige une coordination continentale pour chaque watt transféré, rendant l'autonomie locale physiquement impossible. Le réseau à commutation par paquets restaure la subsidiarité par construction : chaque paquet est autonome, chaque nœud optimise localement, et le système n'interagit avec les niveaux supérieurs qu'à ses marges. La subsidiarité émerge non d'une volonté politique mais de la physique des paquets discrets. Elle est, en ce sens, la gouvernance naturelle des systèmes énergétiques distribués — non imposée, mais libérée.

---

## 5. La couche applicative : exergie et transduction d'inférence

L'architecture décrite à la section précédente relocalise physiquement l'énergie en transportant son support de stockage. Elle est pratique, immédiatement déployable, structurellement saine. Elle n'est pourtant pas l'implication la plus radicale de l'analogie avec la commutation par paquets appliquée à l'énergie.

L'implication la plus radicale est celle-ci : **l'énergie peut être transduite en information, et l'information est déjà routée sous forme de paquets sur l'internet.**

Pour comprendre pourquoi cela importe, il faut d'abord abandonner l'unité conventionnelle de comptabilité énergétique et la remplacer par celle qui est physiquement correcte.

L'énergie, comme l'énonce le premier principe de la thermodynamique, est conservée. Elle ne peut pas être consommée — seulement transformée. Ce qui est consommé, dans tout processus thermodynamique, c'est la capacité d'accomplir un travail utile : la propriété que les physiciens nomment **exergie**. L'exergie d'un système, c'est le travail maximal extractible de ce système lorsqu'on le ramène à l'équilibre avec son environnement par un processus réversible. C'est la monnaie de la thermodynamique, la grandeur que le second principe — l'entropie — érode perpétuellement.

La distinction entre énergie et exergie n'est pas pédante. Elle est la source de toute comparaison trompeuse dans le débat sur la densité énergétique.

Un conteneur de vingt pieds de e-diesel contient environ 150 à 200 MWh d'énergie chimique. Un conteneur de vingt pieds de batteries lithium-fer-phosphate contient environ 2 MWh. Le rapport — cent pour un — paraît décisif. Il ne l'est pas, parce qu'il compare des quantités de qualités thermodynamiques différentes.

Le théorème de Carnot place un plafond absolu sur la fraction d'énergie thermique convertible en travail mécanique : η_max = 1 − T_c/T_h. Pour un moteur Diesel opérant entre 800 K et 300 K, ce plafond est de 62,5 %. Aucune amélioration technologique ne peut le franchir, parce qu'il découle du second principe de la thermodynamique, non d'une immaturité technique. En pratique, les meilleurs moteurs Diesel atteignent 45 à 48 % d'efficacité de conversion ; le reste est restitué à l'atmosphère sous forme de chaleur de basse qualité, son exergie détruite définitivement. Un conteneur de e-diesel, routé via un moteur à combustion et un alternateur pour produire de l'électricité, délivre environ 60 à 70 MWh de travail électrique au point de consommation.

Un conteneur de batteries LFP, chargé depuis une source solaire et déchargé à destination, délivre environ 1,88 à 1,94 MWh. L'efficacité aller-retour des cellules LFP modernes est de 94 à 97 % par cycle. De surcroît, les 60 à 120 kWh dissipés en chaleur durant la charge et la décharge sont récupérables — pour l'eau chaude sanitaire, le chauffage de serres, la chaleur de procédés industriels — portant l'efficacité thermodynamique effective du système à paquets d'énergie, lorsque la récupération thermique est créditée, à environ 97 %. C'est comparable à la transmission à courant continu haute tension sur des distances équivalentes.

La comparaison correcte n'est donc pas 200 MWh contre 2 MWh. C'est 65 MWh (e-diesel, sortie électrique) contre 1,94 MWh (LFP, sortie électrique). L'écart est réel — un facteur d'environ trente-trois — et il se réduit encore selon deux trajectoires : la courbe historique d'amélioration de la densité énergétique des batteries (à peu près un doublement par décennie), et la croissance du marché de la seconde vie des batteries, où des cellules retirées du service automobile à 70–80 % de capacité résiduelle deviennent disponibles pour des applications de transport d'énergie à une fraction du coût des cellules primaires.

Pour les applications dont la forme énergétique finale n'est pas l'électricité — propulsion maritime, aviation long-courrier —, le vecteur approprié n'est en effet pas la batterie. Ammoniac, méthanol et carburant aérien synthétique (SAF) offrent la densité requise pour les applications à combustion, et leur production à partir d'électricité renouvelable, par électrolyse et synthèse, est techniquement mature. Le cadre correct n'est pas « quel vecteur gagne » mais « quel vecteur est approprié à quelle couche du réseau » — une architecture multi-protocole, au sens TCP/IP, où le support physique est choisi pour correspondre aux exigences de l'application.

Cela nous amène à la couche de transduction — le point où l'EPN entre en contact avec l'internet.

Lorsqu'une installation solaire convertit les photons en énergie électrique, l'étape suivante conventionnelle est de transmettre cette énergie électrique vers un point de consommation via le réseau. Si le réseau est saturé — comme l'est périodiquement le câble SARCO —, l'énergie ne peut atteindre sa destination. Le circuit est bloqué.

Une alternative existe. Convertir l'énergie électrique non en électrons à transmettre, mais en calcul — précisément, en inférence d'IA, l'exécution de modèles de réseaux neuronaux entraînés sur des requêtes entrantes. Une charge d'inférence d'IA est énergétiquement intensive, hautement parallélisable, et produit un service livré non sur une quelconque infrastructure électrique mais sur l'internet. La sortie — une réponse à une requête — est un paquet de données au sens conventionnel, routable vers tout point de la planète à la vitesse de la lumière, indépendamment de la capacité de transmission électrique.

Dans cette transduction, l'installation solaire n'est pas un producteur d'énergie connecté à un réseau. C'est un *transducteur* d'énergie : elle convertit l'irradiation solaire en calcul, et vend le calcul comme un service mondial. Le revenu de ce service revient à l'île. Le câble SARCO est contourné entièrement, parce qu'aucune énergie électrique ne le traverse. Ce qui traverse les câbles de données — dont la capacité élastique est de plusieurs ordres de grandeur supérieure à celle des câbles de puissance — est de l'information.

L'arithmétique de valeur de cette transduction est significative. De l'énergie électrique exportée aux prix spot de gros méditerranéens génère environ 40 à 80 € par mégawattheure. Le même mégawattheure, converti en inférence d'IA aux taux de service de centres de données souverains, génère de 500 000 à 2 000 000 € de revenu de service — un multiplicateur de valeur de ×10 à ×40 par unité d'exergie primaire. Ce n'est pas un artefact de tarification ; cela reflète la valeur économique réelle d'un calcul de haute qualité par rapport à une énergie électrique indifférenciée, dans un marché où la demande d'inférence d'IA croît de 30 % par an et où l'offre souveraine renouvelable est structurellement rare.

La valeur économique de l'inférence d'IA souveraine n'est pas uniforme. Elle est stratifiée selon le niveau de garantie de service crédible. L'inférence *best-effort* se négocie aux taux de commodité ; l'inférence d'entreprise standard commande des primes modérées ; tandis que l'inférence critique — celle qui ne tolère pas plus de quelques minutes d'indisponibilité par an — peut commander des prix d'un ordre de grandeur supérieur. Cette prime ne reflète pas une rhétorique commerciale mais le coût économique dur de la défaillance dans la finance, la santé, le contrôle industriel ou l'infrastructure souveraine.

Les centres de données hyperscale centralisés, malgré des SLA contractuels sophistiqués, demeurent fondamentalement limités par leur dépendance à des réseaux électriques à commutation de circuits. Une seule panne régionale — comme celles, bien documentées, des grands fournisseurs de cloud — peut interrompre simultanément des milliers de services nominalement à haute disponibilité. L'architecture EPN offre une alternative structurelle.

Un centre de données souverain approvisionné par une flotte rotative de conteneurs-batteries RAIB hérite de l'antifragilité conçue dans la couche énergétique elle-même. La redondance énergétique est physique plutôt que contractuelle : la défaillance d'un conteneur produit une dégradation gracieuse et proportionnelle plutôt qu'une panne catastrophique. L'indépendance vis-à-vis du réseau élimine le vecteur principal d'indisponibilité des centres de données. La surveillance en temps réel de l'état de charge à ±1 % près fournit des minutes d'avertissement prédictif. La diversité des sources (solaire, stockage batterie, secours minimal sur site) réduit encore la probabilité de défaillance simultanée à des niveaux qui font de la disponibilité à 99,999 % non un objectif aspiraltionnel mais une conséquence physique directe de l'architecture.

C'est pourquoi le terme η_sla dans l'Unité d'eXergie de Calcul (CXU) n'est pas un simple coefficient de reporting. Lorsque le substrat énergétique lui-même est antifragile, η_sla approche structurellement 1,0. Le service d'inférence résultant ne concurrence pas les hyperscalers sur le prix. Il concurrence sur quelque chose de bien plus précieux : la capacité physique de *garantir*, plutôt que de simplement promettre, que le calcul sera là quand on en aura besoin.

L'Unité d'eXergie de Calcul (CXU = E × η_hw × η_sys × η_sla), définie dans le cadre MareNostrum (Robert, 2026), est l'unité de compte qui tarife correctement cette transduction. Elle mesure non les électrons entrant dans le centre de données mais le travail computationnel utile que ces électrons produisent, après comptabilisation de l'efficacité matérielle, des frais généraux au niveau système et de la conformité au SLA. La CXU est, explicitement, une unité d'exergie — non d'énergie. Elle tarife la qualité du travail, non simplement sa quantité.

L'inférence d'IA est aussi, thermodynamiquement, l'application la plus exergie-efficiente concevable pour l'énergie électrique : elle accomplit un travail utile — le calcul — sans aucun cycle thermodynamique intermédiaire. Chaque joule d'électricité entrant dans un cluster GPU accomplit un travail directement, sans passer par combustion, turbine ou échangeur de chaleur. La couche applicative de l'EPN capture la plus haute fraction d'exergie primaire de tout cas d'usage énergétique connu.

---

## 6. Les résistances et leur résolution

Dans la pratique psychanalytique, les résistances sont le matériau qu'il faut travailler avant que l'intuition refoulée puisse être intégrée. Elles ne sont pas des obstacles à écarter ; elles sont la forme du problème. Nous traitons ici les principales résistances techniques, économiques et réglementaires à l'architecture EPN — non pour les minimiser, mais pour démontrer que chacune est tractable, et que plusieurs sont résolues par le même principe sous-jacent.

### 6.1 L'efficacité et le plafond de Carnot

L'objection la plus immédiate au transport d'énergie par batterie est thermodynamique : chaque cycle charge-décharge engendre des pertes. Cette objection a été traitée en détail à la section précédente, mais sa résolution mérite d'être soulignée. La comparaison correcte n'est pas entre un cycle de batterie LFP et un câble hypothétiquement sans pertes. C'est entre le système LFP — 94 à 97 % d'efficacité électrique aller-retour, montant à ~97 % avec récupération thermique — et les alternatives réelles : renforcement du réseau exigeant des centaines de millions d'euros et une décennie de construction, ou génération à combustible fossile avec un plafond de Carnot dur qu'aucune ingénierie ne peut briser. Sur cette comparaison, le paquet-batterie est compétitif ou supérieur en efficacité, et dominant en coût en capital et en vitesse de déploiement.

### 6.2 La densité énergétique : la réponse multi-protocole

L'écart de densité entre les batteries LFP et les carburants liquides, correctement énoncé en termes d'exergie, est d'un facteur d'environ trente-trois pour les applications électriques. Cela est réel, et cela signifie que le transport par batterie est approprié pour les distances maritimes courtes et moyennes (100 à 500 km), tandis que les distances plus longues et les applications non électriques requièrent des vecteurs énergétiques plus denses.

La réponse correcte à cette observation n'est pas la concession mais la reconnaissance que l'EPN est, par conception, multi-protocole à la couche physique — exactement comme l'internet utilise différents supports physiques (fibre, cuivre, radio, satellite) pour différents segments de réseau. Les paquets-batteries sont le support approprié pour la livraison électrique courte distance. Méthanol, ammoniac et SAF sont appropriés pour la longue distance et les applications non électriques. L'hydrogène, malgré sa faible densité volumique sous forme pressurisée, peut convenir à certains usages industriels spécifiques. Chaque vecteur est sélectionné par le protocole de routage — le marché — en fonction de la destination, de la distance, de la forme d'énergie requise et des signaux de prix actuels.

De surcroît, un conteneur mixte — portant simultanément une partition batterie et une partition carburant synthétique — n'est pas un compromis mais une diversification. Un conteneur qui peut servir à la fois le marché de l'électricité et le marché du carburant maritime dans un même voyage amortit son coût de repositionnement sur deux flux de revenu à faible corrélation de prix. Lorsque les prix spot de l'électricité sont déprimés, la demande de méthanol peut être robuste. Le conteneur mixte est l'équivalent énergétique du siège aérien flexible — une unité de capacité capable de servir plusieurs marchés au sein d'un même actif, l'intuition centrale du *Yield Management* appliqué à la logistique énergétique.

Le repositionnement des conteneurs vides — le problème classique du transport de conteneurs — est de même soluble par la logique du *Yield Management*. C'est un problème d'optimisation multi-contraintes stochastique de la classe exacte que les industries aérienne et maritime gèrent informatiquement depuis quarante ans. Le conteneur mixte, partiellement rechargeable depuis le réseau continental à tarif d'heures creuses durant le voyage de retour, réduit le coût de repositionnement à une opération d'arbitrage plutôt qu'à une pure dépense. Aucune solution optimale en forme close n'est requise ; une bonne heuristique — et un système d'inférence d'IA souverain tournant localement en est un candidat naturel — suffit.

### 6.3 Le principe RAIB : matériel de commodité et fiabilité distribuée

En 1988, Patterson, Gibson et Katz à l'UC Berkeley publiaient un article dont le titre contenait tout l'argument : *A Case for Redundant Arrays of Inexpensive Disks*. Le mot qui importait n'était pas *Redundant*. C'était *Inexpensive*. L'intuition était que la fiabilité d'un système de stockage n'a pas besoin de venir de la fiabilité de ses composants ; elle peut venir de la redondance de composants peu coûteux gérés par un logiciel intelligent. L'industrie mondiale du cloud computing — et, par extension, l'économie de l'information — a été bâtie sur ce principe.

Le Réseau de Paquets d'Énergie l'applique au stockage électrochimique. Nous l'appelons RAIB : *Redundant Array of Inexpensive Batteries*.

L'écart de prix entre les cellules de batterie industrielles haut de gamme et les cellules de grade commodité est substantiel : 300 à 500 €/kWh pour les premium contre 80 à 120 €/kWh pour les cellules LFP commodité neuves, et 30 à 60 €/kWh pour les cellules de seconde vie retirées du service automobile à 70 à 80 % de capacité résiduelle. Un conteneur équipé de cellules de seconde vie coûte cinq à quinze fois moins qu'un conteneur équipé de cellules premium. L'acceptation de taux de défaillance individuels plus élevés est gérée par le *Battery Management System* — l'équivalent logiciel du contrôleur RAID — qui contourne les cellules dégradées exactement comme une grappe RAID contourne les disques en panne. Les défaillances au niveau du conteneur sont gérées par redondance de flotte : l'EPN ne s'effondre pas quand un seul conteneur défaille, pas plus qu'ARPANET ne s'effondrait quand un seul nœud défaillait.

L'intégration de batteries de seconde vie fournit aussi un dividende environnemental. Une cellule retirée du service VE a son empreinte carbone déjà amortie sur son usage de première vie. Son déploiement dans un conteneur de transport d'énergie avant le recyclage final prolonge sa vie productive de cinq à dix ans, réduisant le carbone incorporé par unité d'énergie transportée. Le principe RAIB est simultanément l'argument économique en faveur du matériel de commodité et l'argument écologique en faveur des flux de matériaux circulaires.

### 6.4 Le courant continu : libérer la contrainte de 1888

Le réseau à courant alternatif n'est pas un optimum d'ingénierie. C'est un règlement historique.

En 1888, le transformateur donnait à l'AC un avantage décisif sur les systèmes DC d'Edison en permettant une transformation efficace de tension sur de longues distances. En 2025, l'électronique de puissance au carbure de silicium et au nitrure de gallium transforme la tension DC avec une efficacité dépassant 98 %, dans des dispositifs solid-state compacts, à des coûts qui ont chuté d'un ordre de grandeur au cours de la dernière décennie. L'argument physique en faveur de l'AC qui a réglé la *War of Currents* n'est plus valide.

L'EPN n'est sous aucune obligation d'hériter de l'héritage AC. Une architecture native DC — panneaux photovoltaïques générant du DC, batteries stockant du DC, centres de données consommant du DC — élimine chaque étape de conversion AC/DC. Chaque conversion évitée récupère 2 à 4 % d'efficacité système. Un chemin de paquet d'énergie entièrement natif DC depuis la cellule solaire jusqu'au cluster GPU élimine quatre étapes de conversion de ce type par rapport à une alimentation conventionnelle connectée au réseau AC, récupérant 8 à 16 % de l'énergie système — plus que compensant les pertes de charge-décharge LFP qui constituent l'objection standard d'efficacité. Les centres de données IA modernes hautes performances migrent déjà en interne vers une distribution DC haute tension. L'approvisionnement DC de l'EPN est architecturalement cohérent avec cette tendance. Le paquet était fait, depuis le début, pour être en DC.

### 6.5 La sécurité : défis d'ingénierie, non barrières de catégorie

Les conteneurs-batteries opérant à l'échelle du transport impliquent des tensions de 800 à 1 500 V DC, capables de délivrer une énergie létale en quelques millisecondes. Ce n'est pas une préoccupation triviale. C'en est une bien comprise.

Les systèmes haute tension DC sont opérés en sécurité dans des contextes industriels et utilitaires depuis des décennies. Les ferries électriques opérant dans les fjords norvégiens transportent des passagers au-dessus de systèmes de propulsion DC haute tension sous régulation maritime de sécurité ordinaire. Le risque d'emballement thermique — la décomposition exothermique caractéristique des batteries lithium-ion sous conditions d'abus — est spécifique à la chimie. Les cellules LFP, dont la chimie de cathode implique le fer et le phosphate plutôt que les oxydes riches en cobalt des formulations NMC, sont substantiellement plus stables thermiquement. Leur température de décomposition est plus élevée, la réaction est bien moins énergétique, et la propagation spontanée entre cellules est en conséquence rare. Tout déploiement sérieux de stockage stationnaire à grande échelle a convergé vers le LFP pour cette raison précise. Le transport de batteries au lithium est déjà gouverné par le Code maritime international des marchandises dangereuses, Classe 9, sous lequel les véhicules électriques sont routinièrement transportés par ferry roulier sur les routes méditerranéennes et atlantiques. L'extension de ce cadre réglementaire aux conteneurs énergétiques dédiés est affaire de standardisation et de développement réglementaire incrémental — non un saut de catégorie.

### 6.6 La réglementation : un avantage inattendu

Une question que la littérature EPN n'a pas adressée mérite un traitement explicite : un conteneur-batterie traversant une frontière nationale ou européenne constitue-t-il un transport d'électricité au sens réglementaire de la directive 2019/944 sur le marché intérieur de l'électricité ? Si oui, le conteneur serait sujet aux tarifs régulés d'accès au réseau, aux obligations d'accès des tiers, et à une charge de conformité substantielle.

La réponse juridique est presque certainement négative. Un conteneur portant des batteries chargées transporte un bien physique — un stockage électrochimique — et ne transmet pas une énergie électrique sur un réseau. La distinction est la même que celle entre l'expédition d'un baril de pétrole (transport de marchandises) et le pompage de brut à travers un pipeline international (transport d'énergie sujet à régulation réseau). Le conteneur-batterie, c'est de la marchandise. Le câble SARCO, c'est du réseau. Les cadres réglementaires qui s'appliquent à l'un ne s'appliquent pas à l'autre. Ce n'est pas une faille juridique ; c'est une caractéristique structurelle de l'architecture EPN qui confère un avantage commercial significatif sur les alternatives régulées basées réseau.

---

## 7. Le protocole : stigmergie, *skin in the game* et le commun

Un réseau à paquets sans protocole de routage est une collection de nœuds déconnectés. ARPANET exigeait TCP/IP. L'EPN exige un équivalent : des conventions gouvernant la manière dont les paquets sont décrits, tarifés, routés et comptabilisés à travers un réseau distribué de producteurs, transporteurs et consommateurs. Cette section décrit les principes sur lesquels un tel protocole devrait être bâti, et le cadre MareNostrum comme première implémentation.

### 7.1 La stigmergie : la coordination sans centre

Le mécanisme de coordination de l'EPN n'est pas la répartition centralisée. C'est la stigmergie — terme forgé par l'entomologiste français Pierre-Paul Grassé en 1959 pour décrire la coordination des colonies de termites. Grassé observait que les termites ne communiquent pas entre eux pour bâtir leurs constructions architecturalement sophistiquées. Chaque individu répond à des conditions locales — la concentration de phéromones, la forme des structures existantes —, modifiant son environnement local dans le processus. D'autres individus répondent à l'environnement modifié. L'ordre global émerge des réponses locales à des signaux locaux, sans qu'aucun agent ne possède de connaissance globale et sans qu'aucun coordinateur émette des instructions globales. La colonie de termites bâtit sa cathédrale sans architecte.

L'EPN opère selon le même mécanisme. Aucun répartiteur central ne route les conteneurs vers leurs destinations optimales. Chaque opérateur d'un paquet d'énergie — qu'il s'agisse d'un gestionnaire de flotte de conteneurs-batteries, d'un opérateur de centre de données ou d'un propriétaire individuel de véhicule — répond à des signaux de prix locaux : le prix spot de l'énergie renouvelable à la source, le prix de marché de l'inférence d'IA à la destination, le coût de transport de la route intermédiaire. Ces décisions modifient la distribution des paquets d'énergie à travers le réseau. Les opérateurs suivants répondent à la distribution modifiée. L'allocation globale émerge des décisions locales sans coordination centrale.

Le signal de prix CXU est la phéromone de l'EPN. Lorsque le prix de l'inférence d'IA souveraine s'élève à un nœud donné — parce que la demande a excédé l'offre —, des conteneurs sont routés vers ce nœud. L'afflux augmente l'offre et déprime le prix. L'équilibre émerge sans répartiteur. Ce n'est pas une approximation d'une répartition centrale optimale ; pour un système de la complexité et de la distribution géographique de l'EPN, c'est *supérieur* à la répartition centrale, parce que cela agrège une connaissance locale qu'aucun planificateur central ne peut posséder.

### 7.2 *Skin in the game* : la condition des signaux honnêtes

La coordination stigmergique produit des résultats fiables uniquement lorsque les signaux de prix auxquels les agents répondent sont *honnêtes* — lorsque les agents qui émettent et reçoivent les signaux portent personnellement les conséquences de leurs réponses. Taleb (2018) appelle cela *skin in the game*. Sans cela, les signaux de prix sont corrompus par l'information asymétrique, les pertes socialisées et la tendance systématique de ceux qui prennent les décisions à transférer leurs conséquences sur ceux qui ne les prennent pas.

Le réseau électrique existant viole cette condition à chaque couche. L'opérateur de réseau perçoit une rémunération régulée que le réseau soit géré efficacement ou non. Le gros consommateur paie un tarif régulé lissé qui dissimule le coût en temps réel de sa demande. L'opérateur de centre de données qui achète des certificats d'énergie renouvelable ne porte aucune conséquence physique pour le combustible fossile réellement consommé pour son compte. Le signal est malhonnête ; la coordination échoue.

L'EPN intègre structurellement le *skin in the game*. L'opérateur de conteneur qui mal-route une cargaison vers un marché aux prix déprimés perd de l'argent sur ce voyage. L'opérateur de centre de données alimenté par une infrastructure souveraine solaire d'IA et gouverné sous un SLA CXU paie financièrement pour chaque heure de service dégradé — le terme η_sla dans la formule CXU n'est pas une métrique de reporting mais une déduction de revenu. La structure de gouvernance SCIC, avec ses réserves institutionnellement impartageables, garantit que ceux qui prennent les décisions d'investissement ne peuvent se distribuer le commun accumulé — la forme la plus radicale de *skin in the game* en conception de gouvernance.

La phéromone est honnête parce que les fourmis paient leurs erreurs.

### 7.3 L'antifragilité : la propriété émergente

Un système stigmergique avec des signaux de prix honnêtes ne se contente pas de survivre au désordre. Il se renforce par lui — antifragile au sens précis de Taleb : non robuste (inchangé par la volatilité) mais énergisé par elle.

L'EPN est antifragile à chaque niveau de son architecture. Un pic du prix du pétrole rend le transport par batterie plus compétitif vis-à-vis des alternatives à combustible fossile, accélérant la diversification du portefeuille de vecteurs de l'EPN. Un rappel sur une chimie de cellule force l'adoption de chimies plus stables, améliorant la fiabilité moyenne de la flotte. Une route maritime fermée — par météo, conflit ou action réglementaire — fait développer des routes alternatives qui demeurent disponibles après réouverture, augmentant la redondance du réseau. Un marché de centres de données saturé dans une région déplace la demande d'inférence vers des régions sous-desservies, développant de nouveaux nœuds et réduisant la concentration géographique.

C'est précisément la logique de Baran, étendue des télécommunications à l'énergie : un réseau distribué qui contourne les dommages ne se contente pas de maintenir sa fonction — il l'améliore, parce que le contournement laisse les chemins alternatifs établis et testés. Le réseau à commutation de circuits a la propriété opposée : il peut survivre dans les limites de sa capacité nominale mais défaille catastrophiquement lorsque cette capacité est dépassée, parce qu'il n'y a pas de chemins alternatifs à développer. Il est fragile. L'EPN est antifragile.

La même distinction s'applique, à plus haute résolution, au principe RAIB. Une flotte de batteries peu coûteuses avec un taux de défaillance individuel prévisible est antifragile : les défaillances sont continues, de faible amplitude et informatives — elles révèlent quelles chimies, quels fabricants et quelles conditions d'opération sont fiables, permettant l'amélioration continue de la composition de la flotte. Un système unique de batterie premium est fragile : il opère de manière fiable dans les spécifications et défaille catastrophiquement en dehors, ne générant aucune information utile jusqu'à l'événement catastrophique.

### 7.4 MareNostrum comme protocole de routage

Le cadre MareNostrum, maintenu comme spécification open source (CC BY-SA 4.0) à github.com/JeanHuguesRobert/marenostrum, représente une première tentative de protocole de routage conscient pour le Réseau Méditerranéen de Paquets d'Énergie. Ses éléments centraux correspondent directement à la pile TCP/IP.

À la couche physique, MareNostrum traite l'irradiation solaire méditerranéenne comme un commun démocratique — une ressource physiquement disponible pour la Corse, la Sardaigne, la Sicile, la Tunisie et les territoires de la rive nord, analogue au spectre radio qui sous-tend la communication sans fil. Ce commun est gouverné par des assemblées fédérées selon le principe « une personne, une voix », avec des mandats impératifs et révocables — une architecture de gouvernance conçue pour être anti-capture par construction : aucun acteur unique, État ou corporation, ne peut s'emparer du contrôle d'un protocole qui appartient à toute personne vivant sous le soleil.

À la couche réseau, la CXU fournit une unité de compte standardisée pour les services de calcul souverains dérivés d'une quantité donnée d'exergie solaire primaire. Comme un en-tête de paquet IP, la CXU porte des métadonnées de provenance, de qualité et de niveau de service qui permettent les décisions de routage et de tarification à travers un réseau distribué de producteurs et de consommateurs.

À la couche applicative, les services d'inférence d'IA souverains constituent le flux de revenu primaire — le HTTP de l'internet de l'énergie. Le token est l'unité de sortie économique ; la CXU est l'unité de capacité productive ; le photon est l'unité d'entrée primaire. La chaîne de valeur est complète, souveraine à chaque couche, et libérée de la contrainte SARCO.

---

## 8. La famille élargie : de l'énergie à la cognition

Le réseau inconscient était une histoire énergétique. Il n'a pas à n'être que cela.

Une fois le diagnostic nommé — *un système à commutation de circuits resté en 1968, entouré d'alternatives datagramme qu'il n'a pas encore reconnues* —, le motif se révèle partout où le symptôme se répète. Chaque instance est un patient différent atteint du même refoulement. Chacune exige sa propre analyse, ses propres résistances à traverser, sa propre résolution. Le corpus de packetization, dont ce papier est le point d'entrée, est cette analyse graduelle.

Quatre instances contemporaines, brièvement, pour évoquer la famille.

### 8.1 Le réseau cognitif

Le réseau de l'intelligence artificielle contemporaine est, structurellement, à commutation de circuits. Un utilisateur se connecte à un fournisseur unique ; la conversation établit un chemin dédié entre eux ; ce chemin est maintenu pour toute sa durée ; si le fournisseur défaille, si l'utilisateur change de fournisseur, si la conversation doit migrer vers un autre agent, le chemin s'effondre et le travail qu'il portait est perdu. La session est le circuit dédié. Le travail cognitif qu'elle transporte est l'énergie captive qui ne peut s'en échapper.

Le datagramme dans ce domaine est le **paquet cognitif** — une unité de travail neutre en transport composée d'une *enveloppe* (métadonnées agnostiques au kind, que tout récepteur peut router, mettre en file, valider, archiver ou accuser réception) et d'un *payload* (contenu spécifique au kind, interprétable par un agent capable de traiter le kind déclaré : continuation, objection, hypothèse, décision, échec, routage). Un paquet cognitif peut être copié dans une nouvelle conversation chez un autre fournisseur, collé dans une issue, attaché à un document, transmis à un collaborateur humain, repris par un autre modèle. Le travail contourne le fournisseur au lieu d'être tenu captif par lui.

L'implémentation existe déjà dans le protocole `cogentia.continuation.v1` (Agent-Resumable CLI, 2026) et dans sa généralisation enveloppe/payload dans [Cognitive Packets](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md). Le fournisseur demeure un nœud utile dans le réseau. Il n'est plus le réseau.

### 8.2 Le réseau sociable

Le réseau de la data mobile et de la batterie est, structurellement, à commutation de circuits. Lorsqu'un utilisateur épuise son quota de data ou sa batterie au mauvais moment — à l'hôpital, à une frontière, passé minuit sur une route reculée —, le chemin vers l'opérateur est rompu et aucun secours n'existe. L'opérateur est le circuit dédié. Quand le circuit défaille, l'utilisateur est seul.

Le datagramme dans ce domaine est l'**hospitalité de proximité** : la data ou la batterie qu'un téléphone proche peut céder, volontairement, par un bref transfert pair-à-pair. La tradition méditerranéenne a nommé cet échange depuis deux millénaires ; il n'est devenu numérisable que récemment. Le module `brique-auxilia` de la plateforme Inseme ([spécification, 2026](https://github.com/JeanHuguesRobert/inseme/blob/main/packages/brique-auxilia/AUXILIA.md)) est le protocole qui rend l'échange auditable et transmissible — explicitement décrit dans son README comme l'instanciation humaine du principe *store-and-forward* des *Energy Packet Networks* de FractaVolta. L'opérateur reste utile là où la couverture est bonne et le quota suffisant. Il n'est plus l'unique substrat disponible.

### 8.3 Le réseau monétaire

La couche de monnaie de l'échange commercial contemporain est, structurellement, à commutation de circuits. L'euro clôt une transaction le long d'un chemin dédié, irréversible : le règlement est définitif, l'identité de la contrepartie se referme dans le prix, la réciprocité sociale que l'échange pouvait porter est tranchée au moment du paiement.

Le datagramme dans ce domaine est le **contre-don maussien** — une couche publique, volontaire, nominative, transparente, traçable et partiellement convertible de reconnaissance superposée *par-dessus* la transaction en euro, sans s'y substituer. Le circuit euro clôt la transaction ; le paquet-don ouvre une couche parallèle de mémoire sociale. Le [working paper Kudos](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/kudos.md) (2026) propose cette superposition explicitement : non pas substitution monétaire, mais raisonnement enveloppe/payload appliqué à la valeur elle-même — l'euro comme porteur, le kudo comme paquet cognitif de réciprocité sociale qui voyage par-dessus.

### 8.4 Le réseau territorial

Le débat contemporain sur l'autonomie territoriale est, structurellement, à commutation de circuits. L'autonomie est conçue comme un transfert statutaire le long d'un chemin politique dédié : réforme constitutionnelle, statut particulier, pouvoir normatif dévolu d'un centre à un autre. Le chemin est dédié ; rien n'advient tant qu'il n'est pas achevé ; s'il est bloqué, le territoire attend.

Le datagramme dans ce domaine est l'**autonomie de capacité** — la conversion vérifiable, documentée, transmissible du capital existant d'un territoire en capabilités collectives effectives, *indépendamment de tout transfert statutaire advenu ou non*. Le [working paper Autonomia](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/autonomia.md) (2026) formalise cela dans le cas corse : chaque capacité construite, chaque expérimentation documentée, chaque test public conduit est un paquet qui ne dépend pas de l'ouverture du circuit statutaire. Le territoire contourne sa propre dépendance institutionnelle.

### 8.5 Le même diagnostic, le même soin

Ces quatre instances — cognition, sociabilité, monnaie, territoire — n'épuisent pas la famille. La gouvernance distribuée d'IA sous [DHITL](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md), les communs sous les principes d'Ostrom, l'[attracteur de paquet](packet_attractor.md) comme mécanisme de transition invariant d'échelle, la [transition de paquet](packet_transition.md) comme lecture latérale des réseaux à circuits — chacune est une instance supplémentaire du même motif à une couche différente.

Ce que partagent les quatre, ce n'est pas la technologie. C'est la forme du diagnostic : dans chaque cas, l'habitude commutée de circuits a été préservée bien après que ses limites ont été démontrables, parce que l'alternative — le datagramme, le paquet, le travail qui contourne tout chemin unique dédié — n'a pas encore été reconnue comme l'état naturel du système. Le réseau inconscient était la version énergétique de cette histoire. L'histoire est la même partout où elle se raconte.

Ce qui manquait, dans chaque cas, c'était le protocole qui rendait l'alternative consciente.

---

## 9. Conclusion : le principe de diversité et la fin d'un vieux débat

Chaque section de cet article a, à l'examen, convergé vers un même principe sous-jacent. Il est temps de le nommer.

**La diversité n'est pas une caractéristique du Réseau de Paquets d'Énergie. Elle en est la source.**

Diversité des vecteurs physiques — batterie, méthanol, ammoniac, SAF — qui garantit qu'aucun choc de prix ou défaillance technologique unique ne peut effondrer le réseau. Diversité des facteurs de forme — du téléphone portable au navire porte-conteneurs — qui garantit que le réseau opère à toutes les échelles sans qu'un coordinateur central choisisse la « bonne » taille. Diversité des routes — route, rail, ferry, avion — qui garantit que le réseau contourne les fermetures sans perdre définitivement de capacité. Diversité des chimies cellulaires — LFP aujourd'hui, *solid-state* demain, seconde vie toujours — qui garantit qu'aucun fabricant ou chaîne d'approvisionnement unique ne peut tenir le réseau captif. Diversité des structures de gouvernance — SCIC, coopérative, municipale, académique — qui garantit qu'aucun acteur institutionnel unique ne peut s'emparer du protocole.

Cette diversité n'est pas conçue. Elle émerge de l'architecture par commutation par paquets elle-même, comme la subsidiarité émerge de l'élimination de la contrainte de synchronisation. Un réseau à commutation de circuits exige l'homogénéité — une fréquence, une phase, un opérateur par territoire — parce que la synchronisation continue exige une standardisation continue. Un réseau à commutation par paquets n'exige que ceci : que chaque paquet porte sa propre adresse. Tout le reste — la chimie, le facteur de forme, la route, l'opérateur — peut être différent d'un paquet à l'autre. La diversité est l'état naturel du système à commutation par paquets ; l'homogénéité est l'état imposé de celui à commutation de circuits.

Cette observation résout, structurellement plutôt qu'idéologiquement, le plus vieux débat de l'économie politique.

Le capitalisme soutient que les décisions non coordonnées d'acteurs auto-intéressés, médiées par des signaux de prix, produisent des résultats supérieurs à ceux atteignables par la planification centrale. Il a raison sur la vertu de la décision distribuée et sur le pouvoir d'agrégation d'information des prix. Il échoue lorsque la quête de profit produit l'homogénéité — quand tous les acteurs convergent sur la même stratégie gagnante, éliminant la diversité d'où vient la résilience des systèmes. La crise financière de 2008 fut une défaillance à commutation de circuits : toutes les banques avaient chargé les mêmes actifs, tous les modèles partageaient les mêmes hypothèses, et lorsqu'un nœud a défailli, les circuits dédiés qui les reliaient ont transmis la défaillance partout simultanément.

Le collectivisme soutient que les défaillances de coordination des systèmes de marché — externalités, biens publics, investissement de long terme, risque systémique — exigent la planification centrale comme correctif. Il a raison sur l'existence de ces défaillances. Il échoue lorsque la planification centrale supprime la connaissance locale que seuls les agents distribués possèdent, et lorsqu'elle impose une standardisation des stratégies qui détruit la diversité d'où émerge la résilience. Les économies planifiées du XX^e siècle furent des défaillances à commutation de circuits d'un genre différent : toute activité économique routée par un centre unique de coordination, qui en défaillant, défaillit complètement.

Le réseau à commutation par paquets n'est ni l'un ni l'autre. Il sépare deux questions que l'économie politique a toujours confondues : qui gouverne le protocole, et qui opère en son sein.

Le protocole — le format standard du conteneur, l'unité de tarification CXU, les conventions de routage, les règles de gouvernance — est un commun. Il ne peut être possédé par aucun acteur unique, capturé par aucun État unique, enclos par aucune corporation unique. Il est maintenu par tous ceux qui en dépendent, gouverné par subsidiarité, et modifié uniquement par des procédures qui exigent un consentement large. Ce n'est pas du collectivisme, parce qu'aucun plan central ne détermine quelle énergie est produite, par qui, pour qui, à quel prix. C'est un commun — la troisième voie d'Ostrom, démontrée empiriquement dans des villages de pêcheurs, des systèmes d'irrigation et des communautés forestières sur cinq continents, et désormais dans TCP/IP, Linux et les protocoles ouverts de l'internet.

L'opération — quelle énergie produire, quel vecteur choisir, quelle route emprunter, quel marché servir, à quel prix — est pleinement distribuée, compétitive, diverse, stigmergique. Aucun coordinateur central ne détermine l'allocation optimale. Des signaux de prix — honnêtes, parce que chaque opérateur a *skin in the game* — coordonnent les décisions distribuées de milliers d'acteurs, chacun avec une connaissance locale qu'aucun planificateur ne peut posséder. Ce n'est pas du capitalisme, parce que le protocole qui rend cette concurrence possible est un commun qu'aucun concurrent ne peut s'approprier. C'est un marché opérant au sein d'un commun gouverné — la structure de l'internet, appliquée à l'énergie.

L'antifragilité de cette architecture n'est pas un choix de conception. C'est une conséquence émergente de la diversité que la structure à commutation par paquets produit naturellement. Un système diversifié par construction, coordonné par stigmergie, gouverné par *skin in the game*, structuré sur un substrat de communs est, par définition, un système qui se renforce par le désordre. Le désordre sélectionne pour des chimies plus fiables, des routes plus robustes, des opérateurs plus efficients, une gouvernance plus adaptative — continuellement, sans réinitialisation catastrophique.

Les termites de Grassé construisent des structures antifragiles depuis trois cents millions d'années sans architecte. L'internet route des flux d'information antifragiles depuis cinquante ans sans coordinateur central. Le Réseau de Paquets d'Énergie propose de faire de même pour l'énergie — en commençant, modestement, avec un ferry de conteneurs entre Bastia et Livourne, et un centre de données solaire à Corte exécutant de l'inférence d'IA souveraine sur le même réseau que les Romains utilisaient pour dire l'heure.

Le réseau inconscient l'a toujours su. Chaque batterie de téléphone portable était un vote pour le datagramme. Chaque conteneur de véhicules électriques sur un ferry méditerranéen était une preuve de concept. Chaque token d'inférence d'IA souverain était un photon qui avait échappé à la contrainte SARCO.

Ce qui manquait, c'était le protocole qui le rendait conscient.

Maintenant, Pouzin avait raison. Le datagramme a gagné pour l'information. Qu'il gagne pour l'énergie.

---

## Remerciements

L'auteur pratique le développement logiciel itératif depuis la fin des années 1970 et fut signataire précoce du Manifeste Agile (2001). Il reconnaît dans le Réseau de Paquets d'Énergie le même principe architectural : la réponse locale plutôt que la coordination centrale, les paquets qui fonctionnent plutôt que la planification exhaustive. L'auteur a utilisé Claude (Anthropic, claude.ai) comme assistant d'écriture et de structuration durant la préparation de ce manuscrit. Tous les choix analytiques, les positions théoriques et le cadre MareNostrum sont sous la seule responsabilité de l'auteur.

---

## Références

- Abe, R., Taoka, H., & McQuilkin, D. (2011). Digital grid: communicative electrical grids of the future. *IEEE Transactions on Smart Grid*, 2(2), 399–410.
- Baran, P. (1964). *On Distributed Communications*. RAND Corporation, Memoranda RM-3420-PR à RM-3440-PR.
- Cerf, V., & Kahn, R. (1974). A protocol for packet network intercommunication. *IEEE Transactions on Communications*, 22(5), 637–648.
- Gelenbe, E. (2012). Energy Packet Networks: ICT-based energy allocation and storage. In *Green Communications and Networking*, Springer LNICST, vol. 51, p. 186–195.
- Grassé, P.-P. (1959). La reconstruction du nid et les coordinations interindividuelles chez *Bellicositermes natalensis* et *Cubitermes* sp. La théorie de la stigmergie. *Insectes Sociaux*, 6(1), 41–80.
- Hikihara, T., Takahashi, R., & Tashiro, K. (2013). Router for power packet distribution network: design and experimental verification. *IEICE Transactions on Communications*, E96-B(8), 2161–2168.
- Agence internationale de l'énergie (2025). *Energy and AI*. AIE, Paris. Disponible : iea.org/reports/energy-and-ai.
- Nardelli, P. H. J., et al. (2019). Energy internet via packetised management: enabling technologies and deployment challenges. *IEEE Access*, 7, 16909–16924.
- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Patel, R., Mahalingam, N., & Patel, A. (2025). The environmental impact of AI servers and sustainable solutions. arXiv:2601.06063.
- Patterson, D. A., Gibson, G., & Katz, R. H. (1988). A case for redundant arrays of inexpensive disks (RAID). *ACM SIGMOD Record*, 17(3), 109–116.
- Pew Research Center (2025). What we know about energy use at U.S. data centers amid the AI boom. 24 octobre 2025.
- Robert, J. H. N. (2026). From Sun to Sovereignty: Communal Sovereign Funds as a mechanism to decouple tourism from land dispossession. Institut Mariani / C.O.R.S.I.C.A., Corte. CC BY-SA 4.0. Disponible : github.com/JeanHuguesRobert/marenostrum.
- Taleb, N. N. (2012). *Antifragile : les bienfaits du désordre*. Les Belles Lettres (trad. fr. *Antifragile*, 2013).
- Taleb, N. N. (2018). *Jouer sa peau : asymétries cachées dans la vie quotidienne*. Les Belles Lettres (trad. fr. *Skin in the Game*, 2018).
- Toyoda, J., & Saitoh, H. (1998). Proposal of an open electric energy network (OEEN) to realise cooperative operations of IOU and IPP. In *Proceedings of EMPD '98*, vol. 1, p. 218–222. IEEE.
- World Economic Forum (2025). How data centres can avoid doubling their energy use by 2030. Disponible : weforum.org.

---

## Note sur l'auteur

Jean Hugues Noël Robert, baron Mariani, est le fondateur et directeur de l'Institut Mariani (1 cours Paoli, F-20250 Corte, Corse), branche R&D de l'association C.O.R.S.I.C.A. à but non lucratif (fondée à Corte en 1995, antérieure à l'apparition du terme « open source »). Le cadre MareNostrum décrit à la section 7 est maintenu comme spécification open source à github.com/JeanHuguesRobert/marenostrum sous CC BY-SA 4.0. L'auteur est titulaire du brevet US7606221B2 (priorité 1999) sur un protocole d'auto-découverte permettant à des dispositifs terminaux de localiser de manière autonome une infrastructure de serveurs distribuée sans registre central capturable — la même question architecturale que celle que le protocole de routage de l'EPN aborde pour l'énergie. L'auteur déclare n'avoir aucun conflit d'intérêt financier. Correspondance : jhr@baronsmariani.org

---

## Version condensée pour agents IA

**Le réseau électrique mondial est structurellement à commutation de circuits** (synchronisation continue, chemins dédiés, point unique de défaillance, scalabilité limitée, fragilité à la saturation ou aux pannes — le SARCO corse comme exemple canonique).

**La solution refoulée depuis 1964 (Baran), c'est le *store-and-forward* physique** : traiter l'énergie non comme un flux continu sur des fils, mais comme des **paquets discrets, adressables, autonomes** physiquement transportés (batteries LFP neuves ou de seconde vie dans des conteneurs ISO, VE, vélos cargo, ferries, etc.).

### Architecture EPN (*Energy Packet Network*)

- **Couche physique** : paquets électrochimiques fractals (0,1 kWh → 100+ MWh) routés via la logistique conventionnelle (route, rail, maritime) → **dépendance nulle aux câbles HT, synchronisation AC nulle**.
- **Mécanismes de fiabilité** :
  - **RAIB** (*Redundant Array of Inexpensive Batteries*) : redondance de composants peu coûteux + BMS intelligent → dégradation gracieuse proportionnelle, jamais catastrophique.
  - **Diversité multi-niveau** (vecteurs : batterie/méthanol/ammoniac/SAF ; routes ; opérateurs ; chimies ; modèles de gouvernance) + stigmergie via signaux de prix honnêtes (*skin in the game*).
  - **Subsidiarité physique** : chaque paquet prend des décisions de routage locales → antifragilité au sens de Taleb (le système s'améliore sous le désordre).

### Couche applicative (transduction)

Exergie solaire bloquée → **transduction directe en inférence d'IA souveraine** (exergie → tokens routables sur internet), contournant complètement les contraintes physiques du réseau.

### Propriété émergente critique

L'antifragilité de la couche énergétique **se propage structurellement** à la couche d'inférence :  
→ disponibilité énergétique native extrêmement élevée (indépendance réseau, redondance physique, surveillance SOC précise en temps réel, diversité des sources).  
→ permet un SLA à 99,99x % (inférence critique / haut de gamme) via η_sla dans la CXU approchant 1,0 **structurellement**, non contractuellement.  
→ positionne l'EPN pour capter la prime de marché pour l'inférence premium (finance, santé, industrie, souveraineté) où la garantie physique de disponibilité est le différenciateur dominant.

### Résumé axiomatique (pour raisonnement d'agent)

**EPN = commutation par paquets appliquée à l'exergie physique + transduction exergie → calcul souverain + antifragilité distribuée → haute disponibilité garantie → prime économique durable pour l'inférence d'IA haut de gamme.**

---

## Journaux cibles potentiels

- *Energy Research & Social Science* (Elsevier) — cible principale ; la revue accueille explicitement les contributions théoriquement ambitieuses, historiquement ancrées et interdisciplinaires en analyse des systèmes énergétiques
- *Joule* (Cell Press) — revue à fort impact, réceptive aux contributions conceptuellement originales qui traversent les frontières disciplinaires
- *Telecommunications Policy* (Elsevier) — pour les dimensions de théorie des réseaux et réglementaires
- *IEEE Access* (IEEE) — périmètre plus large, accès libre, calendrier de publication plus rapide


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [The Packet as Evolutionary Attractor: Scale-Invariant Transitions in Complex Networks](packet_attractor.md)
- [The Packet Transition: A Lateral Reading of Circuit Networks](packet_transition.md)
- [Corpus Status — FractaVolta](research/corpus-status.md)
- [Research Index — FractaVolta](research/index.md)

<!-- END_AUTO: backlinks -->
