import sqlite3
import pandas as pd

# Path to the SQLite database
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Step 1: Connect to the database
conn = sqlite3.connect(db_path)

# Step 2: Test a simple query
query = """
SELECT 
    p.player_name,
    pa.overall_rating,
    pa.potential,
    m.season,
    t.team_long_name
FROM 
    Player p
JOIN 
    Player_Attributes pa ON p.player_api_id = pa.player_api_id
JOIN 
    Match m ON m.home_team_api_id = pa.player_api_id OR m.away_team_api_id = pa.player_api_id
JOIN 
    Team t ON t.team_api_id = m.home_team_api_id
LIMIT 5;
"""


try:
    result = pd.read_sql_query(query, conn)
    print(result)
except Exception as e:
    print(f"Error: {e}")

# Close the connection
conn.close()
