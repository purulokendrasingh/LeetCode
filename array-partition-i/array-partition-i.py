class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(1, len(nums), 2):
            ans += nums[i]
        return ans