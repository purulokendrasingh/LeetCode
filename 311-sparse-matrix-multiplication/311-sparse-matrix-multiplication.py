class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        
        matt = []
        for _ in range(m):
            matt.append([0]*n)
        
        for i in range(m):
            for j in range(n):
                temp = 0
                for l in range(k):
                    if mat1[i][l] != 0 and mat2[l][j] != 0:
                        temp += mat1[i][l]*mat2[l][j]
                matt[i][j] = temp
        
        return matt