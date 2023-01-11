class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        ans = str(sum([num[i]*(10**(n-i-1)) for i in range(n)]) + k)
        return [int(i) for i in ans]