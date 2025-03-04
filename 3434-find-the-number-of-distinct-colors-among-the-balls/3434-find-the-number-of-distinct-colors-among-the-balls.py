class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mapping = defaultdict(lambda: None)
        colors = defaultdict(int)
        res = []
        for ball,color in  queries:
            if mapping[ball] is None:
                mapping[ball] = color
                colors[color] += 1
            elif mapping[ball] != color:
                colors[mapping[ball]] -= 1
                if colors[mapping[ball]] == 0:
                    del colors[mapping[ball]]
                mapping[ball] = color
                colors[color] += 1

            res.append(len(colors))
        return res    