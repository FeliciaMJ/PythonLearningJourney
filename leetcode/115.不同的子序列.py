def num_distinct(s, t):
    """
    给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
    :param s:
    :param t:
    :return:
    """
    n1 = len(s)
    n2 = len(t)
    # dp[i][j]代表t的前i字符串可以由sj字符串组成最多个数。
    dp = [[0]*(n1 + 1) for _ in range(n2 + 1)]
    for j in range(n1 + 1):
        dp[0][j] = 1
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    parameter1 = "rabbbit"
    parameter2 = "rabbit"
    answer = num_distinct(parameter1, parameter2)
    print(answer)