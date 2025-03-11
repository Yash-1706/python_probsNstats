#Sets: Union, Intersection, Null

# Defining sets
A = {1, 2, 3}
B = {3, 4, 5}

# Union
union_AB = A | B  # or A.union(B)

# Intersection
intersection_AB = A & B  # or A.intersection(B)

# Null set check
is_null = A & {7, 8, 9}  # This will be an empty set

print("A ∪ B (Union):", union_AB)
print("A ∩ B (Intersection):", intersection_AB)
print("Null Set:", is_null)


# A survey was conducted on 50 students about their favorite sports.

# 30 students like Football (F)
# 25 students like Basketball (B)
# 10 students like both Football and Basketball
# Find:
# a) The number of students who like either Football or Basketball (F ∪ B)
# b) The number of students who like only Football
# c) The number of students who like only Basketball
# d) The number of students who like neither sport

# Try solving it first, then check the solution below.

# Given data
total_students = 50
football = 30
basketball = 25
both_sports = 10

# Union (Either Football or Basketball)
either_sport = football + basketball - both_sports

# Only Football
only_football = football - both_sports

# Only Basketball
only_basketball = basketball - both_sports

# Neither Sport
neither_sport = total_students - either_sport

print("Students who like either sport:", either_sport)
print("Students who like only Football:", only_football)
print("Students who like only Basketball:", only_basketball)
print("Students who like neither sport:", neither_sport)
