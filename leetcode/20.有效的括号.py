def is_valid(s: str) -> bool:
    """
    判断一个字符串中的括号是否匹配。
    :param s
    :return:
    """

    temp = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for bracket in s:
        if bracket in temp:
            stack.append(bracket)
        else:
            if stack and bracket == temp.get(stack[-1]):
                stack.pop()
            else:
                return False
    return not stack


if __name__ == '__main__':
    brackets = "]"
    print(is_valid(brackets))
