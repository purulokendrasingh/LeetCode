class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        broke = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                broke = True
                break
            else:
                digits[i] = 0
        if not broke:
            return [1] + digits
        return digits