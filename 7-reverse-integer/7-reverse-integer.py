class Solution:
    def reverse(self, x: int) -> int:
        M = 2**31
        if x == 0:
            return x
        neg = 1
        if x < 0:
            neg = -1
        ans = neg * int(str(abs(x))[::-1])
        if ans > M-1 or ans < -M:
            return 0
        else:
            return ans