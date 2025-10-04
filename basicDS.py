
# Data types in Python:
    
x = 5
print(type(x))
y = 4.00

s = "Naba"

# sequential data structures
# list (ordered, mutable collection of items)
# list is a collection which is ordered and changeable. Allows duplicate members.
list1 = [1, 2, 3, 4, 5]
print(list1)

# tuple (immutable list)
# once a tuple is created, you cannot change its values (add, remove, or modify
tuple1 = [1, 2, 3, 4, 5]
print(tuple1)

# dictionary : key-value pairs (also unordered),mapping type
# key must be unique and immutable (string, number, or tuple with immutable elements)
# unorder meaning the items do not have a defined order, you cannot refer to an item by index
# you can access the value by referring to its key name

dict1 = {'name': 'Naba', 'id': 1}
print(dict1)

dict2 = {
        'name': 'Nosratee', 
        'id': 5
        }
print(dict2)

# set (unordered collection of unique items)
set1 = {1, 2, 2, 2, 3, 3, 4, 5}
print(set1) # output will be {1, 2, 3, 4, 5} as set do not allow duplicate values

# list is indexed, meaning you can access items by referring to their index number
print(list1[0]) # output will be 1
print(tuple1[0]) # output will be 1
print(dict1['name']) # output will be Naba
# print(set1[0]) # this will give an error as set is unordered and does not support indexing
# you can loop through the set items using a for loop


listx = [1, 2, 3]
tuplex = (1, 2, 3)
dictx = {'name': 'Naba', 'id': 1}
setx = {1, 2, 3}
print(listx, tuplex, dictx, setx)

# type checking
print(type(x), type(y), type(s), type(list1), type(tuple1), type(dict1), type(set1))