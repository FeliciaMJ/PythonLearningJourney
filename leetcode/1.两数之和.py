def two_sum(nums, target):
    """
    两数之和
    :param nums:
    :param target:
    :return:
    """
    temp = {}
    for i in range(len(nums)):
        if target - nums[i] not in temp:
            temp[nums[i]] = i
        else:
            return [temp[target - nums[i]], i]


if __name__ == '__main__':
    parameter = [1, 2, 4, 5, 7, 12, 8]
    answer = two_sum(parameter, 14)
    print(answer)
