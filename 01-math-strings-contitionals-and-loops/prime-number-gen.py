"""
A tiny program to get the prime numbers between a certain range
"""

# get numbers
print("Enter first number:")
num_1 = abs(int(input()))
print("Enter second number: ")
num_2 = abs(int(input()))

# loop through range and get primes
for num in range(num_1, num_2):
  if num % 2 == 0:
    continue
  if num % 3 == 0:
    continue
  if num % 5 == 0:
    continue
  if num % 7 == 0:
    continue
  print(num)