# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 11/13/2026
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

import pandas as pd

# TO DO 1: Create dataframe from provided dictionaries in readme.md file.
data1 = {
    "Apple": "Green",
    "Carrot": "Red",
    "Radish": "Purple"
}
data2 = {
    "Okra": "Thin",
    "Potato": "blob",
    "Radish": "Round"
}
data3 = {
    "Apple": 2.1,
    "Okra": 3.5,
    "Carrot": 1.3,
    "Potato": 2.0,
    "Radish": 3.0
}
# TO DO 2: create a data frame provided in dataframe.jpg file.
df1 = pd.DataFrame([data1, data2, data3])

print("Data Frame from dictionaries:")
print(df1)
# TO DO 3: Run the script.

