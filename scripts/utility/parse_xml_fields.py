import pandas as pd
import xml.etree.ElementTree as ET
import os

# Function to parse XML and extract the value of a specific tag
def parse_xml_field(xml_data, tag):
    if not xml_data or pd.isna(xml_data):
        return None
    try:
        root = ET.fromstring(xml_data)
        return root.find(tag).text if root.find(tag) is not None else None
    except ET.ParseError:
        return None

def main():
    # Path to the CSV file with XML data
    csv_file_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/parsed_match_data.csv'
    # Output file for the parsed data
    output_file_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/parsed_match_data_cleaned.csv'

    # Check if the input file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"Input file not found at {csv_file_path}")

    # Load the data
    match_data = pd.read_csv(csv_file_path)
    print("Data loaded successfully!")

    # Extracting specific fields from the XML
    match_data['goal_count'] = match_data['goal'].apply(lambda x: parse_xml_field(x, 'goals'))
    match_data['possession_home'] = match_data['possession'].apply(lambda x: parse_xml_field(x, 'homepos'))
    match_data['possession_away'] = match_data['possession'].apply(lambda x: parse_xml_field(x, 'awaypos'))

    # Save the parsed data to a new CSV
    match_data.to_csv(output_file_path, index=False)
    print(f"Parsed data saved to: {output_file_path}")

    # Print a sample of the processed data
    print(match_data[['goal_count', 'possession_home', 'possession_away']].head())

if __name__ == "__main__":
    main()
