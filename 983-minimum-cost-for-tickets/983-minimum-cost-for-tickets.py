class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = defaultdict(lambda: None)
        
        def helper(idx):
            if dp[idx] != None:
                return dp[idx]
            if idx >= n:
                dp[idx] = 0
            else:
                a = costs[0] + helper(idx + 1)

                i = idx
                while i < n and days[i] <= days[idx] + 6:
                    i += 1
                b = costs[1] + helper(i)

                j = idx
                while j < n and days[j] <= days[idx] + 29:
                    j += 1
                c = costs[2] + helper(j)
                
                dp[idx] = min(a,b,c)
            return dp[idx]
        
        return helper(0)