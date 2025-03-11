# A university surveys 400 students to estimate the average GPA. The population standard deviation is 0.5.
# Find the Standard Error of the sample mean.



import math

# Given values
sigma = 0.5  # Population standard deviation
n = 400  # Sample size

# Standard Error formula
SE = sigma / math.sqrt(n)
print("Standard Error:", SE)
