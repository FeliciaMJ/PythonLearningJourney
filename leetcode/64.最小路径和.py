def min_path_sum(grid) -> int:
    """
    最小路径和
    :param grid:
    :return:
    """
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            elif i == 0:
                grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif j == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j]
            else:
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[-1][-1]


if __name__ == '__main__':
    parameter = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    answer = min_path_sum(parameter)
    print(answer)
