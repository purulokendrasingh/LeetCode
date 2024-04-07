class Solution:
    def checkValidString(self, s: str) -> bool:
        brackets = []
        stars = []
        for i in range(len(s)):
            if s[i] == '(':
                brackets.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if brackets:
                    brackets.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while brackets:
            if not stars or stars[-1] < brackets[-1]:
                return False
            brackets.pop()
            stars.pop()
        return len(brackets) == 0