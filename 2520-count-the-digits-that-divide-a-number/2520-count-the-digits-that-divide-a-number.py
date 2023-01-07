class Solution:
    def countDigits(self, num: int) -> int:
        digits = str(num)
        return sum([num%int(i) == 0 for i in digits])