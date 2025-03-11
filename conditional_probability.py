# A box contains 3 red, 2 blue, and 5 green balls. Two balls are drawn without replacement.

# a) What is the probability of drawing a blue ball first?
# b) What is the probability of drawing a green ball second, given that the first ball was blue?
# c) What is the probability of drawing a blue ball first and a green ball second?


# Given data
total_balls = 10
blue_balls = 2
green_balls = 5

# Probability of drawing a blue ball first
p_blue_first = blue_balls / total_balls

# Probability of drawing a green ball second given first was blue
p_green_given_blue = green_balls / (total_balls - 1)

# Probability of drawing a blue ball first and green ball second
p_blue_and_green = p_blue_first * p_green_given_blue

print("P(Blue first):", p_blue_first)
print("P(Green second | Blue first):", p_green_given_blue)
print("P(Blue first and Green second):", p_blue_and_green)
