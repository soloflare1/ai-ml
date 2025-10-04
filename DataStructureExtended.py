# in python all are classes
# int, float, str, list, tuple, dict, set
# user defined classes
# mutable: list, dict, set
# immutable: int, float, str, tuple
# ordered: list, tuple
# unordered: dict, set
# collection: list, tuple, dict, set
# mapping: dict
# sequential: list, tuple

lst = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)

tpl = (1, 2, 3, 4, 5)
# tpl.append(6) # this will give an error as tuple is immutable
print(tpl)

dic = {'name': 'Naba', 'id': 1, 'name': 'Nosratee'}
dic['id'] = 5 # updating the value of key 'id'
dic['age'] = 25 # adding a new key-value pair
# updating the value of key 'name' will not give an error, but it will update the value
print(dic)


# 1D list
lst2 = [1,2,3, ['naba', 'nosratee', 4.00], 5]
print(lst2)

# 1D list
lst3 = [[1, 2, 3], ['naba', 'nosratee', 4.00], [5],4.00]
print(lst3)

# 2D list
lst4 = [[1, 2, 3], ['naba', 'nosratee', 4.00], [5,6,7], [8,9,10]]
print(lst4)
# but not 
# list4 = [1, 2, 3]['naba', 'nosratee', 4.00] 
# it will give an error as list is not callable

