import pandas as pd

# List of CSV files for different commodities
csv_files = {
    "Barley": "Barley_filtered.csv",
    "Maize": "Maize_filtered.csv",
    "Oats": "Oats_filtered.csv",
    "Wheat": "Wheat_filtered.csv",
    "Potatoes": "Potatoes_filtered.csv",
    "Total cattle": "Total cattle_filtered.csv"
}

# Initialize an empty DataFrame
combined_data = pd.DataFrame()

# Loop through each file and add a 'Commodity' column
for commodity, file_name in csv_files.items():
    df = pd.read_csv(file_name)
    df['Commodity'] = commodity
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Fill missing values with 0
combined_data.fillna(0, inplace=True)

# Save the combined data to CSV
combined_data.to_csv('agricultural_data_combined.csv', index=False)
