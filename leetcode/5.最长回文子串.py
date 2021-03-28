def longest_palindrome(s: str) -> str:
    """

    :param s:
    :return:
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = ""
    for k in range(n):
        for i in range(n):
            j = i + k
            if j >= len(s):
                break
            if k == 0:
                dp[i][j] = True
            elif k == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and k + 1 > len(ans):
                ans = s[i: j + 1]
    return ans


def count_sub_string(s):
    """

    :param s:
    :return:
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for i in range(0, j + 1):
            length = j - i + 1
            if length == 1:
                dp[i][j] = True
                count += 1
            if length == 2 and s[i] == s[j]:
                dp[i][j] = True
                count += 1
            if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                dp[i][j] = True
                count += 1
    return count


if __name__ == '__main__':
    parameter = "babad"
    answer = count_sub_string(parameter)
    print(answer)
