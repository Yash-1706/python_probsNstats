# A factory produces 60% of its products from Machine A and 40% from Machine B.

# Machine A produces 5% defective items.
# Machine B produces 10% defective items.
# A product is randomly selected and found to be defective.
# Find the probability that the defective product came from Machine B.


# Given data
p_A = 0.6  # Prior probability of Machine A
p_B = 0.4  # Prior probability of Machine B
p_D_given_A = 0.05  # Defective from Machine A
p_D_given_B = 0.10  # Defective from Machine B

# Step 1: Compute total probability of defective product
p_D = (p_D_given_A * p_A) + (p_D_given_B * p_B)

# Step 2: Compute Posterior Probability
p_B_given_D = (p_D_given_B * p_B) / p_D

print("Probability that a defective product came from Machine B:", p_B_given_D)
