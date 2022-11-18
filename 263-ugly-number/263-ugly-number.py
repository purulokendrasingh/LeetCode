class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def div(a, b):
            while a % b == 0:
                a //= b
            return a

        for f in [2, 3, 5]:
            n = div(n, f)

        return n == 1