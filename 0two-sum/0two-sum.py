class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i in range(len(nums)):
            if nums[i] in dictt:
                return [dictt[nums[i]], i]
            dictt[target - nums[i]] = i
        return None