import random

# Simulating a coin toss
coin = random.choice(["Heads", "Tails"])
print("Coin Toss Result:", coin)

# Probability calculation for a die roll
favorable_outcomes = 1  # Only one way to get a 3
total_outcomes = 6  # Six sides of a die
probability_of_3 = favorable_outcomes / total_outcomes
print("Probability of rolling a 3:", probability_of_3)


# A bag contains 5 red balls, 3 blue balls, and 2 green balls. If you randomly pick one ball, what is the probability that:

# a) The ball is red?
# b) The ball is blue?
# c) The ball is not green?

redballs = 5
blueballs = 3
greenballs = 2

totalballs = redballs + blueballs + greenballs

redprobability = redballs / totalballs
blueprobability = blueballs / totalballs
greenprobability = greenballs / totalballs

print("Probability of red ball:", redprobability)
print("Probability of blue ball:", blueprobability)
print("Probability of NOT picking a green ball:", 1 - greenprobability)

