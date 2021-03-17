def climb_stairs(n: int) -> int:
    """
    爬楼梯问题
    :param n:
    :return:
    """
    if n <= 2:
        return n
    # dp[i] 代表爬到第i级台阶的方案数。
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


if __name__ == '__main__':
    parameter = 10
    answer = climb_stairs(parameter)
    print(answer)
