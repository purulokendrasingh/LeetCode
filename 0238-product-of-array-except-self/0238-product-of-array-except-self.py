class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(1, len(nums)):
            ans.append(ans[-1]*nums[i-1])
        
        temp = 1
        for i in reversed(range(len(nums))):
            ans[i] *= temp
            temp *= nums[i]
            
        return ans