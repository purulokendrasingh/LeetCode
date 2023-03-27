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
                temp = []
                if r != m-1:
                    temp.append(helper(r+1, c))
                if c != n-1:
                    temp.append(helper(r, c+1))
                dp[r,c] = grid[r][c] + min(temp)
            return dp[r,c]
        
        return helper(0, 0)