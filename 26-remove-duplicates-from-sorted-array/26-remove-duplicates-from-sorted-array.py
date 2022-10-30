class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        curr = nums[0]
        for j in range(1, len(nums)):
            if curr != nums[j]:
                nums[i] = nums[j]
                curr = nums[j]
                i += 1
        return i