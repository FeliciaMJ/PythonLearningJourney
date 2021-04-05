class MyDataWithMethod(object):
    def printFoo(self):
        print("you invoked printFoo()")


md = MyDataWithMethod()
md.printFoo()


class AddrBookEntry(object):
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print("Created instance for : ", self.name)

    def update_phone(self, newph):
        self.phone = newph
        print("Updated phone # for : ", self.name)


ab = AddrBookEntry("iphone11", "123")
ab.update_phone("234")


class EmplAddrBookEntry(AddrBookEntry):
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def update_email(self, newem):
        self.email = newem
        print("Updated e-mail address for: ", self.name)


john = EmplAddrBookEntry("John", "408-555-1212", 42, "john@spam.doe")
print(john.phone)
print(john)
print(john.name)
john.update_phone("123-555-1212")
print(john.phone)

# 考虑用OOD来工作的一个最重要的原因，在于它直接提供建模和解决现实世界问题和情形的途径。
# Person类->消费者、技工、出纳员
# RepairShop 的参与者。
"""
抽象：指对现实世界问题和实体的本质表现、行为和特征建模。
类通常在一个模块的顶层进行定义，以便类实例能够在类定义的源代码文件中的任何地方被创建。

"""


class Demo2(object):
    # my_version = 1.1
    """
    这个是类的文档字符串。
    """
    def func(self):
        pass

    def funce(self):
        raise NotImplementedError("这个方法没有实现")


print(Demo2.__dict__)
print(dir(Demo2))
print(dir(Demo2) == Demo2.__dict__)
print(vars(Demo2))
demo = Demo2()
print(Demo2.__name__)
print(Demo2.__doc__)
print(Demo2.__module__)
