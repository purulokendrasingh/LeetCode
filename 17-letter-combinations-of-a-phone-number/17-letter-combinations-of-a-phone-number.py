class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        digits = list(digits)
        ans = ['']
        ddict = {'2':'abc', 
                 '3':'def',
                 '4':'ghi',
                 '5':'jkl',
                 '6':'mno',
                 '7':'pqrs',
                 '8':'tuv',
                 '9':'wxyz'
                }
        while digits:
            curr = digits.pop(0)
            temp = ans
            ans = []
            for i in ddict[curr]:
                ans.extend([s+i for s in temp])
        return ans