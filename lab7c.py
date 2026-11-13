# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 11/13/2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np

# TO DO 1: Create numArray according to instructions given in readme.md file.
numArray = np.random.randint(0,100,100)
# TO DO 2: Perform the operations on numArray given in readme.md file.
print("Slice and print first 10 values:", numArray[:10])
print("SLice and print last 10 values:", numArray[-10:])
print("Slice and print 30 values starting from index 21:", numArray[21:51])
# Change all values from index 50 to 65 to 101
numArray[50:66]=101
print("Updated array:", numArray)
# TO DO 3: Run the script.

