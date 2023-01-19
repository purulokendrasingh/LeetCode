class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pm, res = 0,0
        groups = [0]*k
        groups[0] = 1
        
        for i in range(n):
            pm = (pm + nums[i]%k)%k
            res += groups[pm]
            groups[pm] += 1
        return res