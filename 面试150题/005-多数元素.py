# author:Carrt
# date:2024-03-15
# content:给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
from collections import defaultdict
from typing import List

class Solution:

    # 使用内置函数
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

    # 使用内置函数
    def majorityElement2(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)

    # 摩尔投票法
    def majorityElement3(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for val in nums:
            if count == 0:
                candidate = val
            count += (1 if val == candidate else -1)

        return candidate

    # 使用字典
    def majorityElement4(self, nums: List[int]) -> int:
        temp = defaultdict(int)
        for val in nums:
            temp[val] += 1
            if temp[val] > len(nums)//2:
                return val


