class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = defaultdict(lambda: None)
        
        if stones[1] - stones[0] > 1:
            return False
        
        ddict = {}
        for i, stone in enumerate(stones):
            ddict[stone] = i

        def helper(i, k):
            if dp[i, k] != None:
                return dp[i,k]
            if i == len(stones) - 1:
                dp[i,k] = True
            elif k == 0:
                dp[i,k] = False
            else:
                temp = False
                if stones[i] + k - 1 in ddict:
                    temp = helper(ddict[stones[i] + k - 1], k - 1)
                if not temp and stones[i] + k in ddict:
                    temp = helper(ddict[stones[i] + k], k)
                if not temp and stones[i] + k + 1 in ddict:
                    temp = helper(ddict[stones[i] + k + 1], k + 1) 
                dp[i,k] = temp
            return dp[i,k]
        
        ans = helper(1, 1)
        return ans