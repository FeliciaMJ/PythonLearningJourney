"""
set:是一个非常有用的数据结构，它与列表的行为类似，区别在于set不能包含重复的值。

"""
some_list = ["a", "b", "c", "d", "b", "m", "n", "n"]
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

set_duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(set_duplicates)

"""
交集
"""
valid = {"yellow", "red", "blue", "green", "black"}
input_set = {"red", "brown"}
print(input_set.intersection(valid))

"""
差集:相当于用一个集合减去另一个集合的数据。
"""
print(input_set.difference(valid))
