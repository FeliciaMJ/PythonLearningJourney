def max_area(height) -> int:
    """
    盛最多水的容器
    :param height:
    :return:
    """
    left = 0
    right = len(height) - 1
    water = 0
    while left < right:
        if height[left] < height[right]:
            water = max(water, height[left] * (right - left))
            left += 1
        else:
            water = max(water, height[right] * (right - left))
            right -= 1
    return water


if __name__ == '__main__':
    parameter = [1,8,6,2,5,4,8,3,7]
    answer = max_area(parameter)
    print(answer)
