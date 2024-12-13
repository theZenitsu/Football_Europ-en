import sqlite3
import pandas as pd
import logging
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(
    filename='/home/corolo/Desktop/europe_football/logs/parse_match_data.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Path to SQLite database
db_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/raw/database.sqlite'

def parse_xml_field(xml_data, tag):
    """
    Parse XML data and extract the text of a specific tag.
    """
    if not xml_data:
        return None
    try:
        root = ET.fromstring(xml_data)
        return root.find(tag).text if root.find(tag) is not None else None
    except ET.ParseError:
        logging.error("Failed to parse XML data: %s", xml_data)
        return None

try:
    # Connect to the database
    logging.info("Connecting to SQLite database.")
    conn = sqlite3.connect(db_path)
    
    # Query to fetch relevant columns
    query = """
    SELECT goal, shoton, shotoff, possession
    FROM Match
    WHERE goal IS NOT NULL OR shoton IS NOT NULL OR shotoff IS NOT NULL OR possession IS NOT NULL
    LIMIT 10;
    """
    logging.info("Executing query: %s", query)
    
    # Fetch data into a DataFrame
    match_data = pd.read_sql_query(query, conn)
    logging.info("Data fetched successfully.")
    
    # Parse XML fields and extract relevant information
    match_data['goal_value'] = match_data['goal'].apply(lambda x: parse_xml_field(x, 'value'))
    match_data['possession_comment'] = match_data['possession'].apply(lambda x: parse_xml_field(x, 'comment'))
    
    # Save the parsed data to a CSV
    output_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/parsed_match_data.csv'
    match_data.to_csv(output_path, index=False)
    logging.info("Parsed match data saved to: %s", output_path)
    
    # Print the parsed data
    print("Parsed Data:")
    print(match_data)

except sqlite3.Error as e:
    logging.error("SQLite error: %s", e)

except Exception as e:
    logging.error("An error occurred: %s", e)

finally:
    if 'conn' in locals():
        conn.close()
        logging.info("Database connection closed.")
