# Find the 25th percentile (Q1), 50th percentile (Q2), and 75th percentile (Q3) of the dataset:
# 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

import numpy as np 

data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)  # Median
Q3 = np.percentile(data, 75)

print("Q1 (25th percentile):", Q1)
print("Q2 (50th percentile / Median):", Q2)
print("Q3 (75th percentile):", Q3)
