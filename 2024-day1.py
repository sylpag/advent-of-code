# IMPORTS
import pandas as pd
import numpy as np

# PART 1
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

# PART 2
# Count the number of times each unique number in array 2 appears
unique_vals_2, unique_counts_2 = np.unique(array2, return_counts=True)

# Map values to their counts
array_dict = dict(zip(unique_vals_2, unique_counts_2))

# Use dict 1 as vector function to count how often vals in array 1 appear in array 2
array1_counts = np.vectorize(array_dict.get)(array1, 0)

# Calculate similarity score element by element
similarity_score = np.dot(array1, array1_counts)

print("Total similarity score:", similarity_score)