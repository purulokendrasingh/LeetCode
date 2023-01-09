class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i, num in enumerate(nums):
            while stack and num < stack[-1]:
                stack.pop()
            stack.append(num)
            ans += len(stack)
        return ans