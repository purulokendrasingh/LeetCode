class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = defaultdict(lambda: None)
        
        def helper(k):
            if dp[k] != None:
                return dp[k]
            if k < 0:
                dp[k] = float('inf')
            elif k == 0:
                dp[k] = 0
            else:
                ans = float('inf')
                isValid = False
                for i in coins:
                    ans = min(ans, 1 + helper(k-i))
                dp[k] = ans
    
            return dp[k]
        
        ans = helper(amount)
        return ans if ans < 1000000 else -1