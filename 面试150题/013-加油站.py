# author:Carrt
# date:2024-03-19
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        n = len(gas)

        total = 0
        start = 0
        current = 0
        for i in range(n):
            temp = gas[i] - cost[i]
            total += temp
            current += temp
            if current < 0:
                start = i + 1
                current = 0
        return start if total >= 0 else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))
