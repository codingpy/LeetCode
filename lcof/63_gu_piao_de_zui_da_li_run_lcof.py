class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        cost = float('inf')

        for price in prices:
            profit = max(profit, price - cost)

            cost = min(cost, price)

        return profit
