# A fair 4-sided die 🎲 has numbers 1, 2, 3, and 4.
# Find P(X ≤ 3) using CDF.


from scipy.stats import randint 

# Define a fair 4-sided die (1 to 4)
cdf_value = randint.cdf(3, 1, 5)  # Upper bound is 5 (exclusive)

print("P(X ≤ 3):", cdf_value)
