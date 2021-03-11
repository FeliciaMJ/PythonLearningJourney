from utils.calculate_time import calculate_time
from utils.my_logger import logger


"""
二分查找:就是将查找的键和数组的中间值作比较，如果被查找的键小于中间值，就在左子数组继续查找；如果大于中间键，就在右子数组中查找，否则中间值就是要找的元素。

注意：代码中的判断条件必须是while (left <= right)，否则的话判断条件不完整，
比如：array[3] = {1, 3, 5};待查找的键为5，此时在(low < high)条件下就会找不到，因为low和high相等时，指向元素5，但是此时条件不成立，没有进入while()中。

二分查找的变种：
    二分查找的变种和二分查找的原理一样，主要是交换判断条件（也就是边界条件）。
    例如：数组之中的数据可能重复，要求返回匹配的数据的最小（或最大）下标；
    需要找出数组中第一个大于key的元素（也就是最小的大于key的元素）的下标等等。

"""


@calculate_time
def binary_search(in_list, target):
    """
    二分查找函数，要求输入的数组必需是有序的。
    :param target:
    :param in_list:
    :return:
    """
    left = 0
    right = len(in_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if in_list[middle] > target:
            right -= 1
        elif in_list[middle] < target:
            left += 1
        else:
            return middle

    return -1


@calculate_time
def test_recursive(in_list, target):
    """
    递归函数，函数运行时间的测试，就是在外面添加一个马甲而已。
    :param in_list:
    :param target:
    :return:
    """
    return binary_search_recursive(in_list, target)


def binary_search_recursive(in_list, target):
    """
    二分查找的递归写法。
    :param in_list:
    :param target:
    :return:
    """
    left = 0
    right = len(in_list) - 1
    middle = (left + right) // 2
    while len(in_list) > 0:
        if in_list[middle] == target:
            # TODO 这里传递的是0，存在index失真的问题，需要解决。
            # return middle
            return True
        elif in_list[middle] < target:
            return binary_search_recursive(in_list[middle + 1:], target)
        else:
            return binary_search_recursive(in_list[: middle], target)
    return False


def binary_search_recursive_todo(in_list, target, left, right):
    """
    解决上面的TODO问题
    :param in_list:
    :param target:
    :param left:
    :param right:
    :return:
    """
    if left <= right:
        middle = (left + right) // 2
        if in_list[middle] == target:
            return middle
        elif in_list[middle] > target:
            return binary_search_recursive_todo(in_list, target, left, middle - 1)
        else:
            return binary_search_recursive_todo(in_list, target, middle + 1, right)
    else:
        return


@calculate_time
def search_first_number(in_list, target):
    """
    查找重复数中的第一个数，数组是排好序的。
    :param in_list:
    :param target:
    :return:
    """
    left = 0
    right = len(in_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if in_list[middle] < target:
            left += 1
        else:
            right -= 1
    return left


@calculate_time
def search_last_number(in_list, target):
    """
    查找重复数中的最后一个数，数组是排好序的。
    :param in_list:
    :param target:
    :return:
    """
    left = 0
    right = len(in_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if in_list[middle] <= target:
            left += 1
        else:
            right -= 1
    return right


if __name__ == '__main__':
    parameter = [i for i in range(9)]
    logger().info(parameter)
    need = 6
    answer = binary_search_recursive_todo(parameter, need, 0, len(parameter))
    logger().info(answer)

    test_second = [1, 2, 3, 3, 3, 3, 4, 5]
    num = 3
    answer_second = search_first_number(test_second, num)
    logger().info(answer_second)

    answer_third = search_last_number(test_second, num)
    logger().info(answer_third)
