class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n == 1:
            return 4
        l = 2
        r = 3
        for i in range(n-2):
            temp = r
            r = r + l
            l = temp
        return r**2 % 1000000007