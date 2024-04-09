class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1]
        r2l = [1]
        for i in nums:
            l2r.append(l2r[-1]*i)
            
        for j in range(len(nums)-1,-1,-1):
            r2l.append(r2l[-1]*nums[j])
        r2l = r2l[::-1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(l2r[i]*r2l[i+1])
        return ans