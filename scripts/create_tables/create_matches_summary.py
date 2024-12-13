"""
Ce script crée la table `matches_summary`, qui résume les données des matchs, y compris les équipes à domicile et à l'extérieur,
les buts marqués, et les détails sur la saison et la phase. Le résultat est sauvegardé sous forme de fichier CSV.
"""

import sqlite3
import pandas as pd

# Chemin vers la base de données SQLite
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Connexion à la base de données
conn = sqlite3.connect(db_path)

# Requête SQL pour créer matches_summary (utilisant `id` au lieu de `match_id`)
query = """
SELECT 
    m.id AS match_id, -- Identifiant unique du match
    m.season, -- Saison
    m.stage, -- Phase du championnat
    t1.team_long_name AS home_team, -- Équipe à domicile
    t2.team_long_name AS away_team, -- Équipe à l'extérieur
    m.home_team_goal, -- Buts marqués à domicile
    m.away_team_goal -- Buts marqués à l'extérieur
FROM 
    Match m
JOIN 
    Team t1 ON t1.team_api_id = m.home_team_api_id
JOIN 
    Team t2 ON t2.team_api_id = m.away_team_api_id;
"""

# Exécution de la requête et sauvegarde des résultats en CSV
matches_summary = pd.read_sql_query(query, conn)
matches_summary.to_csv('/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/matches_summary.csv', index=False)

print("Table matches_summary créée et sauvegardée.")

# Fermeture de la connexion à la base de données
conn.close()
