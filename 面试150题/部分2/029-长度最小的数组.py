from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        res = 0xff
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        pre, tail = 0, 1
        while pre < tail and tail < n + 1:
            temp = pre_sum[tail] - pre_sum[pre]
            if temp < target:
                tail += 1
            else:
                res = max(tail - pre, res)
                pre += 1
        if res == 0xff:
            return 0
        return res

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        s = left = 0
        for right, x in enumerate(nums):
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                res = min(res, right - left + 1)
        return res if res <= n else 0
