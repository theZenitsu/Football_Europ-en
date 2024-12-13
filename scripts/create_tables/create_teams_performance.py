"""
Ce script crée la table `teams_performance`, qui résume les performances des équipes
(buts marqués, encaissés, et différence de buts) pour chaque saison et phase.
Le résultat est sauvegardé sous forme de fichier CSV.
"""

import sqlite3
import pandas as pd

# Chemin vers la base de données SQLite
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Connexion à la base de données
conn = sqlite3.connect(db_path)

# Requête SQL pour créer teams_performance
query = """
SELECT 
    t.team_long_name, -- Nom de l'équipe
    m.season, -- Saison
    m.stage, -- Phase
    SUM(CASE WHEN t.team_api_id = m.home_team_api_id THEN m.home_team_goal ELSE m.away_team_goal END) AS goals_scored, -- Buts marqués
    SUM(CASE WHEN t.team_api_id = m.home_team_api_id THEN m.away_team_goal ELSE m.home_team_goal END) AS goals_conceded, -- Buts encaissés
    SUM(CASE WHEN t.team_api_id = m.home_team_api_id THEN m.home_team_goal ELSE m.away_team_goal END) - 
    SUM(CASE WHEN t.team_api_id = m.home_team_api_id THEN m.away_team_goal ELSE m.home_team_goal END) AS goal_difference -- Différence de buts
FROM 
    Match m
JOIN 
    Team t ON t.team_api_id = m.home_team_api_id OR t.team_api_id = m.away_team_api_id
GROUP BY 
    t.team_long_name, m.season, m.stage;
"""

# Exécution de la requête et sauvegarde des résultats en CSV
teams_performance = pd.read_sql_query(query, conn)
teams_performance.to_csv('/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/teams_performance.csv', index=False)

print("Table teams_performance créée et sauvegardée.")

# Fermeture de la connexion à la base de données
conn.close()
