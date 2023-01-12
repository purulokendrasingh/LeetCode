class Solution:
    def numSub(self, s: str) -> int:
        MOD = 1000000007
        arr = s.split('0')
        ans = 0
        for i in arr:
            if i != '':
                temp = len(i)
                ans += temp*(temp+1)//2
        return ans % MOD