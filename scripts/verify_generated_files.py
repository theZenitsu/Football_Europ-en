import pandas as pd
import os

# Chemins des fichiers générés
base_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed'
files_to_check = {
    "Players Summary": os.path.join(base_path, 'players_summary.csv'),
    "Matches Summary": os.path.join(base_path, 'matches_summary.csv'),
    "Teams Performance": os.path.join(base_path, 'teams_performance.csv'),
}

# Vérification des fichiers
print("Vérification des fichiers générés :")
for name, path in files_to_check.items():
    print(f"\n{name} :")
    if os.path.exists(path):
        data = pd.read_csv(path)
        print(f"- Nombre de lignes : {len(data)}")
        print(data.head())
    else:
        print(f"- Fichier non trouvé : {path}")
