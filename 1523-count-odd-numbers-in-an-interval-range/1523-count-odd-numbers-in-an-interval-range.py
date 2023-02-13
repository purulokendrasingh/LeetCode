class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff == 1:
            return 1
        if diff % 2 == 0:
            if low % 2 == 0:
                return diff//2
            else:
                return diff//2+1
        else:
            return diff//2+1