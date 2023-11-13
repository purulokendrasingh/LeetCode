class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        v = []
        string = []
        for i in s:
            if i in vowels:
                string.append('*')
                v.append(i)
            else:
                string.append(i)
                
        v.sort()
        idx = 0
        for i in range(len(string)):
            if string[i] == '*':
                string[i] = v[idx]
                idx += 1
        
        return ''.join(string)