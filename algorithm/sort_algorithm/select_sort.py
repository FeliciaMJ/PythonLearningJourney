from utils.calculate_time import calculate_time
from utils.my_logger import logger
import random


@calculate_time
def select_sort(array):
    """

    :param array:
    :return:
    """
    for i in range(len(array)):
        init_loc = i
        for j in range(i + 1, len(array)):
            if array[init_loc] > array[j]:
                init_loc = j
        if init_loc != i:
            array[i], array[init_loc] = array[init_loc], array[i]


if __name__ == '__main__':
    test_parameter = list(range(9))
    logger().info(test_parameter)
    random.shuffle(test_parameter)
    logger().info(test_parameter)
    select_sort(test_parameter)
    logger().info(test_parameter)
