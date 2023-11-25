"""
This code takes in 3 values that are supposed to represent the 3 sides of a triangle
These values will be used to calculate the Pythagorean distance between the values
Values should be placed in x, y and z respectively.

The Pythagorean theorem pairs the numbers in such a way that they represent a triangle
ie (x, y), (x, z) and (y, z).

To find the distance, d = x(squared) + y(squared) + z(squared)
"""
# import the math library
import math

# define values
x, y, z = 2, 3, 4

# use the square-root method from the math library
d = math.sqrt(x ** 2 + y ** 2 + z ** 2)

# print the distance
print(d)

# name = "Ernest"
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.count('e'))