# 803z-web-server

Bienvenue sur le repo du serveur web de 803z, une application utilisant Django et Django REST Framework.
Ce serveur fournit les API nécessaires pour l'authentification et la gestion des données pour le client web.

## Prérequis

- Python 3.12+

## Pour commencer

### Installation avec Pipenv (Recommandé)

Le projet utilise Pipenv pour la gestion des dépendances et de l'environnement virtuel.

Si vous n'avez pas Pipenv, installez-le avec `pip` :

```bash
pip install pipenv
```

Puis, installez les dépendances du projet :

```bash
pipenv install
```

### Installation alternative avec venv

Si vous préférez utiliser le module standard `venv`, une alternative est possible grâce au fichier `requirements.txt` fourni :

```bash
# Créer et activer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### Développement

Pour démarrer le serveur de développement local :

**Avec Pipenv :**
```bash
pipenv run python manage.py runserver
```

**Avec venv (si activé) :**
```bash
python manage.py runserver
```

L'API sera disponible sur `http://localhost:8000/`.

## Base de données

Avant de démarrer le serveur, n'oubliez pas d'appliquer les migrations initiales pour mettre en place la base de données :

```bash
pipenv run python manage.py migrate
# Ou avec venv: python manage.py migrate
```
