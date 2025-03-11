# A bag contains 5 red balls and 5 blue balls. You randomly pick one ball, note its color, and put it back. Then, you pick another ball.

# a) Are the two draws mutually exclusive?
# b) Are the two draws independent?
# c) What is the probability of picking a red ball twice?


# Given data
p_red = 5 / 10  # Probability of picking a red ball in one draw

# Since the draws are independent
p_red_twice = p_red * p_red

print("Probability of picking a red ball twice:", p_red_twice)
