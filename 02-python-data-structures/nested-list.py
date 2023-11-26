""""
This program is to show how nested data can be worked with (using lists of course)
"""

# write nested list
m = [[1, 2, 3], [4, 5, 6]]

# print data in second row, second column
print(m[1][1])

# using a loop to print all data content
for i in range(len(m)): # loops through all lists,as rows
  for j in range(len(m[i])): # loops through content of list as columns
    print(m[i][j])

# using matrix ways, specifying columns and rows
for row in m:
  for col in row:
    print(col)