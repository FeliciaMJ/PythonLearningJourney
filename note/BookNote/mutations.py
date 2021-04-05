"""
python 中可变（mutable）与不可变（immutable）的数据类型让新手很是头痛。


"""

foo = ["hi"]
print(foo)

bar = foo
bar += ["bye"]
print(foo)

# 这是对象可变性在作怪。每当你将一个变量赋值为另一个可变类型的变量时，
# 对这个数据的任意改动会同时反映到这两个变量上去。
# 新变量只不过是老变量的一个别名而已。


def add_to(num, target=[]):
    # 在python中当函数被定义时，默认参数只会运算一次，而不是每次调用时都会重新运算。
    # 应该永远不要定义可变类型的默认参数。
    target.append(num)
    return target


def add_2(element, target=None):
    if not target:
        target = []
    target.append(element)
    return target


print(add_to(1))
print(add_to(2))
print(add_to(3))

print(add_2(1))
print(add_2(2))
print(add_2(3))