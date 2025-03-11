# A box contains 4 Green balls and 3 Yellow balls.

# A ball is drawn, recorded, and not replaced.
# Then, another ball is drawn.
# Find:
# a) Probability of drawing two Green balls (GG).
# b) Probability of drawing one Green, then one Yellow (GY).
# c) Probability of drawing one Yellow, then one Green (YG).
# d) Probability of drawing two Yellow balls (YY).



# Given data
total_balls = 7
green = 4
yellow = 3

# Probabilities
p_G1 = green / total_balls
p_Y1 = yellow / total_balls
p_G2_given_G1 = (green - 1) / (total_balls - 1)
p_Y2_given_G1 = yellow / (total_balls - 1)
p_G2_given_Y1 = green / (total_balls - 1)
p_Y2_given_Y1 = (yellow - 1) / (total_balls - 1)

# Compute final probabilities
p_GG = p_G1 * p_G2_given_G1
p_GY = p_G1 * p_Y2_given_G1
p_YG = p_Y1 * p_G2_given_Y1
p_YY = p_Y1 * p_Y2_given_Y1

print("P(GG):", p_GG)
print("P(GY):", p_GY)
print("P(YG):", p_YG)
print("P(YY):", p_YY)
