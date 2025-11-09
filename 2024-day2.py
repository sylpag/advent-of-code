# IMPORTS
import numpy as np

# HELPER FUNCTIONS
def is_safe(array):
    # Get diffs in array
    diffs = np.diff(array)

    # Check 1: is purely ascending or purely descending?
    is_ascending = np.all(diffs > 0)
    is_descending = np.all(diffs < 0)

    if not (is_ascending or is_descending):
        return False

    # Check 2: in valid range?
    is_valid_diff_range = np.all((np.abs(diffs) >= 1) & (np.abs(diffs) <= 3))
    return is_valid_diff_range

# INITIALIZATION
# Read the file line-by-line and convert to a numpy array
with open('data/2024-day2', 'r') as file:
    rows = [np.array(list(map(int, line.strip().split()))) for line in file]

# PART 1
# Initialize good reports counter
good_reports_counter = 0

# Check each row with safe function
for i, row in enumerate(rows, start=1):
    if is_safe(row):
        good_reports_counter += 1

# Print number of good reports
print("# of good reports:", good_reports_counter)

# PART 2 (dampener)
# Initialize good dampened counter
good_dampened_counter = 0

# Check each row
for i, row in enumerate(rows, start=1):
    # 1. Check if the original report is already safe
    if is_safe(row):
        good_dampened_counter += 1
        continue

    # 2. Now try removing every single level one by one
    is_dampened_safe = False

    # Iterate through all removable indices
    for k in range(len(row)):
        # Create a new report by removing the level at index k
        temp_row = np.delete(row, k)

        # Check if dampened report is safe
        if is_safe(temp_row):
            is_dampened_safe = True
            break # Found a removable element that fixes our problem

    if is_dampened_safe:
        good_dampened_counter += 1

# Print number of good dampened reports
print("# of good dampened reports:", good_dampened_counter)
