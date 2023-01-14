class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ansLen = len(word)
        sp = []
        sw = word[0]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == sw:
                    sp.append((i,j))
                    
        if len(word) == 1:
            return True if sp else False
        
        for i in sp:
            q = deque()
            q.append([i])
            while q:
                count = len(q)
                for _ in range(count):
                    vis = q.popleft()
                    lenn = len(vis)
                    x,y = vis[-1]
                    if x > 0 and board[x-1][y] == word[lenn] and (x-1,y) not in vis:
                        q.append(vis+[(x-1,y)])
                        if lenn+1 == ansLen:
                            return True
                    if x < m-1 and board[x+1][y] == word[lenn] and (x+1,y) not in vis:
                        q.append(vis+[(x+1,y)])
                        if lenn+1 == ansLen:
                            return True
                    if y > 0 and board[x][y-1] == word[lenn] and (x,y-1) not in vis:
                        q.append(vis+[(x,y-1)])
                        if lenn+1 == ansLen:
                            return True
                    if y < n-1 and board[x][y+1] == word[lenn] and (x,y+1) not in vis:
                        q.append(vis+[(x,y+1)])
                        if lenn+1 == ansLen:
                            return True
        return False