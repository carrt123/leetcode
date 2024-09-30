from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mint, matt = sum(nums[:3]), sum(nums[-3:])
        if target < mint: return mint
        if target > matt: return matt
        n = len(nums)
        min_diff = inf
        ans = 0
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s

                if s > target:
                    if s - target < min_diff:
                        min_diff = s - target
                        ans = s
                    k -= 1
                else:
                    if target - s < min_diff:
                        min_diff = target - s
                        ans = s
                    j += 1
        return ans



a = 145 + 45j
print(a.imag)


