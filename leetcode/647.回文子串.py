def count_substrings(s: str) -> int:
    """
    给定一个字符串，计算这个字符串中有多少个回文子串。
    :param s:
    :return:
    """
    n = len(s)
    count = 0
    dp = [[False] * n for _ in range(n)]
    for j in range(n):
        for i in range(0, j + 1):
            length = j - i + 1
            if length == 1:
                dp[i][j] = True
                count += 1
            if length == 2 and s[i] == s[j]:
                dp[i][j] = True
                count += 1
            if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                dp[i][j] = True
                count += 1
    return count


if __name__ == '__main__':
    parameter = "aaa"
    answer = count_substrings(parameter)
    print(answer)
