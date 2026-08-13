"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """ Sorting solution
        """
        N = len(intervals)
        if N <= 1:
            return N

        starts = sorted([it.start for it in intervals])
        ends = sorted([it.end for it in intervals])

        res, count, i, j = 0, 0, 0, 0
        while i < N and j < N:
            if starts[min(i, N-1)] < ends[min(j, N-i)]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count) 
        
        return res