class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxx = -1
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                temp = nums[i] + nums[j]
                if temp > maxx and temp < k:
                    maxx = temp
        return maxx