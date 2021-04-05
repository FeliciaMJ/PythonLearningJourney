"""
Map 会将一个函数映射到一个输入列表的所有元素上。
map(function_to_apply, list_of_inputs)
"""
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)
# 大多数情况下，使用匿名函数来配合map，可以这样做。
map_squared = list(map(lambda x: x**2, items))
print(map_squared)


def multiply(x):
    return x*x


def add(x):
    return x + x


# 不经作用于一列表输入，甚至可以作用于一列表的函数。
funcs = [multiply, add]

for i in range(5):
    # x代表funcs中的元素，通过()变成函数，将这个函数作用于i
    value = map(lambda x: x(i), funcs)
    print(list(value))


"""
filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表。

"""

number_list = list(range(-5, 5))
less_than_zero = filter(lambda x: x < 0, number_list)
# python3返回的是迭代器，需要通过list方法转换一下。
print(list(less_than_zero))


"""
reduce：当需要对一个列表进行一些计算并返回结果时，reduce是一个非常有用的函数。
"""
from functools import reduce

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)