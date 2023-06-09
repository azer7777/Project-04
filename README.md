# Project-04

## Exection du script

ETAPE 1
 
Création d'un environnement virtuel : 
````
python -m venv nom_env_virtuel
````
Activation de l'environnement virtiuel : 
````
source nom_env_virtuel/bin/activate
````
Activation de l'environnement virtiuel pour windows powershell : 
````
non_env_virtuel\Scripts\Activate.ps1
````
ETAPE 2

Installation des packages : 
````
pip install -r requirements.txt
````
ETAPE 3

Execution du script : 
````
python main.py
````
## Utilisation

Âpres, l'exécution du script, le menu principal s'affiche.
L'utilisateur sélecte l'option qui lui correspond tout en respectant les indications.

## Générer un rapport Flake8 :

Installez flake8 avec la commande: 
````
pip intall flake8-html
````
Créer un fichier setup.cfg et ecrire le texte suivant dedans:
````
[flake8]
exclude = .git, env, __pycache__, .gitignore, venv
max-line-length = 119
````

Entrez la commande: 
````
flake8 --format=html --htmldir=flake-report
````
