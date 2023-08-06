class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def helper(arr):
            if arr in res:
                return
            res.append(arr)
            for i in range(n-1):
                for j in range(1, n):
                    temp = arr.copy()
                    temp[i], temp[j] = temp[j], temp[i]
                    helper(temp)
           
        helper(nums)
        return res
                