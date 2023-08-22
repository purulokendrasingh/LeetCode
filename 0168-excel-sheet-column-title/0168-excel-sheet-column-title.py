class Solution:
    def convertToTitle(self, c: int) -> str:
        ans = []
        
        while c > 26:
            q = c%26
            if q == 0:
                q = 26
                c -= 1
            ans.append(chr(ord('A') + q - 1))
            c //= 26
            
        ans.append(chr(ord('A') + c - 1))
        
        return ''.join(ans[::-1])