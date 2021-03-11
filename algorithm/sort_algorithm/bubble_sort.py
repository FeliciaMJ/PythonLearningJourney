from utils.calculate_time import calculate_time
from utils.my_logger import logger
import random


"""
冒泡排序：最坏情况下时间复杂度是O(n^2)
"""


@calculate_time
def bubble(array):
    """
    冒泡排序
    :param array:
    :return:
    """
    # 比较的趟数
    for i in range(len(array)-1):
        # 每趟比较的次数
        for j in range(len(array)-1-i):
            # 进行元素交换
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


@calculate_time
def bubble_optimizer(array):
    """
    冒泡排序的优化，通过判断某一趟中是否有元素交换，若没有，说明已经排好序，退出循环。
    :param array:
    :return:
    """
    for i in range(len(array)-1):
        exchange = False
        for j in range(len(array)-1-i):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                exchange = True
        if not exchange:
            return 


if __name__ == '__main__':
    test_parameter = list(range(9))
    random.shuffle(test_parameter)
    logger().info(test_parameter)
    bubble(test_parameter)
    logger().info(test_parameter)