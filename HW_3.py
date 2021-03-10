# 1. Define the id of next variables
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# String formatting:
# 5. With .format and curly braces {}
print('Anna has {} apples and {} peaches'.format(5, 7))
# 6. By passing index numbers into the curly braces.
print('Anna has {0} apples and {1} peaches'.format(5, 7))
# 7. By using keyword arguments into the curly braces.
print("Anna has {apple} apples and {peach} peaches".format(apple = 5, peach = 6))
# 8. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches".format(3, 5))
# 9. With f-strings and variables
m = 5
c = 6
print(f"Anna has {m} apples and {c} peaches")
# 10. With % operator
m = 7
p = 9
print(f"Anna has %s apples and %s peaches" % (m, p))
# 11. With variable substitutions by name (hint: by using dict)
apples = 5
peaches = 8
data_dict = {"a": apples, 'p': peaches}
print("Anna has %(a)s apples and %(p)s peaches" % data_dict)
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#    if num % 2 == 1:
#       lst.append(num ** 2)
#    else:
#        lst.append(num ** 4)
# print(lst)
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# 12. Convert (1) to list comprehension
lst = [num ** 2 if num % 2 == 1 else num ** 1 for num in range(10)]
print(lst)
# 13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

#(3)
#d = {}
#for num in range(1, 11):
#    if num % 2 == 1:
#        d[num] = num ** 2
#print(d)

# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# 14. Convert (3) to dict comprehension.
dict_c3 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_c3)
# 15. Convert (4) to dict comprehension.
dict_c4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_c4)
# 16. Convert (5) to regular for with if.
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
d = {}
for x in range(10):
    if x**3 % 4 == 0:
       d[x] = x ** 3
print(d)

# 17*. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)
# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
# 18. Convert (7) to lambda function
foo_1 = lambda x, y: x if x < y else y
print(foo_1(8, 4))
# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(5, 9 , 25))

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_a = list(map(lambda x: x*2, lst_to_sort))
print(lst_a)
print(sorted(lst_a))
# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_AB = list(map(pow, list_A, list_B))
print(list_AB)
# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
from functools import reduce
lst_sum = reduce(lambda x, y: x + y, lst_to_sort)
print(lst_sum)
# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_f = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_f)
# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
ad = list(filter(lambda m: (m<0), b))
print(ad)
# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)



