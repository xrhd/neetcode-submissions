class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def inbound(i, j):
            return 0 <= i and 0 <= j and i < len(board) and j < len(board[0])

        def dfs(word, i, j, paths):
            # print(f"stack={word}, {i=}, {j=}")
            if len(word) == 0:
                return True
            
            coo = [
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1),
            ]
            res = (
                dfs(word[1:], p, q, paths | {(i, j)})
                for p, q in coo
                if inbound(p, q) and board[p][q] == word[0] and ((p, q) not in paths)
            )
            return any(res) if res else False

        for i in range(len(board)):
            for j, c in enumerate(board[i]):
                if c == word[0]:
                    if dfs(word[1:], i, j, set()):
                        return True

        return False