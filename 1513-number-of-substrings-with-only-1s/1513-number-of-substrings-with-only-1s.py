class Solution:
    def numSub(self, s: str) -> int:
        MOD = 1000000007
        ans = []
        n = len(s)
        l = 0
        r = 0
        for i in range(n):
            if s[i] == '0':
                if r != l:
                    ans.append(r-l)
                r = i+1
                l = r
            else:
                r += 1
        if l != r:
            ans.append(r-l)
        return sum([sum(range(1,i+1)) for i in ans]) % MOD