from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """BFS solution
        time and space: O(R*C)
        """
        R, C = len(grid), len(grid[0])
        visited, Q = set(), deque()

        def add(r, c):
            if not (0 <= r < R) or not (0 <= c < C) or grid[r][c] < 0 or (r, c) in visited:
                return

            Q.append((r, c))
            visited.add((r, c))

        # init with tresure positions
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    add(r, c)

        dist = 0  # its also de depth
        while Q:
            for _ in range(len(Q)):
                r, c = Q.popleft()
                grid[r][c] = min(grid[r][c], dist)
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            dist += 1
