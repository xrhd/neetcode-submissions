import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Naive"""
        counter = Counter(tasks)
        heap = [cnt for cnt in counter.values()]
        heapq.heapify_max(heap)
        queue = deque()

        n_cycles = 0
        while heap or queue:
            # print(f"{n_cycles=}, {heap=}, {queue=}")
            n_cycles += 1
            

            if not heap:
                # idle
                # print("idle")
                n_cycles= queue[0][1]
            else:
                # complete the most freequent task in the heap without cooldown
                cnt = heapq.heappop_max(heap) -1
                if cnt:
                    queue.append([cnt, n_cycles + n])

            # check if we can free a task with cooldown and put it back to then heap
            if queue and queue[0][1] == n_cycles:
                cnt, _ = queue.popleft()
                heapq.heappush_max(heap, cnt)

        return n_cycles
