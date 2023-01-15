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
                minn = 10000
                for j in range(1, nums[i]+1):
                    if i+j < n:
                        temp = 1 + helper(i+j)
                        if temp < minn:
                            minn = temp
                dp[i] = minn
            return dp[i]
        
        return helper(0)