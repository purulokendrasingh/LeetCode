class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        q = deque()
        for i in s:
            if i in ('(','{','['):
                q.appendleft(i)
            else:
                if not q:
                    return False
                if mapp[i] == q[0]:
                    q.popleft()
                else:
                    return False
        return True if not q else False
                