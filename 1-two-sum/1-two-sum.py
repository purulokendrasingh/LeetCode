class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print('TESTING LEETHUB EXTENSION')
        ddict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in ddict:
                return [i, ddict[target - nums[i]]]
            else:
                ddict[nums[i]] = i