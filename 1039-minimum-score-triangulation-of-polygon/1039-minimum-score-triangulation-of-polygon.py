class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = defaultdict(lambda: None)
        n = len(values)
        
        def helper(i,j):
            if dp[i,j] != None:
                return dp[i,j]
            if i == j:
                dp[i,j] = 0
            else:
                temp = []
                for k in range(i,j):
                    temp.append(helper(i,k) + helper(k+1,j) + values[i-1]*values[j]*values[k])
                dp[i,j] = min(temp)
                print(i,j, temp)
            return dp[i,j]
        
        print(dp)
        return helper(1, n-1)