"""
An introduction to zipping and using the zip() method.
"""

# create separate lists
items = ["sugar", "milk", "cookies"]
quantity = [3, 5, 6]

# zip them together to combine them
groceries = zip(items, quantity)
print(groceries) # this creates the new list in memory and tells us

# turn the result in to a list
print(list(groceries))

# make it a tuple
groceries = zip(items, quantity)
print(tuple(groceries))

# make it a dictionary
groceries = zip(items, quantity)
print(dict(groceries))