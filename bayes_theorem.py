# A company is hiring employees, and 20% of applicants are qualified.

# A test correctly identifies 90% of qualified candidates.
# A test incorrectly selects 30% of unqualified candidates.
# A candidate passes the test. What is the probability that they are actually qualified?


# Given data
p_A = 0.2  # Probability of being qualified
p_B_given_A = 0.9  # Test correctly identifies qualified candidates
p_B_given_Ac = 0.3  # Test incorrectly selects unqualified candidates
p_Ac = 1 - p_A  # Probability of not being qualified

# Step 1: Compute P(B) (Total probability of passing the test)
p_B = (p_B_given_A * p_A) + (p_B_given_Ac * p_Ac)

# Step 2: Apply Bayes' Theorem
p_A_given_B = (p_B_given_A * p_A) / p_B

print("Probability that a passing candidate is actually qualified:", p_A_given_B)
