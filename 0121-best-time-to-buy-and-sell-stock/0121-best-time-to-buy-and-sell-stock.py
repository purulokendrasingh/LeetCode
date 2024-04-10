class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        ans = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > sell:
                sell = prices[i]
            elif prices[i] < buy:
                ans = max(ans, sell-buy)
                sell = prices[i]
                buy = prices[i]
        ans = max(ans, sell-buy)
        return ans