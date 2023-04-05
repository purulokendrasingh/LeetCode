class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        summ = 0
        
        for i in range(len(nums)):
            summ += nums[i]
            res = max(res, math.ceil(summ/(i+1)))
        return res