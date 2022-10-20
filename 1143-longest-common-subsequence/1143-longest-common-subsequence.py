class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = defaultdict(lambda: None)
        
        def helper(p1, p2):
            if dp[p1, p2] != None:
                return dp[p1,p2]
            if p1 < 0 or p2 < 0:
                dp[p1, p2] = 0
                return dp[p1, p2]
            else:
                if text1[p1] == text2[p2]:
                    dp[p1,p2] = 1 + helper(p1-1, p2-1)
                else:
                    dp[p1, p2] = max(helper(p1, p2-1), helper(p1-1, p2))
            return dp[p1,p2]
        
        return helper(len(text1)-1, len(text2)-1)