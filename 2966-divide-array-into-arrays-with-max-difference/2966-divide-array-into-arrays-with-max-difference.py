class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        nums = deque(nums)
        ans = []
        while nums:
            left = nums.popleft()
            mid = nums.popleft()
            right = nums.popleft()
            if right - left <= k:
                ans.append([left, mid, right])
            else:
                return []
        return ans