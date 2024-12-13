"""
Ce script vérifie les jointures entre les tables pour diagnostiquer pourquoi aucune donnée n'est retournée.
"""

import sqlite3
import pandas as pd

# Chemin vers la base de données SQLite
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Connexion à la base de données
conn = sqlite3.connect(db_path)

# Requête SQL simplifiée pour vérifier les données des joueurs et leurs attributs
query = """
SELECT 
    p.player_name, -- Nom du joueur
    pa.overall_rating, -- Note globale
    pa.potential, -- Potentiel
    pa.preferred_foot -- Pied préféré
FROM 
    Player p
JOIN 
    Player_Attributes pa ON p.player_api_id = pa.player_api_id
LIMIT 10; -- Limite pour vérifier quelques lignes
"""

try:
    result = pd.read_sql_query(query, conn)
    print(result)
except Exception as e:
    print(f"Erreur : {e}")

# Fermeture de la connexion
conn.close()
