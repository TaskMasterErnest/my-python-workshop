"""
A script to run get the sum of the factorial of a group of numbers
factorial in math => 5! = 5 * 4 * 3 * 2 * 1
"""

# import the math package
import math

# list numbers
numbers = [3, 5, 7]

# loop through numbers
total = 0
for n in numbers:
  total += math.factorial(n)
print(total)