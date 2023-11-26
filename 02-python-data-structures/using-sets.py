"""
An introductoin to sets 
"""

# initialize the set values
s1 = set([1, 2, 3, 4, 5, 6, 7])
s2 = {1, 2, 2, 3, 4, 5, 6, 6, 7}
s3 = {3, 4, 5, 2, 3, 1, 1,}

print(s1)
print(s2)
print(s3)

# adding to sets
s4 = {"garlic", "ginger", "cloves"}
print(s4)
s4.add("rosemary")
print(s4)

# implementing set operations
s5 = {1, 2, 3, 4}
s6 = {3, 4, 5, 6}

# union method
print(s5 | s6)
print(s5.union(s6))

# intersections
print(s5 & s6)
print(s5.intersection(s6))

# difference
print(s6 - s5)
print(s5.difference(s6))

# subset
print(s6 <= s5)
print(s5.issubset(s6))