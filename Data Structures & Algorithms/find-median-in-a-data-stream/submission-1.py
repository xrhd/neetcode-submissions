import heapq

class MedianFinder:

    def __init__(self):
        self.l, self.r = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.l, num)

        if self.l and self.r and self.l[0] > self.r[0]:
            val = heapq.heappop_max(self.l)
            heapq.heappush(self.r, val)

        if len(self.l) > len(self.r) + 1:
            val = heapq.heappop_max(self.l)
            heapq.heappush(self.r, val)

        if len(self.l) +1 < len(self.r):
            val = heapq.heappop(self.r)
            heapq.heappush_max(self.l, val)

    def findMedian(self) -> float:
        if len(self.l) < len(self.r):
            return self.r[0]

        if len(self.l) > len(self.r):
            return self.l[0]

        return round((self.l[0] + self.r[0]) / 2, 4)
