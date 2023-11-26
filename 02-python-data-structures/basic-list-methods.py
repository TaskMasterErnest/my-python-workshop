"""
A bunch of liste methods to call and perform operations on lists
"""

# getting length using the len() method
shopping_list = ["bread", "apple", "eggs"]

# get length
print(len(shopping_list))

# concatenating lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = ["oi"]
final_list = list_1 + list_2
print(final_list)
print(list_3 * 3)


# accessing an item from a list
print(shopping_list[1])
# access item and replace it
shopping_list[1] = "banana"
print(shopping_list)
# more accessing
print(shopping_list[-1])
# access to the third item
print(shopping_list[:3])
# access from second element to the end
print(shopping_list[1:])


# adding an item to a list
shopping_list.append("shampoo")
print(shopping_list)

# using insert to add items into a particular position in the list
shopping_list.insert(2, "biscuit")
print(shopping_list)