class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # for i in range(len(words)):
        #     for j in range(len(words[0])):
        #         if (j >= len(words[i]) and i < len(words[j])) or (j < len(words[i]) and i >= len(words[j])):
        #             return False
        #         if words[]
        maxLen = max([len(i) for i in words])
        if len(words) != maxLen or len(words[0]) != maxLen:
            return False
        m = len(words)
        n = len(words[0])
        for i in range(m):
            if len(words[i]) < n:
                words[i] += '0'*(n-len(words[i]))
        print(words)
        for i in range(m):
            for j in range(n):
                if words[i][j] != words[j][i]:
                    return False
        return True
            