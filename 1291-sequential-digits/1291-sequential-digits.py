class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        comb = '123456789'
        left = 0
        right = 1
        while left < 10:
            if right == 10:
                left += 1
                right = left+1
                if left == 9:
                    break
            num = int(comb[left:right])
            if num >= low and num <= high:
                ans.append(num)
            right += 1
        return sorted(ans)