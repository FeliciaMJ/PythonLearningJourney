def length_of_longest_sub_string(s):
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    :param s:
    :return:
    """
    # 滑动窗口+hash表
    hashmap = {}
    left = max_len = 0
    for i, c in enumerate(s):
        if c in hashmap:
            left = max(left, hashmap[c] + 1)
        hashmap[c] = i
        max_len = max(max_len, i - left + 1)
    return max_len


def length_of_longest_sub_string2(s):
    s = list(s)
    max_len = 0
    i = 0
    n = len(s)
    temp = []
    while i < n:
        if s[i] not in temp:
            temp.append(s[i])
        else:
            while temp[0] != s[i]:
                temp.pop(0)
            temp.pop(0)
            temp.append(s[i])
        max_len = max(max_len, len(temp))
        i += 1
    return max_len


if __name__ == '__main__':
    parameter = "pwwkew"
    answer = length_of_longest_sub_string(parameter)
    print(answer)
