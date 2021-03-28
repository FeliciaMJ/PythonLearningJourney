def climb_stairs(n: int) -> int:
    """
    爬楼梯问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    :param n:
    :return:
    """
    if n <= 2:
        return n
    # 1.dp[i] 跳上一个i级的台阶总共有dp[i]中跳法。
    dp = [0] * n
    # 找出初始条件。
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        # 2.由于情况可以选择跳一级，也可以选择跳两级，所以青蛙到达第 n 级的台阶有两种方式
        # 一种是从第n-1级跳上来
        # 一种是从第n-2级跳上来
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


if __name__ == '__main__':
    parameter = 10
    answer = climb_stairs(parameter)
    print(answer)
