class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals = sorted(intervals, key=lambda item: item[0])

        res = 0
        _, aux = intervals[0]
        for start, end in intervals[1:]:
            # non-overlaping case
            if aux <= start:
                aux = end
            else:
                aux = min(end, aux)
                res += 1

        return res  
        