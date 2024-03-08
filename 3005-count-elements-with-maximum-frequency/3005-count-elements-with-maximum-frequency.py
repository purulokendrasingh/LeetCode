class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0]*101
        for i in nums:
            freq[i] += 1
            
        maxx = max(freq)
        return maxx*freq.count(maxx)