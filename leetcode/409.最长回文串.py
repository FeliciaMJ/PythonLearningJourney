def longest_palindrome(s: str) -> str:
    """
    中心扩展法
    :param s:
    :return:
    """
    res = ''
    for i in range(len(s)):
        s1 = find(s, i, i)  # 以当前字符为中心的最长回文子串（假设长度为奇数）
        s2 = find(s, i, i + 1)  # 以当前字符和下一字符为中心的最长回文子串（假设长度为偶数）
        res = s1 if len(res) < len(s1) else res
        res = s2 if len(res) < len(s2) else res
    return res


def find(s, left, right):
    """找到串s中，以left、right为中心的最长回文串"""
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
