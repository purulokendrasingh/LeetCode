class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        def helper(n):
            return n*(n-1)//2
        
        ans = 0
        curr = -1
        count = 0
        for num in nums:
            if curr < num:
                count += 1
                curr = num
            else:
                ans += helper(count)
                count = 1
                curr = num
        ans += helper(count) + len(nums)
        return ans