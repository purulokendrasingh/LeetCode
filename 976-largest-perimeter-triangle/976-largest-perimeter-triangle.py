class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(1,n-1):
            if nums[i-1] < (nums[i]+nums[i+1]):
                return nums[i]+nums[i+1]+nums[i-1]
        return 0