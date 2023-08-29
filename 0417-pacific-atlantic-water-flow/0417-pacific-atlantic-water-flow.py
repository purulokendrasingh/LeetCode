class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        dp = defaultdict(lambda: None)
        
        def helper(r, c, vis):
            if dp[r,c] != None:
                return dp[r,c]
            
            po, ao = False, False
            if r == 0 or c == 0:
                po = True
            if r == m-1 or c == n-1:
                ao =  True
            
            if po and ao:
                # dp[r,c] = [po,ao]
                # return dp[r,c]
                return [po, ao]
            
            if r > 0 and (r-1,c) not in vis and heights[r-1][c] <= heights[r][c]:
                tpo, tao = helper(r-1,c,vis|{(r,c)})
                po = po or tpo
                ao = ao or tao
            if (not po or not ao) and r < m-1 and (r+1,c) not in vis and heights[r+1][c] <= heights[r][c]:
                tpo, tao = helper(r+1,c,vis|{(r,c)})
                po = po or tpo
                ao = ao or tao
            if (not po or not ao) and c > 0 and (r,c-1) not in vis and heights[r][c-1] <= heights[r][c]:
                tpo, tao = helper(r,c-1,vis|{(r,c)})
                po = po or tpo
                ao = ao or tao
            if (not po or not ao) and c < n-1 and (r,c+1) not in vis and heights[r][c+1] <= heights[r][c]:
                tpo, tao = helper(r,c+1,vis|{(r,c)})
                po = po or tpo
                ao = ao or tao
                
            # dp[r,c] = [po,ao]
            # return dp[r,c]
            return [po, ao]
        
        ans = []
        for i in range(m):
            for j in range(n):
                p,a = helper(i,j,set())
                dp[i,j] = [p,a]
                if p and a:
                    ans.append([i,j])
 
        return ans