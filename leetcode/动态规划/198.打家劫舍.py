def rob(nums) -> int:
    """
    打家劫舍问题
    :param nums:
    :return:
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]


if __name__ == '__main__':
    parameter = [1, 2, 3, 1]
    answer = rob(parameter)
    print(answer)
