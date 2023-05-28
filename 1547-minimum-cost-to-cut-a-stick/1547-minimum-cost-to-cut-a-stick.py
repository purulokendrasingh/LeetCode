class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = defaultdict(lambda: None)
        
        def helper(l,r, cuts):
            if dp[l,r] != None:
                return dp[l,r]
            if not cuts:
                dp[l,r] = 0
            else:
                temp = float('inf')
                cPass = False
                for c in cuts:
                    if c < r and c > l:
                        if not cPass:
                            cPass = True
                        a = cuts.copy()
                        a.remove(c)
                        temp = min(temp, helper(l, c, a) + helper(c, r, a) + r-l)
                if cPass:
                    dp[l,r] = temp
                else:
                    dp[l,r] = 0
            return dp[l,r]
        
        cuts = set(cuts)
        
        return helper(0, n, cuts)