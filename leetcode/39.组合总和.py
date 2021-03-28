def combination_sum(candidates, target):
    """
    数组总和
    :param candidates:
    :param target:
    :return:
    """

    def dfs(candidates, begin, size, path, res, target):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for index in range(begin, size):
            dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

    size = len(candidates)
    if size == 0:
        return []
    path = []
    res = []
    begin = 0
    dfs(candidates, begin, size, path, res, target)
    return res


if __name__ == '__main__':
    parameters = [2, 3, 6, 7]
    total = 7
    answer = combination_sum(parameters, total)
    print(answer)
