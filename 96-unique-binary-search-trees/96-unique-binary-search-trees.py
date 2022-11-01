class Solution:
    def numTrees(self, n: int) -> int:
        a = math.factorial(2*n)//(math.factorial(n)**2)
        return a//(n+1)