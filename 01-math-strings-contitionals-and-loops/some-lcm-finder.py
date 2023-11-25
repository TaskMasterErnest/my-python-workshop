"""
A program to calculate the LCM for some numbers using loops
LCM is the first value that some two specified numbers can divide.
"""

# define numbers
num_1, num_2 = 24, 36

# define iterator
x = 0
while True:
  x += 1
  if (x % num_1 == 0 ) and (x % num_2 == 0):
    print("{} is the LCM for both {} and {}".format(x, num_1, num_2))
    break