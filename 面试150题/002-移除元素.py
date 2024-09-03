# author: Carrt
# date: 2024-03-15

from typing import List
class Solution:

   # 双指针法
   def removeElement1(self, nums: List[int], val: int) -> int:
        pre, tail = 0, 0
        while tail < len(nums):
            if nums[tail] != val:
                nums[pre] = nums[tail]
                pre += 1
            tail += 1
        return pre





