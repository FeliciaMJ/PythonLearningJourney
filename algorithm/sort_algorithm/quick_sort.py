import random
from utils.my_logger import logger
from utils.calculate_time import calculate_time


"""
快速排序：
"""


@calculate_time
def quick_sort_recursive(data):
    """

    :param data:
    :return:
    """
    return quick_sort(data, 0, len(data)-1)


def quick_sort(data, left, right):
    """

    :param data:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


def partition(data, left, right):
    """

    :param data:
    :param left:
    :param right:
    :return:
    """
    temp = data[left]
    while left < right:
        while left < right and data[right] >= temp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= temp:
            left += 1
        data[right] = data[left]
    data[left] = temp
    return left


if __name__ == '__main__':
    test_parameter = list(range(9))
    random.shuffle(test_parameter)
    logger().info(test_parameter)
    quick_sort_recursive(test_parameter)
    logger().info(test_parameter)
