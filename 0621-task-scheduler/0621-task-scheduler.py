class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = [v for k,v in Counter(tasks).most_common()]
        max_occ = c[0]
        mo_freq = c.count(max_occ)
        if mo_freq > n:
            return len(tasks)
        else:
            free_blocks = (max_occ-1)*(n+1-mo_freq)
            return (max_occ-1)*(n+1) + mo_freq + max(0, (len(tasks) - max_occ*mo_freq - free_blocks))