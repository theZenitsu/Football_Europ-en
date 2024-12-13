import sqlite3
import pandas as pd
import logging

# Configuration des logs
logging.basicConfig(
    filename='/home/corolo/Desktop/europe_football/logs/create_players_summary.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Chemin de la base de données
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

try:
    # Connexion à la base de données
    logging.info("Connexion à la base de données SQLite.")
    conn = sqlite3.connect(db_path)

    # Requête SQL
    query = """
    SELECT 
        p.player_name AS nom_joueur, 
        p.player_api_id AS id_joueur, 
        pa.overall_rating AS note_globale, 
        pa.potential AS potentiel, 
        pa.preferred_foot AS pied_préféré, 
        pa.attacking_work_rate AS taux_travail_attaque, 
        t.team_long_name AS nom_equipe, 
        m.season AS saison 
    FROM 
        Player p
    JOIN 
        Player_Attributes pa ON p.
          = pa.player_api_id
    JOIN 
        Match m ON m.home_team_api_id = pa.player_api_id OR m.away_team_api_id = pa.player_api_id
    JOIN 
        Team t ON t.team_api_id = m.home_team_api_id OR t.team_api_id = m.away_team_api_id;
    """

    logging.info("Exécution de la requête SQL.")
    players_summary = pd.read_sql_query(query, conn)

    # Vérification des résultats
    if players_summary.empty:
        logging.warning("Aucun résultat trouvé pour la requête SQL.")
    else:
        logging.info("Requête SQL exécutée avec succès.")

    # Sauvegarde dans un fichier CSV
    output_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/players_summary.csv'
    players_summary.to_csv(output_path, index=False)
    logging.info("Fichier CSV sauvegardé à : %s", output_path)

except sqlite3.Error as e:
    logging.error("Erreur SQLite : %s", e)
except Exception as e:
    logging.error("Erreur générale : %s", e)
finally:
    if 'conn' in locals():
        conn.close()
        logging.info("Connexion fermée.")
