class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: None)
        n = len(nums)
        
        def helper(i):
            if dp[i] != None:
                return dp[i]
            if i == n-1:
                dp[i] = 0
            else:
                dp[i] = 10000
                for j in range(1, nums[i]+1):
                    if i+j < n:
                        dp[i] = min(dp[i], 1 + helper(i+j))
            return dp[i]
        
        return helper(0)