# In a school of 100 students:

# 60 study Math (M)
# 50 study Science (S)
# 30 study both Math and Science
# a) How many students study only Math?
# b) How many students study only Science?
# c) How many students study neither Math nor Science?
# d) What is the probability that a randomly selected student studies either Math or Science?


# Given data
total_students = 100
math = 60
science = 50
both = 30

# Calculations
only_math = math - both
only_science = science - both
neither = total_students - (only_math + only_science + both)
p_either = (only_math + only_science + both) / total_students

print("Students studying only Math:", only_math)
print("Students studying only Science:", only_science)
print("Students studying neither:", neither)
print("Probability of studying either Math or Science:", p_either)
