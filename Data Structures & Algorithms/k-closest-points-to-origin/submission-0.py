import math
import heapq


def euclidean(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(euclidean((0, 0), point), point) for point in points]
        heapq.heapify(heap)

        def foo(t):
            _, point = t
            return point

        return [foo(heapq.heappop(heap)) for _ in range(k)]
