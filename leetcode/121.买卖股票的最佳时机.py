def max_profit(price):
    """
    买卖股票的最佳时机
    :param price:
    :return:
    """
    # dp【i】表示前i天的最大利润
    n = len(price)
    if n == 0:
        return 0
    dp = [0] * n
    min_price = price[0]

    for i in range(n):
        min_price = min(min_price, price[i])
        dp[i] = max(dp[i-1], price[i] - min_price)
    return dp[-1]


if __name__ == '__main__':
    parameter = [1, 5, 3, 4, 6, 2]
    answer = max_profit(parameter)
    print(answer)