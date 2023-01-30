class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return n-1
        arr = [0,1,1]
        for i in range(n-2):
            temp = sum(arr)
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = temp
        return arr[2]