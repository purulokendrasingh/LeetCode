class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        n = len(currentState)
        if n < 2 or currentState.count('+') == 0:
            return []
        pointer = 0
        while pointer < n-1:
            if currentState[pointer:pointer+2] == '++':
                ans.append(currentState[:pointer]+'--'+currentState[pointer+2:])
            pointer += 1
        return ans