"""
A program to determine is a number is a perfect square 
ie. if a value is multiplied by the teh same value, will it give the number provided by the user?
"""

# get input value from user
print("Enter a number to check if it is a perfect square.")
number = input()

# enforce number to be an positive number only
number = abs(int(number))

# select iterator
i = -1
# initialize the square value to be false
square = False

# start loop
while i <= number**(0.5):
  i += 1
  # check if number is the square root of number
  if i * i == number:
    square = True
    break

# print results
if square:
  print("The square root of {} is {}".format(number, i))
else:
  print("{} is not a perfect square".format(number))
