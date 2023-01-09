class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            while stack and num < stack[-1]:
                stack.pop()
            stack.append(num)
            ans += len(stack)
        return ans