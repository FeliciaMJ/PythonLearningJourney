#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
# @lc code=end

def find_sub_string(s, words):
    step = len(words[0])
    current = 0
    n = len(s)
    seen = set()
    ans = []
    while current < n:
        tmp = s[current: current + step]
        if tmp in words and tmp not in seen:
            seen.add(tmp)
            # current += step
        if len(seen) == len(words):
            ans.append(current-step)
            seen = set()
        current += step
    return ans


give = "barfoothefoobarman"
gi = ["foo", "bar"]

res = find_sub_string(give, gi)
print(res)