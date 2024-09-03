# author: Carrt
# date: 2024-03-15
from typing import List


class Solution:

    # 使用内置函数sort
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

    # 双指针
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m, n
        while p1 > 0 and p2 > 0:
            if nums1[p1-1] >= nums2[p2-1]:
                nums1[p1+p2-1] = nums1[p1-1]
                p1-=1
            else:
                nums1[p1+p2-1] = nums2[p2-1]
                p2-=1
        if p2 > 0:
            nums1[:p2] = nums2[:p2]

     # 双指针优化：代码结构优化
    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m-1, n-1, m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]>=nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p-=1
        # 如果nums2有剩余，直接放到nums1前面
        nums1[:p2+1] = nums2[:p2+1]


