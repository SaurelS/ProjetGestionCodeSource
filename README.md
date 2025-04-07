# Suivi Réseau - Détection d'IP Actives/Inactives

# Description

Ce projet est un outil permettant de scanner une plage d'adresses IP afin de détecter les IP actives et inactives. Il est conçu pour être utilisé en ligne de commande et offre des fonctionnalités avancées telles que l'exécution asynchrone pour un scan plus rapide.

# Fonctionnalités

Scanner une plage d'adresses spécifiée par l'utilisateur (ex: 192.168.1.1/24).

Afficher les IP actives avec leur temps de réponse.

Sauvegarder les résultats dans un fichier CSV.

Support du scan asynchrone pour une meilleure performance.

# Installation

Prérequis

Python 3.10+



# Installation des dépendances

# Cloner le dépôt
git clone https://github.com/SaurelS/ProjetGestionCodeSource.git
cd ProjetGestionCodeSource



# Utilisation

# Scanner une plage d'adresses

python3 src/scanner_ip.py --plage 192.168.1.0/24 --sortie resultats.csv ou 
python3 scanner_ip.py --plage 10.0.0.0/24 --sortie resultats.csv (le fichier resultats.csv sera créé dans le même répertoire que le programme).

# Scanner une liste d'adresses IP à partir d'un fichier

python3 src/scanner_ip.py --file ip_list.txt --sortie resultats.csv

# Exemple de sortie

192.168.1.1    Active   (Ping: 5 ms)
192.168.1.10   Active   (Ping: 2 ms)
192.168.1.20   Inactive
192.168.1.30   Active   (Ping: 7 ms)
Résultats sauvegardés dans resultats.csv

# Tests unitaires

Les tests unitaires garantissent la fiabilité du programme.

python -m unittest discover tests/

# Structure du projet

ProjetGestionCodeSource/
├── src/
│   ├── scanner_ip.py  # Programme principal
├── tests/
│   ├── test_programme.py  # Tests unitaires
├── README.md  # Documentation du projet


# Organisation Git

Ce projet suit les bonnes pratiques Git en utilisant différentes branches pour le développement.

La branche principale est main, où se trouvent les versions stables du projet.

Une branche feature/utils a été créée pour le développement de la fonctionnalité d'extraction du temps de réponse, puis fusionnée dans main.

Chaque nouvelle fonctionnalité peut être développée dans une branche dédiée avant d'être fusionnée dans main.



# Documentation avec sphinx

La documentation a été générée avec Sphinx. Je me suis servi de plusieurs commandes telles que sphinx-quickstart, sphinx-apidoc -o, make html, make clean, etc. Toute la documentation est contenue dans le répertoire docs/. Voici la nouvelle arborescence après génération de la documentation : 


ProjetGestionCodeSource/
├── .github/                     # Contient la configuration des workflows GitHub Actions
│   └── workflows/
│       └── ci.yml                # Workflow GitHub Actions pour déployer la doc
├── docs/                         # Dossier contenant la documentation Sphinx
│   ├── _build/                   # Dossier généré par Sphinx (contient la doc HTML générée)
│   ├── conf.py                   # Fichier de configuration Sphinx
│   ├── index.rst                 # Fichier principal de la documentation
│   ├── make.bat                  # Fichier pour générer la doc sous Windows
│   ├── Makefile                  # Fichier pour générer la doc sous Unix
│   ├── modules.rst               # Fichier pour décrire les modules
│   ├── scanner_ip.rst            # Fichier spécifique pour la documentation de `scanner_ip.py`
│   ├── _static/                  # Dossier pour les fichiers statiques (images, CSS, etc.)
│   └── _templates/               # Dossier pour les templates de Sphinx
├── rapport.md                    # Fichier de rapport au format Markdown
├── README.md                     # Fichier README principal du projet
├── src/                          # Code source Python
│   ├── pycache/                  # Cache Python
│   └── scanner_ip.py             # Script Python principal
├── tests/                        # Tests du projet
│   ├── pycache/                  # Cache Python pour les tests
│   └── test_programme.py         # Tests unitaires pour ton programme
├── .gitignore                    # Fichier pour ignorer les fichiers temporaires (ex : pycache, _build)

# Workflow avec Github Actions
Création du fichier ci.yml afin de déployer automaotiquement la documentation à chaque git push origin main. Cela permet d'automatiser la tâche de la documentation.
