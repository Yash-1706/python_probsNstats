# A set of test scores follows a bell curve with a mean of 50 and a standard deviation of 5.
# What is the probability of a student scoring exactly 50?


from scipy.stats import norm

# Given values
mean = 50
std_dev = 5

# Probability of scoring exactly 50
probability = norm.pdf(50, mean, std_dev)

print("Probability of scoring exactly 50:", probability)
