def sort_array(array):
    temp = [0] * 1001
    for i in array:
        temp[i] += 1
    # print(temp)
    res = []
    for i in range(len(temp)-1, -1, -1):
        if temp[i] == 0:
            continue
        for _ in range(temp[i]):
            res.append(i)
    print(res)


def sort_array2(array):
    """
    [5, 3, 1]
    :param array:
    :return:
    """
    n = len(array)
    # 一共有n个数，需要比较n-1趟。
    for i in range(n-1):
        # 每趟之后最后的数是最大的数，变成有序区。
        for j in range(n - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def sort_array3(array, left, right):
    """

    :param array:
    :param left:
    :param right:
    :return:
    """
    while left < right:
        mid = partition(array, left, right)
        sort_array3(array, left, mid - 1)
        sort_array3(array, mid + 1, right)


def partition(array, left, right):
    tmp = array[left]
    while left < right:
        while left < right and tmp <= array[right]:
            right -= 1
        array[left] = array[right]
        while left < right and tmp >= array[left]:
            left += 1
        array[right] = array[left]
    array[left] = tmp
    return array[left]


def middle(array, left, right):
    tmp = array[left]
    while left < right:
        while left < right and array[right] >= tmp:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= tmp:
            left += 1
        array[right] = array[left]
    array[left] = tmp
    return array


def tong_sort(array):
    res = []
    tmp = [0] * 501
    for i in array:
        tmp[i] += 1
    for index, value in enumerate(tmp):
        if value == 0:
            continue
        res.append(index)
    return res


def delete_repeat(array):
    for i in range(len(array)):
        for j in range(len(array)-i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def second_step(array):
    i, j = 0, 0
    while j < len(array) - 1:
        if array[j] != array[j + 1]:
            array[i] = array[j]
            i += 1
        j += 1


def get_code(array):
    res = []
    for i in range(len(array)):
        pass




if __name__ == '__main__':
    # parameter = [8, 100, 50, 22, 15, 6, 1, 1000, 999, 0]
    parameter = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    # print(middle(parameter, 0, len(parameter)-1))
    # 1. 先去重，再排序
    # 2. 先排序，再去重
    parameter2 = [20, 40, 32, 67, 40, 20, 89, 300, 400, 15]
    # answer = tong_sort(parameter2)
    # print(answer)
    answer2 = delete_repeat(parameter2)
    print(answer2)
    second_step(answer2)
    print(answer2)
    code = [6, 3, 1, 7, 5, 8, 9, 2, 4]
