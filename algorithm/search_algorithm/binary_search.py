from utils.calculate_time import calculate_time


@calculate_time
def binary_search(in_list, target):
    """
    二分查找函数，要求输入的数组必需是有序的。
    :param target:
    :param in_list:
    :return:
    """
    left = 0
    right = len(in_list)
    while left < right:
        middle = (left + right) // 2
        if in_list[middle] > target:
            right -= 1
        elif in_list[middle] < target:
            left += 1
        else:
            return middle

    return -1


if __name__ == '__main__':
    parameter = [i for i in range(9)]
    print(parameter)
    need = 6
    answer = binary_search(parameter, need)
    print(answer)

