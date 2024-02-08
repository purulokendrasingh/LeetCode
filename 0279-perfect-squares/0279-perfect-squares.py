class Solution:
    def numSquares(self, n: int) -> int:
        dp = defaultdict(lambda: None)
        
        def helper(i):
            if dp[i] is not None:
                return dp[i]
            if i < 4:
                dp[i] = i
            else:
                max_square = math.floor(math.sqrt(i))
                ans = 10000
                for num in range(1, max_square+1):
                    ans = min(ans, 1 + helper(i - num**2))
                dp[i] = ans
            return dp[i]
        
        return helper(n)