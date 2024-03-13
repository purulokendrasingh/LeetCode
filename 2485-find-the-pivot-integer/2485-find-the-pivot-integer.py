class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = math.sqrt(n*(n+1)//2)
        
        if ans == ans//1:
            return int(ans)
        
        return -1