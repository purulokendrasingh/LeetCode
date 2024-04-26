class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = defaultdict(lambda: None)
        
        def helper(i,j):
            if dp[i,j] is not None:
                return dp[i,j]
            if i == m-1:
                dp[i,j] = grid[i][j]
            else:
                temp = float('inf')
                for k in range(n):
                    if k != j:
                        temp = min(temp, helper(i+1,k))
                dp[i,j] = temp + grid[i][j]
            return dp[i,j]
        
        ans = float('inf')
        for i in range(n):
            ans = min(ans, helper(0,i))

        return ans  