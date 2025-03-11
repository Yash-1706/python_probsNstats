# A weighted coin has a 70% chance of landing on heads and 30% chance of landing on tails.
# Write the PMF for this distribution.


# Define the PMF values for the coin flip
pmf = {
    "Heads": 0.7,
    "Tails": 0.3
}

# Print the PMF
for outcome, probability in pmf.items():
    print(f"P({outcome}) = {probability}")
