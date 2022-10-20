class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = defaultdict(int)
        n = len(s)
        
        def helper(s, l, r):
            if dp[l,r]:
                return dp[l,r]
            if l == r:
                dp[l,r] = 1
            elif l > r:
                dp[l,r] = 0
            else:
                if s[l] == s[r]:
                    dp[l,r] = 2 + helper(s, l+1, r-1)
                else:
                    dp[l,r] = max(helper(s, l+1, r), helper(s, l, r-1))
            return dp[l,r]
        
        return helper(s, 0, n-1)