class Solution:
    def maxScore(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: None)
        
        def helper(cnt, i):
            if dp[cnt, i] != None:
                return dp[cnt, i]
            
            l = len(i)
            if l == 2:
                dp[cnt, i] = cnt*gcd(i[0], i[1])
            else:
                temp = 0
                for a in range(l):
                    for b in range(a+1, l):
                        t = list(i)
                        t.remove(i[a])
                        t.remove(i[b])
                        temp = max(temp, cnt*gcd(i[a],i[b]) + helper(cnt+1, tuple(t)))
                dp[cnt, i] = temp
            return dp[cnt, i]
        
        return helper(1, tuple(nums))