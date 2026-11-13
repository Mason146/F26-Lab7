# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 11/13/2026
# Purpose: Slice 2D NumPy Arrays.
# Usage: ./lab7d.py

import numpy as np

# TO DO 1: Create a 2d NumPy array
arr_2d = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])
# TO DO 2: Slice the first two rows and the last three columns of arr_2d. Store the result in a variable called slice_1
slice_1 = arr_2d[:2, -3:]
print("\nSlice 1:")
print(slice_1)
# TO DO 3: Extract the middle 2x2 subarray (elements 70, 80, 120, 130) from arr_2d and store it in a variable called slice_2
slice_2 = arr_2d[1:3,1:3]
print("\nSlice 2:")
print(slice_2)
# TO DO 4: Slice every other row and every other column from arr_2d. Store the result in a variable called slice_3
slice_3 = arr_2d[::2, ::2]
print("\nSlice 3:")
print(slice_3)