class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = defaultdict(lambda: None)
        
        def helper(i):
            if dp[i] is not None:
                return dp[i]
            if i >= len(nums):
                dp[i] = 0
            else:
                dp[i] = nums[i] + max(helper(i+2), helper(i+3))
            return dp[i]
        
        return max(helper(0), helper(1))