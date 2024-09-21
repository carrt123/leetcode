# author:Carrt
# date:2024-03-23
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # 将第一个字符串作为基准
        prefix = strs[0]
        for i in range(1, len(strs)):
            # 比较基准字符串和当前字符串的公共前缀
            while strs[i].find(prefix) != 0:
                # 如果当前字符串不包含基准字符串，则缩短基准字符串
                prefix = prefix[:-1]
                # 如果基准字符串缩短为空，则没有公共前缀
                if prefix == "":
                    return ""
        return prefix

    # 分治
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def lcp(start, end):
            if start == end:
                return strs[start]
            mid = (start+end) // 2

            left_lcp, right_lcp = lcp(start, mid), lcp(mid+1, end)
            min_len = min(len(left_lcp), len(right_lcp))
            for i in range(min_len):
                if left_lcp[i] != right_lcp[i]:
                    return left_lcp[:i]
            return left_lcp[:min_len]

        return lcp(0, len(strs)-1)
