class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        lenn = len(nums)
        arr = []
        for i, n in enumerate(nums):
            while arr and arr[-1] > n and i < lenn-k+len(arr):
                arr.pop()
            if len(arr) < k:
                arr.append(n)
        return arr