class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        return min([i[0] for i in ops])*min([i[1] for i in ops])