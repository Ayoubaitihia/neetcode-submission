class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = max(prices)
        maxProfit = 0

        for p in prices:
            if p < buy:
                buy = p
            profit = p - buy
            if profit > maxProfit:
                maxProfit = profit

        return(maxProfit)