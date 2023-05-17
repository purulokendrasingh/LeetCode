class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        noh = len(costs)
        noc = len(costs[0])
        dp = defaultdict(lambda: None)
        
        def helper(uc, h):
            if dp[uc, h] != None:
                return dp[uc, h]
            if h == noh:
                dp[uc, h] = 0
            else:
                temp = float('inf')
                for i in range(noc):
                    if i != uc:
                        temp = min(temp, costs[h][i] + helper(i, h+1))
                dp[uc, h] = temp
            return dp[uc, h]
        
        return helper(-1, 0)