class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = defaultdict(lambda: None)
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        def helper(i, j):
            if dp[i, j] != None:
                return dp[i, j]
            if i < 0:
                dp[i, j] = (s2[:j+1] == s3[:j+1])
            elif j < 0:
                dp[i, j] = (s1[:i+1] == s3[:i+1])
            else:
                t = []
                if s1[i] == s3[i+j+1]:
                    t.append(helper(i-1, j))
                if s2[j] == s3[i+j+1]:
                    t.append(helper(i, j-1))
                dp[i, j] = any(t) if t else False
            return dp[i, j]

        return helper(m-1, n-1)