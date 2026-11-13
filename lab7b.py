# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 11/13/2026
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

# TO DO 1: Copy the code from your lab7a.py file and paste here.
import numpy as np

# TO DO 1: Create array1 and array2 according to instructions given in readme.md file.
array1 = np.array(list(range(20, 50)))
array2 = np.arange(20, 50)
print("Array 1:", array1)
print("Array 2:", array2)
# TO DO 2: Create array3 according to instructions given in readme.md file.
array3 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("Array 3:\n", array3)
# TO DO 3: Create array4 according to instructions given in readme.md file.
array4 = np.array([
    [["January", "February"],
     ["March", "April"],
     ["May", "June"]],

    [["July", "August"],
     ["September", "October"],
     ["November", "December"]]
])
print("Array 4:\n", array4)
# TO DO 2: Reshape array1 reshapes array2 according to instructions given in readme.md file.
array1 = np.reshape(array1, (5,6))
print("\nReshaped Array1 (5x6):\n", array1)
array2 = np.reshape(array2, (2, 3, 5))
print("\nReshaped Array2 (2x3x5):\n", array2)
# TO DO 3: Create array5 according to instructions given in readme.md file.
array5 = np.diag([45, 7, 61, 8, 9])
print("\nArray5 (5x5 Diagonal Matrix):\n", array5)
# TO DO 4: Create array6 according to instructions given in readme.md file.
array6 = np.random.randn(7, 7)
print("\nArray6 (7x7 Normal Distribution):\n", array6)
# TO DO 5: Run the script.
