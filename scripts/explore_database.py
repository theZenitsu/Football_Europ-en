import sqlite3
import pandas as pd

# Path to the SQLite database
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

# Connect to the database
conn = sqlite3.connect(db_path)

# Step 1: List all tables in the database
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(tables_query, conn)
print("Tables in the Database:")
print(tables)

# Step 2: Inspect columns and sample data in each table
for table in tables['name']:
    print(f"\nInspecting table: {table}")
    try:
        # Fetch the first few rows
        query = f"SELECT * FROM {table} LIMIT 5;"
        data = pd.read_sql_query(query, conn)
        print(data)
    except Exception as e:
        print(f"Error reading table {table}: {e}")

# Close the connection
conn.close()
