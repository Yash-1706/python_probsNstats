# A company’s employee salaries follow a normal distribution with a mean of $50,000 and a standard deviation of $5,000.
# What is the probability that an employee earns less than $55,000?



from scipy.stats import norm

# Given values
mean = 50000
std_dev = 5000

# Probability of earning less than $55,000
probability = norm.cdf(55000, mean, std_dev)

print("P(Salary < $55,000):", probability)