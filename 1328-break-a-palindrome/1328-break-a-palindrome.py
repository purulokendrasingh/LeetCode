class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        idx = -1
        n = len(palindrome)
        if n == 1:
            return ''
        if palindrome.count('a') == n:
            return palindrome[:-1]+'b'
        t = n//2
        for i in range(t):
            if palindrome[i] != 'a':
                idx = i
                break
        if idx == -1:
            for i in range(t+1, n):
                if palindrome[i] != 'a':
                    idx = i
                    break
            if idx == -1 or idx == n:
                return palindrome[:-1]+'b'
        if idx == n:
            return palindrome[:-1]+'b'
        elif idx != -1:
            return palindrome[:idx]+'a'+palindrome[idx+1:]    
        else:
            return ''