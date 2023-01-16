class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        sc = "!?',;."
        for i in sc:
            paragraph = paragraph.replace(i, ' ')
        arr = paragraph.split(' ')
        arr = [i.lower() for i in arr if not i.isspace or i != '']
        c = Counter(arr)
        ddict = dict(sorted(c.items(), key=lambda item: -item[1]))
        for k,v in ddict.items():
            if k != '.' and k not in banned:
                return k