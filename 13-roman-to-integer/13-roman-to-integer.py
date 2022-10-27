class Solution:
    def romanToInt(self, s: str) -> int:
        ddict = {'I':1,
                 'V':5,
                 'X':10,
                 'L':50,
                 'C':100,
                 'D':500,
                 'M':1000
                }
        
        a = [ddict[i] for i in s]
        
        ans = 0
        for i in range(len(s)-1):
            if a[i] >= a[i+1]:
                ans += a[i]
            else:
                ans -= a[i]
        return ans + a[-1]