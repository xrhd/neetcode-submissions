class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        def inbound(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            return True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            visited.add((i, j))

            for p, q in directions:
                i_new, j_new = i + p, j + q
                if (
                    inbound(i_new, j_new)
                    and heights[i_new][j_new] >= heights[i][j]
                    and (i_new, j_new) not in visited
                ):
                    dfs(i_new, j_new, visited)

        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m - 1, atlantic)

        for j in range(m):
            dfs(0, j, pacific)
            dfs(n - 1, j, atlantic)

        return [
            [i, j]
            for i in range(n)
            for j in range(m)
            if (i, j) in pacific and (i, j) in atlantic
        ]
