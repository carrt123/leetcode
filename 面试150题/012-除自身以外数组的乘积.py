# author:Carrt
# date:2024-03-19

from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]):
        pre, tail = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            tail[i] = tail[i + 1] * nums[i + 1]
        return [pre[i] * tail[i] for i in range(len(nums))]


