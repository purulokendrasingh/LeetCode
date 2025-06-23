class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if board[i][j] != '.':
                    if elem in rows[i] or elem in cols[j] or elem in box[(i//3,j//3)]:
                        return False
                    else:
                        rows[i].add(elem)
                        cols[j].add(elem)
                        box[(i//3,j//3)].add(elem)
        return True