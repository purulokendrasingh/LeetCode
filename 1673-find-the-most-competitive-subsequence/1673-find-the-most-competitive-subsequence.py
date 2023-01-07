class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stk = []
        for i, n in enumerate(nums):
            while stk and stk[-1] > n and len(stk) + len(nums) - i > k:
                stk.pop()
            if len(stk) < k:    
                stk.append(n)
        return stk 