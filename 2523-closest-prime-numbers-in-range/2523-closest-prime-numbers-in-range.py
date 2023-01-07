class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            if n <= 2:
                return 0
            nums = [False, False] + [True]*(n-1)
            i = 2
            while i*i <= n:
                if nums[i]:
                    for j in range(i*i, n+1, i):
                        nums[j] = False
                i += 1
            return nums
        
        nums = sieve(right)
        l = -1
        for i in range(left, right):
            if nums[i]:
                l = i
                break
                
        if l == -1:
            return [-1,-1]
            
        ans = 100000
        r = l + 1
        a = [-1,-1]
        while r <= right:
            if nums[r]:
                if ans > r-l:
                    ans = r-l
                    a[0] = l
                    a[1] = r
                l = r
                r = l+1
            else:
                r += 1
        return a
                