from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Greedy"""
        counter = sorted([cnt for cnt in Counter(tasks).values()])

        most_freq = counter[-1]
        n_idles = (most_freq - 1) * n
        for cnt in counter[:-1]:
            n_idles -= min(most_freq - 1, cnt)

        n_cycles = len(tasks) + max(0, n_idles)
        return n_cycles
