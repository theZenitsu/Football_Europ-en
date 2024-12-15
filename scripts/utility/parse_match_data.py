import pandas as pd
import xml.etree.ElementTree as ET

# Path to your CSV file
csv_file_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/parsed_match_data.csv'

# Load the CSV file
data = pd.read_csv(csv_file_path)

# Function to parse XML and extract specific data
def parse_xml_column(xml_content, tag):
    if pd.isna(xml_content) or not isinstance(xml_content, str):
        return None
    try:
        root = ET.fromstring(xml_content)
        return [elem.text for elem in root.findall(f".//{tag}")]
    except ET.ParseError:
        return None

# Extract relevant data
data['goal_values'] = data['goal'].apply(lambda x: parse_xml_column(x, 'goals'))
data['shoton_values'] = data['shoton'].apply(lambda x: parse_xml_column(x, 'shoton'))
data['shotoff_values'] = data['shotoff'].apply(lambda x: parse_xml_column(x, 'shotoff'))
data['possession_comments'] = data['possession'].apply(lambda x: parse_xml_column(x, 'comment'))

# Save the extracted data to a new CSV file
output_file_path = '/path/to/your/extracted_data.csv'
data.to_csv(output_file_path, index=False)

# Print a preview of the extracted data
print(data.head())
