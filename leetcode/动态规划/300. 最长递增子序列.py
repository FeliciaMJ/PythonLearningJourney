def length_of_list(nums):
    """
    给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
    :param nums:
    :return:
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    parameter = [10, 9, 2, 5, 3, 7, 101, 18]
    answer = length_of_list(parameter)
    print(answer)
