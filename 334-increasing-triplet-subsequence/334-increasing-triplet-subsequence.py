class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s = float('inf')
        m = float('inf')
        for i in nums:
            if i <= s:
                s = i
            elif i <= m:
                m = i
            else:
                return True
        return False
            