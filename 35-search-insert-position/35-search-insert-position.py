class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        temp = sorted(nums)
        return temp.index(target)