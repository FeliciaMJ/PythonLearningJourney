"""
在Python中，每个类都有实例属性。默认情况下Python用一个字典来保持一个对象的实例属性。
这非常有用，因为它允许我们在运行时去设置任意的新属性。

"""


class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class MySecondClass(object):
    __slots__ = ["name", "identifier"]

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


# 第二种写法会为你的内存减轻负担。通过这个技巧，内存占用率几乎40~50%的减少。
