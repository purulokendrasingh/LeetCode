class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ddict = defaultdict(list)
        
        for s in strs:
            ddict[tuple(sorted(s))].append(s)
            
        return ddict.values()