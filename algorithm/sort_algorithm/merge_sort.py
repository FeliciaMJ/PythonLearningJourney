from utils.my_logger import logger
from utils.calculate_time import calculate_time


@calculate_time
def merge2list(first, second):
    """
    归并排序
    :param first:
    :param second:
    :return:
    """
    li = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            li.append(first[i])
            i += 1
        else:
            li.append(second[j])
            j += 1
    while i < len(first):
        li.append(first[i])
        i += 1
    while j < len(second):
        li.append(second[j])
        j += 1
    return li


if __name__ == '__main__':
    parameter1 = [1, 2, 3, 4, 5, 6]
    parameter2 = [1, 4, 5, 6, 7, 8]
    logger().info(merge2list(parameter1, parameter2))
