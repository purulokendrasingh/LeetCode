class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = [v for k,v in Counter(tasks).most_common()]
        max_occ = c[0]
        mo_freq = c.count(max_occ)
        print(max_occ, mo_freq)
        if mo_freq > n:
            return len(tasks)
        else:
            # return (max_occ-1)*(n+1) + mo_freq
            free_blocks = (max_occ-1)*(n+1-mo_freq)
            if free_blocks >= (len(tasks) - max_occ*mo_freq):
                return (max_occ-1)*(n+1) + mo_freq
            else:
                return (max_occ-1)*(n+1) + mo_freq + (len(tasks) - max_occ*mo_freq - free_blocks)