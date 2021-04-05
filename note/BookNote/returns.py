def add(value1, value2):
    # 把值赋给了调用它的变量。
    return value1 + value2


result = add(3, 5)
print(result)


def add2(value1, value2):
    global result
    result = value1 + value2


"""
其实这个就是作用域的问题理解。
return返回的变量是局部变量，而在函数内部的局部变量通过global声明之后，变成全局变量，在任何位置都可以访问了。
在实际编程中，应该避开使用global关键字，他会让生活变得艰难，因为它引入了多余的变量到全局作用域。

"""

add2(3, 5)
print(result)
add2(2, 4)
print(result)


def profile():
    global name
    global age
    name = "Danny"
    age = 30


def profile2():
    name = "Danny"
    age = 30
    return name, age

profile()
print(name)

profile_data = profile2()
print(profile_data[0])
