# A university wants to find the average GPA of its students. Instead of surveying all 20,000 students, they randomly select 500 students.

# What is the population?
# What is the sample?


import random

# Simulated population of 20,000 students with random GPAs
population_gpas = [random.uniform(2.0, 4.0) for _ in range(20000)]

# Select a random sample of 500 students
sample_gpas = random.sample(population_gpas, 500)

# Calculate sample mean GPA
sample_mean = sum(sample_gpas) / len(sample_gpas)

print("Sample Mean GPA:", sample_mean)
