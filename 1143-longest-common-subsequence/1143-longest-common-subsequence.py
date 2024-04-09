class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = defaultdict(lambda: None)
        
        def helper(i, j):
            if dp[i,j] is not None:
                return dp[i,j]
            if i < 0 or j < 0:
                dp[i,j] = 0
            else:
                if text1[i] == text2[j]:
                    dp[i,j] = 1 + helper(i-1,j-1)
                else:
                    dp[i,j] = max(helper(i, j-1), helper(i-1, j))
            return dp[i,j]
        
        return helper(len(text1)-1, len(text2)-1)