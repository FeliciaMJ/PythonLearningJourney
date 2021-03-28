#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
# @lc code=end

def min_window(s, t):
    t = set(list(t))
    n = len(s)
    seen = set()
    ans = []
    start, i = 0, 0
    while i < n:
        if s[i] in t:
            seen.add(s[i])
        if not (t-seen):
            ans.append(s[start:i+1])
            start += i+1
        i += 1
    return ans


s = "ADOBECODEBANC"
t = "ABC"
res = min_window(s, t)
print(res)






