Another way to solve this would be to reverse s and find the LCS of s and s_reverse.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = defaultdict(lambda: None)
        r = s[::-1]
        
        def helper(p1, p2):
            if dp[p1, p2] != None:
                return dp[p1, p2]
            if p1 < 0 or p2 < 0:
                dp[p1, p2] = 0
            else:
                if s[p1] == r[p2]:
                    dp[p1, p2] = 1 + helper(p1-1, p2-1)
                else:
                    dp[p1, p2] = max(helper(p1, p2-1), helper(p1-1, p2))
            return dp[p1, p2]
        
        return helper(len(s)-1, len(r)-1)
