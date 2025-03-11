#Measures of Spread

# Find the Range, Variance, and Standard Deviation of the dataset:
# 8, 10, 12, 14, 16
import statistics

data = [8, 10, 12, 14, 16]

range_value = max(data) - min(data)
variance_value = statistics.variance(data)  # Sample variance
std_dev_value = statistics.stdev(data)  # Sample standard deviation

print("Range:", range_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)
