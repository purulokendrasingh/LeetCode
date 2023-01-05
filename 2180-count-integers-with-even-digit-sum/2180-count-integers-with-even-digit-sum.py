class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num+1):
            summ = 0
            while i > 0:
                summ += i%10
                i //= 10
            if not (summ & 1):
                ans += 1
        return ans