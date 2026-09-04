import heapq
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """Heap solution
        Time: O(n log n)
        Space: O(n)
        """

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            # find a candidate for the first card of the group
            first = heap[0]
            if first not in count:
                heapq.heappop(heap)
                continue
            
            # form the group
            for i in range(groupSize):
                if first + i not in count:
                    return False
                count[first + i] -= 1
                if count[first + i] == 0:
                    count.pop(first + i, None)

        return True
