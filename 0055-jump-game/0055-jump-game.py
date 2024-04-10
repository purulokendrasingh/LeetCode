class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = defaultdict(lambda: None)
        
        def helper(i):
            if dp[i] is not None:
                return dp[i]
            if i >= len(nums):
                dp[i] = False
            elif i == len(nums)-1:
                dp[i] = True
            else:
                ans = False
                for j in range(nums[i],0,-1):
                    if helper(i+j):
                        ans = True
                        break
                dp[i] = ans
            return dp[i]
        
        return helper(0)