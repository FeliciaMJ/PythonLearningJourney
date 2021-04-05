"""
装饰器是Python的一个重要部分。
装饰器是修改其他函数功能的函数。
一切皆对象。
p46
"""


def hi(name="yahoo"):
    return "hi " + name


print(hi())

# 我们甚至可以将一个函数赋值给以便变量。
# 这里没有使用小括号，因此不是在调用hi函数
# 而是在将他放在greet变量里面。
greet = hi
print(greet())

"""
在函数中定义函数。
在Python中可以在一个函数中定义另一个函数。
"""


def hi2():
    print("now you are inside the hi2() function.")

    def greet2():
        return "now you are in the greet2() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet2())
    print(welcome())
    print("now you are back in the hi2() function")


hi2()

"""
函数中可以返回函数。
其实并不需要在一个函数里去执行另一个函数，我们可以将其作为输出返回出来。
"""


def hi3(name="hello"):

    def greet2():
        return "now you are in the greet2() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "hello":
        # 在这里返回的是greet2好welcome而不是greet2（）和welcome（）
        # 这是因为当你把小括号放在后面，这个函数就会执行；
        # 如果不放括号在后面，它可以被到处传递，并且可以复制给别的变量而不去执行它。
        return greet2
    else:
        return welcome


a = hi3(name="world")
print(a)
print(a())


"""
将函数作为参数传递给另一个参数。
"""


def do_something_before_hi(func):
    print("I am doing some boring work before executing hi()...")
    print(func())


do_something_before_hi(hi)


"""
第一个装饰器
"""


def a_new_decorator(a_func):

    def wrap_the_function():
        print("I am doing some boring work before executing a_func")

        a_func()

        print("I am doing some boring work after executing a_func")

    return wrap_the_function


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove")


a_function_requiring_decoration()

ab = a_new_decorator(a_function_requiring_decoration)
ab()


@a_new_decorator
def second():
    print("............")


second()

