# author:Carrt
# date:2024-03-17

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for i, val in enumerate(nums):
            if i > k:
                return False
            k = max(k, i+val)
        return True

