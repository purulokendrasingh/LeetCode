class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        l = 0
        r = len(nums)-1
        while l < r:
            summ = nums[l] + nums[r]
            if summ < k:
                ans = max(ans, summ)
                l += 1
            else:
                r -= 1
        return ans