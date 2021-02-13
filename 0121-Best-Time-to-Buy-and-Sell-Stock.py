class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = math.inf
        maxProfit = 0
        for i in prices:
            minPrice = min(i, minPrice)
            maxProfit = max(i - minPrice, maxProfit)
        return maxProfit
