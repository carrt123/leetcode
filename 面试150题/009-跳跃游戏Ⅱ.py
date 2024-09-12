# author:Carrt
# date:2024-03-19
from typing import List


class Solution:

    # 从后往前
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        end = len(nums) - 1
        while end > 0:
            for i in range(end):
                if i + nums[i] >= end:
                    end = i
                    res += 1
                    break
        return res

    # 动态规划
    # dp[i]表示到达第i个位置需要的最少步数
    # dp[i] = min(dp[i-j]+1, dp[i])
    def jump2(self, nums: List[int]) -> int:
        dp = [0xffff] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    # 贪心算法
    def jump3(self, nums: List[int]) -> int:
        end = 0
        res = 0
        maxLength = 0
        for i in range(len(nums)-1):
            maxLength = max(i+nums[i], maxLength)
            if i == end:
                res += 1
                end = maxLength
        return res

