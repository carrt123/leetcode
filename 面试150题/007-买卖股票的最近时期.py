# author:Carrt
# date:2024-03-15
# content:给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0

from typing import List


class Solution:
    # 贪心算法
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices:
            if price <= buy:
                buy = price
            else:
                profit = max(profit, price - buy)
        return profit

    # 动态规划
    def maxProfit2(self, prices: List[int]) -> int:

        dp = [0] * len(prices)
        minPrice = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return dp[len(prices) - 1]
