"""
Writing a module to handle factorial computation
"""

import math 

# write a function
def factorial_sum(numbers):
  total = 0
  for n in numbers:
    total += math.factorial(n)
  return total