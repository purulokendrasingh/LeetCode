class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        ans = 0
        if len(c1) <= len(c2):
            for k,v in c1.items():
                if v == 1 and c2[k] == 1:
                    ans += 1
        else:
            for k,v in c2.items():
                if v == 1 and c1[k] == 1:
                    ans += 1
        return ans