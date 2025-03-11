# A company’s employee salaries follow a normal distribution with a:

# Mean of $50,000
# Standard deviation of $5,000
# Find:

# The probability that an employee earns less than $55,000 (Use CDF)
# The salary at the 90th percentile (Use PPF)



from scipy.stats import norm

# Given values
mean = 50000
std_dev = 5000

# 1️⃣ Probability of earning less than $55,000
probability = norm.cdf(55000, mean, std_dev)
print("P(Salary < $55,000):", probability)

# 2️⃣ Salary at the 90th percentile
salary_90th = norm.ppf(0.90, mean, std_dev)
print("90th Percentile Salary:", salary_90th)
