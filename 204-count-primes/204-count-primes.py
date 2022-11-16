class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        nums = [False, False] + [True]*(n-2)
        i = 2
        while i*i < n:
            if nums[i]:
                for j in range(i*i, n, i):
                    nums[j] = False
            i += 1
        return sum(nums)