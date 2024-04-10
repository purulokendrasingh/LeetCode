class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(n-1,-1,-1):
            ans = 0
            if i+2 <= n:
                ans += dp[i+2]
            if i+1 <= n:
                ans += dp[i+1]
            dp[i] = ans
        return dp[0]