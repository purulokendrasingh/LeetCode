class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        def helper(s1, s2):
            ans = []
            i,j = 0,0
            while i < len(s1) and j < len(s2):
                w1 = ord(s1[i])
                w2 = ord(s2[j])
                if w1 == w2:
                    ans.append(s1[i])
                    i += 1
                    j += 1
                elif w1 < w2:
                    i += 1
                else:
                    j += 1
            return ''.join(ans)
        s = sorted(words[0])
        for i in range(1, len(words)):
            s = helper(s, sorted(words[i]))
        return s