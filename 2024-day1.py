# IMPORTS
import pandas as pd
import numpy as np
# INITIALIZATION
# Get input data
input_data = pd.read_csv('data/2024-day1', sep=r'\s+', header=None)

# Extract input data
array1 = input_data[0].values
array2 = input_data[1].values

# CALCULATE LIST DIFFERENCES
# Sort arrays by values
array1_sorted = np.array(sorted(array1))
array2_sorted = np.array(sorted(array2))

# Get abs value distance bettwen array elements
pairwise_diff = abs(array1_sorted - array2_sorted)

# Sum distances
array_diff = np.sum(pairwise_diff)
print("Array difference:", array_diff)