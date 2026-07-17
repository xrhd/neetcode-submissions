from functools import reduce

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda el: el[0])

        def merge(acc, it):
            if len(acc) == 0 or acc[-1][1] < it[0]:
                acc.append(it)
            else:
                acc[-1][1] = max(it[1], acc[-1][1])

            return acc

        return reduce(merge, intervals, [])
