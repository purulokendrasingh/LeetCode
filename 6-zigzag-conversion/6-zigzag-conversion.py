class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s
        mat = defaultdict(list)
        
        tr = 1
        pos = 0
        for i in range(n):
            mat[pos].append(s[i])
            if pos == 0:
                tr = 1
            elif pos == numRows-1:
                tr = -1
            
            pos += tr
        
        return ''.join([''.join(i) for i in mat.values()])