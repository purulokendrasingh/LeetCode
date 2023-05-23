class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left, right = 0, n*m-1
        
        while left <= right:
            mid = (left+right)//2
            i,j = mid//n, mid%n
            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] > target:
                right = i*n+j-1
            else:
                left = i*n+j+1
        return False