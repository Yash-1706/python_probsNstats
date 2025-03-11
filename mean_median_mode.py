#Measeres of Central Tendency

# Find the Mean, Median, and Mode of the dataset:
# 5, 10, 15, 20, 10, 25, 10


import statistics

data = [5, 10, 15, 20, 10, 25, 10]

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
