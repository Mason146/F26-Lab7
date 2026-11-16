# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 11/13/2026
# Purpose: Create Histograms.
# Usage: ./lab7h.py

# TO DO 1: Import pandas and matplotlib modules.
import pandas as pd
import matplotlib.pyplot as plt
# TO DO 2: Draw histogram of the data from movies database.
movies = pd.read_csv("./imdb_top_250.csv")
# TO DO 3: Perform the operations provided in readme.md file on this data.
# Copy + Sort years
years = movies["Year"]
years = years.sort_values()
# Find unique years and count
unique_years = years.unique()
year_counts = years.value_counts().sort_index()
# Display first 10 years
unique_years = unique_years[:10]
year_counts = year_counts.head(10)

print("Unique Years:")
print(unique_years)

print("Number of Movies per Year:")
print(year_counts)

# Draw histogram
plt.hist(unique_years, bins=len(unique_years), weights=year_counts.to_numpy())
plt.title("Number of Movies Released per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.xticks(unique_years)
plt.show()
# TO DO 4: Run the script.

