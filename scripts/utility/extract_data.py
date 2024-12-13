import pandas as pd

# Load the CSV file
input_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/parsed_match_data.csv'
output_path = '/home/corolo/Desktop/europe_football/Football_Europ-en/data/processed/extracted_data.csv'

# Read the data
data = pd.read_csv(input_path)

# Display the data for debugging
print("Original Data:")
print(data.head())

# Filtering logic
filtered_data = data[
    (data['goal_value'].notnull()) &  # Non-empty goal_value
    (data['possession_comment'].astype(str).str.isnumeric()) &  # Numeric possession_comment
    (data['possession_comment'].astype(float) > 50)  # Possession > 50%
]

# Debugging the filtering
print("Filtered Data:")
print(filtered_data)

# Save the filtered data to a new CSV
filtered_data.to_csv(output_path, index=False)

print(f"Extracted data saved to: {output_path}")
