class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        temp = 0
        for num in nums:
            if num - 1 not in nums:
                temp = 1
                while num + temp in nums:
                    temp += 1
                    # nums.remove(num+temp)
                max_len = max(max_len, temp)
        return max_len