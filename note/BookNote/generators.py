"""
可迭代对象(Iterable)
    只要定义了可以返回一个迭代器的__iter__方法，或者定义可以支持下标索引的__getitem__方法，那么就是一个可迭代对象。
    简单说，可迭代对象就是能提供迭代器的任何对象。
迭代器(Iterator)
    只要定义了__next__方法，就是一个迭代器。
迭代(Iteration)
    简单说，就是从某个地方(如列表)取出一个元素的过程。
    当我们使用一个循环来遍历某个东西时，这个过程本身就是迭代。
生成器：
    生成器也是一种迭代器，但是你只能对其迭代一次。因为它没有把所有的值存在内存中而是在运行时生成值。
    大多数时候生成器是以函数来实现的，它并不返回一个值，而是yield一个值。
"""


def generator_function():
    for i in range(4):
        yield i


gen = generator_function()
print(next(gen))
print("@@@@@@@@@")
print(next(gen))
print("@@@@@@@@@@@")
print(next(gen))
print("@@@@@@@@@")
print(next(gen))
print("@@@@@@@@@@@")

for item in generator_function():
    print(item)


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in fibon(10):
    print(x)


def fibon2(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


my_string = "yahoo"
my_iter = iter(my_string)
print(next(my_iter))