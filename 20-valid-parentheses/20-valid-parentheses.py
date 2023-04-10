class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        q = []
        for i in s:
            if i in ('(','{','['):
                q.append(i)
            else:
                if not q:
                    return False
                if mapp[i] == q[-1]:
                    q.pop()
                else:
                    return False
        return True if not q else False
                