import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heapq.heapify_max(stones)
        while len(stones) > 1:
            # print(f"{stones=}")
            diff = heapq.heappop_max(stones) - heapq.heappop_max(stones)
            if diff:
                heapq.heappush_max(stones, diff)

        return stones[0] if stones else 0