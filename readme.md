# Hello World App

Cette application simple affiche "Hello, World!" via un backend Flask et un frontend Streamlit.

## Structure du projet

```
Mon application/
├── backend/
│   ├── app.py
│   ├── lib.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── streamlit.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Prérequis

- [Docker](https://www.docker.com/) installé.
- [Docker Compose](https://docs.docker.com/compose/) installé.

## Instructions

### 1. Cloner le projet
Clonez le dépôt ou copiez la structure des fichiers dans un répertoire local.

### 2. Construire et lancer les conteneurs
Depuis la racine du projet, exécutez :

```bash
docker-compose up --build
```

### 3. Accéder à l'application
- **Frontend Streamlit** : [http://localhost:8501](http://localhost:8501)
- **Backend Flask** : [http://localhost:5000](http://localhost:5000)

## Fonctionnalités

- **Backend (Flask)** : Fournit une API REST simple qui renvoie "Hello, World!".
- **Frontend (Streamlit)** : Affiche une interface utilisateur avec "Hello, World!".

## Technologies utilisées

- **Flask** pour le backend.
- **Streamlit** pour le frontend.
- **Docker** pour containeriser l'application.
- **Docker Compose** pour orchestrer les conteneurs.

## Contribution

Les contributions sont les bienvenues ! Forkez le projet, créez une branche et soumettez une pull request.

## Auteur

Raphaël ZAK