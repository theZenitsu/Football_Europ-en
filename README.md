# European Football Analysis

## Description
Ce projet analyse les données de football européen pour identifier les tendances, les performances des joueurs/équipes, et regrouper les entités similaires grâce à des algorithmes de clustering.

## Structure du Projet
- `data/`: Contient les données brutes et transformées.
- `notebooks/`: Notebooks pour chaque étape du projet.
- `scripts/`: Scripts réutilisables pour l'analyse et les visualisations.
- `outputs/`: Résultats finaux, incluant graphiques et rapports.

## Prérequis
Installez les dépendances avec :
```bash
pip install -r requirements.txt


european_football_analysis/
│
├── data/                   # Dossier pour les fichiers de données
│   ├── raw/                # Données brutes
│   │   └── database.sqlite # Base de données SQLite brute
│   ├── processed/          # Données nettoyées ou transformées
│   │   └── consolidated_data.csv
│   └── README.md           # Description des fichiers de données
│
├── notebooks/              # Jupyter Notebooks pour l'exploration et l'analyse
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_analysis.ipynb
│   ├── 04_clustering.ipynb
│   └── 05_visualizations.ipynb
│
├── scripts/                # Scripts Python réutilisables
│   ├── data_cleaning.py    # Script pour nettoyer et transformer les données
│   ├── data_analysis.py    # Script pour les analyses descriptives
│   ├── clustering.py       # Script pour les algorithmes de clustering
│   └── visualizations.py   # Script pour générer des graphiques
│
├── outputs/                # Dossier pour les résultats finaux
│   ├── plots/              # Graphiques générés
│   │   └── clusters.png
│   ├── reports/            # Rapports finaux
│   │   └── final_report.pdf
│   └── cluster_metrics.csv # Scores des modèles de clustering
│
├── requirements.txt        # Dépendances Python nécessaires
├── README.md               # Documentation principale du projet
├── .gitignore              # Fichiers à ignorer dans Git
└── LICENSE                 # Licence du projet

