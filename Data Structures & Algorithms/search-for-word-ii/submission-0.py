class Node:
    def __init__(self):
        self.child = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.is_word = True

    def is_prefix_or_word(self, prefix) -> tuple[bool, bool]:
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return False, False
            curr = curr.child[c]
        return True, curr.is_word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
            is_predix, is_word = trie.is_prefix_or_word(word)
            # print(f"{word=}, {is_predix=}, {is_word=}")

        res = []

        def dfs(i: int, j: int, prefix: str, path: set):
            nonlocal res
            if i < 0 or len(board) <= i or j < 0 or len(board[0]) <= j or (i, j) in path:
                return

            prefix = prefix + board[i][j]
            is_predix, is_word = trie.is_prefix_or_word(prefix)
            if not is_predix:
                return
            if is_word:
                res.append(prefix)

            options = (
                (0, -1),
                (0, 1),
                (1, 0),
                (-1, 0),
            )
            for p, q in options:
                dfs(i + p, j + q, prefix, path | {(i, j)})

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "", set())

        return list(set(res))
