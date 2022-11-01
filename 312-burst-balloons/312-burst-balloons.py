class Solution:
    def maxCoins(self, values: List[int]) -> int:
        dp = defaultdict(lambda: None)
        n = len(values)
        values.append(1)
        values.insert(0,1)
        
        def helper(i,j):
            if dp[i,j] != None:
                return dp[i,j]
            if i == j:
                dp[i,j] = 0
            else:
                temp = []
                for k in range(i,j):
                    temp.append(helper(i,k) + helper(k+1,j) + values[i-1]*values[j]*values[k])
                dp[i,j] = max(temp)
            return dp[i,j]
        
        return helper(0, n)