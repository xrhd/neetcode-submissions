"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        its = sorted(intervals, key=lambda item: item.end)
        for i in range(len(its)-1):
            if its[i].end > its[i+1].start:
                return False

        return True
