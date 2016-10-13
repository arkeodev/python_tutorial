# coding=utf-8

# 1. Three simple examples of list comprehension
# Conversion of Celsius values into Fahrenheit and vice versa
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [((float(9) / 5) * x + 32) for x in Celsius]
print(Fahrenheit)
# [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]

# A Pythagorean triple consists of three positive integers a, b, and c, such that a2 + b2 = c2.
print([(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x ** 2 + y ** 2 == z ** 2])
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15),
#  (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]

# Another example: Let A and B be two sets, the cross product (or Cartesian product) of A and B, written A×B,
# is the set of all pairs wherein the first element is a member of the set A and the second element is a member
# of the set B. Mathematical definition:
# A×B = {(a, b) : a belongs to A, b belongs to B}.
colours = ["red", "green", "yellow", "blue"]
things = ["house", "car", "tree"]
coloured_things = [(x, y) for x in colours for y in things]
print(coloured_things)
# [('red', 'house'), ('red', 'car'), ('red', 'tree'), ('green', 'house'), ('green', 'car'),
#  ('green', 'tree'), ('yellow', 'house'), ('yellow', 'car'), ('yellow', 'tree'), ('blue', 'house'),
#  ('blue', 'car'), ('blue', 'tree')]
