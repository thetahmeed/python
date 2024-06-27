list = ['a', 'b', 'c', 'd', 'e']

# Accessing values in a list
print(list[0])  # a

# Accessing values in a list using negative index
print(list[-1])  # e (-1 = last item)

# Accessing values in a list using range
print(list[1:3])  # ['b', 'c'] (index 1 to 3)

# Accessing values in a list using range
print(list[2:])  # ['c', 'd', 'e'] (index 2 to end)

# Accessing values in a list using range
print(list[:2])  # ['a', 'b'] (start to index 2)

# Existance of an item in a list
if 'a' in list:
    print('a exists in list')  # a exists in list

# change value in a list
list[0] = 'z'

# Add an item to the end of the list
list.append('f')

# Add an item at a specific index
list.insert(1, 'x')

# Remove an item from the list
list.remove('x')

# Remove an item from the list using index
list.pop(1) # remove item at index 1

# remove all items from the list
list.clear()

# extend a list
list.extend(['g', 'h'])

# list length
print(len(list))  # 2

# list iteration
for item in list:
    print(item)

# list comprehension # expression for item in iterable if condition == True
list = [x for x in range(10)]
print(list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list comprehension with condition
list = [x for x in range(10) if x % 2 == 0]
print(list)  # [0, 2, 4, 6, 8]

# list comprehension with condition
list = [x if x % 2 == 0 else 'odd' for x in range(10)]

# list comprehension with nested loop
list = [(x, y) for x in range(3) for y in range(3)]
print(list)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# list comprehension with nested loop
list = [[(x, y) for x in range(3)] for y in range(3)]
print(list)  # [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]

# sort a list
list = [3, 2, 1]
list.sort()
print(list)  # [1, 2, 3]

# sort a list in reverse
list = [3, 2, 1]
list.sort(reverse=True)
print(list)  # [3, 2, 1]

# custom sort
list = ['apple', 'banana', 'cherry']
list.sort(key=lambda x: len(x)) # sort by length
print(list)  # ['apple', 'banana', 'cherry']

# custom sort
list = ['apple', 'banana', 'cherry']
list.sort(key=lambda x: x[1]) # sort by second character

# lambda = anonymous function, x is the argument, len(x) is the expression
# lambda x: len(x) is equivalent to def f(x): return len(x)
# lambda x: x[1] is equivalent to def f(x): return x[1]

# we can use key = str.lower to sort case-insensitive
# we can use key = str.upper to sort case-insensitive

# reverse a list
list = [1, 2, 3]
list.reverse()
print(list)  # [3, 2, 1]

# copy a list
list1 = [1, 2, 3]
list2 = list1.copy()
# or list2 = list(list1)

# join a list
list = ['a', 'b', 'c']
print(''.join(list))  # abc
print(', '.join(list))  # a, b, c

# split a string into a list
string = 'a b c'
list = string.split(' ')
print(list)  # ['a', 'b', 'c']

# join two list
list1 = ['a', 'b']
list2 = ['c', 'd']
list = list1 + list2
print(list)  # ['a', 'b', 'c', 'd']

# join two list
list1 = ['a', 'b']
list2 = ['c', 'd']
list1.extend(list2)
print(list1)  # ['a', 'b', 'c', 'd']