def unique_paths(m, n):
    """
    一个机器人位于一个 m x n 网格的左上角,机器人每次只能向下或者向右移动一步。
    :param m:
    :param n:
    :return:
    """
    # dp[i][j]代表走到这个位置共有多少种走法
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    parameter_m = 3
    parameter_n = 7
    answer = unique_paths(parameter_m, parameter_n)
    assert answer == 28
