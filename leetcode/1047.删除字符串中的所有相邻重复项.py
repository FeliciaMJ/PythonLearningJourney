#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
# class Solution:
#     def removeDuplicates(self, S: str) -> str:
# @lc code=end

def remove_duplicates(S: str) -> str:
    s = list(S)
    stack = []
    i, n = 0, len(s)
    while i < n:
        if not stack or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
        i += 1
    return "".join(stack)

sin = "abbaca"
ans = remove_duplicates(sin)
print(ans)