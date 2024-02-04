class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False]*n for _ in range(m)]
        
        def helper(i,j):
            if i >= 0 and i < m and j >= 0 and j < n and (not vis[i][j]) and grid[i][j] == '1':
                vis[i][j] = True
                helper(i+1,j)
                helper(i-1,j)
                helper(i,j+1)
                helper(i,j-1)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == '1':
                    ans += 1
                    helper(i,j)

        return ans