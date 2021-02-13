class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) == 0:
            return 0

        min_price, profit = [float('inf')] * k, [float('-inf')] * k
        for price in prices:
            min_price[0] = min(min_price[0], price)
            profit[0] = max(profit[0], price - min_price[0])
            for i in range(1, k):
                min_price[i] = min(min_price[i], price - profit[i-1])
                profit[i] = max(profit[i], price - min_price[i])
        
        return profit[k-1]
