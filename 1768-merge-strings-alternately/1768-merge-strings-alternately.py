class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        n = len(word1)
        m = len(word2)
        i,j = 0,0
        while i != n and j != m:
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1
            
        if i == n:
            return ''.join(ans) + word2[j:]
        else:
            return ''.join(ans) + word1[i:]