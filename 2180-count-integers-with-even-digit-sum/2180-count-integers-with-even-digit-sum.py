class Solution:
    def countEven(self, num: int) -> int:
        if num == 1000:
            num = 999
        ans = 0
        for i in range(1, num+1):
            h = i//100
            t = (i-h*100)//10
            o = i-h*100-t*10
            if not (o+t+h)&1:
                ans += 1
        return ans