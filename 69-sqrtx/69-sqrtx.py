class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 0, x//2
        
        while left <= right:
            mid = (left+right)//2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid <= x:
                left = mid+1
            else:
                right = mid-1
        return mid