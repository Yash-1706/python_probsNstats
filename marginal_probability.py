# A company surveyed 200 employees on their work preferences:

# 120 prefer Remote work
# 80 prefer Office work
# 50 are fine with both
# a) What is the probability that a randomly chosen employee prefers Remote work?
# b) What is the probability that a randomly chosen employee prefers Office work?
# c) What is the probability that a randomly chosen employee prefers either Remote or Office work?


# Given data
total_employees = 200
remote = 120
office = 80
both = 50

# Marginal probabilities
p_remote = remote / total_employees
p_office = office / total_employees
p_either = (remote + office - both) / total_employees

print("P(Remote work):", p_remote)
print("P(Office work):", p_office)
print("P(Either Remote or Office work):", p_either)
