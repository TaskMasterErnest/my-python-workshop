"""
A program that performs math multiplication operations on matrices
"""

# create matrices
X = [[1, 2], [4, 5], [3, 6]]
Y = [[1, 2, 3, 4], [5, 6, 7, 8]]

# initialize a reult matrix with zero as placeholders
result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# operations to multiply matrices. 
# note that to multiply matrices, no of columns of first matrix = no of rows of second matrix
for i in range(len(X)):
  for j in range(len(Y)):
    # iterating over rows of Y
    for k in range(len(Y)):
      result[i][j] += X[i][k] * Y[k][j]

for r in result:
  print(r)