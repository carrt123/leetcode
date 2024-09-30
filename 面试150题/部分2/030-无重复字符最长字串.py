class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()
        l = res = 0
        for r, v in enumerate(s):

            while v in w:
                w.remove(s[l])
                l += 1
            w.add(v)
            res = max(res, r - l + 1)
        return res
