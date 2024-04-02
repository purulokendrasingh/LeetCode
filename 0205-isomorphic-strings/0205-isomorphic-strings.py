class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1,dict2 = {},{}
        for i,j in zip(s,t):
            if i not in dict1 and j not in dict2:
                dict1[i] = j
                dict2[j] = i
            elif (i in dict1 and dict1[i] != j) or (j in dict2 and dict2[j] != i):
                return False
        return True