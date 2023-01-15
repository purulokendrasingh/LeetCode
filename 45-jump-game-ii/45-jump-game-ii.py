class Solution:
    def jump(self, nums: List[int]) -> int:
        maxx = 0
        ans = 0
        curr = 0
        n = len(nums)
        
        for i in range(n-1):
            maxx = max(maxx, i + nums[i])
            if i == curr:
                ans += 1
                curr = maxx
            if curr >= n-1:
                break
        return ans