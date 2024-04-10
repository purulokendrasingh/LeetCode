class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = defaultdict(lambda: None)
        
        def helper(i):
            if dp[i] is not None:
                return dp[i]
            if i == 0:
                dp[i] = 0
            else:
                ans = float('inf')
                for j in coins:
                    if i >= j:
                        ans = min(ans, 1 + helper(i-j))
                dp[i] = ans
            return dp[i]
        
        ans = helper(amount)
        if ans == float('inf'):
            return -1
        return ans