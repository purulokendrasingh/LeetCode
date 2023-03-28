class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        @lru_cache(1000)
        def helper(idx):
            if idx >= n:
                return 0
            
            a = costs[0] + helper(idx + 1)
            
            i = idx
            while i < n and days[i] <= days[idx] + 6:
                i += 1
            b = costs[1] + helper(i)
            
            j = idx
            while j < n and days[j] <= days[idx] + 29:
                j += 1
            c = costs[2] + helper(j)
            
            return min(a,b,c)
        
        return helper(0)