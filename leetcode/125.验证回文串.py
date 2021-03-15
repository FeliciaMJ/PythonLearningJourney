def is_palindrome(s):
    """
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    :param s:
    :return:
    """
    if len(s) < 2:
        return True
    s = s.lower()
    i, n = 0, len(s) - 1
    while i < n:
        # 验证左侧和右侧的是不是字母或者数字，如果不是，需要将指针增加1或者减小1.
        if not s[i].isalnum():
            i += 1
            continue
        if not s[n].isalnum():
            n -= 1
            continue
        if s[i] == s[n]:
            i += 1
            n -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    parameter = "A man, a plan, a canal: Panama"
    answer = is_palindrome(parameter)
    print(answer)
