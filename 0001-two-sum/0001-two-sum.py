class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ddict = {}
        for i in range(len(nums)):
            if nums[i] in ddict:
                return [i, ddict[nums[i]]]
            ddict[target - nums[i]] = i