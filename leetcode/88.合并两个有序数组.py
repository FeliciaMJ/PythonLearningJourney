def merge(nums1, nums2):
    """
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
    :param nums1:
    :param nums2:
    :return:
    """
    n1 = len(nums1)
    n2 = len(nums2)
    i, j = 0, 0
    answer = []
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            answer.append(nums1[i])
            i += 1
        else:
            answer.append(nums2[j])
            j += 1
    while i < n1:
        answer.append(nums1[i])
        i += 1
    while j < n2:
        answer.append((nums2[j]))
        j += 1
    return answer


def merge2(nums1, m, nums2, n):
    """
    本地修改，从nums1的后面开始进行判断。
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """

    i, j, k = m-1, n-1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    # 无论是nums1有剩余还是nums2有剩余都进行判断。
    while i >= 0:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


if __name__ == '__main__':
    parameter1 = [1, 3, 5, 0, 0, 0]
    parameter2 = [2, 4, 6]
    merge2(parameter1, 3, parameter2, 3)
    print(parameter1)
