class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n&1 == 1:
                n -= 1
                ans += 1
            n //= 2
        return ans