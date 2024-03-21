import re
import os
import csv

# Directory where your files are stored
directory = "C:/Users/bkotl/PycharmProjects/DeePoreCollab/results_folder/coated_res"
pattern = r"Absolute Permeability \(um2\)\s+([\d\.]+).*?Tortuosity \(ratio\)\s+([\d\.]+)"

# Name of the CSV file where results will be saved
csv_file_path = "C:/Users/bkotl/PycharmProjects/DeePoreCollab/results_coating_7.csv"

# Store results
results = [("Filename", "Absolute Permeability (um2)", "Tortuosity (ratio)")]

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file follows the naming convention
    if filename.startswith("results3e.") and filename.endswith("c7.txt"):
        # Construct the full path to the file
        filepath = os.path.join(directory, filename)
        # Read the file content
        with open(filepath, 'r') as file:
            content = file.read()
            # Search for the pattern
            match = re.search(pattern, content, re.DOTALL)
            if match:
                # Extract and store the absolute permeability and tortuosity
                permeability, tortuosity = match.groups()
                results.append((filename, float(permeability), float(tortuosity)))

# Write the results to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(results)

print(f"Results have been saved to {csv_file_path}")
