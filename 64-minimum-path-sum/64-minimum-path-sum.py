class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = defaultdict(lambda: None)
        m = len(grid)
        n = len(grid[0])
        
        def helper(r, c):
            if dp[r,c] != None:
                return dp[r,c]
            if r == m-1 and c == n-1:
                dp[r,c] = grid[r][c]
            else:
                temp = 10000
                if r != m-1:
                    temp = min(temp, helper(r+1, c))
                if c != n-1:
                    temp = min(temp, helper(r, c+1))
                dp[r,c] = temp + grid[r][c]
            return dp[r,c]
        
        return helper(0, 0)