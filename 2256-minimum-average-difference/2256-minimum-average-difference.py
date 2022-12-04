class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        lr_sum = list(accumulate(nums))
        n = len(nums)
        ans = 1000000
        idx = 0
        for i in range(n):
            a = lr_sum[i]//(i+1)
            b = (lr_sum[n-1] - lr_sum[i])//(n-i-1) if n-i-1 > 0 else 0
            temp = abs(a - b)
            if temp < ans:
                ans = temp
                idx = i
        return idx
        