import sqlite3
import pandas as pd

# Path to the SQLite database
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Step 1: Connect to the database
conn = sqlite3.connect(db_path)

# Step 2: Test a simple query
query = "SELECT * FROM Player LIMIT 5;"
result = pd.read_sql_query(query, conn)
print(result)



try:
    result = pd.read_sql_query(query, conn)
    print(result)
except Exception as e:
    print(f"Error: {e}")

# Close the connection
conn.close()
