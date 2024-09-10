# author:Carrt
# date:2024-03-15
# content:给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

from typing import List

class Solution:

    # 暴力法
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # 三次反转法
    def rotate2(self, nums: List[int], k: int) -> None:

        def reverse(start, end, arr):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        k = k % len(nums)
        reverse(0, len(nums) - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, len(nums) - 1, nums)
