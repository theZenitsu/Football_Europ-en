import sqlite3
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename='/home/corolo/Desktop/europe_football/logs/check_relevant_match_data.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Path to the SQLite database
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

try:
    # Connect to the database
    logging.info("Connecting to SQLite database.")
    conn = sqlite3.connect(db_path)
    
    # Query to fetch non-empty rows for relevant columns
    query = """
    SELECT goal, shoton, shotoff, possession
    FROM Match
    WHERE goal IS NOT NULL OR shoton IS NOT NULL OR shotoff IS NOT NULL OR possession IS NOT NULL
    LIMIT 10;
    """
    logging.info("Executing query: %s", query)
    
    # Execute the query and load data into a DataFrame
    data = pd.read_sql_query(query, conn)
    logging.info("Query executed successfully. Data fetched.")
    
    # Output the data to a CSV file for inspection
    output_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/relevant_match_data.csv'
    data.to_csv(output_path, index=False)
    logging.info("Relevant match data saved to: %s", output_path)

    # Display the DataFrame
    print("Sample Data (Relevant Match Columns):")
    print(data)

except sqlite3.Error as e:
    logging.error("SQLite error: %s", e)

except Exception as e:
    logging.error("An error occurred: %s", e)

finally:
    if 'conn' in locals():
        conn.close()
        logging.info("Database connection closed.")
