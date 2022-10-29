class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        n = len(nums)
        lis = [1]*n
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i],1+lis[j])
        print(lis)
        return max(lis)