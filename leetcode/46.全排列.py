def permute(nums):
    """
    全排列,采用回溯法。
    :param nums:
    :return:
    """

    def dfs(nums, size, depth, path, used, res):
        if depth == size:
            res.append(path[:])
            return

        for i in range(size):
            if not used[i]:
                """
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                """
                used[i] = True
                path.append(nums[i])

                dfs(nums, size, depth + 1, path, used, res)

                used[i] = False
                path.pop()

    # nums.sort()  # 如果判断是否重复的时候需要先进行排序。
    size = len(nums)
    if len(nums) == 0:
        return []

    used = [False for _ in range(size)]
    res = []
    dfs(nums, size, 0, [], used, res)
    return res
                

if __name__ == '__main__':
    parameters = [1, 2, 3]
    res = permute(parameters)
    print(res)
