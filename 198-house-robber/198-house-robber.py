class Solution:
    def __init__(self):
        self.dp = defaultdict(int)
        
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        if set(nums) == {0}:
            return 0
        ans = max(self.solve(0, nums), self.solve(1, nums))
        return ans
    
    def solve(self, pos, nums):
        if self.dp[pos]:
            return self.dp[pos]
        if pos >= len(nums):
            self.dp[pos] = 0
        else:
            self.dp[pos] = nums[pos] + max(self.solve(pos+2, nums), self.solve(pos+3, nums))
        return self.dp[pos]