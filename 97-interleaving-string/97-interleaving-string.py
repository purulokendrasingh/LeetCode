class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = defaultdict(lambda: None)
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        
        if len_s1 + len_s2 != len_s3:
            return False
        
        def helper(p1, p2):
            if dp[p1, p2] != None:
                return dp[p1, p2]
            if p1 == -1:
                dp[p1, p2] = (s2[:p2+1] == s3[:p2+1])
            elif p2 == -1:
                dp[p1, p2] = (s1[:p1+1] == s3[:p1+1])
            else:
                t = []
                if s1[p1] == s3[p1+p2+1]:
                    t.append(helper(p1-1, p2))
                if s2[p2] == s3[p1+p2+1]:
                    t.append(helper(p1, p2-1))
                dp[p1, p2] = any(t) if t else False
            return dp[p1, p2]
        
        return helper(len_s1-1, len_s2-1)