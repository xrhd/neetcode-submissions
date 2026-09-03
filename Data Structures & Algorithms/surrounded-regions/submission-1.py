class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """DFS solution
        Time: O(n*m)
        Space: O(1)
        """
        R, C = len(board), len(board[0])

        def dfs(r, c):
            nonlocal board
            if not (0 <= r < R and 0 <= c < C) or board[r][c] != "O":
                return

            board[r][c] = "A"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # use 'A' as marker for non-surrounded cell
        for r in [0, R - 1]:
            for c in range(C):
                if board[r][c] == "O":
                    dfs(r, c)

        for c in [0, C - 1]:
            for r in range(R):
                if board[r][c] == "O":
                    dfs(r, c)

        # replace all 'O' -> 'X' and 'A' -> 'O'
        for r in range(R):
            for c in range(C):
                match board[r][c]:
                    case "O":
                        board[r][c] = "X"
                    case "A":
                        board[r][c] = "O"
                    case _:
                        continue
