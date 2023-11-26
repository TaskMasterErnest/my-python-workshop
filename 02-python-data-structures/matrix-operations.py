"""
A program that performs math operations on matrices
"""

# create matrices
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# initialize a reult matrix with zero as placeholders
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate over the rows and columns and perform addition
for i in range(len(X)):
  for j in range(len(Y)):
    result[i][j] = X[i][j] + Y[i][j]
print("Addtion result: {}".format(result))

# iterate over the rows and columns and perform subtraction
for i in range(len(X)):
  for j in range(len(Y)):
    result[i][j] = X[i][j] - Y[i][j]
print("Subtraction result: {}".format(result))