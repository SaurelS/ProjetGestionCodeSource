#Rapport du projet


#Introduction 

1 - Objectif du projet
L’objectif de mon projet est tout de se familiariser avec git et GitHub en utilisant les bonnes pratiques, de documenter le code de mon programme en utilisant des outils tels que les docstrings et sphinx, mais également documenter le suivi de mon projet.  Il faudra également appliquer des tests unitaires à mon programme et pour finir mettre en place une intégration continue avec GitHub Actions.

2 - Cible choisie
Pour ce projet, j’ai choisi de réaliser l’option B : Suivi du réseau, le programme consistera à scanner des plages d’adresses IP et de voir quels adresses IP sont actives et inactives sur le réseau tout en les répertoriant dans un fichier .csv.

#Solutions techniques

1 - Outils et Bibliothèques utilisés

argparse
Cette bibliothèque permet de gérer les arguments de ligne de commande de manière claire et structurée. Elle est utilisée pour permettre à l'utilisateur de spécifier la plage d'IP à analyser et le fichier de sortie des résultats.

asyncio
Cela permet d’éviter les blocages inutiles. Il est utilisé pour exécuter les tests d'IP de manière asynchrone, améliorant ainsi les performances du programme.


csv
csv est un module standard pour manipuler des fichiers CSV, facilitant l’enregistrement et la lecture des résultats. Il est utilisé pour sauvegarder les résultats des analyses de réseau sous forme de fichier exploitable.

ipaddress
Cette bibliothèque permet de manipuler des adresses et plages IP de manière simple et efficace. Elle est utilisée pour générer les adresses IP d'une plage donnée et les tester individuellement.

platform
Elle permet d’identifier le système d’exploitation, ce qui est utile pour exécuter la commande ping avec les bons paramètres. Elle est utilisée pour adapter les commandes ping entre Windows et Linux/MacOS.

subprocess
Cette bibliothèque permet d’exécuter des commandes système et de capturer leur sortie. Elle est utilisée. Elle est utilisée dans le projet pour envoyer des pings aux adresses IP et récupérer les résultats.
threadPookExecutor (concurrent.futures)
ThreadPoolExecutor permet d’exécuter des tâches en parallèle dans un pool de threads. l est utilisé pour tester plusieurs adresses IP simultanément sans bloquer l'exécution principale.

unittest
unittest est un module de test intégré à Python qui permet de valider le bon fonctionnement du programme. Il est utilisé pour tester les fonctions d’extraction du temps de ping et l’enregistrement des résultats dans un fichier CSV.





2 - Justification de mes choix

Certaines de ces bibliothèques vont permettre d’accroître la performance du programme notamment asyncio et ThreadPoolExecutor qui permettent de réduire le temps d’attente en exécutant plusieurs pings en parallèle.
Certaines permettent une meilleure simplicité du programme notamment argparse qui facilite l’ajout de nouveaux arguments de ligne de commande sans modifier la structure du code.
Plateform va permettre de rendre le programme compatible avec plusieurs systèmes d’exploitation.
Et unittest qui va permettre au programme d’avoir plus de robustesse car unittest garantit la fiabilité des principales fonctionnalités du programme.

Grâce à la combinaison de ses outils et bibliothèques, le projet offre une solution performante, simple à utiliser et extensible pour l’analyse de réseau.


#Difficultés rencontrées

Durant le projet j’ai rencontré beaucoup de problèmes que ce soit sur le programme, git, github et la documentation. En effet, j’ai réalisé ce projet sur le serveur de monsieur Roussille. 

1 - Problèmes liés à la gestion de Git/github

Mes plus gros problèmes se sont passés sur git et GitHub, notamment pour la synchronisation sur le dépôt distant. J’ai eu le plus de problèmes sur les commandes push, pull, etc… car je ne sais pas pourquoi mais les commandes simples ne marchait pas j’ai donc dû rajouter « - force » pour pouvoir pousser les modifications sur le dépôt distant. J’ai également eu des difficultés sur les commit car à chaque connexion sur le serveur et au premier git commit je devais à chaque m’identifier avec « git config –global user. » A ma grande surprise je n’ai pas eu de grandes difficultés à gérer les branches. Cependant ma plus grosse difficulté a été sur la génération de la documentation, qui ne fonctionnait pas du tout. Mais en regardant quelques vidéos j’ai pu surpasser ces difficultés.

2 - Problèmes de code ou de logique

Je n’ai pas eu tellement de difficulté au niveau du programme, cependant je ne peux pas l’exécuter sur le serveur, car je pense que celui-ci n’a pas assez de ressources pour le faire fonctionner (hypothèse).


3 - Problèmes de configuration des workflows CI/CD

Je n’ai pas eu de difficultés sur cette partie car je ne l’ai tout simplement pas fait car je ne comprends rien.

#Améliorations et optimisations

1 - Points faibles du programme et solutions : 

	- La fiabilité du ping, n effet certaines réponses peuvent être filtrées 	par des pare-feu, mais peut également varier selon le système 			d’exploitation. Solution : utiliser une bibliothèque qui 		permettrait d’envoyer des requêtes ICMP de manière plus fine afin d’éviter 		les restrictions.
	- Les erreurs ne sont pas enregistrées, Solution : mettre place un système de logs pour mieux suivre les erreurs et le comportement du programme (Avec logging)

2 - Fonctionnalités ou optimisation avancées que j’aurai souhaité intégrer

	Une interface graphique qui aurait permis de lancer le scan grâce à un 		simple clic au lieu de lancer le programme avec des lignes de commande. 	Avec Tkinter par exemple.
	Et bien sûr l’optimisation des requêtes et logging pour la gestion des 		erreurs.


#Bilan personnel

Durant ce projet, malgré les difficultés j’ai su développer de nombreuses compétences notamment sur Git et GitHub en adoptant les bonnes pratiques, mais également avec la documentation sphinx. Grâce à ce programme j’ai appris l’existence de nouvelles bibliothèques qui m’ont permis de faire fonctionner mon programme j’ai également amélioré mes compétences sur les tests unitaires. J’ai eu un bon sens de l’organisation tout le long du projet notamment avec les commit et les branches.

Personnellement, si je pouvais recommencer, je me serais d’abord plus renseigné sur les commandes git et également sur la documentation sphinx qui longtemps été catastrophique et qui m’a beaucoup posé de problèmes et également sur les workflows CI/CD. Globalement, ce que je retiens le plus sur ce projet, c’est qu’il faut mobiliser un grand sens de l’organisation et de la rigueur pour se servir de git et GitHub correctement en utilisant les bonnes pratiques.

