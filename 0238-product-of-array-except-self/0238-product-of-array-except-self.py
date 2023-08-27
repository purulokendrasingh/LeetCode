class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1]*n
        for i in range(1, n):
            arr[i] = arr[i-1]*nums[i-1]
            
        curr = 1
        for i in range(n-2, -1, -1):
            temp = nums[i+1]*curr
            curr = temp
            arr[i] *= temp
            
        return arr