class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        MAX = 1000000
        w1 = MAX
        w2 = MAX
        rec = -1
        ans = MAX
        for i in range(n):
            if wordsDict[i] != word1 and wordsDict[i] != word2:
                continue
                
            if rec == 1:
                if wordsDict[i] == word2:
                    w2 = i
                    ans = min(ans, abs(w1-w2))
                    rec = 2
                else:
                    w1 = i
            elif rec == 2:
                if wordsDict[i] == word1:
                    w1 = i
                    ans = min(ans, abs(w1-w2))
                    rec = 1
                else:
                    w2 = i
            else:
                if wordsDict[i] == word1:
                    w1 = i
                    ans = min(ans, abs(w1-w2))
                    rec = 1
                elif wordsDict[i] == word2:
                    w2 = i
                    ans = min(ans, abs(w1-w2))
                    rec = 2
        return ans
                
            