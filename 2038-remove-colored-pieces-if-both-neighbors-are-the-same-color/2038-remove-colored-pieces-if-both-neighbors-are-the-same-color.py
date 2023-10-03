class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_turns = 0
        b_turns = 0
        curr = None
        count = 0
        idx = 0
        while idx <= len(colors):
            if idx == len(colors) or curr != colors[idx]:
                if count > 2:
                    if curr == 'A':
                        a_turns += count-2
                    elif curr == 'B':
                        b_turns += count-2
                count = 1
                if idx != len(colors):
                    curr = colors[idx]
            elif curr == colors[idx]:
                count += 1
            idx += 1
        return a_turns > b_turns