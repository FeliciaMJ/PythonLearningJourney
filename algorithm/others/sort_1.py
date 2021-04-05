def sort_array(array):
    """
    删除重复元素。例如[1, 2, 2, 2, 3, 5, 5, 8] ->[1, 2, 3, 5, 8]
    :param array:
    :return:
    """
    i, j = 0, 0
    n = len(array)
    while j < n-1:
        if array[j] != array[j+1]:
            array[i+1] = array[j+1]
            i += 1
        j += 1
    return array


if __name__ == '__main__':
    parameter = [1, 2, 2, 2, 3, 5, 5, 8]
    answer = sort_array(parameter)
    print(answer)