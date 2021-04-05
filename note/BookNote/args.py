"""
*args 和 *kwargs 主要用于函数的定义。将不定数量的参数传递给一个函数。
这里的不定，是预先并不知道函数使用者会传递多少个参数给你，这种场景需要使用这两个关键字。
标准参数与*args, **kwargs在使用时的顺序：
    some_func(frags, *args, **kwargs)
"""


def test_var_args(f_arg, *args):
    """ *args 用来发送一个非键值对的可变数量的参数列表给一个函数。"""
    print("first normal arg :", f_arg)
    for arg in args:
        print("another arg through *args : ", arg)


test_var_args("yahoo", "python", "eggs", "test")


def greet_me(**kwargs):
    """ **kwargs 允许你将不定长度的键值对，作为参数传递给一个函数。"""
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


greet_me(name="yahoo")


def test_args_kwargs(arg1, arg2, arg3):
    """

    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    """
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# args = ("two", 3, 5)
args = ["two", 3, 5]
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
