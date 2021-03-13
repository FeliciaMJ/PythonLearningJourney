from utils.my_logger import logger
from utils.calculate_time import calculate_time
import random


@calculate_time
def insert_sort(array):
    """
    插入排序。
    :param array:
    :return:
    """
    # [3, 2, 1, 4, 5, 6]
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        # 当前的数比前面的数小。
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp


if __name__ == '__main__':
    test_parameter = list(range(9))
    random.shuffle(test_parameter)
    logger().info(test_parameter)
    insert_sort(test_parameter)
    logger().info(test_parameter)
