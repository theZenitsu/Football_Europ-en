import sqlite3

# Path to your database
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Connect to the database
conn = sqlite3.connect(db_path)

# Query to check table structure
cursor = conn.execute("PRAGMA table_info(Match)")
columns = cursor.fetchall()

print("Columns in Match Table:")
for col in columns:
    print(col)

conn.close()
