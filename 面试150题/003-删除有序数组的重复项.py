# author: Carrt
# date: 2024-03-15
# comment:给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
# 然后返回 nums 中唯一元素的个数。
from typing import List

class Solution:

    # 暴力法
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)

        pre = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pre] = nums[i]
                pre += 1
        return pre

    # 双指针法：
    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)

        pre, tail = 1, 1
        while tail < len(nums):
            if nums[tail] != nums[tail-1]:
                nums[pre] = nums[tail]
                pre += 1
            tail += 1
        return pre

    # 使用库函数
    def removeDuplicates3(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

