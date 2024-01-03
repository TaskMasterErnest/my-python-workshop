"""
Code to find the maximum number in a list.

1. set max number to 0
2. for each number in the list, check if that number is greater than the set max number
3. if number is greater, set that number as current max number
4. max number is now equal to the largest number in the list
"""

# create a list
lixt = [1, 34, 6, 8, 9, 24]

# set maximum number = 0
maximum = 0

# loop through list and compare each number to maximum
# set the number as maximum
for number in lixt:
  if number > maximum:
    maximum = number
print(maximum)