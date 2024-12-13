"""
Ce script vérifie les colonnes disponibles dans la table `Player_Attributes`.
"""

import sqlite3

# Chemin vers la base de données SQLite
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Connexion à la base de données
conn = sqlite3.connect(db_path)

# Requête pour obtenir les colonnes de la table Player_Attributes
query = "PRAGMA table_info(Player_Attributes);"
columns = conn.execute(query).fetchall()

# Afficher les colonnes
for col in columns:
    print(col)

# Fermer la connexion
conn.close()
