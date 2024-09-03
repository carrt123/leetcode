# author: Carrt
# date: 2024-03-15
# comment:
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
from collections import defaultdict
from typing import List


class Solution:

    # 方法一：双指针
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)

        valDict = defaultdict(int)
        # 记录每个数字出现的次数
        pre, tail = 0, 0
        while tail < len(nums):
            valDict[nums[tail]] += 1
            if valDict[nums[tail]] <= 2:
                nums[pre] = nums[tail]
                pre += 1
            tail += 1
        return pre

    #  方法二: xx
    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)

        k = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k






